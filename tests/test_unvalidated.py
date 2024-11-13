from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_unvalidated_login_success():
    response = client.post("/unvalidated/login", data={"email": "teste@teste.com", "password": "teste"})
    assert response.status_code == 200
    assert response.json() == {"message": "Login aceito sem validação: teste@teste.com"}


def test_unvalidated_login_xss():
    name = '<script>alert("XSS")</script>'
    response = client.get(f"/unvalidated/greet?name={name}")
    assert response.status_code == 200
    assert response.json() == {"message": f"Olá, {name}"}


def test_unvalidated_login_empty_email():
    response = client.post("/unvalidated/login", data={"email": "", "password": "teste"})
    assert response.status_code == 200
    assert response.json() == {"message": "Login aceito sem validação: "}
