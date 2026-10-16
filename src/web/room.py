from fastapi import APIRouter

@router.get("/")
def root():
	return "Main page"

