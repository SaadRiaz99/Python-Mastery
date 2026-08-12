import React, { useState, useCallback } from 'react';
import TreeAnimation from './components/TreeAnimation';
import FallingLeaves from './components/FallingLeaves';
import BirthdayMessage from './components/BirthdayMessage';
import ParticleBackground from './components/ParticleBackground';
import AudioControl from './components/AudioControl';
import './styles.css';

function App() {
  const [animationPhase, setAnimationPhase] = useState('growing');
  const [mousePos, setMousePos] = useState({ x: 0.5, y: 0.5 });

  const handleMouseMove = useCallback((e) => {
    setMousePos({ x: e.clientX / window.innerWidth, y: e.clientY / window.innerHeight });
  }, []);

  const handleStart = useCallback(() => {
    setAnimationPhase((phase) => (phase === 'idle' || phase === 'reveal' ? 'growing' : phase));
  }, []);

  const handleGrowthComplete = useCallback(() => {
    setAnimationPhase((phase) => (phase === 'growing' ? 'leaves' : phase));
  }, []);

  const handleLeavesComplete = useCallback(() => {
    setAnimationPhase((phase) => (phase === 'leaves' ? 'reveal' : phase));
  }, []);

  const handleReplay = useCallback(() => {
    setAnimationPhase('growing');
  }, []);

  const isIdle = animationPhase === 'idle';
  const isReveal = animationPhase === 'reveal';

  return (
    <div className="app" onPointerMove={handleMouseMove}>
      <ParticleBackground mousePos={mousePos} phase={animationPhase} />

      <div className="scene">
        <TreeAnimation
          phase={animationPhase}
          mousePos={mousePos}
          onGrowthComplete={handleGrowthComplete}
        />

        {animationPhase === 'leaves' && (
          <FallingLeaves mousePos={mousePos} onComplete={handleLeavesComplete} />
        )}
      </div>

      <div className="vignette" aria-hidden="true" />
      <div className="light-rays" aria-hidden="true" />

      {isIdle && (
        <div className="controls">
          <button className="btn start-btn" onClick={handleStart}>
            Grow the Tree 🌱
          </button>
          <p className="hint">A quiet night. A tiny seed. Watch it grow.</p>
        </div>
      )}

      {isReveal && (
        <div className="controls">
          <button className="btn replay-btn" onClick={handleReplay}>
            Replay Experience ↻
          </button>
        </div>
      )}

      {isReveal && <BirthdayMessage />}

      <AudioControl />

      <footer className="footer">225</footer>
    </div>
  );
}

export default App;
