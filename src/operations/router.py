import time
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_cache.decorator import cache

from database import get_async_session
from operations.models import operation
from operations.schemas import OperationCreate

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
    try:
        query = select(operation).where(operation.c.type == operation_type )
        result = await session.execute(query)
        return {   
            "status":"success",
            "data":result.mappings().all()
        }
    except Exception:
        raise HTTPException(status_code=500,detail={
            "status":"success",
            "data":None
        })

@router.post("/", status_code=201)
async def add_specific_operation(new_operation:OperationCreate, session: AsyncSession = Depends(get_async_session)):
    query = insert(operation).values(**new_operation.model_dump())
    await session.execute(query)
    await session.commit()
    return{"status":"success"}