from os import system
from platform import system as sys


class website:
    def __init__(self):
        self.run() # Call the run function

    def run(self):
        """
        Create the files necessaries to create you website.
        """

        if sys() == "Linux":
            sis = "/"
        elif sys() == "Windows":
            sis = r"\\"

        system(f'mkdir -p app{sis}home')
        with open(f'app{sis}home{sis}views.py', 'w+') as f:
            f.write("""from . import home
from flask import render_template

@home.route('/')
def homepage():
    return render_template('home.html')

""")

        system(f'mkdir app{sis}templates')
        with open(f'app{sis}templates{sis}home.html', 'w+') as f:
            f.write("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hell</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Hell</h1>
</body>
</html>
""")
        system(f'mkdir app{sis}static')
        with open(f'app{sis}static{sis}style.css', 'w+') as f:
            f.write("""
* {
    margin: 0%;
    padding: 0%;
    font-family: sans-serif;
}
""")

        with open(f'app{sis}home{sis}__init__.py', 'w+') as f:
            f.write("""from flask import Blueprint

home = Blueprint('home', __name__)

from . import views
""")
        with open(f'app{sis}templates{sis}404.html', 'w+') as f:
            f.write("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hell - not_found</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Hell - Not Found</h1>
</body>
</html>
""")

        with open(f'app{sis}run.py', 'w+') as f:
            f.write("""from flask import Flask, render_template
from home import home

app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

app.register_blueprint(home)
app.run(debug=True)
""")
