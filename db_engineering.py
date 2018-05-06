# -*- coding: utf-8 -*-
"""
Created on Sun May  6 10:48:20 2018

@author: corey
"""

# dependencies
from flask import Flask, render_template, jsonify, request, redirect
from sqlalchemy import MetaData
from sqlalchemy.ext.automap import automap_base


from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)

db_url = "sqlite:///db/belly_button_biodiversity.sqlite"

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)






metadata = MetaData()
tables = ['otu', 'samples', 'samples_metadata']
metadata.reflect(db.engine, only=tables)
Base = automap_base()
Base.prepare(db.engine, reflect=True)
