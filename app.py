"""
Personal Website - Flask Application
Minimal, fast, SEO-friendly personal website with YAML-based content management.
"""

import os
import yaml
import markdown
import requests
import feedparser
from datetime import datetime
from flask import Flask, render_template, send_from_directory
from functools import lru_cache
from pathlib import Path

app = Flask(__name__)

# Configuration
CONTENT_FILE = Path("content/data.yaml")
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 3600  # Cache static files for 1 hour

# Initialize markdown parser with extensions
md = markdown.Markdown(extensions=["fenced_code", "tables", "nl2br"])


@lru_cache(maxsize=1)
def get_content_mtime():
    """Get the last modification time of content file for cache invalidation."""
    return os.path.getmtime(CONTENT_FILE)


def fetch_goodreads_books(user_id):
    """Fetch currently reading books from Goodreads RSS feed."""
    try:
        # Goodreads RSS feed for currently-reading shelf
        rss_url = f"https://www.goodreads.com/review/list_rss/{user_id}?shelf=currently-reading"
        feed = feedparser.parse(rss_url)

        books = []
        for entry in feed.entries[:3]:  # Get top 3 books
            title = entry.title.split(" by ")[0] if " by " in entry.title else entry.title
            author = entry.title.split(" by ")[1] if " by " in entry.title else "Unknown"
            
            # Extract book cover image from description
            cover_url = None
            if hasattr(entry, 'description'):
                # Parse the HTML description to find the image
                import re
                img_match = re.search(r'<img[^>]+src="([^"]+)"', entry.description)
                if img_match:
                    cover_url = img_match.group(1)
            
            books.append({
                "title": title, 
                "author": author,
                "cover": cover_url
            })

        return books if books else None
    except Exception as e:
        print(f"Error fetching Goodreads data: {e}")
        return None


def load_content():
    """Load and parse content from YAML file with caching."""
    # Cache invalidation based on file modification time
    get_content_mtime()

    with open(CONTENT_FILE, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    # Process markdown fields
    if data.get("about", {}).get("bio"):
        data["about"]["bio_html"] = md.convert(data["about"]["bio"])

    if data.get("outside_work", {}).get("description"):
        data["outside_work"]["description_html"] = md.convert(data["outside_work"]["description"])

    # Process work experience descriptions
    for job in data.get("work_experience", []):
        if job.get("description"):
            job["description_html"] = md.convert(job["description"])

    # Fetch Goodreads books if user_id is configured
    if data.get("life", {}).get("goodreads_user_id"):
        books = fetch_goodreads_books(data["life"]["goodreads_user_id"])
        if books and data.get("life", {}).get("cards"):
            # Update the books card with fetched data
            for card in data["life"]["cards"]:
                if card.get("type") == "books":
                    card["books"] = books
                    break

    return data


@app.route("/")
def index():
    """Render the main landing page."""
    try:
        content = load_content()
        return render_template("index.html", **content)
    except FileNotFoundError:
        return "Content file not found. Please create content/data.yaml", 404
    except yaml.YAMLError as e:
        return f"Error parsing YAML: {e}", 500


@app.route("/static/<path:filename>")
def static_files(filename):
    """Serve static files."""
    return send_from_directory("static", filename)


@app.context_processor
def utility_processor():
    """Add utility functions to template context."""

    def format_date(date_str):
        """Format date string for display."""
        if date_str.lower() == "present":
            return "Present"
        try:
            date_obj = datetime.strptime(date_str, "%Y-%m")
            return date_obj.strftime("%b %Y")
        except (ValueError, AttributeError):
            return date_str

    def current_year():
        """Get current year."""
        return datetime.now().year

    return dict(format_date=format_date, current_year=current_year)


@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    try:
        content = load_content()
        return render_template("index.html", **content), 404
    except Exception:
        return "Page not found", 404


@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors."""
    return "Internal server error", 500


# Cache invalidation route (useful for development)
@app.route("/refresh-cache")
def refresh_cache():
    """Clear the content cache."""
    get_content_mtime.cache_clear()
    return "Cache cleared", 200


if __name__ == "__main__":
    # Development server
    # Using port 5001 since 5000 is often used by AirPlay on macOS
    app.run(debug=True, host="0.0.0.0", port=5001)
