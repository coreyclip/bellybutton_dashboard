
# dependencies
from flask import Flask, render_template, jsonify, request, redirect
from sqlalchemy import MetaData
from sqlalchemy.ext.automap import automap_base


from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)

db_url = "sqlite:///db/belly_button_biodiversity.sqlite"

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
db = SQLAlchemy(app)

metadata = MetaData()
tables = ['otu', 'samples', 'samples_metadata']
metadata.reflect(db.engine, only=tables)
Base = automap_base(metadata=metadata)
Base.prepare(db.engine, reflect=True)

#from .models import otu, samples_metadata 



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

    #retrieve the sample names
    sample_names = [str(x) for x in db.session.query(metadata.SAMPLEID).all()]

    return jsonify(sample_names)


@app.route("/otu")
def get_otu():
    """List of OTU descriptions.

    Returns a list of OTU descriptions in the following format

    [
        "Archaea;Euryarchaeota;Halobacteria;Halobacteriales;Halobacteriaceae;Halococcus",
        "Archaea;Euryarchaeota;Halobacteria;Halobacteriales;Halobacteriaceae;Halococcus",
        "Bacteria",
        "Bacteria",
        "Bacteria",
        ...
    ]
    """

    unit_names = [str(x) for x in db.session.query(otu.taxonomic_unit).all()]
    print(unit_names)
    return jsonify(unit_names)


@app.route("/metadata/<sample>")
def get_sample_meta(sample):
    """MetaData for a given sample.

    Args: Sample in the format: `BB_940`

    Returns a json dictionary of sample metadata in the format

    {
        AGE: 24,
        BBTYPE: "I",
        ETHNICITY: "Caucasian",
        GENDER: "F",
        LOCATION: "Beaufort/NC",
        SAMPLEID: 940
    }
    """
    result = db.session.query(samples_metadata.AGE,
                               samples_metadata.BBTYPE,
                               samples_metadata.ETHNICITY,
                               samples_metadata.GENDER,
                               samples_metadata.LOCATION,
                               samples_metadata.SAMPLEID
                               ).filter(samples_metadata.SAMPLEID == sample)
    print(result)
    return jsonify(result)

@app.route('/wfreq/<sample>')
def get_wfreq(sample):
    """Weekly Washing Frequency as a number.

    Args: Sample in the format: `BB_940`

    Returns an integer value for the weekly washing frequency `WFREQ`
    """
    result = db.session.query(samples_metadata.WFREQ).filter(samples_metadata.SAMPLEID == sample)
    print(result)
    return jsonify(result)

@app.route('/samples/<sample>')
def get_samples(sample):
    """OTU IDs and Sample Values for a given sample.

    Sort your Pandas DataFrame (OTU ID and Sample Value)
    in Descending Order by Sample Value

    Return a list of dictionaries containing sorted lists  for `otu_ids`
    and `sample_values`

    [
        {
            otu_ids: [
                1166,
                2858,
                481,
                ...
            ],
            sample_values: [
                163,
                126,
                113,
                ...
            ]
        }
    ]
    """
 
    otu_samples = []
    samples = Base.classes.samples

    for row in session.query(samples).all():
        otu_samples.append(row)
    print(otu_samples)

    return jsonify(otu_samples)

if __name__ == "__main__":
    app.run(debug=True)





    





