from fastapi import APIRouter, Query, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from api.schemas.responses import BasicResponse
from sqlalchemy import text
from typing import Annotated
from api.clients.db import get_db
        
router = APIRouter()

@router.get("/id", response_model=BasicResponse)
async def get_ids(
    db: Annotated[AsyncSession, Depends(get_db)],
    start: int = Query(default=0, ge=0),
    size: int = Query(default=50, gt=0),
    prefix: str = Query(
        default=None, 
        min_length=4,
        max_length=4,
        description="ID's prefix"
    ),
):
    select_by_prefix = "WHERE prefix ILIKE :prefix" if prefix else ''
    
    select_ids_query = text(f"""
        SELECT *
        FROM app_id 
        { select_by_prefix }
        ORDER BY created_date ASC
        LIMIT :size
        OFFSET :start;
    """)  
    
    try:
        select_ids_res = await db.execute(select_ids_query, { 
            "prefix": prefix, 
            "size": size,
            "start": start,
        })
        
        # selected_ids = list(select_ids_res)
        selected_ids = [ dict(row) for row in select_ids_res.mappings().all() ]
                
        return BasicResponse(data=selected_ids)

    except Exception as ex:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=BasicResponse(
                result="ERROR",
                message=str(ex),
            ).model_dump()
        )
