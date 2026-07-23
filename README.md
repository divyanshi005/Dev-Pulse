# DevPulse

DevPulse is a data engineering project that collects data from developer platforms such as GitHub, Reddit, Stack Exchange, and job APIs.

The project builds an analytics warehouse that answers questions such as:

- Which repositories are trending?
- Which programming languages are growing?
- Which AI frameworks are gaining popularity?
- Which skills are most requested in software engineering jobs?

## Tech Stack

- Python
- PostgreSQL
- SQLAlchemy
- Streamlit
- Docker
- GitHub Codespaces

## Project Architecture

API Sources
↓
Extractors
↓
Raw Storage
↓
Staging
↓
Warehouse
↓
Analytics Views
↓
Dashboard