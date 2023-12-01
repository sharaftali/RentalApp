from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import user, auth, item

# models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Rental App")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(item.router)


@app.get("/")
def root():
    return {"message": "Hello World pushing out to ubuntu"}