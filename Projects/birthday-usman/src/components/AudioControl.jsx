import React, { useRef, useState, useCallback } from 'react';

const AudioControl = () => {
  const [enabled, setEnabled] = useState(false);
  const ctxRef = useRef(null);
  const nodesRef = useRef(null);

  const stopAudio = useCallback(() => {
    const nodes = nodesRef.current;
    if (nodes) {
      const now = ctxRef.current ? ctxRef.current.currentTime : 0;
      const { master, windGain, padGain, noiseSrc, osc1, osc2, lfo1, lfo2, lfo3 } = nodes;
      try {
        windGain.gain.setTargetAtTime(0, now, 0.4);
        padGain.gain.setTargetAtTime(0, now, 0.4);
        lfo1.stop(now + 1.2);
        lfo2.stop(now + 1.2);
        lfo3.stop(now + 1.2);
        osc1.stop(now + 1.2);
        osc2.stop(now + 1.2);
        noiseSrc.stop(now + 1.2);
        master.gain.setTargetAtTime(0, now, 0.2);
        setTimeout(() => {
          if (ctxRef.current && ctxRef.current.state !== 'closed') {
            ctxRef.current.close();
          }
          ctxRef.current = null;
          nodesRef.current = null;
        }, 2000);
      } catch {
        ctxRef.current = null;
        nodesRef.current = null;
      }
    }
  }, []);

  const startAudio = useCallback(() => {
    const AC = window.AudioContext || window.webkitAudioContext;
    if (!AC) return false;
    if (!ctxRef.current) {
      ctxRef.current = new AC();
    }
    const ctx = ctxRef.current;
    if (ctx.state === 'suspended') ctx.resume();

    const master = ctx.createGain();
    master.gain.value = 0;
    master.connect(ctx.destination);

    const windBufferSize = ctx.sampleRate * 2;
    const buffer = ctx.createBuffer(1, windBufferSize, ctx.sampleRate);
    const data = buffer.getChannelData(0);
    for (let i = 0; i < windBufferSize; i++) {
      data[i] = Math.random() * 2 - 1;
    }
    const noiseSrc = ctx.createBufferSource();
    noiseSrc.buffer = buffer;
    noiseSrc.loop = true;

    const windFilter = ctx.createBiquadFilter();
    windFilter.type = 'lowpass';
    windFilter.frequency.value = 380;
    windFilter.Q.value = 0.6;

    const windGain = ctx.createGain();
    windGain.gain.value = 0.05;

    const padGain = ctx.createGain();
    padGain.gain.value = 0.018;

    const lfo1 = ctx.createOscillator();
    lfo1.frequency.value = 0.08;
    const lfo1Gain = ctx.createGain();
    lfo1Gain.gain.value = 180;
    lfo1.connect(lfo1Gain);
    lfo1Gain.connect(windFilter.frequency);

    const lfo2 = ctx.createOscillator();
    lfo2.frequency.value = 0.13;
    const lfo2Gain = ctx.createGain();
    lfo2Gain.gain.value = 0.025;
    lfo2.connect(lfo2Gain);
    lfo2Gain.connect(windGain.gain);

    const osc1 = ctx.createOscillator();
    osc1.type = 'sine';
    osc1.frequency.value = 98;
    const osc2 = ctx.createOscillator();
    osc2.type = 'sine';
    osc2.frequency.value = 147;
    const lfo3 = ctx.createOscillator();
    lfo3.frequency.value = 0.05;
    const lfo3Gain = ctx.createGain();
    lfo3Gain.gain.value = 8;
    lfo3.connect(lfo3Gain);
    lfo3Gain.connect(osc1.detune);
    lfo3Gain.connect(osc2.detune);

    noiseSrc.connect(windFilter);
    windFilter.connect(windGain);
    windGain.connect(master);
    osc1.connect(padGain);
    osc2.connect(padGain);
    padGain.connect(master);

    noiseSrc.start();
    lfo1.start();
    lfo2.start();
    lfo3.start();
    osc1.start();
    osc2.start();

    nodesRef.current = { master, windGain, padGain, noiseSrc, windFilter, osc1, osc2, lfo1, lfo2, lfo3 };

    const now = ctx.currentTime;
    master.gain.setTargetAtTime(0.9, now, 1.2);
    windGain.gain.setTargetAtTime(0.05, now, 1.0);
    padGain.gain.setTargetAtTime(0.018, now, 1.0);
    return true;
  }, []);

  const handleToggle = useCallback(() => {
    setEnabled((prev) => {
      const next = !prev;
      if (next) {
        startAudio();
      } else {
        stopAudio();
      }
      return next;
    });
  }, [startAudio, stopAudio]);

  return (
    <button
      type="button"
      className="audio-control"
      onClick={handleToggle}
      aria-pressed={enabled}
      aria-label={enabled ? 'Sound off' : 'Sound on'}
    >
      <span className="audio-icon">{enabled ? '🔇' : '🔊'}</span>
      <span className="audio-label">{enabled ? 'Sound Off' : 'Sound On'}</span>
    </button>
  );
};

export default AudioControl;
