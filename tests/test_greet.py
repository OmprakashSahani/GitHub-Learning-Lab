import sys

from app.greet import greet, main


def test_greet():
    assert greet("Om") == "Hello, Om! Welcome to GitHub."


def test_main_default(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["prog"])
    main()
    captured = capsys.readouterr()
    assert "Hello, Omprakash!" in captured.out


def test_main_with_arg(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["prog", "Alice"])
    main()
    captured = capsys.readouterr()
    assert "Hello, Alice!" in captured.out
