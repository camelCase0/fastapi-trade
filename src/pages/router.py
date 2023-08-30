from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/",
    tags=["Pages"]
)
templates = Jinja2Templates(directory="templates")

@router.get("")
def get_base_page():
    pass

@router.get("/search/{operation_type}")
def get_search_page():
    pass