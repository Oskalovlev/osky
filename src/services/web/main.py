from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

from src.services.web.routes.user.user_routes import router as user_router
# from src.services.web.routes.user.auth_routes import router as auth_router
# from common.security.security import JWTAuth
# from starlette.middleware.authentication import AuthenticationMiddleware

app = FastAPI()
# app.include_router(guest_router)
app.include_router(user_router)
# app.include_router(auth_router)

# Сборщик метрик Prometeus
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)


# app.add_middleware(AuthenticationMiddleware, backend=JWTAuth())

origins = ["*"]
methods = ["*"]
headers = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=headers,
)


@app.get('/')
def health_check():
    return JSONResponse(content={"status": "Running!"})
