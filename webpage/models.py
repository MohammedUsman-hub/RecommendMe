from webpage import db, login_manager
from webpage import bcrypt
from flask_login import UserMixin


#user_loader callback, allows application to understand if user is logged in or not
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#model created to create user and insert user values to 'account.db' database
class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
#    event = db.relationship('Event', backref='owned_user')

    # returning property when users wants it
    @property
    def password(self):
        return self.password
    # generates a password hash when user creates account.
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    # checks if password is correct
    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)



# model created to create Events table and its columns.
class Event(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=38), nullable=False, unique=False)
    location = db.Column(db.String(length=38), nullable=False, unique=False)
    type = db.Column(db.String(length=38), nullable=False, unique=False)
    datetime = db.Column(db.String(), nullable=False, unique=False)


    def __repr__(self):
        return f'Event {self.name}'


# model created to create Movie table and its columns.
class Movie(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, unique=False)
    genre = db.Column(db.String(length=50), nullable=False, unique=False)
    age = db.Column(db.Integer(), nullable=False, unique=False)
    date = db.Column(db.String(length=50), nullable=False, unique=False)


    def __repr__(self):
        return f'Event {self.name}'



class Group(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    grouptitle = db.Column(db.String(length=50), nullable=False, unique=False)
    members = db.Column(db.String(length=100), nullable=False, unique=False)
    numofmem = db.Column(db.Integer(), nullable=False, unique=False)
    datecreated = db.Column(db.String(length=50), nullable=False, unique=False)








class Family(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, unique=False)
    genre = db.Column(db.String(length=50), nullable=False, unique=False)
    age = db.Column(db.Integer(), nullable=False, unique=False)
    date = db.Column(db.String(length=50), nullable=False, unique=False)


    def __repr__(self):
        return f'Event {self.name}'



class Crime(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, unique=False)
    genre = db.Column(db.String(length=50), nullable=False, unique=False)
    age = db.Column(db.Integer(), nullable=False, unique=False)
    date = db.Column(db.String(length=50), nullable=False, unique=False)


    def __repr__(self):
        return f'Event {self.name}'


class Comedy(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, unique=False)
    genre = db.Column(db.String(length=50), nullable=False, unique=False)
    age = db.Column(db.Integer(), nullable=False, unique=False)
    date = db.Column(db.String(length=50), nullable=False, unique=False)


    def __repr__(self):
        return f'Event {self.name}'


class Thriller(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, unique=False)
    genre = db.Column(db.String(length=50), nullable=False, unique=False)
    age = db.Column(db.Integer(), nullable=False, unique=False)
    date = db.Column(db.String(length=50), nullable=False, unique=False)


    def __repr__(self):
        return f'Event {self.name}'


class Fantasy(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, unique=False)
    genre = db.Column(db.String(length=50), nullable=False, unique=False)
    age = db.Column(db.Integer(), nullable=False, unique=False)
    date = db.Column(db.String(length=50), nullable=False, unique=False)


    def __repr__(self):
        return f'Event {self.name}'



class Action(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, unique=False)
    genre = db.Column(db.String(length=50), nullable=False, unique=False)
    age = db.Column(db.Integer(), nullable=False, unique=False)
    date = db.Column(db.String(length=50), nullable=False, unique=False)


    def __repr__(self):
        return f'Event {self.name}'



class Drama(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, unique=False)
    genre = db.Column(db.String(length=50), nullable=False, unique=False)
    age = db.Column(db.Integer(), nullable=False, unique=False)
    date = db.Column(db.String(length=50), nullable=False, unique=False)


    def __repr__(self):
        return f'Event {self.name}'



class Social(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=38), nullable=False, unique=False)
    location = db.Column(db.String(length=38), nullable=False, unique=False)
    type = db.Column(db.String(length=38), nullable=False, unique=False)
    datetime = db.Column(db.String(), nullable=False, unique=False)


    def __repr__(self):
        return f'Event {self.name}'




class Concert(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=38), nullable=False, unique=False)
    location = db.Column(db.String(length=38), nullable=False, unique=False)
    type = db.Column(db.String(length=38), nullable=False, unique=False)
    datetime = db.Column(db.String(), nullable=False, unique=False)


    def __repr__(self):
        return f'Event {self.name}'