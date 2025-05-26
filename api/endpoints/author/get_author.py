from fastapi import APIRouter, Query
from api.schemas.responses import BasicResponse
from typing import Optional

router = APIRouter()

@router.get("/author", response_model=BasicResponse)
def get_books(
    first_name: Optional[str] = Query(
        default=None, 
        description="Filter by author's first name"
    ),
    last_name: Optional[str] = Query(
        default=None,
        description="Filter by author's last name"
    ),
    middle_name: Optional[str] = Query(
        default=None,
        description="Filter by author's last name"
    )
): 
    return BasicResponse()
