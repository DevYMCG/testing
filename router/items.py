from typing import List
from fastapi import Depends, APIRouter, HTTPException, status
from database import get_db
from sqlalchemy.orm import Session
from models import Items
from schemas import ItemCreate, ShowItem
from datetime import datetime

router = APIRouter()

@router.post('/items', tags=["items"], response_model=ShowItem)
def create_item(item: ItemCreate, db:Session=Depends(get_db)):
    date_posted = datetime.now().date()
    item = Items(**item.dict(), date_posted=date_posted, owner_id=1)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.get("/item/all", tags=["items"], response_model=List[ShowItem])
def retrieve_all_items(db:Session=Depends(get_db)):
    items = db.query(Items).all()
    return items


@router.get("/item/{id}", tags=["items"], response_model=ShowItem)
def retrieve_item_by_id(id: int, db:Session=Depends(get_db)):
    item = db.query(Items).filter(Items.id == id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item