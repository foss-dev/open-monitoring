"""
https://flask-migrate.readthedocs.io/en/latest/

We use Flask-Migrate to database migrations.

These are commands to flask-migrate

python manage.py db init --> init migrations

python manage.py db migrate --> migrate models

python manage.py db upgrade --> apply changes

python manage.py db --help --> :)
"""
from werkzeug import generate_password_hash

from om_core.data.models import db, User
from om_core import app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

db.init_app(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manager.run()
