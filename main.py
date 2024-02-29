from fastapi import FastAPI,Depends,Query,HTTPException 
from sqlalchemy.orm import Session
from database import engine, SessionLocal,Base
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import model
app=FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

class UserRequest(BaseModel):
    email:str
    password:str
    isActive:bool
    name:str


def getdb():
    db=SessionLocal()
    try:   
        yield db
    finally:
        db.close()   

@app.get("/getAllUser")
def getAllUser(db:Session=Depends(getdb)):
    users=db.query(model.User).filter(model.User.company_id==None).all()
    print(users)
    return  users



@app.post("/saveUser")
def saveUser(request:UserRequest,db:Session=Depends(getdb)):
    user=model.User(email=request.email,password=request.password,is_active=request.isActive,name=request.name)
    db.add(user)
    db.commit()
    return user.id


@app.put("/updateUser/{user_id}")
def update_user(user_id: int, request: UserRequest, db: Session = Depends(getdb)):
    user = db.query(model.User).filter(model.User.id == user_id).first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    user.email = request.email
    user.is_active = request.isActive
    user.name = request.name
    user.password = request.password

    db.commit()

    return {"message": "User updated successfully"}

@app.get("/sendSms/{mobileNumber}")
def sendsms(mobileNumber: str):
    print(mobileNumber)
    return {"message": f"Received mobile number: {mobileNumber}"}

@app.get("/getUserById/{userId}")
def getUserById(userId:int,db:Session=Depends(getdb)):
    user=db.query(model.User).filter(model.User.id==userId).first()
    return user


@app.delete("/deleteUserById/{userId}")
def deleteUserById(userId:int,db:Session=Depends(getdb)):
    user=db.query(model.User).filter(model.User.id==userId).first()
    if user is None:
        raise Exception("user does not exist")
    db.delete(user)
    db.commit()
    return {"message":"delete successfully"}








