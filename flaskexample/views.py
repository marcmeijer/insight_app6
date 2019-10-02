""" This file largely follows the steps outlined in the Insight Flask tutorial, except data is stored in a
flat csv (./assets/births2012_downsampled.csv) vs. a postgres database. If you have a large database, or
want to build experience working with SQL databases, you should refer to the Flask tutorial for instructions on how to
query a SQL database from here instead.

May 2019, Donald Lee-Brown
"""

from flask import render_template
from flaskexample import app
from flaskexample.a_model import ModelIt
import pandas as pd
from flask import request

# here's the homepage
@app.route('/')
def homepage():
   # pull 'drug_check' from input field and store it
   rx = request.args.get('drug_check')

   # read in our csv file
   dbname = './flaskexample/static/data/cvs_oncology_formulary.csv'
   drug_db = pd.read_csv(dbname)

   # let's only select Oncology drugs with the specified drug check
   #drug_db = drug_db[drug_db['specialty'] == 'oncology']
   drug_db = drug_db[drug_db['drug'] == rx]

   # we really only need the likelihood and drug check for this one
   drug_db = drug_db[['drug','likelihood_short','brand_name','alert']]

   # just select oncology  from the drug data base for the drug that the user inputs
   drugs = []
   for i in range(0, drug_db.shape[0]):
      drugs.append(dict(index=drug_db.iloc[i]['drug'], attendant=drug_db.iloc[i]['alert'],
                        drug_check=drug_db.iloc[i]['brand_name']))
   the_result = ModelIt(rx, drugs)
   return render_template("model_output.html", births=drugs, the_result=the_result)
