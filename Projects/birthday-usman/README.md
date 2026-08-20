# 🎂 Happy Birthday Usman Zafar

A premium, cinematic, single-page birthday experience built with **React + Vite**.

From **Saad Bin Riaz** with love ❤️

## Story

> Seed → Growth → Tree → Falling Leaves → Celebration

Watch a tiny seed grow into a mature tree under a moonlit night sky, feel the
wind move through its leaves, watch autumn leaves fall, and then celebrate:

> **Happy Birthday Usman Zafar**

## Features

- Procedurally grown tree (deterministic, organic easing) on HTML Canvas
- Realistic nature physics: wind, branch sway, leaf sway, gravity, leaf tumbling
- Cinematic night environment: moonlight, stars, fog, fireflies, golden glow
- Interactive camera parallax on mouse move
- "Grow the Tree 🌱" and "Replay Experience ↻" controls
- Optional synthesized ambient wind audio (WebAudio, no autoplay)
- Premium typography (Cormorant Garamond + Inter)
- Fully responsive (desktop / tablet / mobile, adaptive particle counts)
- `prefers-reduced-motion` support
- Vercel-ready static build

## Getting started

```bash
npm install
npm run dev
```

Open the printed local URL.

## Build

```bash
npm run build
npm run preview
```

## Lint

```bash
npm run lint
```

## Deploy to Vercel

```bash
npm i -g vercel
vercel          # preview
vercel --prod   # production
```

Or push to GitHub and import the repository in Vercel — the `vercel.json`
build settings (`npm run build`, output `dist`) are picked up automatically.

## Project structure

```text
birthday-usman/
├── src/
│   ├── components/
│   │   ├── TreeAnimation
│   │   ├── FallingLeaves
│   │   ├── BirthdayMessage
│   │   ├── ParticleBackground
│   │   └── AudioControl
│   ├── App.jsx
│   ├── main.jsx
│   ├── index.css
│   └── styles.css
├── public/
├── package.json
├── vite.config.js
└── README.md
```
