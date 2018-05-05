import sqlalchemy
from sqlalchemy.ext.automap import automap_base

from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    inspect,
    Column,
    String,
    Integer)

from sqlalchemy.orm import (
    Session,
    mapper,
    scoped_session,
    sessionmaker)


#import pandas as pd

#from flask import Flask, jsonify,render_template
# reflect an existing database into a new model
Base = automap_base()    

engine = create_engine("sqlite:///belly_button_biodiversity.sqlite")
metadata = MetaData(engine)
print("engine created.........")

# reflect the tables
Base.prepare(engine, reflect=True)

samples = Base.classes.samples
#otu = Base.classes.otu

print("Tables reflected....")

# Create our session (link) from Python to the DB
session = Session(engine)

inspector = inspect(engine)
inspector.get_table_names()

# Create an app, being sure to pass __name__
#app = Flask(__name__)




