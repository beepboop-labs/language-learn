import pytest
from app import create_app, db
from app.models.user import User
from app.models.language import Language
from app.models.activity import Activity


@pytest.fixture(scope="module")
def app():
    # Create a Flask application instance
    app = create_app('config.Testing')

    # Initialize SQLAlchemy with the Flask application instance
    # db = SQLAlchemy()
    # dn.init_app(app)


    # Create and seed the test database
    with app.app_context():
        db.create_all()
        db.session.add(Language(name='spanish'))
        db.session.add(Language(name='english'))
        db.session.add(Language(name='swahili'))

        span = Language.query.filter_by(name='spanish').first()
        engl = Language.query.filter_by(name='english').first()
        swah = Language.query.filter_by(name='swahili').first()

        user = User(username='test', password='password')

        spanish_activity = Activity(language_id=span.id, user_id=user.id)
        swahili_activity = Activity(language_id=swah.id, user_id=user.id)

        user.activities.append(spanish_activity)
        user.activities.append(swahili_activity)

        db.session.add(user)

        db.session.commit()
        # Add test data here if necessary

    # Return the Flask application instance for use in testing
    yield app

    # Clean up the test database after the tests have completed
    with app.app_context():
        db.drop_all()


@pytest.fixture(scope="function")
def client(app):
    # Create a test client using the Flask application instance
    with app.test_client() as client:
        yield client