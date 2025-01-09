from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=200, response_model=Message)
def read_root():
    return {'message': 'Olá mundo'}


@app.get('/ola', status_code=200, response_class=HTMLResponse)
def ola_mundo():
    return """
    <html>
    <head>
        <title>Olá mundo</title>
    </head>
    <body>
        <h1>Olá mundo</h1>
    </body>
    </html>
    """
