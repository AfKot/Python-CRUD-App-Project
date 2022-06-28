from application import app, db
from application.models import Movies, Directors
from application.forms import MovieForm, DirectorForm
from flask import Flask, redirect, url_for, render_template, request

@app.route('/')
def home():
    movies = Movies.query.all()
    return render_template("home.html", Movies=movies)

@app.route('/viewDirectors')
def viewD():
    directors = Directors.query.all()
    return render_template("viewDirectors.html", Directors=directors)


@app.route('/addMovie', methods=['GET', 'POST'])
def add():
    form = MovieForm()
    form.director.choices = [(directors.id,directors.dir_name) for directors in Directors.query.all()]
    if request.method == 'POST':
        if form.validate_on_submit():
            movieData = Movies(
                movie_name = form.movie_name.data,
                rel_yr = form.rel_yr.data,
                dirID = form.director.data
            )
            db.session.add(movieData)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('addMovie.html', form=form)

@app.route('/addDirector', methods=['GET', 'POST'])
def addD():
    form = DirectorForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            directorData = Directors(
                dir_name = form.dir_name.data,                
            )
            db.session.add(directorData)
            db.session.commit()
            return redirect(url_for('viewD'))
    return render_template('addDirector.html', form=form)

@app.route('/delete/<id>')
def delete(id):
    movie_del = Movies.query.get(id)
    db.session.delete(movie_del)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/deleteD/<id>')
def deleteD(id):
    director_del = Directors.query.get(id)
    db.session.delete(director_del)
    db.session.commit()
    return redirect(url_for('viewD'))

