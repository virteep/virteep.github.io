#!/usr/bin/env python3
"""
Freeze the Flask app to static HTML files for GitHub Pages deployment.
Run this script to generate static files in the 'build' directory.
"""

from flask_frozen import Freezer
from app import app
import os
import shutil

# Configure the freezer
app.config['FREEZER_DESTINATION'] = 'build'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True

freezer = Freezer(app)

@freezer.register_generator
def static_files():
    """Register static files to be copied."""
    static_dir = 'static'
    for root, dirs, files in os.walk(static_dir):
        for filename in files:
            # Get the relative path from static directory
            rel_path = os.path.relpath(os.path.join(root, filename), static_dir)
            yield 'static', {'filename': rel_path}

if __name__ == '__main__':
    print("🔥 Freezing Flask app to static HTML...")
    print("=" * 50)
    
    # Clean build directory if it exists
    if os.path.exists('build'):
        print("🗑️  Cleaning old build directory...")
        shutil.rmtree('build')
    
    # Freeze the app
    print("📦 Generating static files...")
    freezer.freeze()
    
    print("=" * 50)
    print("✅ Successfully generated static files!")
    print(f"📁 Output directory: {os.path.abspath('build')}")
    print("\n📋 Next steps:")
    print("1. cd build")
    print("2. git init")
    print("3. git add .")
    print('4. git commit -m "Deploy to GitHub Pages"')
    print("5. git branch -M gh-pages")
    print("6. git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git")
    print("7. git push -u origin gh-pages")
    print("\nThen enable GitHub Pages in your repo settings!")
