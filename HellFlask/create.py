from os import system

class create:
    def __init__(self, website_name):
        self.website_name = website_name
        self.run() # Call the run function
    def run(self):
        """
        Websites templates.
        """
        ques = input('\n\033[0;33m[1] Basic app\n > A Simple website with one file\n[2] Basic app with Blueprint\n > A Simple website with blueprint\n\033[0;35mType it:\033[m')

        if ques == "1":
            self.one_file()
        elif ques == "2":
            self.blueprint()
        else:
            print('\033[0;35mYou type it something wrong\033[m')

    def blueprint(self):
        """
        Blueprint template.
        """

        system('mkdir -p app/home')
        with open('app/home/views.py', 'w') as f:
            f.write("""
from . import home
from flask import render_template

@home.route('/')
def homepage():
    return render_template('home.html')
# Hell
""")

        system('mkdir app/templates')
        with open('app/templates/home.html', 'w') as f:
            f.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.website_name}</title>
</head>
<body>
    <h1>{self.website_name}</h1>
</body>
</html>
""")

        with open('app/home/__init__.py', 'w') as f:
            f.write("""
from flask import Blueprint

home = Blueprint('home', __name__)

from . import views

# Hell
""")

        with open('app/run.py', 'w') as f:
            f.write("""
from flask import Flask
from home import home

app = Flask(__name__)
app.register_blueprint(home)

app.run(debug=True)

# Hell
""")

    def one_file(self):
        """
        One file template.
        """

        system('mkdir app')
        with open('app/main.py', 'w') as f:
            f.write("""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return '<h1>Hell</h1>'

app.run(debug=True)

# Hell
""")
