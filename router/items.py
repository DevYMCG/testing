from fastapi import APIRouter

router = APIRouter()

@router.get("/items", tags=["product"])
def get_items():
    return {"message": "hello items"}