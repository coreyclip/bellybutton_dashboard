from .flask_app import db

class otu(db.Model):
    __tablename__ = 'otu'

    otu_id = db.Column(db.Integer, primary_key=True)
    taxonomic_unit = db.Column(db.String)
    
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
    ZIP = db.Column(db.Integer)
    DOG = db.Column(db.String)
    CAT = db.Column(db.String)

    def __repr__(self):
        return '<id %r>' % (self.SAMPLEID)