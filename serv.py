# This is the code
# Find me on discord ZDev1#4511
# We shouldn't install flask in the terminal, it is already imported
from flask import (Flask, request)
from flask_cors import CORS, cross_origin
import numpy as np
import pandas as pd

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# route
@app.route('/', methods=['POST'])##
@cross_origin()
# route function
def col2df():
  ##df = pd.read_csv("ConsolidadoMainDB.csv")
  file = request.files['file']
  df = pd.read_csv(file)
  listDF = []
  for i in range(len(df.columns)):
    a = pd.unique(df.iloc[:, i].str.replace(' ', ''))
    colname = df.columns[i]
    df2=pd.DataFrame(a, columns=['AGI'])
    df3 = df2[df2.iloc[:, 0].notna()].set_index('AGI').assign(**{colname:1})
    listDF.append(df3)
  conc= pd.concat(listDF, axis=1, ignore_index=False).fillna(0)
  conc.loc[:,'Total'] = conc.sum(axis=1)
  js= conc.to_json(orient="index")
  return(js)

# route
@app.route('/file')##
@cross_origin()
# route function
def col2dfe():
  df = pd.read_csv("ConsolidadoMainDB.csv")
  ##file = request.files['file']
  ##df = pd.read_csv(file)
  listDF = []
  for i in range(len(df.columns)):
    a = pd.unique(df.iloc[:, i].str.replace(' ', ''))
    colname = df.columns[i]
    df2=pd.DataFrame(a, columns=['AGI'])
    df3 = df2[df2.iloc[:, 0].notna()].set_index('AGI').assign(**{colname:1})
    listDF.append(df3)
  conc= pd.concat(listDF, axis=1, ignore_index=False).fillna(0)
  conc.loc[:,'Total'] = conc.sum(axis=1)
  js= conc.to_json(orient="index")
  return(js)




# listen
if __name__ == "__main__":
  #from waitress import serve
  #serve(app, host="0.0.0.0", port=5000)
  app.run(port=5000)
  # if you need to make it live debuging add 'debug=True'
  # app.run(port=3000, debug=True)
  
 # Hope you enjoyed ;)
