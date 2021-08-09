import pickle
from fastapi import FastAPI
import pandas as pd

app = FastAPI()
@app.post('/model')

def titanic(Sex:int, Age: float, Lifeboat: int, Pclass: int):
    dados = pd.DataFrame([[Sex,Age, Lifeboat,Pclass]], columns = ['Sex','Age','Lifeboat','Pclass'])
    with open('codigo/model/Titanic.pkl', 'rb') as fid: 
        titanic = pickle.load(fid)

    resposta = titanic.predict(dados)

    if resposta[0] == 1:
        survived = True
        message = "Sobreviveu!!!"
    else: 
        survived = False
        message = "Não sobreviveu :/"
    
    retornar = {'survived': survived, 'status':200, 'message': message}

    return retornar

@app.get('/model')
def get():
    return {'hello':'test'}
