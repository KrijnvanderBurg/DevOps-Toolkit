from hello_world.__main__ import main


def test_always_pass1() -> None:
    assert True


def test_always_pass2() -> None:
    assert True


def test_always_pass3() -> None:
    assert True


def test_main() -> None:
    main(filepath="path/to/test.txt")
