import pytest
from io import StringIO
from main import user_input,console_output


def test_user_input(monkeypatch):

    buffer = StringIO()
    monkeypatch.setattr("sys.stdin", buffer)
    s = "abc"
    buffer.write(s)
    buffer.seek(0)
   
    assert s==user_input()


def test_console_output(capsys):
    s = "abc\n"
    console_output()
    assert s ==capsys.readouterr().out