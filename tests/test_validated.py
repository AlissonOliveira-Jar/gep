from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_validated_login_success():
    client.post("/register/", data={"email": "test@teste.com", "password": "Password123!"})

    response = client.post("/validated/login", data={"email": "test@teste.com", "password": "Password123!"})
    assert response.status_code == 200
    assert response.json() == {"message": "Login bem-sucedido!"}


def test_validated_login_user_not_found():
    response = client.post("/validated/login", data={"email": "notregistered@teste.com", "password": "password123!"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Usuário não encontrado"}


def test_validated_login_xss():
    name = '<script>alert("XSS")</script>'
    response = client.get(f"/validated/greet?name={name}")
    assert response.status_code == 200
    assert response.json() == {"message": "Olá, &lt;script&gt;alert(&quot;XSS&quot;)&lt;/script&gt;"}


def test_validated_login_weak_password():
    client.post("/register/", data={"email": "test3@teste.com", "password": "password123!"})

    response = client.post("/validated/login", data={"email": "test3@teste.com", "password": "weak"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Password must contain at least one letter, one number, and one special character"}
