from flask import url_for
from flask_testing import TestCase

from app import app
from application import db
from application.models import Directors, Movies
from application.forms import DirectorForm, MovieForm

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = "sqlite:///testdata.db",
            SECRET_KEY = "testsecurityKey",
            WTF_CSRF_ENABLED=False
            )
        return app

    def setUp(self):
        db.create_all()

        testDir = Directors(
            dir_name = "TestDirector"
        )
        db.session.add(testDir)
        db.session.commit()

        testMov = Movies(
            movie_name = "TestMovie",
            rel_yr = 2000 ,
            dirID = 1
        )
        db.session.add(testMov)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestAddDir(TestBase):
    def test_add_director(self):
        response = self.client.post(
            url_for('addD'),
            data = dict(
                dir_name = "TestDir2"
                )
        )
        assert Directors.query.filter_by(dir_name = "TestDir2").first().id == 2

    def test_view_director(self):
        response = self.client.get(url_for('viewD'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'TestDirector', response.data)
    
    def test_view_add_director(self):
        response = self.client.get(url_for('addD'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Director Name", response.data)
    
    def test_no_movs(self):
        response = self.client.get(url_for('noMovies'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"No Movies to Display!", response.data)


class TestAddMovie(TestBase):
    def test_add_movie(self):
        response = self.client.post(
            url_for('add'),
            data = dict(
                movie_name = "TestMovie1",
                dirID = 1
                )
        )
        assert Movies.query.filter_by(movie_name = "TestMovie1").first().id == 2
    
    def test_view_add_movie(self):
        response = self.client.get(url_for('add'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Movie Title", response.data)



class TestViewHome(TestBase):
    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Director:", response.data)

class TestDirMovies(TestBase):
    def test_dir_movs(self):
        response = self.client.get(url_for('dirMovs', id=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Movies: ", response.data)

class TestUpdateDirector(TestBase):
    def testUpdateDir(self):
        response = self.client.get(url_for('updateD', id=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Update Director:', response.data)
    
    def testUpdateDirpost(self):
        response = self.client.post(
            url_for('updateD', id=1),
            data = dict(
                dir_name = "TestDir",
                )
        )
        assert Directors.query.filter_by(dir_name = "TestDir").first().id == 1

class TestUpdateMovie(TestBase):
    def testUpdateMov(self):
        response = self.client.get(url_for('update', id=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Update Movie:', response.data)
    
    def testUpdateMovpost(self):
        response = self.client.post(
            url_for('update', id=1),
            data = dict(
                movie_name = "TestMovie1",
                
                )
        )
        assert Movies.query.filter_by(movie_name = "TestMovie1").first().id == 1


class TestDelDir(TestBase):
    def test_delDirector(self):
        response = self.client.get(url_for('deleteD', id=1))
        assert len(Directors.query.all()) == 0



class TestDelMov(TestBase):
    def test_delMovie(self):
        response = self.client.get(url_for('delete', id=1))
        assert len(Movies.query.all()) == 0