import sqlite3
import traceback
from webpage import app, db
from flask import render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from webpage.forms import RegisterForm, LoginForm, CreateGroup
from webpage.models import User, Event, Movie, Group, Family, Crime, \
    Comedy, Thriller, Fantasy, Action, Drama, Concert, Social
from flask_login import login_user, logout_user, login_required







# Setting up different routes/pages


@app.route('/error/', methods=['GET'])
def error():
    error_trace = traceback.format_exc()
    print(error_trace)
    return error_trace, 500

#Home
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')







#Movie browsing page
@app.route('/movies', methods=['GET', 'POST'])
@login_required
def movie_page():
    movies = Movie.query.all()
    return render_template('movie.html', movies=movies)





#Individual user recommendation page
@app.route('/profile/movie/recommendation', methods=['GET', 'POST'])
@login_required
def movie_recommendation():
    return render_template('movie_recommend.html')

#conn = sqlite3.connect('account.db')

#c = conn.cursor()

#c.execute("SELECT * FROM movie WHERE age=18")

#print(c.fetchall())
#conn.commit()
#conn.close()








# Event browsing page
@app.route('/events', methods=['GET', 'POST'])
@login_required
def event_page():
    events = Event.query.all()
    return render_template('event.html', events=events)


#Event recommendation to individual user page
@app.route('/profile/events/recommendation', methods=['GET', 'POST'])
@login_required
def event_recommendation():
    return render_template('event_recommend.html')












#registration page
@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Account has been created successfully! You are now logged in as {user_to_create.username}"
                                                                                    , category='success')
        return redirect(url_for('movie_page'))
    if form.errors != {}:  #If there are no errors within the validation
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)


#login page
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('movie_page'))
        else:
            flash('Username or Password are incorrect! Please try again.', category='danger')
    return render_template('login.html', form=form)

#logout page
@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))





#profile page
@app.route('/profile')
@login_required
def profile_page():

    return render_template('profile.html')





#viewing groups that individual users are in.
@app.route('/profile/groups', methods=['GET', 'POST'])
@login_required
def profile_group():
    create = CreateGroup()
    if create.validate_on_submit():
        group_to_create = Group(grouptitle=create.grouptitle.data,
                                      members=create.members.data,
                                      numofmem=create.numofmem.data,
                                      datecreated=create.datecreated.data)
        db.session.add(group_to_create)
        db.session.commit()
        flash(f"Group has been created successfully!", category='success')
        return redirect(url_for('profile_group'))
    if create.errors != {}:
        for err_msg in create.errors.values():
            flash(f'There was an error with creating a group: {err_msg}', category='danger')
    groups = Group.query.all()
    return render_template('profile_group.html', create=create, groups=groups)








@app.route('/profile/movie/family', methods=['GET', 'POST'])
@login_required
def movie_family():
    familys = Family.query.all()
    return render_template('movie_family.html', familys=familys)



@app.route('/profile/movie/crime', methods=['GET', 'POST'])
@login_required
def movie_crime():
    crimes = Crime.query.all()
    return render_template('movie_crime.html', crimes=crimes)

@app.route('/profile/movie/comedy', methods=['GET', 'POST'])
@login_required
def movie_comedy():
    comedys = Comedy.query.all()
    return render_template('movie_comedy.html', comedys=comedys)

@app.route('/profile/movie/thriller', methods=['GET', 'POST'])
@login_required
def movie_thriller():
    thrillers = Thriller.query.all()
    return render_template('movie_thriller.html', thrillers=thrillers)

@app.route('/profile/movie/fantasy', methods=['GET', 'POST'])
@login_required
def movie_fantasy():
    fantasys = Fantasy.query.all()
    return render_template('movie_fantasy.html', fantasys=fantasys)

@app.route('/profile/movie/action', methods=['GET', 'POST'])
@login_required
def movie_action():
    actions = Action.query.all()
    return render_template('movie_action.html', actions=actions)

@app.route('/profile/movie/drama', methods=['GET', 'POST'])
@login_required
def movie_drama():
    dramas = Drama.query.all()
    return render_template('movie_drama.html', dramas=dramas)




@app.route('/profile/event/music', methods=['GET', 'POST'])
@login_required
def event_music():
    musics = Concert.query.all()
    return render_template('event_music.html', musics=musics)



@app.route('/profile/event/social', methods=['GET', 'POST'])
@login_required
def event_social():
    socials = Social.query.all()
    return render_template('event_social.html', socials=socials)