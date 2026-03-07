from .base import BaseCRUD
from models.shortcuts import ShortcutsModel


class ShortcutsCRUD(BaseCRUD):
    async def increment_visits(self, db, *, id: int) -> ShortcutsModel | None:
        shortcut = await self.get_by_id(db, id=id)
        if shortcut:
            shortcut.visits += 1
            db.add(shortcut)
            await db.commit()
            await db.refresh(shortcut)
        return shortcut


shortcuts_crud = ShortcutsCRUD(ShortcutsModel)
