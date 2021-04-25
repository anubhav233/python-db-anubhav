import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from main import app

from project.models import db
from project.models import *

#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI")
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://tht:tht@ad292e33ac7d74aa2a72e1a8fd9859d3-636793537.ap-south-1.elb.amazonaws.com:5432/tht"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CORS_HEADERS'] = 'Content-Type'

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
