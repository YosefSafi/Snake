# JobForge

JobForge is a professional, production-quality Job Search Automation System designed to find real, current job listings without hallucinations using real-time web search and grounding.

## Core Features
- **Real-time Job Search**: Uses Google Search and Web Fetching for verified listings.
- **Profile Matching**: Match jobs to your resume and experience.
- **Application Tracking**: Manage your application lifecycle.
- **Tailored Documents**: Generate ATS-friendly resumes and cover letters.
- **Daily Digests**: Stay updated with new opportunities.

## Tech Stack
- **Python 3.11+**
- **SQLite** for data storage.
- **Pydantic** for data validation.
- **Rich** for beautiful CLI output.
- **Playwright/BeautifulSoup4** for web scraping.

## Getting Started
1. Clone the repository.
2. Install dependencies: `pip install -e .`
3. Configure your profile in `.env`.
4. Run the CLI: `python -m jobforge.cli`
