from flask import Flask
from flask import Flask, render_template
from config import Config
from routes import register_routes
from models import db

app = Flask(__name__)
app.config.from_object(Config)


db.init_app(app)

register_routes(app)

@app.route('/index')
def index():
    return render_template('index.html')  

if __name__ == '__main__':
    app.run(debug=True)