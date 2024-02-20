import sys
sys.path.append('C:/PROGRAMAÇÃO/Vulture/app')

from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask.cli import FlaskGroup
import os

app = Flask("__name__", template_folder="app/templates", static_folder="app/static")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///vul_databank.db"

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/x-ico')


db = SQLAlchemy()
migrate = Migrate(app, db)

db.init_app(app)

cli = FlaskGroup(app)

@cli.command('create_db')
def create_db():
    if not os.path.exists('vul_databank.db'):
        with app.app_context():
            db.create_all()
        print('Databank created.')
    else:
        print('Databank already exists.')


@cli.command("update_db")
def update_db():
    with app.app_context():
        db.session.commit()
    print('Databank updated.')


if __name__ == '__main__':
    cli()