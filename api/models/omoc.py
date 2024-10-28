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


class DelayMachinePaymentCancel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    hash: Optional[str] = None
    blockNumber: Optional[int] = None
    idTx: int = Field(alias="id")
    source: Optional[str] = None
    destination: Optional[str] = None
    amount: Optional[str] = None
    createdAt: Optional[datetime.datetime] = None
    lastUpdatedAt: Optional[datetime.datetime] = None

    class Config:
        json_schema_extra = {
            "example": {
                "_id": "658dac848e6961287ceb62e5",
                "hash": "0xaddc1a3b49fcd5528a4a394d98e095c1f89475e1e30b9a237e93231c15e4a265",
                "blockNumber": 4643915,
                "idTx": 15,
                "source": "0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3",
                "destination": "0xF20Ee80f56F41b6323D140b07A011c77509Fb99D",
                "amount": "177577695063561323",
                "createdAt": "2023-12-28T14:15:01.629000Z",
                "lastUpdatedAt": "2023-12-28T14:15:01.629000Z"
            }
        }


class DelayMachinePaymentCancelList(BaseModel):
    results: List[DelayMachinePaymentCancel]
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


class DelayMachinePaymentDeposit(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    hash: Optional[str] = None
    blockNumber: Optional[int] = None
    idTx: int = Field(alias="id")
    source: Optional[str] = None
    destination: Optional[str] = None
    amount: Optional[str] = None
    expiration: Optional[int] = None
    createdAt: Optional[datetime.datetime] = None
    lastUpdatedAt: Optional[datetime.datetime] = None

    class Config:
        json_schema_extra = {
            "example": {
                "_id": "658dac848e6961287ceb62e5",
                "hash": "0xaddc1a3b49fcd5528a4a394d98e095c1f89475e1e30b9a237e93231c15e4a265",
                "blockNumber": 4643915,
                "idTx": 15,
                "source": "0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3",
                "destination": "0xF20Ee80f56F41b6323D140b07A011c77509Fb99D",
                "amount": "177577695063561323",
                "expiration": "177577695063561323",
                "createdAt": "2023-12-28T14:15:01.629000Z",
                "lastUpdatedAt": "2023-12-28T14:15:01.629000Z"
            }
        }


class DelayMachinePaymentDepositList(BaseModel):
    results: List[DelayMachinePaymentDeposit]
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


class DelayMachinePaymentWithdraw(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    hash: Optional[str] = None
    blockNumber: Optional[int] = None
    idTx: int = Field(alias="id")
    source: Optional[str] = None
    destination: Optional[str] = None
    amount: Optional[str] = None
    createdAt: Optional[datetime.datetime] = None
    lastUpdatedAt: Optional[datetime.datetime] = None

    class Config:
        json_schema_extra = {
            "example": {
                "_id": "658dac848e6961287ceb62e5",
                "hash": "0xaddc1a3b49fcd5528a4a394d98e095c1f89475e1e30b9a237e93231c15e4a265",
                "blockNumber": 4643915,
                "idTx": 15,
                "source": "0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3",
                "destination": "0xF20Ee80f56F41b6323D140b07A011c77509Fb99D",
                "amount": "177577695063561323",
                "createdAt": "2023-12-28T14:15:01.629000Z",
                "lastUpdatedAt": "2023-12-28T14:15:01.629000Z"
            }
        }


class DelayMachinePaymentWithdrawList(BaseModel):
    results: List[DelayMachinePaymentWithdraw]
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


class SupportersAddStake(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    hash: Optional[str] = None
    blockNumber: Optional[int] = None
    user: Optional[str] = None
    subaccount: Optional[str] = None
    sender: Optional[str] = None
    amount: Optional[str] = None
    mocs: Optional[str] = None
    createdAt: Optional[datetime.datetime] = None
    lastUpdatedAt: Optional[datetime.datetime] = None

    class Config:
        json_schema_extra = {
            "example": {
                "_id": "658dac848e6961287ceb62e5",
                "hash": "0xaddc1a3b49fcd5528a4a394d98e095c1f89475e1e30b9a237e93231c15e4a265",
                "blockNumber": 4643915,
                "user": "0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3",
                "subaccount": "0xF20Ee80f56F41b6323D140b07A011c77509Fb99D",
                "sender": "0xF20Ee80f56F41b6323D140b07A011c77509Fb99D",
                "amount": "177577695063561323",
                "mocs": "177577695063561323",
                "createdAt": "2023-12-28T14:15:01.629000Z",
                "lastUpdatedAt": "2023-12-28T14:15:01.629000Z"
            }
        }


class SupportersAddStakeList(BaseModel):
    results: List[SupportersAddStake]
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


class SupportersCancelEarnings(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    hash: Optional[str] = None
    blockNumber: Optional[int] = None
    earnings: Optional[str] = None
    start: Optional[int] = None
    end: Optional[int] = None
    createdAt: Optional[datetime.datetime] = None
    lastUpdatedAt: Optional[datetime.datetime] = None

    class Config:
        json_schema_extra = {
            "example": {
                "_id": "658dac848e6961287ceb62e5",
                "hash": "0xaddc1a3b49fcd5528a4a394d98e095c1f89475e1e30b9a237e93231c15e4a265",
                "blockNumber": 4643915,
                "earnings": "177577695063561323",
                "start": "177577695063561323",
                "end": "177577695063561323",
                "createdAt": "2023-12-28T14:15:01.629000Z",
                "lastUpdatedAt": "2023-12-28T14:15:01.629000Z"
            }
        }


class SupportersCancelEarningsList(BaseModel):
    results: List[SupportersCancelEarnings]
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


class SupportersPayEarnings(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    hash: Optional[str] = None
    blockNumber: Optional[int] = None
    earnings: Optional[str] = None
    start: Optional[int] = None
    end: Optional[int] = None
    createdAt: Optional[datetime.datetime] = None
    lastUpdatedAt: Optional[datetime.datetime] = None

    class Config:
        json_schema_extra = {
            "example": {
                "_id": "658dac848e6961287ceb62e5",
                "hash": "0xaddc1a3b49fcd5528a4a394d98e095c1f89475e1e30b9a237e93231c15e4a265",
                "blockNumber": 4643915,
                "earnings": "177577695063561323",
                "start": "177577695063561323",
                "end": "177577695063561323",
                "createdAt": "2023-12-28T14:15:01.629000Z",
                "lastUpdatedAt": "2023-12-28T14:15:01.629000Z"
            }
        }


class SupportersPayEarningsList(BaseModel):
    results: List[SupportersPayEarnings]
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


class SupportersWithdraw(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    hash: Optional[str] = None
    blockNumber: Optional[int] = None
    msgSender: Optional[str] = None
    subacount: Optional[str] = None
    receiver: Optional[str] = None
    mocs: Optional[str] = None
    blockNum: Optional[int] = None
    createdAt: Optional[datetime.datetime] = None
    lastUpdatedAt: Optional[datetime.datetime] = None

    class Config:
        json_schema_extra = {
            "example": {
                "_id": "658dac848e6961287ceb62e5",
                "hash": "0xaddc1a3b49fcd5528a4a394d98e095c1f89475e1e30b9a237e93231c15e4a265",
                "blockNumber": 4643915,
                "msgSender": "0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3",
                "subacount": "0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3",
                "receiver": "0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3",
                "mocs": "177577695063561323",
                "blockNum": 4643915,
                "createdAt": "2023-12-28T14:15:01.629000Z",
                "lastUpdatedAt": "2023-12-28T14:15:01.629000Z"
            }
        }


class SupportersWithdrawList(BaseModel):
    results: List[SupportersWithdraw]
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


class SupportersWithdrawStake(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    hash: Optional[str] = None
    blockNumber: Optional[int] = None
    user: Optional[str] = None
    subacount: Optional[str] = None
    destination: Optional[str] = None
    amount: Optional[str] = None
    mocs: Optional[str] = None
    createdAt: Optional[datetime.datetime] = None
    lastUpdatedAt: Optional[datetime.datetime] = None

    class Config:
        json_schema_extra = {
            "example": {
                "_id": "658dac848e6961287ceb62e5",
                "hash": "0xaddc1a3b49fcd5528a4a394d98e095c1f89475e1e30b9a237e93231c15e4a265",
                "blockNumber": 4643915,
                "user": "0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3",
                "subacount": "0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3",
                "destination": "0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3",
                "amount": "177577695063561323",
                "mocs": "177577695063561323",
                "createdAt": "2023-12-28T14:15:01.629000Z",
                "lastUpdatedAt": "2023-12-28T14:15:01.629000Z"
            }
        }


class SupportersWithdrawStakeList(BaseModel):
    results: List[SupportersWithdrawStake]
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


class VotingMachineVoteEvent(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    hash: Optional[str] = None
    blockNumber: Optional[int] = None
    user: Optional[str] = None
    subacount: Optional[str] = None
    destination: Optional[str] = None
    amount: Optional[str] = None
    mocs: Optional[str] = None
    createdAt: Optional[datetime.datetime] = None
    lastUpdatedAt: Optional[datetime.datetime] = None

    class Config:
        json_schema_extra = {
            "example": {
                "_id": "658dac848e6961287ceb62e5",
                "hash": "0xaddc1a3b49fcd5528a4a394d98e095c1f89475e1e30b9a237e93231c15e4a265",
                "blockNumber": 4643915,
                "user": "0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3",
                "subacount": "0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3",
                "destination": "0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3",
                "amount": "177577695063561323",
                "mocs": "177577695063561323",
                "createdAt": "2023-12-28T14:15:01.629000Z",
                "lastUpdatedAt": "2023-12-28T14:15:01.629000Z"
            }
        }


class VotingMachineVoteEventList(BaseModel):
    results: List[VotingMachineVoteEvent]
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
