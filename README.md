# English to Kannada Translation - Landing Page

A beautiful and professional landing page for the English to Kannada translator project.

## Features

- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Modern UI**: Clean and professional interface with smooth animations
- **Navigation**: Easy-to-use navigation menu with smooth scrolling
- **Feature Showcase**: Highlights key features of the translator
- **Call-to-Action**: Clear buttons to guide users to the translator
- **Contact Section**: Easy way for users to get in touch

## Project Structure

```
english_to_kannada_translation/
├── app.py              # Flask application to serve the landing page
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Landing page HTML (with Jinja2 templating)
└── static/
    ├── style.css      # Styling for the landing page
    └── script.js      # JavaScript for animations and interactivity
```

## Getting Started

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Installation

1. Navigate to the project directory
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## Features Included

1. **Hero Section**: Eye-catching header with language icons and main CTA
2. **Features Grid**: 6 key features with icons and descriptions
3. **How It Works**: Step-by-step guide showing the translation process
4. **Call-to-Action**: Prominent section encouraging users to start translating
5. **Contact Section**: Easy way to reach out
6. **Footer**: Professional footer with links
7. **Animations**: Smooth scroll effects and hover animations

## Customization

### Colors
Edit the CSS variables in `static/style.css`:
```css
:root {
    --primary: #2b6cb0;      /* Main brand color */
    --secondary: #ff6b35;    /* Accent color */
    --success: #2ecc71;      /* Success color */
    --bg: #f6f8fa;           /* Background */
    --card: #fff;            /* Card background */
    --text: #1a202c;         /* Text color */
    --text-light: #718096;   /* Light text */
}
```

### Content
Modify the HTML content in `templates/index.html` to update:
- Feature descriptions
- Hero text
- Contact information
- Footer links

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## License

This project is open source and available under the MIT License.