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

@app.route('/noMovies')
def noMovies():
    return render_template("noMovies.html")

@app.route('/directorsMovies/<id>')
def dirMovs(id):
    directors = Directors.query.get(id)
    movs = []
    movie = Movies.query.all()
    for movies in movie:
        if movies.dirID == directors.id :
            movs.append(movies.movie_name) 
    if movs == []:
        return url_for('noMovies')
    movs = ", ".join(movs)         
    return render_template("directorsMovies.html", Directors=directors, Movies=movs)

@app.route('/addMovie', methods=['GET', 'POST'])
def add():
    form = MovieForm()
    form.director.choices = [(directors.id,directors.dir_name) for directors in Directors.query.all()]
    if request.method == 'POST':
        # if form.validate_on_submit():
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

@app.route('/updateMovie/<int:id>', methods=['GET', 'POST'])
def update(id):
    form = MovieForm()    
    movies = Movies.query.get(id)
    form.director.choices = [(directors.id,directors.dir_name) for directors in Directors.query.all()]
    if request.method == 'POST':
        movies.movie_name = form.movie_name.data
        movies.rel_yr = form.rel_yr.data
        movies.dirID = form.director.data
        db.session.commit()
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.movie_name.data = movies.movie_name
        form.rel_yr.data = movies.rel_yr
        form.director.data = movies.dirID
        db.session.commit()
    return render_template('updateMovie.html', form=form, oldMovie=Movies.query.get(id).movie_name)

@app.route('/updateDirector/<int:id>', methods=['GET', 'POST'])
def updateD(id):
    form = DirectorForm()    
    directors = Directors.query.get(id)
    if form.validate_on_submit():
        directors.dir_name = form.dir_name.data
        db.session.commit()
        return redirect(url_for('viewD'))
    elif request.method == 'GET':
        form.dir_name.data = directors.dir_name
        db.session.commit()
    return render_template('updateDirector.html', form=form, oldDir=Directors.query.get(id).dir_name)