from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.src.routers import products, users

app = FastAPI()

# CORS
origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"msg": "API is running!"}


# Products routes
app.include_router(products.router)

# Users routes
app.include_router(users.router)
