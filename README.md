# Personal Website

A modern, minimal personal website built with Python (Flask) and Tailwind CSS. Features a clean, mobile-first design with content managed through YAML files—no code changes needed to update content.

## ✨ Features

- **Single-page layout** - Clean, minimal design inspired by modern portfolio sites
- **Content management** - Update content via YAML without touching code
- **Markdown support** - Write rich content with markdown formatting
- **SEO-friendly** - Optimized meta tags and semantic HTML
- **Mobile-first** - Responsive design that works on all devices
- **Fast & cached** - Built-in content caching for optimal performance
- **Easy deployment** - Deploy to any platform that supports Python (Vercel, Railway, PythonAnywhere, etc.)

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd PersonalWebsite_VP
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your content**
   - Edit `content/data.yaml` with your personal information
   - Add your profile photo to `static/images/profile.jpg`

5. **Run the development server**
   ```bash
   python app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:5000`

## 📝 Content Management

All content is managed through `content/data.yaml`. Simply edit this file to update:

- **About section** - Name, headline, bio, and photo
- **Work experience** - Job titles, companies, dates, and descriptions
- **Education** - Degrees, institutions, and details
- **Outside of work** - Interests and hobbies
- **Contact info** - Email, LinkedIn, GitHub, Twitter

Markdown is supported in the `bio` and `description` fields, so you can use **bold**, *italic*, links, and more.

### Example YAML Structure

```yaml
about:
  name: "Your Name"
  headline: "Your professional headline"
  photo: "/static/images/profile.jpg"
  bio: "Your bio with **markdown** support"

work_experience:
  - title: "Job Title"
    company: "Company Name"
    location: "City, State"
    start_date: "2022-06"
    end_date: "Present"
    description: "Job description with markdown support"
```

## 🛠️ Development Commands

```bash
# Run development server
python app.py

# Run tests
pytest

# Format code with black
black app.py tests/

# Lint code with flake8
flake8 app.py tests/

# Clear content cache (during development)
curl http://localhost:5000/refresh-cache
```

## 🚢 Deployment

### Deploy to Vercel

1. Install Vercel CLI: `npm i -g vercel`
2. Create `vercel.json` (already included)
3. Run: `vercel --prod`

### Deploy to Railway

1. Push your code to GitHub
2. Connect your repo to Railway
3. Railway will auto-detect Python and deploy

### Deploy to PythonAnywhere

1. Upload your code
2. Set up a virtual environment
3. Configure WSGI file to point to `app:app`

### Deploy to Heroku

1. Create `Procfile` (already included)
2. Run:
   ```bash
   heroku create
   git push heroku main
   ```

## 📁 Project Structure

```
PersonalWebsite_VP/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── content/
│   └── data.yaml         # Your content (edit this!)
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   └── images/
│       └── profile.jpg   # Your profile photo
├── tests/
│   └── test_app.py       # Test suite
├── .gitignore
├── Procfile              # For Heroku deployment
├── vercel.json           # For Vercel deployment
└── README.md
```

## 🎨 Customization

### Styling

The site uses Tailwind CSS via CDN. To customize:

1. Edit the `<style>` section in `templates/index.html`
2. Modify Tailwind classes directly in the HTML
3. For advanced customization, set up a local Tailwind build

### Layout

Edit `templates/index.html` to:
- Reorder sections
- Add new sections
- Modify spacing and typography
- Customize colors and effects

### Content Fields

Edit `app.py` to add support for new YAML fields and modify the `load_content()` function.

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app tests/

# Run specific test
pytest tests/test_app.py::test_index
```

## 🤝 Contributing

Feel free to fork this project and customize it for your own use!

## 📄 License

MIT License - feel free to use this for your personal website.

## 🐛 Troubleshooting

### Content not updating?
- Restart the Flask server or visit `/refresh-cache`

### Profile image not showing?
- Ensure your image is at `static/images/profile.jpg`
- Check file permissions
- Verify the path in `content/data.yaml`

### Styling issues?
- Clear your browser cache
- Check browser console for errors
- Ensure Tailwind CDN is loading

## 📧 Support

For issues or questions, please open an issue on GitHub.

---

Built with ❤️ using Flask and Tailwind CSS
