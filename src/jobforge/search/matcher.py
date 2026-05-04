import logging
from typing import List, Dict
import re

logger = logging.getLogger(__name__)

class MatchEngine:
    def __init__(self, profile_skills: List[str]):
        self.profile_skills = [s.lower() for s in profile_skills]

    def calculate_score(self, description: str) -> float:
        if not description:
            return 0.0
        
        description_lower = description.lower()
        matches = 0
        
        for skill in self.profile_skills:
            # Use regex to find whole words/phrases to avoid partial matches (e.g., "net" in "internet")
            pattern = rf'\b{re.escape(skill)}\b'
            if re.search(pattern, description_lower):
                matches += 1
        
        if not self.profile_skills:
            return 0.0
            
        score = (matches / len(self.profile_skills)) * 100
        return round(score, 2)
