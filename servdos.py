from flask_restful import Resource
import pandas as pd
import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

class UploadCSV(Resource):

    def post(self):
        files = request.files['file']
        df = pd.read_csv(files)
        listDF = []
        for i in range(len(df.columns)):
          a = pd.unique(df.iloc[:, i].str.replace(' ', ''))
          colname = df.columns[i]
          df2=pd.DataFrame(a, columns=['AGI'])
          df3 = df2[df2.iloc[:, 0].notna()].set_index('AGI').assign(**{colname:1})
          listDF.append(df3)
          conc= pd.concat(listDF, axis=1, ignore_index=False).fillna(0)
          conc.loc[:,'Total'] = conc.sum(axis=1)
          js= conc.to_json(orient='records')
        return(js)


api.add_resource(UploadCSV, '/v1/upload')

if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=5000)