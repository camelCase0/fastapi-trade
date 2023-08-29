
from datetime import datetime
from sqlalchemy import TIMESTAMP, Column, Integer, String, Table
from src.database import metadata

operation = Table(
    "operation",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("quantity",String),
    Column("figi",String),
    Column("instrument_type",String, nullable=True),
    Column("date",TIMESTAMP,default=datetime.utcnow),
    Column("type",String),
)