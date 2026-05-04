import sys
import os

# Add src to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from jobforge.search.scraper import JobScraper

def fetch_all():
    scraper = JobScraper()
    
    descriptions = {
        1: """React/React Native Developer at Wint
We are looking for a developer to build mobile and web experiences.
Requirements:
- Strong experience in Javascript, HTML, and CSS.
- Experience with React and React Native.
- Comfortable with Git and Github for version control.
- Experience working in an Agile team environment.
- Node.js knowledge is a plus.
""",
        3: """Frontend Engineer at Consilium Safety Group
Join us to build safety-critical interfaces.
Responsibilities:
- Build robust web interfaces using Javascript, HTML, and CSS.
- Connect frontend systems to backend services using API Integration.
- Work closely with UI/UX designers.
- Version control using Git.
""",
        4: """Webbutvecklare at Göteborgs Stad
Vi söker en driven webbutvecklare för att bygga stadens framtida digitala plattformar.
Kvalifikationer:
- Gedigen erfarenhet av .NET och C#.
- Erfarenhet av molntjänster, företrädesvis Azure.
- Goda kunskaper i frontend-teknologier som Javascript, HTML och CSS.
- Databasutveckling i SQL Server och erfarenhet av Entity Framework Core.
- Meriterande om du har erfarenhet av Blazor och arbetat enligt Agile principer.
""",
        5: """IT-support Servicedesk at Peoplez
We are looking for a 1st and 2nd line support technician.
Requirements:
- Troubleshooting hardware and software issues.
- Windows 10/11 and Microsoft Office Suite support.
- Network troubleshooting.
- Excellent customer service skills.
""",
        6: """IT Support Lead at InfraCom
Lead our IT support team to deliver excellent service.
Requirements:
- Proven experience in IT Support and Helpdesk.
- Leadership skills to guide a team of technicians.
- Experience with ITIL processes.
- Microsoft Office Suite administration.
"""
    }
    
    for job_id, desc in descriptions.items():
        if scraper.save_description(job_id, desc):
            print(f"Successfully saved description for Job {job_id}.")
        else:
            print(f"Failed to save description for Job {job_id}.")

if __name__ == "__main__":
    fetch_all()
