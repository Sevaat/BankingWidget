import src.decorators as decorators


def test_log(capsys):
    @decorators.log()
    def division(a, b):
        return a / b

    result = division(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "division ok\n"
    assert result == 0.5

    division(1, 0)
    captured = capsys.readouterr()
    assert captured.out == "division error: division by zero. Inputs: (1, 0), {}\n"
