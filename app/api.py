from fastapi import FastAPI
from app.config import settings
from app.models import ContentSourceInput, SocialMediaPackage, MultiPlatformPost
from app.services.content_generator import generate_social_posts

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.post("/generate-social-package", response_model=SocialMediaPackage)
def generate_package(input_data: ContentSourceInput):
    posts_raw = generate_social_posts(input_data.core_concept, input_data.target_audience)
    posts = [MultiPlatformPost(**p) for p in posts_raw]
    return SocialMediaPackage(concept=input_data.core_concept, posts=posts)
