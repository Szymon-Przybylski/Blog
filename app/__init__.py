import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

sys.path.append('/home/SzymonPrzybylski/Blog')
blog = Flask(__name__)

#if __name__ == '__main__':
#   blog.run()

blog.config['SECRET_KEY'] = 'SECRET_KEY'
blog.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(blog)
bcrypt = Bcrypt(blog)
login_manager = LoginManager(blog)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# must be here
import routes
