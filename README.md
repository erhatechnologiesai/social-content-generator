# Multi-Platform Social Content Generator

[![Python 3.12](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

An omnichannel content repurposing engine that transforms core ideas or articles into platform-optimized posts for LinkedIn, X (Twitter), and Threads.

---

## Key Features

- **Platform-specific**: formatting rules (character limits, hashtag density, tone)
- **LinkedIn**: thought-leadership post generation with engagement hooks
- **X**: / Twitter thread generation with numbered sequential tweets
- **Call-to-Action**: (CTA) optimizer for maximizing link clicks and shares
- **Batch**: export for social media scheduling tools (Buffer, Hootsuite)

---

## Architecture

```mermaid
flowchart TD
    Source([Long-Form Article / Core Idea]) --> Engine[Repurposing Engine]
    Engine --> LinkedIn[LinkedIn Professional Post]
    Engine --> Twitter[X / Twitter Thread]
    Engine --> Threads[Threads Casual Post]
    LinkedIn --> Package[Omnichannel Social Media Package]
    Twitter --> Package
    Threads --> Package
```

---

## Tech Stack

| Component | Technology | Purpose |
|---|---|---|
| **Runtime** | Python 3.12 | Core execution environment |
| **API Framework** | FastAPI & Uvicorn | High-performance asynchronous REST endpoints |
| **Data Validation** | Pydantic v2 | Strict schema validation and serialization |
| **Execution Engine** | Dual-Mode (Local + Cloud) | Production-ready logic with offline verification |
| **Testing** | Unittest & Pytest | Deterministic automated verification suite |

---

## Project Structure

```text
social-content-generator/
├── app/
│   ├── __init__.py
│   ├── api.py           # FastAPI routes and server definitions
│   ├── config.py        # Environment variables and application settings
│   ├── models.py        # Pydantic data schemas
│   └── services/        # Core business automation logic
├── tests/
│   ├── __init__.py
│   └── test_social_generator.py   # Automated test suite
├── .env.example         # Template for environment configuration
├── .gitignore           # Python and runtime exclusions
├── LICENSE              # MIT License
├── README.md            # Comprehensive project documentation
└── requirements.txt     # Python package dependencies
```

---

## Getting Started

### Prerequisites

- Python 3.10+ (Python 3.12 recommended)
- `pip` package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/erhatechnologiesai/social-content-generator.git
   cd social-content-generator
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   ```bash
   cp .env.example .env
   ```

---

## Running the Application

Start the local development server with auto-reload:

```bash
python -m uvicorn app.api:app --reload --host 0.0.0.0 --port 8000
```

Once running, interactive documentation is accessible at:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/generate-social-package` | Repurpose article or concept across LinkedIn, X, and Threads |

### Example Request

```bash
curl -X POST http://127.0.0.1:8000/generate-social-package -H "Content-Type: application/json" -d '{"concept": "Why Retrieval-Augmented Generation outclasses fine-tuning for internal enterprise data"}'
```

---

## Running Tests

Execute the automated test suite:

```bash
python -m unittest tests/test_social_generator.py
```

Or using pytest:

```bash
pytest tests/
```

All test cases are self-contained and run offline without requiring third-party API credentials.

---

## Security & Best Practices

- **Zero Credential Leakage**: API tokens and secrets are loaded exclusively via environment variables and excluded by `.gitignore`.
- **Strict Validation**: All incoming request payloads are strictly validated using Pydantic schemas.
- **Fail-Safe Fallbacks**: Deterministic offline engines guarantee application continuity even during external provider outages.

---

## License

This project is licensed under the terms of the [MIT License](LICENSE).
