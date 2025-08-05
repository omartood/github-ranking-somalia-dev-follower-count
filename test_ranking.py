#!/usr/bin/env python3
"""
Test version of the Somali GitHub Developer Ranking Bot
This version works without authentication for testing purposes
"""

import requests
import json
from datetime import datetime
import time

def test_github_api():
    """Test the GitHub API without authentication"""
    print("🧪 Testing GitHub API access...")
    
    # Test basic API access
    url = "https://api.github.com/search/users"
    params = {
        'q': 'location:Somalia type:user',
        'sort': 'followers',
        'order': 'desc',
        'per_page': 5  # Small number for testing
    }
    
    try:
        response = requests.get(url, params=params)
        print(f"API Response Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            users = data.get('items', [])
            print(f"Found {len(users)} users in test")
            
            for user in users[:3]:  # Show first 3
                print(f"- {user['login']}: {user.get('followers', 'N/A')} followers")
                
            return True
        else:
            print(f"API Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"Error: {e}")
        return False

def create_sample_readme():
    """Create a sample README with mock data"""
    sample_data = [
        {"username": "example1", "name": "Ahmed Hassan", "followers": 534, "profile_url": "https://github.com/example1"},
        {"username": "example2", "name": "Fatima Ali", "followers": 418, "profile_url": "https://github.com/example2"},
        {"username": "example3", "name": "Mohamed Omar", "followers": 402, "profile_url": "https://github.com/example3"},
    ]
    
    markdown = "# 🇸🇴 Top Somali Developers on GitHub\n\n"
    markdown += "A ranking of Somali developers based on their GitHub followers.\n\n"
    markdown += "| Rank | Developer | Followers | Profile |\n"
    markdown += "|------|-----------|-----------|----------|\n"
    
    rank_emojis = {1: "🥇", 2: "🥈", 3: "🥉"}
    
    for i, dev in enumerate(sample_data, 1):
        emoji = rank_emojis.get(i, "")
        name_display = dev['name'] if dev['name'] else dev['username']
        markdown += f"| {emoji} {i} | [{name_display}]({dev['profile_url']}) | {dev['followers']} | [@{dev['username']}]({dev['profile_url']}) |\n"
    
    timestamp = datetime.now().strftime("%Y-%m-%d")
    markdown += f"\n_Last updated: {timestamp} (Sample Data)_\n"
    
    return markdown

if __name__ == "__main__":
    print("🇸🇴 Testing Somali GitHub Developer Ranking Bot...")
    
    # Test API access
    api_works = test_github_api()
    
    if api_works:
        print("✅ GitHub API is accessible")
    else:
        print("⚠️  GitHub API test failed (this is expected without authentication)")
    
    # Create sample README
    print("\n📝 Creating sample README...")
    sample_content = create_sample_readme()
    
    with open('README_sample.md', 'w', encoding='utf-8') as f:
        f.write(sample_content)
    
    print("✅ Sample README created as README_sample.md")
    print("\n🔧 To run the full version:")
    print("1. Get a GitHub Personal Access Token from https://github.com/settings/tokens")
    print("2. Set it as environment variable: export GH_TOKEN=your_token")
    print("3. Run: python generate_ranking.py")