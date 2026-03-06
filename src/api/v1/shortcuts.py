from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession

from cruds.shortcuts_crud import shortcuts_crud
from database.database import get_async_session
from schemas.shortcuts_schemas import ShortcutsCreateSchema, ShortcutsReadSchema

router = APIRouter()


@router.post(
    "/shorten/",
    response_model=ShortcutsReadSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_shortcut(
    new_shortcut: ShortcutsCreateSchema,
    db_session: AsyncSession = Depends(get_async_session),
):
    """"Create a new shortcut for the given original URL.

    **- original**: The original URL to be shortened.
    """

    return await shortcuts_crud.create(db_session, obj_in=new_shortcut)


@router.get("/{id}/")
async def redirect(
    id: int,
    db_session: AsyncSession = Depends(get_async_session),
):
    """Redirect to the original URL associated with the given shortcut ID and increment the visit count.

    **- id**: The ID of the shortcut to redirect to.
    """
    shortcut = await shortcuts_crud.get_by_id(db_session, id=id)
    if not shortcut:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not found"
        )
    shortcut.visits += 1
    await shortcuts_crud.save(db_session, db_obj=shortcut)
    return RedirectResponse(
        url=shortcut.original,
        status_code=status.HTTP_301_MOVED_PERMANENTLY
    )


@router.get("/stats/{id}/", response_model=ShortcutsReadSchema)
async def get_shortcut_stats(
    id: int,
    db_session: AsyncSession = Depends(get_async_session)
):
    """Get the statistics of a shortcut, including the original URL and the number of visits.
    **- id**: The ID of the shortcut to retrieve statistics for.
    """
    shortcut = await shortcuts_crud.get_by_id(db_session, id=id)
    if not shortcut:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return shortcut
