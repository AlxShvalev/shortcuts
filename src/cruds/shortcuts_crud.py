from .base import BaseCRUD
from models.shortcuts import ShortcutsModel


class ShortcutsCRUD(BaseCRUD):
    pass


shortcuts_crud = ShortcutsCRUD(ShortcutsModel)
