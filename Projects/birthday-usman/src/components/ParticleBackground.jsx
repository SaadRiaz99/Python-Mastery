import React, { useRef, useEffect } from 'react';

const reducedMotion = typeof window !== 'undefined'
  ? window.matchMedia('(prefers-reduced-motion: reduce)').matches
  : false;

const ParticleBackground = ({ mousePos, phase }) => {
  const canvasRef = useRef(null);
  const mouseRef = useRef(mousePos);

  useEffect(() => {
    mouseRef.current = mousePos;
  }, [mousePos]);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    let raf = 0;
    let width = 0;
    let height = 0;
    let sparkles = [];
    let confetti = [];
    let time = 0;

    const resize = () => {
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      width = window.innerWidth;
      height = window.innerHeight;
      canvas.width = Math.floor(width * dpr);
      canvas.height = Math.floor(height * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

      const isMobile = width < 640;
      const sparkleCount = reducedMotion ? 0 : isMobile ? 18 : 34;
      sparkles = Array.from({ length: sparkleCount }, () => ({
        x: Math.random() * width,
        y: Math.random() * height,
        r: 0.8 + Math.random() * 1.8,
        vx: (Math.random() - 0.5) * 0.15,
        vy: -0.08 - Math.random() * 0.2,
        baseAlpha: 0.1 + Math.random() * 0.25,
        hue: Math.random() > 0.6 ? 45 : 90,
        swayPhase: Math.random() * Math.PI * 2,
        swayFreq: 0.0006 + Math.random() * 0.0012,
      }));

      const confettiCount = reducedMotion ? 0 : isMobile ? 20 : 40;
      confetti = Array.from({ length: confettiCount }, () => ({
        x: width / 2 + (Math.random() - 0.5) * width * 0.55,
        y: height * 0.25 + (Math.random() - 0.5) * height * 0.45,
        r: 1.5 + Math.random() * 3,
        alpha: 0.1 + Math.random() * 0.25,
        vx: (Math.random() - 0.5) * 0.4,
        vy: (Math.random() - 0.5) * 0.3,
        phase: Math.random() * Math.PI * 2,
        hue: Math.random() * 60 - 15,
      }));
    };

    const draw = () => {
      time += 1;
      ctx.clearRect(0, 0, width, height);

      const px = mouseRef.current.x - 0.5;
      const py = mouseRef.current.y - 0.5;

      // Gentle light from above
      const rays = ctx.createLinearGradient(0, 0, 0, height);
      rays.addColorStop(0, 'rgba(255, 250, 220, 0.12)');
      rays.addColorStop(0.5, 'rgba(255, 250, 220, 0)');
      ctx.fillStyle = rays;
      ctx.fillRect(0, 0, width, height);

      // Floating sparkles
      for (const s of sparkles) {
        s.x += s.vx + Math.sin(time * s.swayFreq * 30 + s.swayPhase) * 0.2 + px * 0.2;
        s.y += s.vy + py * 0.1;
        if (s.y < -10) { s.y = height + 10; s.x = Math.random() * width; }
        if (s.x < -10) s.x = width + 10;
        if (s.x > width + 10) s.x = -10;

        const flicker = 0.5 + 0.5 * Math.sin(time * 0.02 + s.swayPhase);
        const g = ctx.createRadialGradient(s.x, s.y, 0, s.x, s.y, s.r * 6);
        g.addColorStop(0, `hsla(${s.hue}, 95%, 75%, ${0.45 * flicker})`);
        g.addColorStop(1, `hsla(${s.hue}, 95%, 75%, 0)`);
        ctx.fillStyle = g;
        ctx.beginPath();
        ctx.arc(s.x, s.y, s.r * 6, 0, Math.PI * 2);
        ctx.fill();
      }

      // Golden celebration confetti after growth
      if (phase === 'leaves' || phase === 'reveal') {
        for (const c of confetti) {
          c.x += c.vx;
          c.y += c.vy;
          if (c.x < 0 || c.x > width) c.vx *= -1;
          if (c.y < 0 || c.y > height) c.vy *= -1;
          const tw = 0.5 + 0.5 * Math.sin(time * 0.03 + c.phase);
          const g = ctx.createRadialGradient(c.x, c.y, 0, c.x, c.y, c.r * 6);
          g.addColorStop(0, `hsla(${40 + c.hue}, 100%, 75%, ${c.alpha * tw})`);
          g.addColorStop(1, 'hsla(45, 100%, 75%, 0)');
          ctx.fillStyle = g;
          ctx.beginPath();
          ctx.arc(c.x, c.y, c.r * 6, 0, Math.PI * 2);
          ctx.fill();
        }
      }

      raf = requestAnimationFrame(draw);
    };

    resize();
    window.addEventListener('resize', resize);
    if (reducedMotion) {
      draw();
      cancelAnimationFrame(raf);
    } else {
      raf = requestAnimationFrame(draw);
    }

    return () => {
      window.removeEventListener('resize', resize);
      cancelAnimationFrame(raf);
    };
  }, [phase]);

  return <canvas ref={canvasRef} className="particles-canvas" aria-hidden="true" />;
};

export default ParticleBackground;
