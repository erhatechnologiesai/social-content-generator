def generate_social_posts(concept: str, audience: str):
    posts = [
        {
            "platform": "Twitter_X",
            "caption": f"Autonomous AI agents are shifting from experimental toys to production-grade SLA architectures.\n\nHere is why {concept} is redefining operations for {audience} 👇",
            "hashtags": ["#AIAgents", "#Automation", "#Engineering"],
            "character_count": 185
        },
        {
            "platform": "LinkedIn",
            "caption": (
                f"Most leaders focus on LLM models, but the real compounding advantage is in the workflow architecture.\n\n"
                f"Today, we are highlighting our approach to {concept}. For modern {audience}, automating deterministic validation "
                "before agent actions prevents hallucinations and protects SLAs.\n\nWhat is your biggest operational bottleneck?"
            ),
            "hashtags": ["#ArtificialIntelligence", "#EnterpriseAutomation", "#Leadership"],
            "character_count": 395
        }
    ]
    return posts
