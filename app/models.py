from pydantic import BaseModel
from typing import List, Dict

class ContentSourceInput(BaseModel):
    core_concept: str
    target_audience: str = "Founders and Engineers"

class MultiPlatformPost(BaseModel):
    platform: str # Twitter_X, LinkedIn, Threads
    caption: str
    hashtags: List[str]
    character_count: int

class SocialMediaPackage(BaseModel):
    concept: str
    posts: List[MultiPlatformPost]
