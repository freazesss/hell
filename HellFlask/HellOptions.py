from platform import system
from subprocess import call


class Built:
    def write(f_name: str, *f_arguments):
        with open(f_name, "w+") as f:
            for i in range(len(f_arguments)):
                f.write(f_arguments[i])
    
    def create_folders(*folders):
        for i in range(len(folders)):
            call(f"mkdir -p {folders[i]}")

    verify = lambda : r"\\" if system() == "Windows" else "/"

class HellOptions:
    def create(self, name):
        Built.create_folders("app", f"app{Built.verify()}home", f"app{Built.verify()}templates")

        # Create the base of a project.

        Built.write("run.py", "from app import app\n\n", "if __name__ == '__main__':\n", " app.run(debug=True)")
        Built.write(f"app{Built.verify()}__init__.py", 
                    "from flask import Flask\n",
                    "from .home import home\n\n", 
                    "app = Flask(__name__)\n",
                    "app.register_blueprint(home)")

        # Create the things of homepage.

        Built.write(f"app{Built.verify()}home{Built.verify()}__init__.py", 
                    "from flask import Blueprint\n\n", 
                    "home = Blueprint('home', __name__)\n",
                    "from . import views")
        
        Built.write(f"app{Built.verify()}home{Built.verify()}views.py", 
                    "from . import home\n",
                    "from flask import render_template\n\n", 
                    "@home.route('/')\n",
                    "def homepage():\n",
                    "   return render_template('home.html')")

        # Create the first template
        
        Built.write(f"app{Built.verify()}templates{Built.verify()}home.html",
                    "<h1>Hello, World!</h1>")

    def run(self):
        call("python run.py")
