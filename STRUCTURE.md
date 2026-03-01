# 📁 Project Structure

Complete overview of all files and directories in this project.

```
PersonalWebsite_VP/
│
├── 📄 app.py                      # Main Flask application (core logic)
├── 📄 requirements.txt            # Python dependencies
├── 📄 runtime.txt                 # Python version for deployment
├── 📄 Procfile                    # Heroku deployment config
├── 📄 vercel.json                 # Vercel deployment config
├── 📄 pyproject.toml              # Black formatter config
├── 📄 pytest.ini                  # Pytest configuration
├── 📄 .flake8                     # Flake8 linter config
├── 📄 .gitignore                  # Git ignore rules
├── 📄 .python-version             # Python version file
│
├── 📚 README.md                   # Full documentation
├── 📚 QUICKSTART.md               # Quick start guide (3-minute setup)
├── 📚 DEPLOYMENT.md               # Deployment guide for all platforms
├── 📚 STRUCTURE.md                # This file
│
├── 📂 content/                    # Content management
│   └── 📄 data.yaml              # ⭐ EDIT THIS - All your content here
│
├── 📂 templates/                  # HTML templates
│   └── 📄 index.html             # Main landing page template
│
├── 📂 static/                     # Static files (images, CSS)
│   ├── 📂 css/
│   │   └── 📄 custom.css         # Custom CSS (optional)
│   └── 📂 images/
│       └── 🖼️ profile.jpg        # ⭐ REPLACE THIS - Your profile photo
│
└── 📂 tests/                      # Test suite
    └── 📄 test_app.py            # Automated tests
```

---

## 🔑 Key Files to Customize

### 1. `content/data.yaml` ⭐ MOST IMPORTANT
**What it is:** Your entire website content in one file  
**What to do:** Edit with your personal information  
**Supports:** Markdown formatting in bio and descriptions

### 2. `static/images/profile.jpg` ⭐ IMPORTANT
**What it is:** Your profile photo  
**What to do:** Replace with your actual photo (JPG, PNG, or SVG)  
**Recommended size:** 400x400px minimum, square aspect ratio

### 3. `templates/index.html` (Optional)
**What it is:** The HTML template  
**What to do:** Customize layout, colors, sections if desired  
**Tech:** Uses Tailwind CSS for styling

---

## 📝 File Descriptions

### Core Application Files

**`app.py`** (190 lines)
- Main Flask application
- Content loading with caching
- Markdown processing
- Route handlers
- Error handling

**`requirements.txt`**
- Flask (web framework)
- PyYAML (YAML parsing)
- markdown (Markdown to HTML)
- gunicorn (production server)
- pytest (testing)
- black & flake8 (code quality)

### Content Files

**`content/data.yaml`**
- Structured content in YAML format
- Sections: about, work_experience, education, outside_work, contact
- Easy to edit, no code required
- Supports markdown in text fields

### Template Files

**`templates/index.html`** (370+ lines)
- Responsive design (mobile-first)
- Tailwind CSS styling
- SEO-optimized meta tags
- Sections: Hero, Work, Education, Interests, Contact
- Custom animations and hover effects

### Static Files

**`static/css/custom.css`**
- Optional custom styles
- Extends Tailwind CSS
- Animation definitions

**`static/images/profile.jpg`**
- SVG placeholder (replace with your photo)

### Test Files

**`tests/test_app.py`** (180+ lines)
- Unit tests for Flask app
- Content loading tests
- Route tests
- Markdown processing tests
- Run with: `pytest`

### Configuration Files

**`pyproject.toml`**
- Black code formatter settings
- Line length: 100 characters

**`pytest.ini`**
- Pytest configuration
- Test discovery settings

**`.flake8`**
- Flake8 linter settings
- Code style rules

**`.gitignore`**
- Ignores Python cache, virtual envs, etc.

### Deployment Files

**`Procfile`** (for Heroku)
```
web: gunicorn app:app
```

**`vercel.json`** (for Vercel)
- Vercel serverless configuration

**`runtime.txt`** (for Heroku/Railway)
- Specifies Python 3.11.7

---

## 🎯 Workflow

### Development
1. Edit `content/data.yaml`
2. Replace `static/images/profile.jpg`
3. Run `python app.py`
4. Visit `http://localhost:5000`
5. Make changes and refresh

### Before Deployment
1. Run `pytest` (ensure tests pass)
2. Run `black app.py tests/` (format code)
3. Run `flake8 app.py tests/` (check style)
4. Update meta tags in `index.html`

### Deployment
1. Push to GitHub
2. Connect to deployment platform
3. Deploy!

---

## 🔄 Content Update Flow

```
Edit content/data.yaml
        ↓
app.py loads YAML
        ↓
Processes markdown
        ↓
Caches content (performance)
        ↓
Renders templates/index.html
        ↓
Browser displays page
```

---

## 🚀 Adding New Features

### Add a new section
1. Add data to `content/data.yaml`
2. Add section HTML to `templates/index.html`
3. (Optional) Add processing in `app.py` if markdown needed

### Add a blog
1. Create `content/blog/` directory
2. Add markdown files for posts
3. Update `app.py` to load and route blog posts
4. Add blog template

### Add a projects page
1. Add `projects` section to `data.yaml`
2. Add section to `index.html` or create new route
3. (Optional) Link to GitHub repos

---

## 📊 Performance Features

- **Content caching**: Loaded content is cached with LRU
- **Cache invalidation**: Based on file modification time
- **Static file caching**: 1-hour cache headers
- **Minimal dependencies**: Fast load times
- **CDN for Tailwind**: No build step needed

---

## 🔧 Customization Points

| What to customize | File | Difficulty |
|-------------------|------|------------|
| Content | `content/data.yaml` | ⭐ Easy |
| Profile photo | `static/images/profile.jpg` | ⭐ Easy |
| Colors | `templates/index.html` (Tailwind classes) | ⭐⭐ Medium |
| Layout | `templates/index.html` (HTML structure) | ⭐⭐ Medium |
| Fonts | `templates/index.html` (Google Fonts link) | ⭐⭐ Medium |
| Add features | `app.py` + templates | ⭐⭐⭐ Advanced |

---

## 📈 Next Steps

1. **Customize content**: Edit `data.yaml`
2. **Add your photo**: Replace `profile.jpg`
3. **Test locally**: Run `python app.py`
4. **Deploy**: Follow `DEPLOYMENT.md`
5. **Set up domain**: Add custom domain
6. **Analytics**: Add Google Analytics or Plausible
7. **Monitor**: Set up uptime monitoring

---

Questions? Check `README.md` for full documentation!
