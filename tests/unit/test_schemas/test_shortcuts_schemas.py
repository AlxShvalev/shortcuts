import pytest
from pydantic import ValidationError

from src.schemas.shortcuts_schemas import ShortcutsCreateSchema, ShortcutsReadSchema


class TestShortcutsCreateSchema:
    def test_create_with_valid_url(self):
        schema = ShortcutsCreateSchema(original="https://google.com/")
        assert str(schema.original) == "https://google.com/"

    def test_create_with_www_url(self):
        schema = ShortcutsCreateSchema(original="https://www.example.com/path")
        assert str(schema.original) == "https://www.example.com/path"

    def test_create_with_http_url(self):
        schema = ShortcutsCreateSchema(original="http://localhost:8080/path")
        assert str(schema.original) == "http://localhost:8080/path"

    def test_create_with_query_params(self):
        schema = ShortcutsCreateSchema(original="https://example.com?param=value")
        assert str(schema.original) == "https://example.com/?param=value"

    def test_create_with_invalid_url_raises_error(self):
        with pytest.raises(ValidationError):
            ShortcutsCreateSchema(original="not-a-url")

    def test_create_with_empty_url_raises_error(self):
        with pytest.raises(ValidationError):
            ShortcutsCreateSchema(original="")

    def test_serialize_to_string(self):
        schema = ShortcutsCreateSchema(original="https://example.com/")
        data = schema.model_dump()
        assert isinstance(data["original"], str)
        assert data["original"] == "https://example.com/"


class TestShortcutsReadSchema:
    def test_read_schema_with_all_fields(self):
        schema = ShortcutsReadSchema(original="https://example.com/", id=1, visits=0)
        assert schema.id == 1
        assert schema.visits == 0
        assert str(schema.original) == "https://example.com/"

    def test_read_schema_serialization(self):
        schema = ShortcutsReadSchema(original="https://example.com/", id=42, visits=100)
        data = schema.model_dump()
        assert data["id"] == 42
        assert data["visits"] == 100
        assert data["original"] == "https://example.com/"
