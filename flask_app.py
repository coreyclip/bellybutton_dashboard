
# dependencies
import os
from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


import pandas as pd

app = Flask(__name__)

db_url = "sqlite:///db/belly_button_biodiversity.sqlite"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", '') or db_url
db = SQLAlchemy(app)

####################
# Import or define table classes 
####################
class Otu(db.Model):
    __tablename__ = 'otu'

    otu_id = db.Column(db.Integer, primary_key=True)
    lowest_taxonomic_unit_found = db.Column(db.String)
    
    def __repr__(self):
        return '<id %r>' % (self.otu_id)

class samples_metadata(db.Model):
    SAMPLEID = db.Column(db.Integer, primary_key=True)
    EVENT = db.Column(db.String)
    ETHNICITY = db.Column(db.String)
    GENDER = db.Column(db.String)
    AGE = db.Column(db.Integer)
    WFREQ = db.Column(db.Integer)
    BBTYPE = db.Column(db.String)
    LOCATION = db.Column(db.String)
    COUNTRY = db.Column(db.String)
    ZIP012 = db.Column(db.Integer)
    COUNTRY1319 = db.Column(db.String)
    ZIP1319 = db.Column(db.Integer)
    DOG = db.Column(db.String)
    CAT = db.Column(db.String)
    IMPSURFACE013  = db.Column(db.Integer)
    NPP013 = db.Column(db.Float)
    MMAXTEMP013  = db.Column(db.Float)
    PFC013  = db.Column(db.Float)
    IMPSURFACE1319  = db.Column(db.Integer)
    NPP1319	= db.Column(db.Float)  
    MMAXTEMP1319  = db.Column(db.Float)
    PFC1319 = db.Column(db.Float)


#from models import Otu, samples_metadata 


# Create database tables
@app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()

@app.route("/data")
def data():
    '''
    for debuging purposes
    '''
    results = session.query.all()
    df = pd.DataFrame(results)
    return jsonify(df.to_dict(orient='records'))

@app.route("/")
def home_page():

    return render_template('index.html')

@app.route("/sampleNames")
def get_sample_names():

    #retrieve the sample names
    sample_names = ["BB_" + str(x).strip("(").rstrip(",)") for x in db.session.query(samples_metadata.SAMPLEID).all()]
    print(sample_names)
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

    unit_names = [str(x).strip("(").rstrip(",)") for x in db.session.query(Otu.lowest_taxonomic_unit_found).all()]
    #print(unit_names)
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
    query = int(sample.strip("BB_"))
    print(query, " data type: ", type(query))
    result = db.session.query(samples_metadata.AGE,
                               samples_metadata.BBTYPE,
                               samples_metadata.ETHNICITY,
                               samples_metadata.GENDER,
                               samples_metadata.LOCATION,
                               samples_metadata.SAMPLEID
                               ).filter(samples_metadata.SAMPLEID == query).all()[0]
    
    print(result)

    final_json = {
        "AGE": result[0],
        "BBTYPE": result[1],
        "ETHNICITY": result[2],
        "GENDER": result[3],
        "LOCATION": result[4],
        "SAMPLEID": result[5],
    }

    print(final_json)
    
    return jsonify(final_json)

@app.route('/wfreq/<sample>')
def get_wfreq(sample):
    """Weekly Washing Frequency as a number.

    Args: Sample in the format: `BB_940`

    Returns an integer value for the weekly washing frequency `WFREQ`
    """
    query = int(sample.strip("BB_"))
    print(query, " data type: ", type(query))
    result = db.session.query(
            samples_metadata.WFREQ).\
            filter(samples_metadata.SAMPLEID == query).all()
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
    df = pd.read_csv("DataSets/belly_button_biodiversity_samples.csv",
                    index_col='otu_id', encoding="utf-8", dtype=None)
    
    
    query = pd.to_numeric(df[str(sample)], downcast='float', errors='coerce')

    raw_values = query.sort_values(ascending=False)[:10].to_dict()
    print(raw_values)

    #print(raw_values.keys())
    #print(raw_values.values())

    final_dict =  [
        {
            "otu_ids": [int(i) for i in raw_values.keys()],
            "sample_values": [int(i) for i in raw_values.values()]
        }
    ]

    import json 
    final_json = json.dumps(final_dict)

    

    return jsonify(final_json)

if __name__ == "__main__":
    app.run(debug=True)





    





