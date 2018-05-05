
# dependencies
from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)

db_url = "sqlite:///belly_button_biodiversity.sqlite"

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
db = SQLAlchemy(app)

class otu(db.Model):
    __tablename__ = 

# Create database tables
@app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/sampleNames")
def get_sample_names():

    # create engine that connects us to the database
    engine = create_engine(db_url, echo='debug')

    # use automap_base so that we don't have to define classes for our tables
    Base = automap_base()

    Base.prepare(engine, reflect=True)

    #extract the samples_metadata which has the sample names
    samples_metadata = Base.classes.samples_metadata

    #create a session
    session = Session(engine)

    #retrieve the sample names
    sample_names = [str(x) for x in session.query(samples_metadata.SAMPLEID).all()]

    return jsonify(sample_names)


@app.route("/otu")
def get_otu():
    # create engine that connects us to the database
    engine = create_engine(db_url, echo='debug')

    # use automap_base so that we don't have to define classes for our tables
    Base = automap_base()

    Base.prepare(engine, reflect=True)

    #extract the otu which has the sample names
    otu = Base.classes.otu

    #create a session
    session = Session(engine)

    #retrieve the sample names
    unit_names = [str(x) for x in session.query(otu.taxonomic_unit).all()]

    return jsonify(unit_names)


@app.route("/metadata/<sample>")
def get_sample_meta(sample):
        # create engine that connects us to the database
    engine = create_engine(db_url, echo='debug')

    # use automap_base so that we don't have to define classes for our tables
    Base = automap_base()

    Base.prepare(engine, reflect=True)

    #extract the samples_metadata which has the sample names
    samples_metadata = Base.classes.samples_metadata

    #create a session
    session = Session(engine)

    final_json = session.query(samples_metadata.AGE,
                               samples_metadata.BBTYPE,
                               samples_metadata.ETHNICITY,
                               samples_metadata.GENDER,
                               samples_metadata.LOCATION,
                               samples_metadata.SAMPLEID
                               ).filter(samples_metadata.SAMPLEID == sample)
    print(final_json)
    return jsonify(final_json)

if __name__ == "__main__":
    app.run(debug=True)





    





