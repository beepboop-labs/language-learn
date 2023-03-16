# language-learn

## Frontend Vue.js Application

### Setting up the development environment
First, make sure you have Node.js version 18 and NPM installed.

Next, install the project dependencies. From the root project directory `/front-end` run:
```
npm install
```

This should create a `node_modules` directory that stores all the external libraries for the project. It's not checked into version control and is listed in `.gitignore`

**NOTE**: When you install new packages with `npm install <SOME-PACKAGE>` they will automatically be added to the `package.json` and tracked so other devs can install the same dependencies for running the project.

### Running the application

To run a development server locally, from the root directory `front-end/` use:
```
npm run dev
```

### Project Structure
```
.
├── README.md
├── index.html
├── package-lock.json
├── package.json
├── public
│   └── favicon.ico
└── src
    ├── App.vue
    ├── assets
    │   ├── base.css
    │   ├── icons
    │   │   └── logo.svg
    │   └── main.css
    ├── components
    │   ├── Footer.vue
    │   └── Navbar.vue
    ├── main.js
    ├── router
    │   └── index.js
    └── views
        ├── Home.vue
        ├── Login.vue
        ├── MultipleChoiceQuiz.vue
        └── Register.vue
```

#### app.vue
This is the main vue.js application. All other components and views are generated inside of here. 

#### assets/
The application-wide .css files as well as other app assets like logos and icons live here

#### views/
Individual pages such as `Login.vue` live here. They need to be registered with vue-router in `router/index.js` in order to be able to work.

#### components/
Contains vue templates which aren't pages on their own, but that may be used inside views or inside other components. Things like Navbars, Footers, or forms that may be re-used in multuple places are examples of what goes here.

#### router/
Contains the file which sets up page routing for the app. If you create a new page ('view'), make sure to import and register the view here.

#### package.json
This is the file that tracks javascript project dependencies using npm (Node Package Manager).

## Backend Flask API

### Setting up the development environment
First, make sure Python 3.x is installed

To keep the python dependencies for the project seperate from other environments on your computer, create a virtual environment in the root of the `/api` project:
```
pip install virtualenv
python3.9 -m venv pyenv
```
This should create a new folder `pyenv` that will contain all of the project-specific dependencies.
The `pyenv` directory is kept out of version control via `.gitignore`, if it's named something else this won't work and you may accidentally check a bunch of libraries into get.

When working on the project, you'll need to first activate the virtual environment from the root directory with:
```
source pyenv/bin/activate
```
Next, install the required project dependencies:
```
pip install -r requirements.txt
```
If you have installed new project dependencies, save them to the `requirements.txt` file using:
```
pip freeze > requirements.txt
```

In order for the API to connect to databases and function correctly, you will need a file that contains keys and passwords. `example.env` contains the format required for the app. Make a copy of this file, fill in the required keys and passwords, and rename it `.env`. This key file is kept out of version control via `.gitignore`

### Running the application
To run the application, from the root directory `/api`:
```
flask run
```

### Running Tests
The tests live in the directory `api/tests` and are grouped into subdirectories that mimic the directory structure of `api/app`. The `conftest.py` file contains setup, tear-down, and other instructions to configure the tests.

To run the tests, from the root directory `/api`:
```
pytest
```

### Creating or Updating Database models

If you create a new database model or update an existing one, you'll need to apply a 'migration' to see the changes reflected in the db. This is part of the SQL Alchemy library and related tools that help connect and manage a database.
There's a more extensive reference here:
[Flask-Migrate Docs](https://flask-migrate.readthedocs.io/en/latest/)

After making changes to models, navigate to the root project directory at `/api` and run the following with a 'commit-style' message:
```
flask db migrate -m "<INSERT A MESSAGE HERE>"

flask db upgrade
```

### Project Structure

```
.
├── app
│   ├── __init__.py
│   ├── models
│   │   ├── __init__.py
│   │   └── user.py
│   ├── routes
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── quiz.py
│   │   └── user.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── quiz_service.py
│   │   └── user_service.py
│   └── utils
│       └── __init__.py
├── config.py
├── migrations/ {contents not listed}
├── requirements.txt
└── tests
    ├── __init__.py
    ├── conftest.py
    ├── routes
    │   ├── test_auth.py
    │   └── test_quiz.py
    ├── services
    │   ├── test_auth_service.py
    │   └── test_quiz_service.py
    └── utils
```

#### Why is `__init__.py` everywhere?
`__init__.py` is a python-ism that essentially defines a directory or subdirectory as a module. This means if you want to be able to import modules, classes, or methods from one place to another, then they need to be in a folder with an `__init__.py` file. These are almosty all empty files with one important exception: `/app/__init__.py` contains the code that initializes the main flask application (our server).


#### app/models
Contains classes that map to database tables. The app uses Flask-SQLAlchemy to interact with the MySQL db and provides tools for ORM(object relational mapping). Each file here is a class, like `Users.py`, that define a db table and any helper methods associated with it.

**NOTE**:If you are adding or updating a model, you need to apply a database migration to update the database. See section on db migrations.

#### app/routes
Contains the routes that serve as the applications API endpoints. Many route files are associated with a database model, like `routes/user.py`, but some are associated with other actions like `routes/auth.py` which contain endpoints for logging in and registering users.

Route modules are only concerned with directing requests and calling the needed methods from `services/` to perform logical operations, db calls, etc. 

**NOTE**: If you are adding a new route to the api, make sure to import and register the route in `api/app/__init__.py

#### app/services
Contains the methods that do the heavy lifting in the application. Mostly this will involve making calls to the database. Methods are organized together within a module that is associated with a given route. So, for example, `auth_service.py` contains methods associated with the `routes/auth.py` endpoint.


#### app/utils
There's nothing here right now, but this is a place for helper modules that aren't associated with any particular api endpoint. Things like password hashing or maybe calculating new english/spanish/swahili word pairs would belong here. 