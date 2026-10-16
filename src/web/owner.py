import os
from pathlib import Path
from fastapi import APIRouter, HTTPException
from model.owner import Owner
from service import owner as service

router = APIRouter(prefix = "/owner")
top = Path(__file__).resolve().parent

@router.get("")
def get_all() -> list[Owner]:
    return service.get_all()

@router.get("/{owner_id}")
def get_one(owner_id: int) -> Owner:
    try:
        return service.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.post("", status_code=201)
def create(owner: Owner) -> Owner:
    try:
        return service.create(Owner)
    except Duplicate as exc:
        raise HTTPException(status_code=409, detail=exc.msg)
