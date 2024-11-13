from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_register_form():
    response = client.get("/register/")
    assert response.status_code == 200
    assert "form" in response.text


def test_register_user_success():
    response = client.post("/register/", data={"email": "teste@teste.com", "password": "teste"})
    assert response.status_code == 200
    assert "Usuário registrado com sucesso!" in response.text


def test_register_user_already_registered():
    client.post("/register/", data={"email": "teste@teste.com", "password": "teste"})
    response = client.post("/register/", data={"email": "teste@teste.com", "password": "teste"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Usuário já registrado"}
