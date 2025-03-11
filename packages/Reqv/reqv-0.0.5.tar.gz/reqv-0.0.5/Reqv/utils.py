# api_scraper/utils.py
import random

def get_random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        # Add more user agents here
    ]
    return random.choice(user_agents)

def build_headers():
    return {
        "User-Agent": get_random_user_agent(),
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
