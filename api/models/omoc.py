import datetime
from pydantic import BaseModel, Field
from typing import Optional, List
import uuid

DATE_FIELDS = [
    'createdAt',
    'lastUpdatedAt',
]

class VestingCreated(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    hash: Optional[str] = None
    blockNumber: Optional[int] = None
    holder: Optional[str] = None
    vesting: Optional[str] = None
    createdAt: Optional[datetime.datetime] = None
    lastUpdatedAt: Optional[datetime.datetime] = None

    class Config:
        json_schema_extra = {
            "example": {
                "_id": "658dac848e6961287ceb62e5",
                "hash": "0xaddc1a3b49fcd5528a4a394d98e095c1f89475e1e30b9a237e93231c15e4a265",
                "blockNumber": 4643915,
                "holder": "0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3",
                "vesting": "0xF20Ee80f56F41b6323D140b07A011c77509Fb99D",
                "createdAt": None,
                "lastUpdatedAt": "2023-12-28T14:15:01.629000Z"
            }
        }


class VestingCreatedList(BaseModel):
    transactions: List[VestingCreated]
    count: int = 0
    total: int = 0
    last_block_indexed: int = 0

    class Config:
        json_schema_extra = {
            "example": {
                "results": "[]",
                "count": "0",
                "total": "0",
                "last_block_indexed": "12345678"
            }
        }


class ClaimOK(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    hash: Optional[str]
    blockNumber: Optional[int] = None
    recipient: Optional[str] = None
    origin: Optional[str] = None
    value: Optional[str] = None
    createdAt: Optional[datetime.datetime] = None
    lastUpdatedAt: Optional[datetime.datetime] = None

    class Config:
        json_schema_extra = {
            "example": {
                "_id": "658dac848e6961287ceb62e5",
                "hash": "0xaddc1a3b49fcd5528a4a394d98e095c1f89475e1e30b9a237e93231c15e4a265",
                "blockNumber": 4643915,
                "recipient": "0xF20Ee80f56F41b6323D140b07A011c77509Fb99D",
                "origin": "0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3",
                "value": "177577695063561323",
                "createdAt": None,
                "lastUpdatedAt": "2023-12-28T14:15:01.629000Z"
            }
        }


class ClaimOKList(BaseModel):
    results: List[ClaimOK]
    count: int = 0
    total: int = 0
    last_block_indexed: int = 0

    class Config:
        json_schema_extra = {
            "example": {
                "results": "[]",
                "count": "0",
                "total": "0",
                "last_block_indexed": "12345678"
            }
        }
