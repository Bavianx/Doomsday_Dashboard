# Doomsday Dashboard

An AI-powered geopolitical intelligence dashboard that tracks global threat levels in real time inspired by the Bulletin of Atomic Scientists' Doomsday Clock.

The application aggregates live news data across multiple threat vectors, uses Claude AI to score each headline for threat severity, and calculates a global risk score displayed as a visual clock showing how close the world is to midnight.


**Live Demo:** https://bavianx.pythonanywhere.com/threats/

Note: This is V1. V2 with Globe.gl, Three.js and PostgreSQL is in active development.

---
## Overview
 
The Doomsday Dashboard ingests live news headlines, scores them using AI, calculates a weighted global risk score, and displays everything on a dark-themed intelligence dashboard — complete with a doomsday clock, country risk map, and live market data.

## Live Threat Categories

- **Nuclear** — nuclear weapons, missile tests, proliferation
- **Geopolitical** — conflict, NATO, military escalation
- **Economic** — recession, market instability, sanctions
- **Cyber** — cyberattacks, data breaches, ransomware

---

## Features

- **Live Threat Intelligence Feed** — real-time headlines scored by AI across nuclear, geopolitical, economic, and cyber categories
- **AI Scoring Engine** — each headline is scored 1-10 using the Anthropic Claude API (mock scoring in V1)
- **Weighted Global Risk Score** — calculated using category weights (Nuclear 0.35, Geopolitical 0.25, Economic 0.25, Cyber 0.15)
- **Doomsday Clock** — SVG clock face with hand position driven by the live global risk score
- **Country Risk Map** — Plotly choropleth world map with colour-coded country threat levels
- **Live Search** — search any topic or country and all three columns update with live NewsAPI results
- **World Stock News** — auto-scrolling live market news feed
- **Stock Ticker Bar** — live prices and daily change for SPY, QQQ, GLD, USO via yfinance
- **AI Assessment** — structured intelligence briefing generated from current threat data
- **Responsive Design** — clean dark UI that adapts across screen sizes

---

## In Development

- Version 2

---

## Version 2 Roadmap

- [ ] **Automated Data Refresh** — time-based auto fetch/score/calculate on page load (Celery + Redis)
- [ ] **3D Interactive Globe** — Three.js/Globe.gl spinning globe
- [ ] **Real Time Heartbeat Pulses** — countries pulse with threat activity
- [ ] **Clickable Country Panels** — click any country for detailed threat breakdown
- [ ] **WebSocket Updates** — live score updates without page refresh
- [ ] **React Frontend** — replace Django templates with React components
- [ ] **Microservices Architecture** — separate data ingestion, AI scoring and API services
- [ ] **Redis Caching** — cache live scores for performance
- [ ] **Celery Scheduling** — automated news fetching every hour
- [ ] **Docker Containerisation** — portable deployment
- [ ] **PostgreSQL** — production database replacing SQLite
- [ ] **RAG Pipeline** — AI summary generated from live vector database of threat intelligence
- [ ] **Search Results AI Scoring** — real-time Claude API scoring of search results
- [ ] **AJAX Search** — update columns without page reload
- [ ] **Full World Dataset** — country risk map expanded beyond current static dataset
- [ ] **Real Claude API Scoring** — replace mock scorer with live Anthropic API calls

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django 5.1 |
| Database | SQLite (dev) |
| AI Scoring | Anthropic Claude API |
| News Data | NewsAPI |
| Market Data | yfinance |
| Visualisation | Plotly, SVG |
| Frontend | Bootstrap 5, HTML, CSS, JavaScript |
| Version Control | Git, GitHub |

---
## Learning Context

Built as part of a structured software engineering development programme transitioning from Python scripting and OOP into  full stack Django web development with AI integration.

This project demonstrates:
- Django MTV architecture
- Real world API integration
- AI-powered data analysis
- System design thinking
- Geopolitical and security domain knowledge

## Important Context update for V1 functionality

Visit these URLs in order to populate the dashboard with live data:
 
```
/threats/fetch-news/       — fetch latest headlines from NewsAPI
/threats/score-news/       — AI score each headline
/threats/avg_news_score/   — calculate weighted global risk score
/threats/generate-summary/ — generate AI assessment briefing
```

