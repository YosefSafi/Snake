import logging
from typing import Dict
from datetime import datetime

logger = logging.getLogger(__name__)

class ApplicationHelper:
    def __init__(self, profile: Dict):
        self.profile = profile

    def generate_cover_letter(self, job_title: str, company: str, description: str) -> str:
        """
        Generates a tailored cover letter. 
        In a production system, this would call an LLM.
        For now, it uses a high-quality template with profile data.
        """
        name = self.profile.get("name", "Applicant")
        email = self.profile.get("email", "")
        phone = self.profile.get("phone", "")
        skills = ", ".join(self.profile.get("skills", [])[:5]) # Top skills
        
        date_str = datetime.now().strftime("%B %d, %Y")
        
        template = f"""
{name}
{email} | {phone}
{date_str}

Hiring Manager
{company}

Subject: Application for {job_title}

Dear Hiring Manager,

I am writing to express my strong interest in the {job_title} position at {company}. As an IT developer specialized in .NET and Cloud with a proven track record of solving complex problems, I am confident that my background aligns perfectly with the requirements of your team.

In my recent experience, I have developed a deep expertise in {skills}. My work on projects like the "Hospition.IT" triage prototype, where I implemented a weighted scoring system for clinical decisions, demonstrates my ability to build stable, well-functioning solutions that deliver real value.

I am particularly drawn to {company} because of your reputation for innovation in the industry. I am eager to bring my skills in C#, Azure, and modern AI solutions to contribute to your ongoing success.

Thank you for your time and consideration. I look forward to the possibility of discussing how my skills and experience can benefit {company}.

Sincerely,

{name}
"""
        return template.strip()
