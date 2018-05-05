
# dependencies

from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from flask_sqlalchemy import SQLAlchemy
import pandas as pd


db_url = "sqlite:///belly_button_biodiversity.sqlite"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
db = SQLAlchemy(app)

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





    





