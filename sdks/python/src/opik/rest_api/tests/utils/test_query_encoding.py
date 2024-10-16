# This file was auto-generated by Fern from our API Definition.

from Opik.core.query_encoder import encode_query


def test_query_encoding() -> None:
    assert encode_query({"hello world": "hello world"}) == {
        "hello world": "hello world"
    }
    assert encode_query({"hello_world": {"hello": "world"}}) == {
        "hello_world[hello]": "world"
    }
    assert encode_query(
        {"hello_world": {"hello": {"world": "today"}, "test": "this"}, "hi": "there"}
    ) == {
        "hello_world[hello][world]": "today",
        "hello_world[test]": "this",
        "hi": "there",
    }
