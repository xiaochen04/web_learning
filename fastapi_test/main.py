"""
   测试FastAPI功能
   1、开启uvicorn服务器的方式
    (1)在命名行使用uvicorn main:app --reload, main表示模块名，app时FastAPI的核心对象
    （2）在模块中通过代码开启uvicorn服务器
    uvicorn.run(
        app="main:app",
        host="localhost",
        port=8000,
        reload= True
    )
    2、@app.get("/"),路径操作
   本质是一个装饰器，app是FastAPI的核心对象，get表示处理的请求的请求方式，其中的参数"/"表示处理的请求的qq地址（路径）
   即浏览器访问服务器发送的请求的请求方式是get，请求地址是"/"时，当前请求会被装饰器所装饰的函数处理
   / ==http://localhost:8000
   /user == http://localhost:8000/user

    3、请求方式（操作方式）
    GET（查询资源）、POST（新增资源）、PUT（修改资源）、DELETE（删除资源）

    4、请求参数
    （1）路径参数
    格式：通过路径模型中的的{}占位符匹配路径参数，例如：@app.get("/items/{item_id}"
    获取方式：在装饰器所装饰的函数的形参位置，设置占位符系统名字的参数即可获取所对应的路径参数
    参数类型的设置，在形参位置，为形参设置指定的类型，例如：def xx(item_id: int)
    return {"item_id":item_id}
                获取的路径参数默认为字符串类型，设置参数类型后，会自动转换为设置类型
    （2）查询参数
    格式：请求路径？参数名=参数值&参数名=参数值&....
    获取方式：在装饰器所装饰的函数的形参位置，设置和参数名相同名字的形参即可获取所对应的查询参数
    参数类型的设置：在形参位置，为形参设置指定的类型，例如：def xxx{username:str)
                获取的查询参数默认为字符串类型，设置参数类型后，会自动转换为设置类型
    参数的默认值（可选参数）：查询参数所对应的函数的形参，可以设置默认值，当形参设置了默认值，那么所对应的查询参数可以不传
    类型转换：若查询参数所对应的形参设置为bool类型，此时可以在浏览器端输入0，false，False，no,1|true，yes)

    （3）请求体参数
    请求体参数本质是json
    创建一个类型，继承BaseModel，以当前数据为模板设置数据，保证类型中的属性的属性名（类型）要json保持一致
    获取方式：在装饰器所装饰的函数的形参位置，设置一个形参，其类型为继承BaseModel的模板类
    注意：此时一定不能使用get请求方式，因为个体、请求没有请求体


    5、函数的返回值
    处理请求的函数的返回值会被自动转换为json格式，并作为响应报文的响应体响应到浏览器

"""
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    age: int
    gender: str






#创建FastAPI的实例对象（核心对象）
app = FastAPI()
@app.get("/")
def read_root():
    # 响应到浏览器的响应报文的响应体
    return {"message":"Hello World"}

#路径参数
@app.get("/items/{item_id}")
def read_item(item_id: int,username: str= None,flag: bool= False):
    return {"item_id":item_id,"user_name":username,"flag":flag}

@app.post("/test/requestbody")
def read_requestbody(item:Item):
    return {"item":item}


@app.get("/items/{item_id}/test/{item_name}")
def read_items(item_id,item_name):
    return {"item_id":item_id,"item_name":item_name}

@app.get("/user")
def read_user():
    return {"message":"hello user"}

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="localhost",
        port=8000,
        reload= True
    )
