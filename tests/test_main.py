from src.main import HelloWorld


def test_greeting():
    expected = "Hello Andre!"
    actual = HelloWorld(name="Andre").greeting()
    assert actual == expected


def test_goodbye():
    expected = "Goodbye!"
    actual = HelloWorld(name="andre").Goodbye()
    assert actual == expected
