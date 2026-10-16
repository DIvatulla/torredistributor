import os
from model.owner import Owner
from data import owner as data

def get_all() -> list[Owner]:
    return data.get_all()

def get_one(owner_id: int) -> Owner:
    return data.get_one(owner_id)

def create(owner: Owner) -> Owner:
    return data.create(owner_id)