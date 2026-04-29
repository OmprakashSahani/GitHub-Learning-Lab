from app.greet import greet


def test_greet():
    assert greet("Om") == "Hello, Om! Welcome to GitHub."
