# 🚀 Quick Start Guide

Get your personal website running in 3 minutes!

## Step 1: Install Dependencies

```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # Mac/Linux
# OR
venv\Scripts\activate     # Windows

# Install packages
pip install -r requirements.txt
```

## Step 2: Customize Your Content

Edit `content/data.yaml` with your information:
- Name, headline, and bio
- Work experience
- Education
- Interests
- Contact info

## Step 3: Add Your Photo

Replace `static/images/profile.jpg` with your actual profile photo.

## Step 4: Run the Website

```bash
python app.py
```

Open your browser to: **http://localhost:5000**

---

## 📋 Common Commands

```bash
# Development server
python app.py

# Run tests
pytest

# Format code
black app.py tests/

# Lint code
flake8 app.py tests/

# Clear cache (if content not updating)
curl http://localhost:5000/refresh-cache
```

## 🚢 Deploy to Production

### Option 1: Vercel (Recommended)
```bash
npm i -g vercel
vercel --prod
```

### Option 2: Railway
1. Push code to GitHub
2. Connect repo to Railway
3. Deploy automatically

### Option 3: Heroku
```bash
heroku create
git push heroku main
```

---

## 🎨 Customization Tips

1. **Colors**: Edit the Tailwind classes in `templates/index.html`
2. **Sections**: Reorder or remove sections in the template
3. **Fonts**: Change the Google Fonts link in `<head>`
4. **Layout**: Modify the max-width and spacing classes

---

## 🐛 Troubleshooting

**Content not updating?**
- Restart Flask server
- Visit `/refresh-cache`
- Check YAML syntax in `data.yaml`

**Image not showing?**
- Verify file path in YAML
- Check file exists in `static/images/`
- Clear browser cache

**Server won't start?**
- Check Python version (3.9+)
- Ensure all dependencies installed
- Look for errors in terminal

---

## 📚 Learn More

See `README.md` for full documentation!
