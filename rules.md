# 🤖 Cursor AI Prompt for Somali GitHub Dev Ranking Bot

## 📌 Project Goal:
Build an AI-assisted GitHub automation that:
- Fetches developers with "Somalia" in their GitHub profile bio or location
- Sorts them by number of followers
- Generates a markdown leaderboard of Somali GitHub developers
- Updates daily via GitHub Actions
- Outputs results in `README.md`

## 🧠 Cursor AI Role (Rules & Tasks)

```markdown
You are an expert assistant helping build a GitHub automation project. Your job is to:

1. Write a Python or Node.js script that:
   - Queries GitHub REST API for users matching 'location:Somalia'
   - Sorts the users by followers count (descending)
   - Collects: username, profile URL, followers count
   - Writes the result to `README.md` in a markdown table format
   - Adds a timestamp "Last updated: YYYY-MM-DD"

2. Schedule this script to run daily using GitHub Actions
   - Create `.github/workflows/dev-ranker.yml`
   - Set the cron to run every 24 hours

3. Add error handling for API rate limits
   - If rate-limited, retry or skip users gracefully

4. Use a GitHub Personal Access Token (stored as `GH_TOKEN` secret) to authenticate the API

5. Markdown format in README should look like:

   ```markdown
   | Rank | Username | Followers | Profile |
   |------|----------|-----------|---------|
   | 🥇 1 | @dev1    | 520       | https://github.com/dev1 |
   | 🥈 2 | @dev2    | 460       | https://github.com/dev2 |
   ```

6. Add a Somali flag 🇸🇴 emoji at the top with title: `Top Somali Developers on GitHub`
```

---

## 📂 Output File Structure

```bash
/top-somali-devs/
├── .github/workflows/dev-ranker.yml
├── generate_ranking.py  # or generate_ranking.js
└── README.md            # Auto-updated with leaderboard
```

---

## 🔐 GitHub Secrets Required
- `GH_TOKEN`: A GitHub Personal Access Token with read access

---

## ✅ Output Format Example

```markdown
# 🇸🇴 Top Somali Developers on GitHub

| Rank | Username | Followers | Profile |
|------|----------|-----------|---------|
| 🥇 1 | @xuseen | 534 | https://github.com/xuseen |
| 🥈 2 | @aaminah | 418 | https://github.com/aaminah |
| 🥉 3 | @mustafe | 402 | https://github.com/mustafe |

_Last updated: 2025-08-05_
```

---

## 🧪 Notes
- Use pagination for GitHub API (max 100 users per page)
- Filter out bots and organizations by checking user type = `User`
- Bonus: Allow custom queries like `location: