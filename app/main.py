#1. Importing Libraries
import uvicorn
from fastapi import FastAPI
from Record import PatientRecord
import joblib
import os

#2. Creating app object
curr_dir=os.getcwd()
#print(curr_dir)
parent_path=os.path.dirname(curr_dir)
#print(parent_path)
model_path=parent_path+'\Models\model.pkl'
app=FastAPI()
model=joblib.load(model_path)

#3. Index route automatically to localhost
@app.get('/')
def index():
    return {'message':'Hello'}

#4. Route with a single parameter
@app.get('/{name}')
def get_name(name:str):
    return {'message':f"Hello {name}"}

#5. Route to post request for prediction
@app.post('/predict')
def get_predict(val:PatientRecord):
    data=val.model_dump()
    Clump_Thickness=data['Clump_Thickness']
    Uniformity_of_Cell_Size=data['Uniformity_of_Cell_Size']
    Uniformity_of_Cell_Shape=data['Uniformity_of_Cell_Shape']
    Marginal_Adhesion=data['Marginal_Adhesion']
    Single_Epithelial_Cell_Size=data['Single_Epithelial_Cell_Size']
    Bare_Nuclei=data['Bare_Nuclei']
    Bland_Chromatin=data['Bland_Chromatin']
    Normal_Nucleoli=data['Normal_Nucleoli']
    Mitoses=data['Mitoses']
    prediction=model.predict([[Clump_Thickness,Uniformity_of_Cell_Size,Uniformity_of_Cell_Shape,Marginal_Adhesion,Single_Epithelial_Cell_Size,Bare_Nuclei,Bland_Chromatin,Normal_Nucleoli,Mitoses]])
    if(prediction[0]==2):
        return {'prediction':'Benign'}
    elif(prediction[0]==4):
        return {'prediction':'Malignant'}

if(__name__=="__main__"):
    uvicorn.run(app,host='127.0.0.1',port=8000)

