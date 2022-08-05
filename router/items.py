from fastapi import Depends, APIRouter
from database import get_db
from sqlalchemy.orm import Session
from models import Items
from schemas import ItemCreate, ShowItem
from datetime import datetime

router = APIRouter()

@router.post('/items', tags=["item"], response_model=ShowItem)
def create_item(item: ItemCreate, db:Session=Depends(get_db)):
    date_posted = datetime.now().date()
    item = Items(**item.dict(), date_posted=date_posted, owner_id=1)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item