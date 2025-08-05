#!/usr/bin/env python3
"""
Demo version of Somali GitHub Developer Ranking Bot
This version works without authentication but with limited API calls
"""

import requests
import json
from datetime import datetime
import time

def search_somali_developers_demo():
    """Search for Somali developers without authentication (limited)"""
    print("🔍 Searching for Somali developers (demo mode)...")
    
    developers = []
    
    # Search with limited results (no auth)
    url = "https://api.github.com/search/users"
    params = {
        'q': 'location:Somalia type:user',
        'sort': 'followers',
        'order': 'desc',
        'per_page': 10  # Limited for demo
    }
    
    try:
        response = requests.get(url, params=params)
        print(f"API Response: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            users = data.get('items', [])
            
            print(f"Found {len(users)} users")
            
            for user in users:
                # Get basic info (some details may be limited without auth)
                developers.append({
                    'username': user['login'],
                    'name': user.get('login', ''),  # Use login as name fallback
                    'followers': user.get('followers', 0),
                    'profile_url': user['html_url'],
                    'avatar_url': user['avatar_url'],
                    'location': 'Somalia',
                    'bio': ''
                })
                
        return developers
        
    except Exception as e:
        print(f"Error: {e}")
        return []

def generate_demo_markdown(developers):
    """Generate demo markdown leaderboard"""
    if not developers:
        # Create sample data if no real data available
        developers = [
            {"username": "demo1", "name": "Ahmed Hassan", "followers": 534, "profile_url": "https://github.com/demo1"},
            {"username": "demo2", "name": "Fatima Ali", "followers": 418, "profile_url": "https://github.com/demo2"},
            {"username": "demo3", "name": "Mohamed Omar", "followers": 402, "profile_url": "https://github.com/demo3"},
        ]
        print("Using sample data for demo")
    
    # Sort by followers
    sorted_devs = sorted(developers, key=lambda x: x['followers'], reverse=True)
    
    markdown = "# 🇸🇴 Top Somali Developers on GitHub (Demo)\n\n"
    markdown += "A ranking of Somali developers based on their GitHub followers.\n\n"
    markdown += "| Rank | Developer | Followers | Profile |\n"
    markdown += "|------|-----------|-----------|----------|\n"
    
    rank_emojis = {1: "🥇", 2: "🥈", 3: "🥉"}
    
    for i, dev in enumerate(sorted_devs, 1):
        emoji = rank_emojis.get(i, "")
        name_display = dev['name'] if dev['name'] else dev['username']
        
        markdown += f"| {emoji} {i} | [{name_display}]({dev['profile_url']}) | {dev['followers']} | [@{dev['username']}]({dev['profile_url']}) |\n"
    
    timestamp = datetime.now().strftime("%Y-%m-%d")
    markdown += f"\n_Last updated: {timestamp} (Demo Mode)_\n"
    markdown += f"\n_Found {len(sorted_devs)} developers_\n"
    
    return markdown

def main():
    """Demo main function"""
    print("🇸🇴 Somali GitHub Developer Ranking Bot - Demo Mode")
    print("This version runs without authentication for testing purposes\n")
    
    # Search for developers
    developers = search_somali_developers_demo()
    
    # Generate markdown
    markdown_content = generate_demo_markdown(developers)
    
    # Write to demo file
    with open('README_demo.md', 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print("✅ Demo README created as README_demo.md")
    print("\n📋 To use the full version:")
    print("1. Get GitHub Personal Access Token")
    print("2. Set as environment variable: export GH_TOKEN=your_token")
    print("3. Run: python generate_ranking.py")

if __name__ == "__main__":
    main()