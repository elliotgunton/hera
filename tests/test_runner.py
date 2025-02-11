import pytest

from hera.shared.serialization import serialize
from hera.workflows.runner import _runner


@pytest.mark.parametrize(
    "entrypoint,kwargs_list,expected_output",
    [
        (
            "examples.workflows.callable_script:my_function",
            [{"name": "input", "value": '{"a": 2, "b": "bar"}'}],
            '{"output": [{"a": 2, "b": "bar"}]}',
        ),
        (
            "examples.workflows.callable_script:another_function",
            [{"name": "inputs", "value": '[{"a": 2, "b": "bar"}, {"a": 2, "b": "bar"}]'}],
            '{"output": [{"a": 2, "b": "bar"}, {"a": 2, "b": "bar"}]}',
        ),
        (
            "examples.workflows.callable_script:str_function",
            [{"name": "input", "value": '{"a": 2, "b": "bar"}'}],
            '{"output": [{"a": 2, "b": "bar"}]}',
        ),
    ],
)
def test(entrypoint, kwargs_list, expected_output):
    # WHEN
    output = _runner(entrypoint, kwargs_list)
    # THEN
    assert serialize(output) == expected_output
