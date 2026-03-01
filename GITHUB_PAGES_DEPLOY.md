# GitHub Pages Deployment Guide

Deploy your personal website to GitHub Pages (like https://virteep.github.io/resume/)

## 📋 Overview

Since GitHub Pages only serves static files, we'll use `Flask-Frozen` to convert your Flask app to static HTML files.

## 🚀 Step-by-Step Deployment

### 1. Install Dependencies

```bash
cd /Users/virtee/Documents/PersonalWebsite_VP
source venv/bin/activate
pip install Frozen-Flask==1.0.1
```

### 2. Generate Static Files

```bash
python freeze.py
```

This creates a `build/` directory with all static HTML files.

### 3. Create GitHub Repository

Two options:

#### Option A: User/Organization Site (Recommended)
- Repository name: `YOUR_USERNAME.github.io`
- Your site will be: `https://YOUR_USERNAME.github.io/`

#### Option B: Project Site
- Repository name: Any name (e.g., `personal-website`)
- Your site will be: `https://YOUR_USERNAME.github.io/personal-website/`

### 4. Deploy to GitHub Pages

```bash
# Navigate to build directory
cd build

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Deploy to GitHub Pages"

# Create gh-pages branch
git branch -M gh-pages

# Add remote (replace with your repo URL)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# Push to GitHub
git push -u origin gh-pages
```

### 5. Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** → **Pages**
3. Under "Source", select:
   - Branch: `gh-pages`
   - Folder: `/ (root)`
4. Click **Save**
5. Wait ~2 minutes for deployment
6. Your site will be live! 🎉

## 🔄 Updating Your Site

When you make changes:

```bash
# 1. Update your content in data.yaml or code
cd /Users/virtee/Documents/PersonalWebsite_VP

# 2. Re-generate static files
python freeze.py

# 3. Deploy updated files
cd build
git add .
git commit -m "Update website"
git push origin gh-pages
```

Changes will be live in ~2 minutes.

## 🎨 For User Site (username.github.io)

If you want your site at `https://YOUR_USERNAME.github.io/`:

```bash
# Use 'main' or 'master' branch instead of gh-pages
cd build
git init
git add .
git commit -m "Deploy to GitHub Pages"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_USERNAME.github.io.git
git push -u origin main
```

Then in GitHub Settings → Pages:
- Source: `main` branch, `/ (root)` folder

## ⚙️ Custom Domain Setup

If you have a custom domain (e.g., `virteeparekh.com`):

### 1. Add CNAME file

```bash
cd build
echo "virteeparekh.com" > CNAME
git add CNAME
git commit -m "Add custom domain"
git push
```

### 2. Update DNS Settings

Add these records with your domain provider:

```
Type: A
Name: @
Value: 185.199.108.153

Type: A
Name: @
Value: 185.199.109.153

Type: A
Name: @
Value: 185.199.110.153

Type: A
Name: @
Value: 185.199.111.153

Type: CNAME
Name: www
Value: YOUR_USERNAME.github.io
```

### 3. Enable in GitHub

1. Go to Settings → Pages
2. Enter your custom domain in "Custom domain"
3. Check "Enforce HTTPS" (after DNS propagates)

## 📝 Important Notes

### ⚠️ Goodreads Books

The Goodreads integration fetches books dynamically. With static files:
- Books are fetched **at build time**
- To update books, re-run `python freeze.py` and redeploy
- Books won't auto-update on the live site

### 🔄 Automation Option

You can automate rebuilds using GitHub Actions (optional):

Create `.github/workflows/deploy.yml` in your main repo:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]
  schedule:
    - cron: '0 0 * * *'  # Daily at midnight (updates Goodreads books)

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.12'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      
      - name: Build static site
        run: python freeze.py
      
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./build
```

This auto-deploys on every push and updates daily!

## 🐛 Troubleshooting

### 404 Error
- Check branch is `gh-pages` (or `main` for user sites)
- Verify `index.html` exists in root of branch
- Wait 2-5 minutes after pushing

### CSS/Images Not Loading
- Check all paths are relative (not starting with `/`)
- Verify files exist in `build/static/`
- Clear browser cache

### Books Not Showing
- Run `python freeze.py` again to fetch fresh data
- Check Goodreads RSS feed is accessible
- Look in `build/index.html` to verify books are embedded

## ✅ Quick Reference

```bash
# Update and deploy workflow:
python freeze.py           # Generate static files
cd build                   # Go to build directory
git add .                  # Stage changes
git commit -m "Update"     # Commit changes
git push origin gh-pages   # Deploy to GitHub Pages
```

## 🔗 Example

Your site structure will match https://virteep.github.io/resume/:
- Static HTML files ✅
- CSS and images ✅
- Fast loading ✅
- Free hosting ✅
- HTTPS enabled ✅

---

**Ready to deploy?** Run `python freeze.py` and follow the steps above! 🚀
