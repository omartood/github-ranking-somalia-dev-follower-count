#!/usr/bin/env python3
"""
Somali GitHub Developer Ranking Bot
Fetches and ranks Somali developers by follower count
"""

import requests
import json
import os
from datetime import datetime
import time
import sys

class GitHubRanker:
    def __init__(self, token):
        self.token = token
        self.headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'Somali-Dev-Ranker'
        }
        self.base_url = 'https://api.github.com'
        
    def search_somali_developers(self):
        """Search for developers with Somalia in their profile"""
        developers = []
        page = 1
        
        # Search queries to find Somali developers
        queries = [
            'location:Somalia',
            'location:Mogadishu',
            'location:Hargeisa',
            'location:Somaliland'
        ]
        
        for query in queries:
            print(f"Searching for: {query}")
            page = 1
            
            while True:
                url = f"{self.base_url}/search/users"
                params = {
                    'q': f'{query} type:user',
                    'sort': 'followers',
                    'order': 'desc',
                    'per_page': 100,
                    'page': page
                }
                
                try:
                    response = requests.get(url, headers=self.headers, params=params)
                    
                    if response.status_code == 403:
                        print("Rate limit hit, waiting...")
                        time.sleep(60)
                        continue
                        
                    if response.status_code != 200:
                        print(f"Error: {response.status_code}")
                        break
                        
                    data = response.json()
                    users = data.get('items', [])
                    
                    if not users:
                        break
                        
                    for user in users:
                        # Get detailed user info
                        user_details = self.get_user_details(user['login'])
                        if user_details:
                            developers.append(user_details)
                            
                    page += 1
                    
                    # Respect rate limits
                    time.sleep(1)
                    
                except Exception as e:
                    print(f"Error fetching data: {e}")
                    break
                    
        return self.deduplicate_developers(developers)   
 def get_user_details(self, username):
        """Get detailed information for a specific user"""
        url = f"{self.base_url}/users/{username}"
        
        try:
            response = requests.get(url, headers=self.headers)
            
            if response.status_code == 403:
                print(f"Rate limit hit for user {username}")
                time.sleep(60)
                response = requests.get(url, headers=self.headers)
                
            if response.status_code != 200:
                return None
                
            user_data = response.json()
            
            # Filter out bots and organizations
            if user_data.get('type') != 'User':
                return None
                
            return {
                'username': user_data['login'],
                'name': user_data.get('name', ''),
                'followers': user_data['followers'],
                'profile_url': user_data['html_url'],
                'avatar_url': user_data['avatar_url'],
                'location': user_data.get('location', ''),
                'bio': user_data.get('bio', '')
            }
            
        except Exception as e:
            print(f"Error fetching user {username}: {e}")
            return None
            
    def deduplicate_developers(self, developers):
        """Remove duplicate developers based on username"""
        seen = set()
        unique_developers = []
        
        for dev in developers:
            if dev['username'] not in seen:
                seen.add(dev['username'])
                unique_developers.append(dev)
                
        return unique_developers
        
    def generate_markdown(self, developers):
        """Generate markdown leaderboard"""
        # Sort by followers count (descending)
        sorted_devs = sorted(developers, key=lambda x: x['followers'], reverse=True)
        
        # Take top 50 to keep it manageable
        top_devs = sorted_devs[:50]
        
        markdown = "# 🇸🇴 Top Somali Developers on GitHub\n\n"
        markdown += "A ranking of Somali developers based on their GitHub followers.\n\n"
        markdown += "| Rank | Developer | Followers | Profile |\n"
        markdown += "|------|-----------|-----------|----------|\n"
        
        rank_emojis = {1: "🥇", 2: "🥈", 3: "🥉"}
        
        for i, dev in enumerate(top_devs, 1):
            emoji = rank_emojis.get(i, "")
            name_display = dev['name'] if dev['name'] else dev['username']
            
            markdown += f"| {emoji} {i} | [{name_display}]({dev['profile_url']}) | {dev['followers']} | [@{dev['username']}]({dev['profile_url']}) |\n"
            
        # Add timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d")
        markdown += f"\n_Last updated: {timestamp}_\n"
        markdown += f"\n_Found {len(top_devs)} developers_\n"
        
        return markdowndef 
main():
    """Main function to run the ranking bot"""
    # Get GitHub token from environment
    token = os.getenv('GH_TOKEN')
    if not token:
        print("Error: GH_TOKEN environment variable not set")
        sys.exit(1)
        
    print("🇸🇴 Starting Somali GitHub Developer Ranking Bot...")
    
    # Initialize ranker
    ranker = GitHubRanker(token)
    
    # Search for developers
    print("Searching for Somali developers...")
    developers = ranker.search_somali_developers()
    
    if not developers:
        print("No developers found!")
        sys.exit(1)
        
    print(f"Found {len(developers)} developers")
    
    # Generate markdown
    print("Generating markdown leaderboard...")
    markdown_content = ranker.generate_markdown(developers)
    
    # Write to README.md
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(markdown_content)
        
    print("✅ README.md updated successfully!")
    print(f"Top developer: {developers[0]['username'] if developers else 'None'}")

if __name__ == "__main__":
    main()