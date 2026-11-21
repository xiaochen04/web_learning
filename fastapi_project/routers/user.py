from fastapi import APIRouter

router=APIRouter(
    prefix="/user",
    tags=["用户管理"],
)

@router.get("/")
def read_root():
    return {"message": "Hello user"}

@router.get("/{user_id}")
def read_root(user_id: int):
    return {"user_id": user_id}





