import React, { useRef, useEffect, useCallback } from 'react';

const reducedMotion = typeof window !== 'undefined'
  ? window.matchMedia('(prefers-reduced-motion: reduce)').matches
  : false;

function makeLeafSprite(hue, size) {
  const pad = 3;
  const c = document.createElement('canvas');
  c.width = c.height = size + pad * 2;
  const g = c.getContext('2d');
  const cx = c.width / 2;
  const cy = c.height / 2;
  const s = size / 2;
  const grad = g.createLinearGradient(-s, -s, s, s);
  grad.addColorStop(0, `hsl(${hue}, 65%, 48%)`);
  grad.addColorStop(0.55, `hsl(${hue}, 62%, 36%)`);
  grad.addColorStop(1, `hsl(${hue}, 58%, 25%)`);
  g.fillStyle = grad;
  g.beginPath();
  g.ellipse(cx, cy, s, s * 0.5, 0, 0, Math.PI * 2);
  g.fill();
  g.strokeStyle = `hsla(${hue}, 45%, 14%, 0.85)`;
  g.lineWidth = 1;
  g.beginPath();
  g.moveTo(cx - s * 0.8, cy);
  g.quadraticCurveTo(cx, cy - s * 0.35, cx + s * 0.8, cy);
  g.stroke();
  return c;
}

const FallingLeaves = ({ mousePos, onComplete }) => {
  const canvasRef = useRef(null);
  const rafRef = useRef(0);
  const leavesRef = useRef([]);
  const spawnedRef = useRef(0);
  const totalRef = useRef(0);
  const completeSentRef = useRef(false);
  const timeoutsRef = useRef([]);
  const mouseRef = useRef(mousePos);

  useEffect(() => {
    mouseRef.current = mousePos;
  }, [mousePos]);

  const createLeaf = useCallback((x, y) => {
    const hue = 100 + Math.random() * 50;
    return {
      x,
      y,
      vx: (Math.random() - 0.5) * 0.8,
      vy: 0.4 + Math.random() * 0.5,
      rotation: Math.random() * Math.PI * 2,
      rotSpeed: (Math.random() - 0.5) * 0.12,
      size: 7 + Math.random() * 7,
      swayAmp: 1 + Math.random() * 2.5,
      swayFreq: 0.012 + Math.random() * 0.02,
      swayPhase: Math.random() * Math.PI * 2,
      gustPhase: Math.random() * Math.PI * 2,
      gustMag: 0.4 + Math.random() * 1.2,
      alpha: 0.75 + Math.random() * 0.25,
      landY: 0,
      landed: false,
      sprite: Math.floor(Math.random() * 4),
      hue,
      tumble: 0.0006 + Math.random() * 0.0012,
    };
  }, []);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    let width = 0;
    let height = 0;
    let groundY = 0;
    let centerX = 0;
    let time = 0;

    const sprites = [
      makeLeafSprite(100, 30),
      makeLeafSprite(118, 34),
      makeLeafSprite(132, 28),
      makeLeafSprite(108, 32),
    ];

    const resize = () => {
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      width = window.innerWidth;
      height = window.innerHeight;
      canvas.width = Math.floor(width * dpr);
      canvas.height = Math.floor(height * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      groundY = height * 0.75;
      centerX = width / 2;
    };
    resize();
    window.addEventListener('resize', resize);

    const isMobile = width < 640;
    const count = reducedMotion ? 6 : isMobile ? 26 : 42;
    totalRef.current = count;
    leavesRef.current = [];
    spawnedRef.current = 0;
    completeSentRef.current = false;

    const spawn = () => {
      if (spawnedRef.current >= totalRef.current) return;
      const spreadX = Math.min(width * 0.22, 260);
      const leaf = createLeaf(
        centerX + (Math.random() - 0.5) * spreadX,
        groundY - height * (0.28 + Math.random() * 0.16)
      );
      leavesRef.current.push(leaf);
      spawnedRef.current += 1;
      const delay = reducedMotion ? 90 : 170 + Math.random() * 90;
      if (spawnedRef.current < totalRef.current) {
        timeoutsRef.current.push(setTimeout(spawn, delay));
      }
    };
    timeoutsRef.current.push(setTimeout(spawn, reducedMotion ? 60 : 120));

    const drawLeaf = (leaf) => {
      ctx.save();
      ctx.translate(leaf.x, leaf.y);
      ctx.rotate(leaf.rotation);
      ctx.globalAlpha = leaf.alpha * (leaf.landed ? 0.5 : 1);
      const dim = leaf.size + 6;
      ctx.drawImage(sprites[leaf.sprite], -dim / 2, -dim / 2, dim, dim);
      ctx.restore();
    };

    const animate = () => {
      time += 16;
      ctx.clearRect(0, 0, width, height);

      const gust = Math.sin(time * 0.003) * 1.4 + Math.sin(time * 0.0011 + 2.4) * 2.2;
      const mx = mouseRef.current.x * width;
      const my = mouseRef.current.y * height;

      let allLanded = true;
      for (const leaf of leavesRef.current) {
        if (leaf.landed) {
          drawLeaf(leaf);
          continue;
        }

        const sway = Math.sin(time * leaf.swayFreq + leaf.swayPhase) * leaf.swayAmp;
        const windX = sway * 0.05 + gust * 0.01 * leaf.gustMag + Math.sin(time * 0.0018 + leaf.gustPhase) * 0.3;

        leaf.vy = Math.min(leaf.vy + 0.022, 1.5);
        leaf.vx = leaf.vx * 0.985 + windX * 0.35;
        leaf.vx = Math.max(-1.8, Math.min(1.8, leaf.vx));

        // Pointer interaction
        const dx = leaf.x - mx;
        const dy = leaf.y - my;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < 90) {
          const push = (90 - dist) / 90;
          leaf.vx += (dx / (dist || 1)) * push * 0.18;
          leaf.vy -= push * 0.05;
        }

        leaf.x += leaf.vx;
        leaf.y += leaf.vy;
        leaf.rotation += leaf.rotSpeed + Math.sin(time * leaf.tumble * 1000) * 0.004;

        if (leaf.y >= groundY - (2 + Math.random() * 26)) {
          leaf.landed = true;
          leaf.landY = groundY - 2;
          leaf.y = groundY - 2;
          leaf.vx *= 0.4;
        }
        drawLeaf(leaf);
      }

      if (spawnedRef.current >= totalRef.current && leavesRef.current.length > 0) {
        allLanded = leavesRef.current.every((leaf) => leaf.landed);
      } else {
        allLanded = false;
      }

      if (allLanded && !completeSentRef.current) {
        completeSentRef.current = true;
        setTimeout(() => onComplete(), reducedMotion ? 200 : 900);
      }

      rafRef.current = requestAnimationFrame(animate);
    };

    if (reducedMotion) {
      // Simplified: drop the handful of leaves immediately
      for (let i = 0; i < count; i++) {
        leavesRef.current.push(createLeaf(
          centerX + (Math.random() - 0.5) * 200,
          groundY - height * 0.3
        ));
      }
      spawnedRef.current = count;
      animate();
    } else {
      rafRef.current = requestAnimationFrame(animate);
    }

    return () => {
      window.removeEventListener('resize', resize);
      cancelAnimationFrame(rafRef.current);
      timeoutsRef.current.forEach((id) => clearTimeout(id));
      timeoutsRef.current = [];
    };
  }, [createLeaf, onComplete]);

  return <canvas ref={canvasRef} className="leaves-canvas" aria-hidden="true" />;
};

export default FallingLeaves;
