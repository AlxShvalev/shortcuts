from fastapi import APIRouter

from .shortcuts import router as shortcuts_router


router = APIRouter()

router.include_router(shortcuts_router, prefix="", tags=["shortcuts"])