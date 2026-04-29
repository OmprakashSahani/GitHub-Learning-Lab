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


def test_main_logs(monkeypatch, caplog):
    monkeypatch.setattr(sys, "argv", ["prog", "Bob"])

    with caplog.at_level("INFO"):
        main()

    assert "greet CLI started" in caplog.text
    assert "Input name: Bob" in caplog.text
    assert "Output message: Hello, Bob! Welcome to GitHub." in caplog.text
