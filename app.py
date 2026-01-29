from flask import Flask, render_template, request
from deep_translator import GoogleTranslator
import os

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


def en_to_kn(text: str) -> str:
    """Translate English text to Kannada."""
    if not text:
        return ""
    try:
        return GoogleTranslator(source='en', target='kn').translate(text)
    except Exception as e:
        raise RuntimeError(f"Translation en->kn failed: {e}")


@app.route('/')
def landing():
    """Serve the landing page"""
    return render_template('index.html')


@app.route('/translate', methods=['GET', 'POST'])
def translate():
    """Serve the translator page and handle translation requests"""
    translation = None
    text = ''
    error = None
    
    if request.method == 'POST':
        text = request.form.get('text', '')
        try:
            if text.strip():
                translation = en_to_kn(text)
            else:
                error = "Please enter some text to translate"
        except Exception as e:
            error = f'Error: {str(e)}'
    
    return render_template('translate.html', translation=translation, text=text, error=error)


if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
