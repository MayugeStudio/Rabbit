# --- Third Party Library ---
import pytest

# --- First Party Library ---
from rabbit_todo.common.result import Result


class TestResult:
    def test_ok(self):
        result = Result.ok("OK")
        assert result.is_success() is True
        assert result.unwrap() == "OK"

    def test_error(self):
        result = Result.error("ERROR")
        assert result.is_success() is False
        with pytest.raises(RuntimeError) as info:
            result.unwrap()
        assert info.value.message == "Result is not a success"
