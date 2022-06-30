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

        
    
class TestViews(TestBase):
    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Director:", response.data)