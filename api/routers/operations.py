from fastapi import APIRouter, Query, HTTPException
from typing import Annotated

from api.db import get_db
from api.models.operations import OperationsList, Operations, DATE_FIELDS
from api.utils import fields_date_to_str


router = APIRouter()


@router.get(
    "/v1/operations/list/",
    tags=["operations"],
    response_description="List operations of the given address user",
    response_model=OperationsList
)
async def operations_list(
        recipient: Annotated[str, Query(
            title="Recipient address",
            description="Recipient address",
            regex='^0x[a-fA-F0-9]{40}$')] = '0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3',
        limit: Annotated[int, Query(
            title="Limit",
            description="Limit",
            le=1000)] = 20,
        skip: Annotated[int, Query(
            title="Skip",
            description="Skip",
            le=10000)] = 0
):

    # get mongo db connection
    db = await get_db()

    if db is None:
        raise HTTPException(status_code=400, detail="Cannot get DB")

    query_filter = {
        "$or": [
            {"params.recipient": {"$regex": recipient.lower(), '$options': 'i'}},
            {"params.sender": {"$regex": recipient.lower(), '$options': 'i'}}
        ]
    }

    operations = await db["operations"]\
        .find(query_filter)\
        .skip(skip)\
        .limit(limit)\
        .to_list(limit)

    operations_count = await db["operations"].count_documents(query_filter)

    for trx in operations:
        trx['_id'] = str(trx['_id'])

        fields_date_to_str(trx, DATE_FIELDS)

    # Last block indexed

    indexer = await db["moc_indexer"] \
        .find_one(sort=[("updatedAt", -1)])

    last_block_indexed = 0
    if indexer:
        if 'last_raw_tx_block' in indexer:
            last_block_indexed = indexer['last_raw_tx_block']

    dict_values = {
        "operations": operations,
        "count": len(operations),
        "total": operations_count,
        "last_block_indexed": last_block_indexed
    }

    return dict_values


@router.get(
    "/v1/operations/oper_id/",
    tags=["operations"],
    response_description="Status operations given oper id",
    response_model=Operations
)
async def operations_oper_id(
        oper_id: Annotated[int, Query(
            title="Recipient address",
            description="Recipient address")] = 13
):

    # get mongo db connection
    db = await get_db()

    if db is None:
        raise HTTPException(status_code=400, detail="Cannot get DB")

    query_filter = {
        "operId_": oper_id
    }

    operations = await db["operations"]\
        .find_one(query_filter)

    if not operations:
        raise HTTPException(status_code=404, detail="Operation id not found")

    operations['_id'] = str(operations['_id'])

    fields_date_to_str(operations, DATE_FIELDS)

    # Last block indexed
    indexer = await db["moc_indexer"] \
        .find_one(sort=[("updatedAt", -1)])

    last_block_indexed = 0
    if indexer:
        if 'last_raw_tx_block' in indexer:
            last_block_indexed = indexer['last_raw_tx_block']

    operations['last_block_indexed'] = last_block_indexed

    return operations
