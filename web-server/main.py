import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return[1,2,3]

@app.get('/contact', response_class= HTMLResponse)
def get_list():
    return """
        <h1> Hola con response_class= HTMLResponse puedo crear html desde un @app.get o como sea que se llame esto de ingrasar a funciones de manera rapida o facil (no olvides llamaro de la libreria con from) </h1>
        <p>ay que tener buena practicas en todo nuestro entorno python para evitar errores y dolores de cabeza</p>
        """

def  run():
    store.get_categories()

if __name__ == '__main__':
    run()