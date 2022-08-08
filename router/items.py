from typing import List
from fastapi import Depends, APIRouter, HTTPException, status
from database import get_db
from sqlalchemy.orm import Session
from models import Items, User
from fastapi.encoders import jsonable_encoder
from schemas import ItemCreate, ShowItem
from datetime import datetime
from router.login import oauth2_scheme
from jose import jwt
from config import setting

router = APIRouter()

def get_user_from_token(db, token):
    try:
        payload = jwt.decode(token, setting.SECRET_KEY, algorithms=setting.ALGORITHM)
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unable to verify credentials")
        user = db.query(User).filter(User.email == username).first()
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unable to verify credentials")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unable to verify credentials")
    return user


@router.post('/items', tags=["items"], response_model=ShowItem)
def create_item(item: ItemCreate, db:Session=Depends(get_db), token:str = Depends(oauth2_scheme)):
    user = get_user_from_token(db, token)
    date_posted = datetime.now().date()
    item = Items(**item.dict(), date_posted=date_posted, owner_id=user.id)
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


@router.put("/item/update/{id}", tags=["items"])
def update_item_by_id(id:int, item: ItemCreate, db:Session=Depends(get_db),token:str= Depends(oauth2_scheme)):
    user = get_user_from_token(db, token)
    existing_item = db.query(Items).filter(Items.id == id)
    if not existing_item.first():
        return {"message": f"No details exists for Item ID {id}"}
    if existing_item.first().owner_id == user.id:
        # existing_item.update(jsonable_encoder(item))
        existing_item.update(item.__dict__)
        db.commit()
        return {"message": f"Details for Item ID {id} successfully updated"}
    else:
        return {"message": "You are not authorized"}


@router.delete("/item/delete/{id}", tags=["items"])
def delete_item_by_id(id:int, db:Session=Depends(get_db), token:str= Depends(oauth2_scheme)):
    user = get_user_from_token(db, token)
    existing_item = db.query(Items).filter(Items.id == id)
    if not existing_item.first():
        return {"message": f"No details exists for Item ID {id}"}
    if existing_item.first().owner_id == user.id:
        existing_item.delete()
        db.commit()
        return {"message": f"Item id {id} has been successfully delleted"}
    else:
        return {"message": "You are not authorized"}