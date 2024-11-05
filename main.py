from fastapi import FastAPI

from app.configs.database_settings import initialize
from app.routers.article_router import router as article_router
from app.routers.health_router import router as health_router
from app.routers.like_router import router as like_router

app = FastAPI()
app.include_router(article_router)
app.include_router(health_router)
app.include_router(like_router)
app.include_router(article_router)
initialize(app)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

#
# # http verb get
# @app.get("/")
# async def root() -> dict[str, str]:
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str) -> dict[str, str]:
#     return {"message": f"Hello {name}"}
#
#
# if __name__ == "__main__":
#     import uvicorn
#
#     uvicorn.run(app, host="0.0.0.0", port=8000)
