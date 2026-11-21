from fastapi import FastAPI
from routers import user,iterm
import uvicorn
app=FastAPI(title="管理系统")
app.include_router(user.router)
app.include_router(iterm.router)


@app.get("/")
def read_root():
    return {"message": "Hello World"}

if __name__ == "__main__":
# 直接在代码中启动uvicorn服务器
    uvicorn.run(
                app="main:app",                # 指定要运行的FastAPI应用实例
                host="localhost",     # 允许外部访问（本地可通过127.0.0.1或localhost访问）
                port=8000,           # 端口号
                reload=True          # 开发模式：代码修改后自动重启（生产环境需去掉）
          )




