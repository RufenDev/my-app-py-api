from fastapi import APIRouter, Query, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from api.schemas.responses import BasicResponse
from sqlalchemy import text
from typing import Annotated
from api.clients.db import get_db
        
router = APIRouter()

@router.post("/id", response_model=BasicResponse)
async def create_id(
    db: Annotated[AsyncSession, Depends(get_db)],
    prefix: str = Query(
        default=..., 
        min_length=4,
        max_length=4,
        description="ID's prefix"
    ),
): 
    insert_id_query = text("""
        INSERT INTO app_id(prefix, created_by)
        VALUES (:prefix, 'api')
        RETURNING *;                       
    """)

    try:
        new_app_id_res = await db.execute(insert_id_query, { "prefix": prefix })
        new_app_id = new_app_id_res.mappings().fetchone()
        
        await db.commit()
        
        return BasicResponse(data=dict(new_app_id))

    except Exception as ex:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=BasicResponse(
                result="ERROR",
                message=str(ex),
            ).model_dump()
        )
