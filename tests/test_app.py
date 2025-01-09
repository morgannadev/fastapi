from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá mundo'}


def test_ola_mundo_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/ola')

    assert response.status_code == HTTPStatus.OK
    assert (
        response.text
        == """
    <html>
    <head>
        <title>Olá mundo</title>
    </head>
    <body>
        <h1>Olá mundo</h1>
    </body>
    </html>
    """
    )
