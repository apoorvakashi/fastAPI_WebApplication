from fastapi import APIRouter, Depends, Response, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm 
from sqlalchemy.orm import Session
from .. import database

from .. import models, schemas, utils, oauth2


router = APIRouter(tags=["Authentication"])

@router.get('/login', response_model=schemas.Token)
def login(user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    login_user = db.query(models.User).filter(models.User.email == user.username).first()

    if not login_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")

    if not utils.verify(user.password, login_user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
    
    access_token = oauth2.create_access_token(data= {"user_id" : login_user.id})

    return {"access_token" : access_token, "token_type" : "Bearer"}
