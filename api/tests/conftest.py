import pytest
from app import create_app, db
from app.models.user import User


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
        db.session.add(User(username='test', password='password'))
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