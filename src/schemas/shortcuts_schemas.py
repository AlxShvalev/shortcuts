from pydantic import BaseModel, HttpUrl, field_serializer


class ShortcutsCreateSchema(BaseModel):
    original: HttpUrl

    @field_serializer('original')
    def serialize_url(self, value: HttpUrl) -> str:
        return str(value)


class ShortcutsReadSchema(ShortcutsCreateSchema):
    id: int
    visits: int
