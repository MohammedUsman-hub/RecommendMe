from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
# Initialize the database
db = SQLAlchemy(app)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:greenwich123@localhost/projectdb'

# Inserting Sqlite database, 'account.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///account.db'

#API secret key
app.config['SECRET_KEY'] = '0405871cef85fc80ab6e7df0'

#used for password, to make password more secure.
bcrypt = Bcrypt(app)

# allows application to recognise which flask application user wants to manage the login system with.
login_manager = LoginManager(app)
# telling login_manager where the login route is located
login_manager.login_view = 'login_page'
# displays flash message in a specific way.
login_manager.login_message_category="info"



from webpage import route

# sql password: usman123 <- ignore