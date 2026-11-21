from fastapi import APIRouter

router=APIRouter(
    prefix="/item",
    tags=["商品管理"],
)

@router.get("/")
def read_root():
    return {"message": "Hello item"}

@router.get("/{item_id}")
def read_root(item_id: int):
    return {"item_id": item_id}