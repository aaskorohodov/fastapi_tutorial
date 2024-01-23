from starlette.testclient import TestClient
from .main import app


client = TestClient(app)


def test_read_main():
    json_body = {
        'name': 'some name',
        'description': 'some description',
        'price': 100.0,
        'tax': 50.5
    }
    response = client.post("/items/", json=json_body)
    assert response.status_code == 200
    assert response.json() == {'Your overall price': 150.5}


if __name__ == '__main__':
    test_read_main()
