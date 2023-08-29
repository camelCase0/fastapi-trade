import time
from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_cache.decorator import cache

from src.database import get_async_session
from src.operations.models import operation
from src.operations.schemas import OperationCreate

router = APIRouter(
    prefix="/operations",
    tags=["operation"],
)

@router.get("/big-amount")
@cache(expire=30)
async def get_big_operations():
    time.sleep(2)
    return "BIG DATA"


@router.get("/")
async def get_specific_operation(operation_type:str, session: AsyncSession = Depends(get_async_session)):
    query = select(operation).where(operation.c.type == operation_type )
    result = await session.execute(query)
    return result.mappings().all()

@router.post("/")
async def add_specific_operation(new_operation:OperationCreate, session: AsyncSession = Depends(get_async_session)):
    query = insert(operation).values(**new_operation.model_dump())
    await session.execute(query)
    await session.commit()
    return{"status":"success"}