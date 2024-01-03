import datetime
from pydantic import BaseModel, Field
from typing import Optional, List
import uuid


def mongo_date_to_str(x):
    return str(x.isoformat(timespec='milliseconds'))+"Z"


class Params(BaseModel):
    tp: Optional[str] = None
    token: Optional[str] = None
    amount: Optional[str] = None
    qTP: Optional[str] = None
    qTC: Optional[str] = None
    qACmax: Optional[str] = None
    qACmin: Optional[str] = None
    qTPmin: Optional[str] = None
    qTCmin: Optional[str] = None
    tpFrom: Optional[str] = None
    tpTo: Optional[str] = None
    sender: Optional[str] = None
    recipient: Optional[str] = None
    vendor: Optional[str] = None
    hash: Optional[str]
    blockNumber: Optional[int] = None
    createdAt: Optional[datetime.datetime] = None
    lastUpdatedAt: Optional[datetime.datetime] = None


class Executed(BaseModel):
    tp_: Optional[str] = None
    tpFrom_: Optional[str] = None
    tpTo_: Optional[str] = None
    qTPfrom_: Optional[str] = None
    qTPto_: Optional[str] = None
    tp: Optional[str] = None
    qTP_: Optional[str] = None
    qTC_: Optional[str] = None
    qAC_: Optional[str] = None
    qACfee_: Optional[str] = None
    qFeeToken_: Optional[str] = None
    qACVendorMarkup_: Optional[str] = None
    qFeeTokenVendorMarkup_: Optional[str] = None
    vendor_: Optional[str] = None
    operId_: Optional[int] = None
    sender_: Optional[str] = None
    recipient_: Optional[str] = None
    hash: Optional[str]
    blockNumber: Optional[int] = None
    createdAt: Optional[datetime.datetime] = None
    lastUpdatedAt: Optional[datetime.datetime] = None


class Operations(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    hash: Optional[str]
    blockNumber: Optional[int] = None
    operId_: Optional[int] = None
    gas: Optional[int] = None
    gasPrice: Optional[str] = None
    gasUsed: Optional[int] = None
    gasFeeRBTC: Optional[str] = None
    status: Optional[int] = None
    errorCode_: Optional[str] = None
    msg_: Optional[str] = None
    reason_: Optional[str] = None
    operation: Optional[str] = None
    createdAt: Optional[datetime.datetime] = None
    lastUpdatedAt: Optional[datetime.datetime] = None
    confirmationTime: Optional[datetime.datetime] = None
    params: Optional[Params] = None
    executed: Optional[Executed] = None
    last_block_indexed: Optional[int] = None

    class Config:
        #allow_population_by_field_name = True
        json_schema_extra = {
            "example": {
                "id": "0x0000000",
                "hash": "0x0000000"
            }
        }


class OperationsList(BaseModel):
    operations: List[Operations]
    count: int = 0
    total: int = 0
    last_block_indexed: int = 0

    class Config:
        json_schema_extra = {
            "example": {
                "operations": "[]",
                "count": "0",
                "total": "0",
                "last_block_indexed": "12345678"
            }
        }
