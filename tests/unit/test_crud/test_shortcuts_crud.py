from unittest.mock import AsyncMock, MagicMock

import pytest

from src.cruds.shortcuts_crud import ShortcutsCRUD
from src.models.shortcuts import ShortcutsModel
from src.schemas.shortcuts_schemas import ShortcutsCreateSchema


class TestShortcutsCRUD:
    @pytest.fixture
    def crud(self):
        return ShortcutsCRUD(ShortcutsModel)

    @pytest.fixture
    def mock_session(self):
        session = AsyncMock()
        session.execute = AsyncMock()
        session.add = MagicMock()
        session.commit = AsyncMock()
        session.refresh = AsyncMock()
        return session

    @pytest.mark.asyncio
    async def test_get_by_id_returns_shortcut(self, crud, mock_session):
        mock_result = MagicMock()
        mock_result.scalars.return_value.first.return_value = ShortcutsModel(
            id=1, original="https://example.com/", visits=0
        )
        mock_session.execute.return_value = mock_result

        result = await crud.get_by_id(mock_session, id=1)

        assert result is not None
        assert result.id == 1
        assert result.original == "https://example.com/"
        mock_session.execute.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_by_id_returns_none_when_not_found(self, crud, mock_session):
        mock_result = MagicMock()
        mock_result.scalars.return_value.first.return_value = None
        mock_session.execute.return_value = mock_result

        result = await crud.get_by_id(mock_session, id=999)

        assert result is None

    @pytest.mark.asyncio
    async def test_create_adds_and_commits(self, crud, mock_session):
        schema = ShortcutsCreateSchema(original="https://example.com/")

        result = await crud.create(mock_session, obj_in=schema, commit=True)

        mock_session.add.assert_called_once()
        mock_session.commit.assert_called_once()
        mock_session.refresh.assert_called_once()
        assert result is not None

    @pytest.mark.asyncio
    async def test_create_without_commit(self, crud, mock_session):
        schema = ShortcutsCreateSchema(original="https://example.com/")

        result = await crud.create(mock_session, obj_in=schema, commit=False)

        mock_session.add.assert_called_once()
        mock_session.commit.assert_not_called()
        mock_session.refresh.assert_not_called()

    @pytest.mark.asyncio
    async def test_save_commits_and_refreshes(self, crud, mock_session):
        db_obj = ShortcutsModel(id=1, original="https://test.com/", visits=5)

        result = await crud.save(mock_session, db_obj=db_obj)

        mock_session.add.assert_called_once()
        mock_session.commit.assert_called_once()
        mock_session.refresh.assert_called_once()
        assert result == db_obj
