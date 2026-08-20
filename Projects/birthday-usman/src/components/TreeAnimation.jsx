import React, { useRef, useEffect } from 'react';

const MAX_DEPTH = 4;
const DEPTH_START = [0.1, 0.2, 0.32, 0.46, 0.58];

const reducedMotion = typeof window !== 'undefined'
  ? window.matchMedia('(prefers-reduced-motion: reduce)').matches
  : false;

const clamp = (v, lo, hi) => (v < lo ? lo : v > hi ? hi : v);

function mulberry32(seed) {
  let a = seed >>> 0;
  return function () {
    a |= 0;
    a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function easeGrowth(t) {
  if (t <= 0) return 0;
  if (t >= 1) return 1;
  return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
}

function buildTree(seed) {
  const rand = mulberry32(seed);
  const branches = [];
  const branchLeaves = [];
  const canopy = [];
  const roots = [];
  let minY = 0;
  let maxSpan = 0;

  const grow = (x, y, angle, len, depth, thick) => {
    const ex = x + Math.cos(angle) * len;
    const ey = y - Math.sin(angle) * len;
    branches.push({ x, y, ex, ey, depth, thick, seed: rand() * 1000, angle });
    minY = Math.min(minY, ey);
    maxSpan = Math.max(maxSpan, Math.abs(ex));

    if (depth >= MAX_DEPTH) return;

    const childCount = depth === 0 ? 3 : 2 + (rand() > 0.72 ? 1 : 0);
    const spread = depth === 0 ? 0.42 : 0.55;
    for (let i = 0; i < childCount; i++) {
      const off = i - (childCount - 1) / 2;
      const a = angle + off * spread + (rand() - 0.5) * 0.18;
      const l = len * (0.68 + rand() * 0.14);
      grow(ex, ey, a, l, depth + 1, thick * (depth === 0 ? 0.58 : 0.66));
    }
  };

  grow(0, 0, Math.PI / 2, 175, 0, 26);

  for (let bi = 0; bi < branches.length; bi++) {
    const b = branches[bi];
    if (b.depth < 1) continue;
    const count = b.depth === 1 ? 2 : b.depth === 2 ? 3 : b.depth === 3 ? 4 : 5;
    for (let i = 0; i < count; i++) {
      const t = 0.55 + rand() * 0.45;
      branchLeaves.push({
        x: b.x + (b.ex - b.x) * t,
        y: b.y + (b.ey - b.y) * t,
        branchIndex: bi,
        size: 12 + rand() * 8,
        shade: rand(),
        seed: rand() * 1000,
        shed: rand(),
      });
    }
  }

  const topY = minY - 40;
  for (let i = 0; i < 64; i++) {
    const r = 26 + rand() * 150;
    const a = rand() * Math.PI * 2;
    canopy.push({
      x: Math.cos(a) * r * 0.85,
      y: topY + Math.sin(a) * r * 0.42,
      size: 17 + rand() * 13,
      shade: rand(),
      seed: rand() * 1000,
      shed: rand(),
      bloom: rand(),
    });
  }

  for (let i = 0; i < 7; i++) {
    const side = i % 2 === 0 ? 1 : -1;
    const spreadX = 40 + rand() * 60;
    roots.push({
      c1x: side * spreadX * 0.3,
      c1y: 18 + rand() * 22,
      c2x: side * spreadX * 0.7,
      c2y: 4 + rand() * 24,
      ex: side * spreadX,
      ey: 30 + rand() * 65,
      side,
      seed: rand() * 100,
    });
  }

  const naturalHeight = -minY + 60;
  return { branches, branchLeaves, canopy, roots, naturalHeight, maxSpan };
}

// Moonlit night palette
const BARK = ['#24150b', '#2f1c0e', '#3a2413'];
const FOLIAGE = ['#23401f', '#2c4f24', '#38602a', '#1e3a1c'];
const FOLIAGE_LIT = ['#3f6a30', '#4a7a38', '#588d3f', '#38602a'];

const TreeAnimation = ({ phase, mousePos, onGrowthComplete }) => {
  const canvasRef = useRef(null);
  const rafRef = useRef(0);
  const timeRef = useRef(0);
  const rawRef = useRef(0);
  const doneRef = useRef(false);
  const shedStartRef = useRef(0);
  const ambientRef = useRef(1);
  const mouseRef = useRef(mousePos);
  const treeRef = useRef(null);

  useEffect(() => {
    mouseRef.current = mousePos;
  }, [mousePos]);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    let width = 0;
    let height = 0;
    let scale = 1;
    let stars = [];
    let grassBlades = [];
    let motes = [];

    if (!treeRef.current) {
      treeRef.current = buildTree(2026);
    }
    const tree = treeRef.current;

    if (phase === 'growing') {
      rawRef.current = 0;
      doneRef.current = false;
    }
    if (phase === 'reveal') {
      rawRef.current = 1;
    }
    if (reducedMotion && (phase === 'leaves' || phase === 'reveal')) {
      rawRef.current = 1;
    }

    const resize = () => {
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      width = window.innerWidth;
      height = window.innerHeight;
      canvas.width = Math.floor(width * dpr);
      canvas.height = Math.floor(height * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

      const targetHeight = height * 0.42;
      scale = Math.min(targetHeight / tree.naturalHeight, (width * 0.9) / (tree.maxSpan * 2.4));

      const rand = mulberry32(99);
      const starCount = reducedMotion ? 40 : Math.min(150, Math.floor((width * height) / 9000));
      stars = Array.from({ length: starCount }, () => ({
        x: rand() * width,
        y: rand() * height * 0.72,
        r: 0.4 + rand() * 1.1,
        phase: rand() * Math.PI * 2,
        speed: 0.004 + rand() * 0.012,
        bright: 0.25 + rand() * 0.6,
      }));

      const bladeCount = reducedMotion ? 24 : Math.min(90, Math.floor(width / 14));
      grassBlades = Array.from({ length: bladeCount }, (_, i) => ({
        x: (i * 149) % width,
        h: 8 + ((i * 73) % 18),
        lean: (i % 3) - 1,
        phase: rand() * Math.PI * 2,
      }));

      const moteCount = reducedMotion ? 0 : width < 640 ? 8 : 14;
      const cx = width / 2;
      const gy = height * 0.75;
      motes = Array.from({ length: moteCount }, () => ({
        x: cx + (rand() - 0.5) * width * 0.3,
        y: gy - rand() * height * 0.3,
        r: 1 + rand() * 2,
        vy: 0.2 + rand() * 0.5,
        vx: (rand() - 0.5) * 0.3,
        phase: rand() * Math.PI * 2,
        alpha: 0.3 + rand() * 0.4,
      }));
    };
    resize();
    window.addEventListener('resize', resize);

    const draw = (time) => {
      ctx.clearRect(0, 0, width, height);

      const raw = rawRef.current;
      const p = phase === 'growing' ? easeGrowth(raw) : phase === 'idle' ? 0 : 1;
      const ambient = ambientRef.current;
      const windBase = Math.sin(time * 0.0016) * 0.7 + Math.sin(time * 0.0009 + 1.3) * 0.5;
      const wind = windBase * (phase === 'leaves' ? 1.7 : phase === 'reveal' ? 1.2 : 1);
      const px = (mouseRef.current.x - 0.5) * scale * 0.35;
      const py = (mouseRef.current.y - 0.5) * scale * 0.2;

      const groundY = height * 0.75;
      const centerX = width / 2;
      const moonX = width * 0.76;
      const moonY = height * 0.17;

      // --- Night sky ---
      const sky = ctx.createLinearGradient(0, 0, 0, groundY);
      sky.addColorStop(0, '#020509');
      sky.addColorStop(0.45, '#06101f');
      sky.addColorStop(0.8, '#0b1a2e');
      sky.addColorStop(1, '#0e2238');
      ctx.fillStyle = sky;
      ctx.fillRect(0, 0, width, groundY);

      // --- Moonlight wash from the moon ---
      const moonGlow = ctx.createRadialGradient(moonX, moonY, 0, moonX, moonY, Math.min(width, height) * 0.7);
      moonGlow.addColorStop(0, 'rgba(170, 195, 235, 0.14)');
      moonGlow.addColorStop(0.35, 'rgba(170, 195, 235, 0.05)');
      moonGlow.addColorStop(1, 'rgba(170, 195, 235, 0)');
      ctx.fillStyle = moonGlow;
      ctx.fillRect(0, 0, width, groundY);

      // --- Stars ---
      for (const s of stars) {
        const tw = 0.5 + 0.5 * Math.sin(time * s.speed + s.phase);
        ctx.globalAlpha = s.bright * tw * (0.35 + 0.65 * clamp(p * 1.4, 0, 1));
        ctx.fillStyle = '#cfe0ff';
        ctx.beginPath();
        ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
        ctx.fill();
      }
      ctx.globalAlpha = 1;

      // --- Moon ---
      const mr = Math.min(width, height) * 0.052;
      const moonDisc = ctx.createRadialGradient(moonX - mr * 0.25, moonY - mr * 0.25, mr * 0.1, moonX, moonY, mr);
      moonDisc.addColorStop(0, '#f4f7ff');
      moonDisc.addColorStop(0.7, '#e4ecfb');
      moonDisc.addColorStop(1, '#c9d8f0');
      ctx.fillStyle = moonDisc;
      ctx.beginPath();
      ctx.arc(moonX, moonY, mr, 0, Math.PI * 2);
      ctx.fill();
      // craters
      ctx.globalAlpha = 0.18;
      ctx.fillStyle = '#aebfdc';
      for (const [ox, oy, orr] of [[-0.32, -0.1, 0.18], [0.28, 0.2, 0.13], [0.05, -0.35, 0.1], [0.38, -0.3, 0.08]]) {
        ctx.beginPath();
        ctx.arc(moonX + mr * ox, moonY + mr * oy, mr * orr, 0, Math.PI * 2);
        ctx.fill();
      }
      ctx.globalAlpha = 1;

      // --- Distant hills (depth) ---
      ctx.fillStyle = 'rgba(8, 18, 32, 0.9)';
      ctx.beginPath();
      ctx.moveTo(0, groundY);
      for (let x = 0; x <= width; x += 20) {
        ctx.lineTo(x, groundY - height * 0.05 - Math.sin(x * 0.006) * height * 0.02 - Math.sin(x * 0.013 + 2) * height * 0.012);
      }
      ctx.lineTo(width, groundY);
      ctx.closePath();
      ctx.fill();

      // --- Ground ---
      const ground = ctx.createLinearGradient(0, groundY, 0, height);
      ground.addColorStop(0, '#0e1c14');
      ground.addColorStop(0.35, '#0a150f');
      ground.addColorStop(1, '#060b08');
      ctx.fillStyle = ground;
      ctx.fillRect(0, groundY, width, height - groundY);

      // moonlight sheen on ground
      const sheen = ctx.createRadialGradient(moonX, groundY, 0, moonX, groundY, width * 0.5);
      sheen.addColorStop(0, 'rgba(170, 195, 235, 0.08)');
      sheen.addColorStop(1, 'rgba(170, 195, 235, 0)');
      ctx.fillStyle = sheen;
      ctx.fillRect(0, groundY, width, height - groundY);

      // --- Grass silhouettes ---
      ctx.strokeStyle = '#13281c';
      ctx.lineWidth = 1.6;
      ctx.lineCap = 'round';
      for (const g of grassBlades) {
        const sway = Math.sin(time * 0.0035 + g.phase) * (1 + wind * 0.6);
        ctx.beginPath();
        ctx.moveTo(g.x, groundY + 3);
        ctx.quadraticCurveTo(
          g.x + g.lean * 3 + sway * 0.5,
          groundY - g.h * 0.5,
          g.x + g.lean * 5 + sway,
          groundY - g.h
        );
        ctx.stroke();
      }

      // --- World transform (tree space) ---
      ctx.save();
      ctx.translate(centerX + px, groundY + py);
      ctx.scale(scale, scale);

      // Soil mound (moonlit dark earth)
      const soilAlpha = clamp(p * 3, 0.25, 1);
      ctx.globalAlpha = soilAlpha;
      const soilGrad = ctx.createLinearGradient(0, -14, 0, 26);
      soilGrad.addColorStop(0, '#33200f');
      soilGrad.addColorStop(1, '#1a1007');
      ctx.fillStyle = soilGrad;
      ctx.beginPath();
      ctx.ellipse(0, 9, 100, 18, 0, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = 'rgba(140, 160, 120, 0.08)';
      ctx.beginPath();
      ctx.ellipse(0, 6, 92, 10, 0, 0, Math.PI * 2);
      ctx.fill();
      ctx.globalAlpha = 1;

      // Roots (tapered organic curves)
      const rootP = clamp((p - 0.02) / 0.38, 0, 1);
      ctx.lineCap = 'round';
      for (const r of tree.roots) {
        const len = rootP;
        if (len <= 0.02) continue;
        const sx = r.c1x * len;
        const sy = r.c1y * len;
        const sx2 = r.c2x * len;
        const sy2 = r.c2y * len;
        const ex = r.ex * len;
        const ey = r.ey * len;
        // underlay
        ctx.strokeStyle = 'rgba(12, 8, 4, 0.85)';
        ctx.lineWidth = 7 * len;
        ctx.beginPath();
        ctx.moveTo(0, 9);
        ctx.bezierCurveTo(sx, sy, sx2, sy2, ex, ey);
        ctx.stroke();
        // bark
        ctx.strokeStyle = '#3a2413';
        ctx.lineWidth = 4.4 * len;
        ctx.beginPath();
        ctx.moveTo(0, 9);
        ctx.bezierCurveTo(sx, sy, sx2, sy2, ex, ey);
        ctx.stroke();
        // moonlit top highlight
        ctx.strokeStyle = 'rgba(190, 175, 130, 0.14)';
        ctx.lineWidth = 1.6 * len;
        ctx.beginPath();
        ctx.moveTo(0, 8);
        ctx.bezierCurveTo(sx, sy * 0.92, sx2, sy2 * 0.92, ex, ey);
        ctx.stroke();
      }

      // Seed
      const seedP = clamp((0.12 - p) / 0.1, 0, 1);
      if (seedP > 0) {
        ctx.globalAlpha = seedP;
        ctx.fillStyle = '#6a4418';
        ctx.beginPath();
        ctx.ellipse(0, 3, 7, 4.5, 0.3, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = 'rgba(220, 200, 150, 0.25)';
        ctx.beginPath();
        ctx.ellipse(-1.5, 1.5, 2.6, 1.6, 0.3, 0, Math.PI * 2);
        ctx.fill();
        ctx.globalAlpha = 1;
      }

      // Life glow while sprouting
      const sproutGlow = clamp((0.2 - p) / 0.18, 0, 1);
      if (sproutGlow > 0) {
        const g = ctx.createRadialGradient(0, 0, 0, 0, 0, 130 * (1 - p * 0.4));
        g.addColorStop(0, `rgba(160, 255, 160, ${0.28 * sproutGlow})`);
        g.addColorStop(1, 'rgba(160, 255, 160, 0)');
        ctx.fillStyle = g;
        ctx.beginPath();
        ctx.arc(0, 0, 130, 0, Math.PI * 2);
        ctx.fill();
      }

      // Moonlit shadow of the tree
      ctx.globalAlpha = 0.3 * p;
      ctx.fillStyle = '#000000';
      ctx.beginPath();
      ctx.ellipse(px * 0.1, 15, 108 * p, 11, 0, 0, Math.PI * 2);
      ctx.fill();
      ctx.globalAlpha = 1;

      // --- Trunk & branches (organic curves, tapered) ---
      const branchP = tree.branches.map((b) => clamp((p - DEPTH_START[b.depth]) / 0.5, 0, 1));
      ctx.lineCap = 'round';
      for (let i = 0; i < tree.branches.length; i++) {
        const b = tree.branches[i];
        const bp = branchP[i];
        if (bp <= 0) continue;

        const sway = Math.sin(time * 0.002 + b.seed) * wind * (0.5 + b.depth * 0.45) * 5;
        const ex = b.x + (b.ex - b.x) * bp + sway;
        const ey = b.y + (b.ey - b.y) * bp + sway * 0.3 * Math.sin(b.seed * 7);
        const cx = (b.x + ex) / 2 + Math.sin(b.seed * 3.1) * 14;
        const cy = (b.y + ey) / 2 - Math.cos(b.seed * 2.7) * 9;
        const lw = Math.max(0.8, b.thick * bp);
        const bark = BARK[Math.min(b.depth, BARK.length - 1)];

        // silhouette underlay
        ctx.strokeStyle = 'rgba(10, 7, 4, 0.8)';
        ctx.lineWidth = lw * 1.7;
        ctx.beginPath();
        ctx.moveTo(b.x, b.y);
        ctx.quadraticCurveTo(cx, cy, ex, ey);
        ctx.stroke();

        // bark body
        ctx.strokeStyle = bark;
        ctx.lineWidth = lw;
        ctx.beginPath();
        ctx.moveTo(b.x, b.y);
        ctx.quadraticCurveTo(cx, cy, ex, ey);
        ctx.stroke();

        // moonlit rim on top side
        ctx.strokeStyle = 'rgba(196, 182, 138, 0.16)';
        ctx.lineWidth = Math.max(0.7, lw * 0.3);
        ctx.beginPath();
        ctx.moveTo(b.x, b.y - lw * 0.16);
        ctx.quadraticCurveTo(cx, cy - lw * 0.12, ex, ey - lw * 0.12);
        ctx.stroke();
      }

      // --- Canopy (individual leaves, moonlit) ---
      const shedFrac = clamp((performance.now() - shedStartRef.current) / 9000, 0, 1);
      const phaseShed = phase === 'leaves' || phase === 'reveal';

      const drawLeaf = (x, y, size, shade, alpha, seed) => {
        if (alpha <= 0.02) return;
        const sway = Math.sin(time * 0.0035 + seed) * (1.2 + wind * 1.6);
        const lx = x + sway;
        const ly = y + Math.abs(sway) * 0.22;
        const tilt = Math.sin(time * 0.0022 + seed * 1.7) * 0.35;
        const rx = size;
        const ry = size * 0.46;
        const ci = Math.floor(shade * FOLIAGE.length);
        const base = FOLIAGE[ci];
        const lit = FOLIAGE_LIT[ci];

        ctx.save();
        ctx.translate(lx, ly);
        ctx.rotate(tilt);
        ctx.globalAlpha = alpha;
        // base leaf
        ctx.fillStyle = base;
        ctx.beginPath();
        ctx.ellipse(0, 0, rx, ry, 0, 0, Math.PI * 2);
        ctx.fill();
        // moonlit highlight toward the moon (upper area)
        ctx.fillStyle = lit;
        ctx.beginPath();
        ctx.ellipse(rx * 0.12, -ry * 0.22, rx * 0.62, ry * 0.52, -0.3, 0, Math.PI * 2);
        ctx.fill();
        // soft specular
        ctx.fillStyle = 'rgba(205, 230, 170, 0.18)';
        ctx.beginPath();
        ctx.ellipse(rx * 0.2, -ry * 0.34, rx * 0.3, ry * 0.22, -0.35, 0, Math.PI * 2);
        ctx.fill();
      ctx.restore();

      // --- Golden celebration aura + rising motes at reveal ---
      if (phase === 'reveal' && ambient > 1.02) {
        const glowX = centerX;
        const glowY = groundY - height * 0.18;
        const auraR = Math.min(width, height) * (0.17 + 0.05 * Math.sin(time * 0.003));
        const auraG = ctx.createRadialGradient(glowX, glowY, 0, glowX, glowY, auraR);
        auraG.addColorStop(0, `rgba(255, 214, 140, ${0.12 * (ambient - 1)})`);
        auraG.addColorStop(0.6, `rgba(255, 214, 140, ${0.05 * (ambient - 1)})`);
        auraG.addColorStop(1, 'rgba(255, 214, 140, 0)');
        ctx.fillStyle = auraG;
        ctx.fillRect(glowX - auraR, glowY - auraR, auraR * 2, auraR * 2);

        for (const m of motes) {
          m.y -= m.vy * (ambient - 1);
          m.x += m.vx + Math.sin(time * 0.002 + m.phase) * 0.15;
          const tw = 0.5 + 0.5 * Math.sin(time * 0.012 + m.phase);
          const mg = ctx.createRadialGradient(m.x, m.y, 0, m.x, m.y, m.r * 5);
          mg.addColorStop(0, `rgba(255, 220, 160, ${0.55 * tw * m.alpha * (ambient - 1)})`);
          mg.addColorStop(1, 'rgba(255, 220, 160, 0)');
          ctx.fillStyle = mg;
          ctx.fillRect(m.x - m.r * 5, m.y - m.r * 5, m.r * 10, m.r * 10);
          if (m.y < height * 0.08) {
            m.y = groundY - height * 0.3;
            m.x = glowX + (Math.random() - 0.5) * width * 0.3;
          }
        }
      }
        ctx.globalAlpha = 1;
      };

      const leafDensity = width < 640 ? 0.55 : 1;

      for (const leaf of tree.branchLeaves) {
        if (leaf.seed * 100 < (1 - leafDensity) * 1000) continue;
        const bp = branchP[leaf.branchIndex];
        const bloom = clamp((bp - 0.5) / 0.4, 0, 1);
        if (bloom <= 0) continue;
        const falloff = phaseShed && leaf.shed > 0.72 ? 1 - shedFrac * ((leaf.shed - 0.72) / 0.28) : 1;
        const alpha = clamp(bloom * falloff, 0, 1) * 0.95;
        drawLeaf(leaf.x, leaf.y, leaf.size * 0.78 * (0.6 + 0.4 * bloom), leaf.shade, alpha, leaf.seed);
      }

      const canopyP = clamp((p - 0.45) / 0.4, 0, 1);
      if (canopyP > 0) {
        for (const leaf of tree.canopy) {
          const bloom = clamp((canopyP - leaf.bloom * 0.25) / 0.75, 0, 1);
          if (bloom <= 0) continue;
          const falloff = phaseShed && leaf.shed > 0.72 ? 1 - shedFrac * ((leaf.shed - 0.72) / 0.28) : 1;
          const alpha = clamp(bloom * falloff, 0, 1) * 0.95;
          drawLeaf(leaf.x, leaf.y, leaf.size * 0.85 * (0.6 + 0.4 * bloom), leaf.shade, alpha, leaf.seed);
        }
      }

      ctx.restore();

      // --- Ground fog drifting across the base ---
      for (let i = 0; i < 5; i++) {
        const fw = width * 0.5;
        const fx = ((time * 0.004 * (1 + i * 0.18) + i * 213) % (width + fw)) - fw / 2;
        const fy = groundY + 4 + ((i * 37) % 14);
        const fg = ctx.createRadialGradient(fx, fy, 0, fx, fy, fw * 0.32);
        fg.addColorStop(0, `rgba(150, 170, 200, ${0.05 + i * 0.008})`);
        fg.addColorStop(1, 'rgba(150, 170, 200, 0)');
        ctx.fillStyle = fg;
        ctx.fillRect(fx - fw * 0.32, fy - 40, fw * 0.64, 90);
      }

      // --- Ambient brightening at reveal ---
      if (ambient > 1.01) {
        ctx.fillStyle = `rgba(255, 240, 190, ${(ambient - 1) * 0.1})`;
        ctx.fillRect(0, 0, width, height);
      }
    };

    const animate = () => {
      timeRef.current += 16;
      const time = timeRef.current;

      if (phase === 'growing') {
        rawRef.current = Math.min(rawRef.current + (reducedMotion ? 1 : 0.0034), 1);
        if (rawRef.current >= 1 && !doneRef.current) {
          doneRef.current = true;
          shedStartRef.current = performance.now();
          onGrowthComplete();
        }
      } else if (phase === 'idle') {
        rawRef.current = 0;
        doneRef.current = false;
      }

      const targetAmbient = phase === 'reveal' ? 1.35 : 1;
      ambientRef.current += (targetAmbient - ambientRef.current) * 0.012;

      draw(time);
      rafRef.current = requestAnimationFrame(animate);
    };

    if (reducedMotion) {
      rawRef.current = phase === 'growing' ? 0 : 1;
      ambientRef.current = phase === 'reveal' ? 1.35 : 1;
      draw(0);
      rafRef.current = requestAnimationFrame(animate);
    } else {
      rafRef.current = requestAnimationFrame(animate);
    }

    return () => {
      window.removeEventListener('resize', resize);
      cancelAnimationFrame(rafRef.current);
    };
  }, [phase, onGrowthComplete]);

  return <canvas ref={canvasRef} className="tree-canvas" aria-hidden="true" />;
};

export default TreeAnimation;
