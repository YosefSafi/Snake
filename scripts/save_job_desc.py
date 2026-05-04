import sys
import os

# Add src to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from jobforge.search.scraper import JobScraper

def save_desc():
    scraper = JobScraper()
    description = """Junior .NET Developer
Location: Gothenburg, Sweden (Hybrid)

Job Description:
We are looking for a passionate Junior .NET Developer to join our agile development team in Gothenburg. In this role, you will work on building and maintaining modern web applications and services using the Microsoft technology stack.

Key Responsibilities:
- Develop and maintain web applications using C# and ASP.NET Core.
- Write clean, scalable, and maintainable code following SOLID principles.
- Participate in code reviews and contribute to technical discussions.

Requirements:
- Degree in Computer Science or related field.
- Solid understanding of C# and the .NET framework/Core.
- Familiarity with ASP.NET MVC/WebAPI, HTML5, CSS3, and JavaScript.
- Basic knowledge of SQL Server or other relational databases.
"""
    if scraper.save_description(2, description):
        print("Successfully saved description for Job 2.")
    else:
        print("Failed to save description.")

if __name__ == "__main__":
    save_desc()
