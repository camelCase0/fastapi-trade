from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from starlette.datastructures import URL
from src.operations.router import get_specific_operation

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)
templates = Jinja2Templates(directory="src/templates")

@router.get("/")
def get_base_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@router.get("/search/{operation_type}")
def get_search_page(request: Request, operation=Depends(get_specific_operation)):
    return templates.TemplateResponse("base.html", {"request": request, "operation":operation["data"]})

@router.get("/login")
def get_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
async def login(request: Request):
    form = await request.form()
    return templates.TemplateResponse("base.html", {"request": request})