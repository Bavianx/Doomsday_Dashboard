# Doomsday Dashboard

An AI-powered geopolitical intelligence dashboard that tracks 
global threat levels in real time inspired by the Bulletin 
of Atomic Scientists' Doomsday Clock.

The application aggregates live news data across multiple 
threat vectors, uses Claude AI to score each headline for 
threat severity, and calculates a global risk score displayed 
as a visual clock showing how close the world is to midnight.

---

## Live Threat Categories

- **Nuclear** — nuclear weapons, missile tests, proliferation
- **Geopolitical** — conflict, NATO, military escalation
- **Economic** — recession, market instability, sanctions
- **Cyber** — cyberattacks, data breaches, ransomware

---

## Current Features

- Live news ingestion via NewsAPI across all threat categories
- Django ORM models for ThreatScore, NewsItem and AISummary
- Duplicate prevention using `get_or_create`
- Django admin panel for data management
- Environment variable protection for API keys

---

## In Development

- **Claude AI Scoring** — each headline scored 1-10 for threat severity
- **Global Risk Score** — weighted average across all threat vectors
- **AI Daily Briefing** — Claude generates a morning intelligence summary
- **Dashboard Frontend** — live news feed, risk scores, threat breakdown
- **Doomsday Clock Visual** — animated clock face showing minutes to midnight
- **Stock Ticker** — live market data scrolling across the top
- **Country Risk Map** — Plotly choropleth map with country threat levels

---

## Version 2 Roadmap

- **3D Interactive Globe** — Three.js/Globe.gl spinning globe
- **Real Time Heartbeat Pulses** — countries pulse with threat activity
- **Clickable Country Panels** — click any country for detailed threat breakdown
- **WebSocket Updates** — live score updates without page refresh
- **React Frontend** — replace Django templates with React components
- **Microservices Architecture** — separate data ingestion, AI scoring and API services
- **Redis Caching** — cache live scores for performance
- **Celery Scheduling** — automated news fetching every hour
- **Docker Containerisation** — portable deployment
- **PostgreSQL** — production database replacing SQLite

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3, Django 5.1 |
| Database | SQLite (dev) → PostgreSQL (prod) |
| AI Scoring | Anthropic Claude API |
| News Data | NewsAPI |
| Frontend | Bootstrap 5, Django Templates |
| Future Frontend | React, Three.js, Globe.gl |
| Deployment | Railway / AWS (planned) |

---
## Learning Context

Built as part of a structured software engineering development 
programme transitioning from Python scripting and OOP into 
full stack Django web development with AI integration.

This project demonstrates:
- Django MTV architecture
- Real world API integration
- AI-powered data analysis
- System design thinking
- Geopolitical and security domain knowledge

