# Python Mastery

A curated collection of clean, well-documented Python projects demonstrating core programming concepts, from data structures and algorithms to API integrations and practical applications.

## Projects

### Shopping Cart System
Full-featured console-based shopping cart with stock management, bill generation, discount calculation, and CSV persistence.

**Features:** Product catalog, cart management, stock tracking, bill search, discount & tax calculation

### Quiz Application
Interactive quiz app with JSON-based question bank, timed questions, score tracking, and highscore leaderboard.

**Features:** Randomized questions, 10-second timer, highscore persistence, shuffle options

### Electricity Bill Calculator
Pakistan K-Electric tariff calculator supporting protected/unprotected consumer types with slab-based billing.

**Features:** Slab-based pricing, duty & GST calculation, protected/unprotected categories

### ATM Simulator
Console-based banking simulator with account management, deposits, withdrawals, and transaction history.

**Features:** Account creation, login, balance check, deposits, withdrawals, transaction history, CSV persistence

### Weather Agent
AI-style weather agent using OpenWeatherMap and Open-Meteo APIs with forecast support.

**Features:** Current weather, 5-day forecast, API fallback, formatted reports, dataclass models

### Birthday Usman
A cinematic birthday experience with procedural tree growth animation on HTML Canvas.

**Features:** Procedural tree growth, realistic nature physics, cinematic night environment, interactive parallax

### httpx Weather Agent
An HTTP client-based weather agent using httpx for async API calls.

**Features:** Async HTTP requests, weather API integration, structured agent pattern

### Wedding Invitation Generator (FastAPI)
A modern wedding invitation generator built with FastAPI and Supabase.

**Features:** 4 Pakistani wedding themes, CSV guest upload, unique invitation links, WhatsApp sharing, personalized invitations

## Tech Stack

- Python 3.10+
- FastAPI + Uvicorn
- Supabase (PostgreSQL + Auth)
- Jinja2 Templates
- Tailwind CSS (CDN)
- requests, pandas

## Getting Started

```bash
git clone https://github.com/SaadRiaz99/Python-Mastery.git
cd Python-Mastery
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your Supabase credentials
python main.py
```

## Project Structure

```
Python-Mastery/
├── Projects/
│   ├── Shopping-Cart/
│   ├── Quiz-App/
│   ├── Electricity-Bill-Calculator/
│   ├── ATM-Simulator/
│   ├── Weather-Agent/
│   ├── birthday-usman/
│   ├── httpx/
│   └── Pakistan-Railway/
├── templates/              # Jinja2 HTML templates
│   ├── base.html
│   ├── home.html
│   ├── create.html
│   ├── dashboard.html
│   └── invite.html
├── routes/                 # FastAPI route modules
│   ├── pages.py
│   └── api.py
├── main.py                 # FastAPI application entry point
├── config.py               # Configuration & environment loading
├── database.py             # Supabase client setup
├── models.py               # Pydantic data models
├── utils.py                # Themes, slug generation, helpers
├── requirements.txt
└── .env.example
```

## Author

**Saad Bin Riaz** — [GitHub](https://github.com/SaadRiaz99)
