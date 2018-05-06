
from flask_app import db

class Otu(db.Model):
    __tablename__ = 'otu'

    otu_id = db.Column(db.Integer, primary_key=True)
    lowest_taxanomic_unit_found = db.Column(db.String)
    
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

    def __repr__(self):
        return '<id %r>' % (self.SAMPLEID)