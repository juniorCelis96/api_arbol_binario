from fastapi import FastAPI
from service.arbol import ArbolBinario

app = FastAPI()

@app.get('/')
async def home():
    return "Hola mundo"

@app.post('/create-tree')
async def crear_arbol(data: list):
    arbol_binario = ArbolBinario(data[0])
    for i in data[1:]:
        dato = i
        data = arbol_binario.agregar(dato=dato)
        

    return data

