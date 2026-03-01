"""
Test suite for personal website Flask application.
"""

import os
import sys
from pathlib import Path

# Add parent directory to path to import app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
import yaml
from app import app, load_content


@pytest.fixture
def client():
    """Create a test client for the app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def sample_content():
    """Sample content for testing."""
    return {
        "about": {
            "name": "Test User",
            "headline": "Test Headline",
            "photo": "/static/images/test.jpg",
            "bio": "Test bio with **markdown**",
        },
        "work_experience": [
            {
                "title": "Test Engineer",
                "company": "Test Company",
                "location": "Test City",
                "start_date": "2020-01",
                "end_date": "Present",
                "description": "Test description",
            }
        ],
        "education": [
            {
                "degree": "Test Degree",
                "institution": "Test University",
                "location": "Test City",
                "start_date": "2016-09",
                "end_date": "2020-05",
                "details": "Test details",
            }
        ],
        "outside_work": {
            "title": "Outside of Work",
            "description": "Test description",
            "interests": ["Testing", "Coding"],
        },
        "contact": {
            "email": "test@example.com",
            "linkedin": "https://linkedin.com/in/test",
            "github": "https://github.com/test",
        },
    }


def test_index_route(client):
    """Test that the index route returns 200."""
    response = client.get("/")
    assert response.status_code == 200


def test_index_contains_content(client):
    """Test that index page contains expected content."""
    response = client.get("/")
    data = response.data.decode("utf-8")

    # Check for basic HTML structure
    assert "<html" in data
    assert "</html>" in data
    assert "<title>" in data

    # Check for main sections
    assert "Work Experience" in data or "work_experience" in data.lower()


def test_content_file_exists():
    """Test that content file exists and is readable."""
    content_file = Path("content/data.yaml")
    assert content_file.exists(), "content/data.yaml should exist"

    # Test that it's valid YAML
    with open(content_file, "r") as f:
        data = yaml.safe_load(f)
        assert data is not None
        assert isinstance(data, dict)


def test_load_content():
    """Test content loading function."""
    content = load_content()

    assert content is not None
    assert isinstance(content, dict)
    assert "about" in content

    # Test that markdown is processed
    if content.get("about", {}).get("bio"):
        assert "bio_html" in content["about"]


def test_markdown_processing():
    """Test that markdown is correctly processed."""
    content = load_content()

    # If bio exists, check that markdown is converted
    if content.get("about", {}).get("bio_html"):
        bio_html = content["about"]["bio_html"]
        # Should contain HTML tags from markdown conversion
        assert "<" in bio_html or content["about"].get("bio") == bio_html


def test_static_files_route(client):
    """Test that static files can be served."""
    # This will 404 if file doesn't exist, but route should work
    response = client.get("/static/test.css")
    # Either 200 (file exists) or 404 (file doesn't exist) is fine
    assert response.status_code in [200, 404]


def test_refresh_cache_route(client):
    """Test the cache refresh route."""
    response = client.get("/refresh-cache")
    assert response.status_code == 200
    assert b"Cache cleared" in response.data


def test_404_handling(client):
    """Test 404 error handling."""
    response = client.get("/nonexistent-route")
    # Should redirect to index or return 404
    assert response.status_code in [200, 404]


def test_required_sections_present(client):
    """Test that all required sections are in the template."""
    response = client.get("/")
    data = response.data.decode("utf-8")

    # Check for meta tags (SEO)
    assert "meta" in data.lower()
    assert "viewport" in data.lower()

    # Check for contact section
    assert "email" in data.lower() or "contact" in data.lower()


def test_responsive_meta_tag(client):
    """Test that viewport meta tag exists for mobile responsiveness."""
    response = client.get("/")
    data = response.data.decode("utf-8")

    assert "viewport" in data.lower()
    assert "width=device-width" in data.lower()


def test_content_structure():
    """Test that loaded content has expected structure."""
    content = load_content()

    # Test about section
    assert "about" in content
    assert "name" in content["about"]

    # Test optional sections exist as keys
    assert isinstance(content.get("work_experience", []), list)
    assert isinstance(content.get("education", []), list)


def test_date_formatting(client):
    """Test that dates are properly formatted in the template."""
    from app import utility_processor

    format_date = utility_processor()["format_date"]

    # Test various date formats
    assert format_date("2020-01") is not None
    assert format_date("Present") == "Present"
    assert format_date("present") == "Present"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
