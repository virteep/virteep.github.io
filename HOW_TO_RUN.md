# 🚀 How to Run Your Personal Website

## Quick Start (3 minutes)

### Option 1: Automated Setup (Recommended)

**Mac/Linux:**
```bash
chmod +x setup.sh
./setup.sh
python app.py
```

**Windows:**
```cmd
setup.bat
python app.py
```

Then open: **http://localhost:5000**

---

### Option 2: Manual Setup

1. **Create virtual environment:**
   ```bash
   python -m venv venv
   ```

2. **Activate it:**
   ```bash
   # Mac/Linux:
   source venv/bin/activate
   
   # Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server:**
   ```bash
   python app.py
   ```

5. **Open browser:**
   Navigate to `http://localhost:5000`

---

## 🎨 Customize Your Website

### Step 1: Edit Your Content

Open `content/data.yaml` and update:
- Your name, headline, and bio
- Work experience
- Education
- Interests and hobbies
- Contact information (email, LinkedIn, etc.)

### Step 2: Add Your Photo

Replace `static/images/profile.jpg` with your actual photo:
- Recommended size: 400x400px or larger
- Square aspect ratio works best
- Formats: JPG, PNG, or even SVG

### Step 3: Test Your Changes

1. Save your files
2. Refresh your browser
3. If content doesn't update, restart the Flask server

---

## 🛠️ Development Commands

```bash
# Start development server
python app.py

# Run tests
pytest

# Run tests with coverage
pytest --cov=app

# Format code
black app.py tests/

# Lint code
flake8 app.py tests/

# Clear content cache
curl http://localhost:5000/refresh-cache
```

---

## 🚢 Deploy Your Website

See `DEPLOYMENT.md` for detailed deployment instructions for:
- ✅ Vercel (Recommended - easiest)
- ✅ Railway
- ✅ Heroku
- ✅ PythonAnywhere
- ✅ Google Cloud Run
- ✅ DigitalOcean

**Quick Vercel Deploy:**
```bash
npm i -g vercel
vercel --prod
```

---

## 📁 Project Structure

```
PersonalWebsite_VP/
├── app.py                    # Main Flask application
├── content/data.yaml         # ⭐ Your content (edit this!)
├── static/images/profile.jpg # ⭐ Your photo (replace this!)
├── templates/index.html      # HTML template
└── requirements.txt          # Python dependencies
```

---

## 🐛 Troubleshooting

**Port 5000 already in use?**
```bash
# Run on a different port:
python -c "from app import app; app.run(port=5001)"
```

**Content not updating?**
1. Restart Flask server
2. Clear browser cache (Cmd+Shift+R or Ctrl+Shift+R)
3. Visit `/refresh-cache`

**YAML syntax error?**
- Check indentation (use spaces, not tabs)
- Validate YAML at https://www.yamllint.com/

**Image not showing?**
- Verify path in `content/data.yaml`
- Check file exists at `static/images/profile.jpg`
- Clear browser cache

---

## 📚 More Information

- **Full Documentation:** See `README.md`
- **Deployment Guide:** See `DEPLOYMENT.md`
- **Project Structure:** See `STRUCTURE.md`
- **Quick Reference:** See `QUICKSTART.md`

---

## ✅ Next Steps

1. ✏️ Customize `content/data.yaml`
2. 🖼️ Add your profile photo
3. 🧪 Test locally
4. 🚀 Deploy to production
5. 🌐 Set up custom domain (optional)
6. 📊 Add analytics (optional)

---

## 💡 Tips

- **Markdown Support:** Use `**bold**`, `*italic*`, and `[links](url)` in your bio and descriptions
- **Professional Photo:** Use a high-quality, well-lit headshot
- **Keep it Updated:** Regularly update your work experience and projects
- **Mobile First:** The site is fully responsive - test on your phone!
- **SEO:** Update meta tags in `templates/index.html` for better search rankings

---

**Need help?** Check the other documentation files or open an issue on GitHub!

🎉 **Happy coding!**
