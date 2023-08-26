from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.operations.models import operation
from src.operations.schemas import OperationCreate

router = APIRouter(
    prefix="/operations",
    tags=["operation"],
)

@router.get("/")
async def get_specific_operation(operation_type:str, session: AsyncSession = Depends(get_async_session)):
    query = select(operation).where(operation.c.type == operation_type )
    result = await session.execute(query)
    return result.mappings().all()

# BUGS!!!!
@router.post("/")
async def add_specific_operation(new_operation:OperationCreate, session: AsyncSession = Depends(get_async_session)):
    
    query = insert(operation).values(
        quantity = new_operation.quantity,
        figi = new_operation.figi,
        instrument_type = new_operation.instrument_type,
        type = new_operation.type,
    )
    await session.execute(query)
    await session.commit()
    return{"status":"success"}