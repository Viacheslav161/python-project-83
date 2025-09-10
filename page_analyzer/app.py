from flask import Flask, render_template
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
# Поддержка SECRET_KEY через .env или дефолт для разработки
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev_secret')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # В разработке удобно debug=True, в проде уберите
    app.run(debug=True)
