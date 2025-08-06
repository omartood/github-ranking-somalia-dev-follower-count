#!/usr/bin/env python3
"""
Quick version of Somali GitHub Developer Ranking Bot
Fetches top developers with follower counts (limited to 20 for speed)
"""

import requests
import os
from datetime import datetime
import time

# Load .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    if os.path.exists('.env'):
        with open('.env', 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key.strip()] = value.strip()

def quick_search():
    """Quick search for top Somali developers"""
    token = os.getenv('GH_TOKEN')
    if not token:
        print("❌ No GitHub token found. Using demo data...")
        return []
    
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'Somali-Dev-Ranker'
    }
    
    print("🔍 Searching for top Somali developers...")
    
    # Search for users with Somalia in location, sorted by followers
    url = "https://api.github.com/search/users"
    params = {
        'q': 'location:Somalia type:user',
        'sort': 'followers',
        'order': 'desc',
        'per_page': 20  # Limit to 20 for speed
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code != 200:
            print(f"❌ API Error: {response.status_code}")
            return []
        
        data = response.json()
        users = data.get('items', [])
        
        developers = []
        for user in users:
            # Get detailed user info for follower count
            user_url = f"https://api.github.com/users/{user['login']}"
            user_response = requests.get(user_url, headers=headers)
            
            if user_response.status_code == 200:
                user_data = user_response.json()
                if user_data.get('type') == 'User':  # Filter out bots
                    developers.append({
                        'username': user_data['login'],
                        'name': user_data.get('name', ''),
                        'followers': user_data['followers'],
                        'profile_url': user_data['html_url']
                    })
                    print(f"✅ Found: {user_data['login']} ({user_data['followers']} followers)")
            
            time.sleep(0.5)  # Rate limiting
        
        return sorted(developers, key=lambda x: x['followers'], reverse=True)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return []

def main():
    print("🇸🇴 Quick Somali GitHub Developer Ranking")
    print("=" * 40)
    
    developers = quick_search()
    
    if developers:
        print(f"\n📊 Found {len(developers)} developers with follower data")
        
        print("\n🏆 Top 5 developers:")
        for i, dev in enumerate(developers[:5], 1):
            name = dev['name'] if dev['name'] else dev['username']
            print(f"{i}. {name} (@{dev['username']}) - {dev['followers']} followers")
    else:
        print("❌ No developers found or API error")

if __name__ == "__main__":
    main()