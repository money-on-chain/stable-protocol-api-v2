from fastapi import APIRouter, Query, HTTPException
from typing import Annotated

from api.db import get_db
from api.models.omoc import DATE_FIELDS, VestingCreatedList, ClaimOKList
from api.utils import fields_date_to_str


router = APIRouter()


@router.get(
    "/v1/omoc/vesting_created/",
    tags=["omoc"],
    response_description="Returns vesting created from a holder address",
    response_model=VestingCreatedList
)
async def vesting_created(
        holder: Annotated[str, Query(
            title="Holder address",
            description="Holder Address",
            regex='^0x[a-fA-F0-9]{40}$')] = '0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3',
        limit: Annotated[int, Query(
            title="Limit",
            description="Limit",
            le=100)] = 50,
        skip: Annotated[int, Query(
            title="Skip",
            description="Skip",
            le=1000)] = 0):

    # get mongo db connection
    db = await get_db()

    if db is None:
        raise HTTPException(status_code=400, detail="Cannot get DB")

    query_filter = {
        "holder": {"$regex": holder.lower(), '$options': 'i'}
    }

    rows = await db["event_VestingFactory_VestingCreated"]\
        .find(query_filter)\
        .sort("createdAt", -1)\
        .skip(skip)\
        .limit(limit)\
        .to_list(limit)

    rows_count = await db["event_VestingFactory_VestingCreated"].count_documents(query_filter)

    for trx in rows:
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
        "transactions": rows,
        "count": len(rows),
        "total": rows_count,
        "last_block_indexed": last_block_indexed
    }

    return dict_values


@router.get(
    "/v1/omoc/claim_ok/",
    tags=["omoc"],
    response_description="Returns Claim from a holder address",
    response_model=ClaimOKList
)
async def claim_ok(
        holder: Annotated[str, Query(
            title="Holder address",
            description="Holder Address",
            regex='^0x[a-fA-F0-9]{40}$')] = '0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3',
        limit: Annotated[int, Query(
            title="Limit",
            description="Limit",
            le=100)] = 20,
        skip: Annotated[int, Query(
            title="Skip",
            description="Skip",
            le=1000)] = 0):

    # get mongo db connection
    db = await get_db()

    if db is None:
        raise HTTPException(status_code=400, detail="Cannot get DB")

    query_filter = {
        "recipient": {"$regex": holder.lower(), '$options': 'i'}
    }

    rows = await db["event_IncentiveV2_ClaimOK"]\
        .find(query_filter)\
        .sort("createdAt", -1)\
        .skip(skip)\
        .limit(limit)\
        .to_list(limit)

    rows_count = await db["event_IncentiveV2_ClaimOK"].count_documents(query_filter)

    for trx in rows:
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
        "results": rows,
        "count": len(rows),
        "total": rows_count,
        "last_block_indexed": last_block_indexed
    }

    return dict_values
