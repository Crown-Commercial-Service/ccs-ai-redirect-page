from flask import Flask, render_template
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

redirect_link = os.getenv("REDIRECT_LINK")

@app.route('/')
def index():
    return render_template('index.html', redirect_link=redirect_link)

if __name__ == '__main__':
    app.run(debug=True)

