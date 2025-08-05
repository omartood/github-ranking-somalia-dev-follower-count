# 🇸🇴 Top Somali Developers on GitHub

A ranking of Somali developers based on their GitHub followers.

| Rank | Developer | Followers | Profile |
|------|-----------|-----------|----------|
| 🥇 1 | Loading... | - | - |

_Last updated: Initializing..._

_This leaderboard is automatically updated daily via GitHub Actions._

## 🤖 How it works

This project uses a Python script that:
- Searches GitHub for users with "Somalia", "Mogadishu", "Hargeisa", or "Somaliland" in their location
- Filters out bots and organizations  
- Ranks developers by follower count
- Updates this README automatically every 24 hours

## 🚀 Setup Instructions

### Step 1: Fork this repository
Click the "Fork" button at the top right of this page.

### Step 2: Create a GitHub Personal Access Token
1. Go to [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens)
2. Click "Generate new token (classic)"
3. Give it a name like "Somali Dev Ranker"
4. Select scopes: `public_repo` and `read:user`
5. Click "Generate token" and copy it

### Step 3: Add the token as a repository secret
1. Go to your forked repository
2. Click Settings > Secrets and variables > Actions
3. Click "New repository secret"
4. Name: `GH_TOKEN`
5. Value: Paste your token
6. Click "Add secret"

### Step 4: Enable GitHub Actions
1. Go to the "Actions" tab in your repository
2. Click "I understand my workflows, go ahead and enable them"

### Step 5: Test the workflow
1. Go to Actions > "Somali GitHub Developer Ranker"
2. Click "Run workflow" to test it manually

## 🧪 Running locally

```bash
# Clone the repository
git clone https://github.com/yourusername/top-somali-devs.git
cd top-somali-devs

# Install dependencies
pip install -r requirements.txt

# Set your GitHub token
export GH_TOKEN=your_token_here

# Run the script
python generate_ranking.py

# Or test without a token (limited results)
python test_ranking.py
```

## 📊 Features

- ✅ Daily automatic updates via GitHub Actions
- ✅ Rate limit handling and error recovery
- ✅ Deduplication of developers across different location searches
- ✅ Filters out bots and organizations
- ✅ Top 50 developers ranking
- ✅ Beautiful markdown table with emojis

## 📈 Contributing

Found a bug or want to improve the ranking algorithm? Feel free to:
- Open an issue
- Submit a pull request
- Suggest new features

## 🔧 Customization

You can modify the search queries in `generate_ranking.py` to include more locations or search terms:

```python
queries = [
    'location:Somalia',
    'location:Mogadishu', 
    'location:Hargeisa',
    'location:Somaliland',
    # Add more locations here
]
```

---

Made with ❤️ for the Somali developer community