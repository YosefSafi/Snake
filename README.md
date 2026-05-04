# JobForge 🛠️

JobForge is a professional, production-quality Job Search Automation System designed to find real, current job listings without hallucinations using real-time web search and grounding.

## Core Features
- **Verified Search**: Uses Agent-assisted real-time search to find actual open positions.
- **Profile Matching**: Ranks jobs against your resume using a weighted keyword matching engine.
- **Description Scraper**: Fetches full job requirements to enable deep analysis.
- **Application Tracking**: Manage your application lifecycle (Applied, Interview, Rejected).
- **Document Generator**: Creates tailored cover letters based on your profile and job specifics.
- **Daily Digest**: Quickly see your top matching opportunities.

## Tech Stack
- **Python 3.11+**
- **SQLite** for robust local data storage.
- **SQLAlchemy** (ORM) & **Pydantic** (Validation).
- **Rich** for beautiful, interactive CLI tables.
- **Pytest** for automated functional testing.

## CLI Usage
Ensure you are in the project root and have your `PYTHONPATH` set to `src`.

### 1. Initial Setup
```bash
pip install -e .
cp .env.example .env
# Edit profile.json with your details
```

### 2. Listing Jobs
```bash
python -m jobforge.cli list
```

### 3. Calculating Match Scores
```bash
python -m jobforge.cli match
```

### 4. Viewing Job Details
```bash
python -m jobforge.cli detail <id>
```

### 5. Fetching Full Descriptions
```bash
python -m jobforge.cli fetch-desc <id>
```

### 6. Updating Status
```bash
python -m jobforge.cli status <id> Applied
```

### 7. Generating Cover Letters
```bash
python -m jobforge.cli generate-letter <id>
```

### 8. Daily Digest
```bash
python -m jobforge.cli digest --threshold 30
```

## Testing
```bash
$env:DATABASE_URL="sqlite:///test_jobforge.db"; pytest
```

## Architecture
JobForge uses a modular `src/` layout:
- `core/`: Configuration and settings.
- `db/`: Models and session management.
- `search/`: Engine, Scraper, and Matcher logic.
- `application/`: Document generation and helper tools.
