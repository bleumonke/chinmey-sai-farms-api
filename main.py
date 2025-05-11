from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core import lifespan, __routes__

app = FastAPI(
    title="Chimney Farms API",
    description="API backend for managing customer records.",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://main.d2ut8kjo40hhn.amplifyapp.com", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for route in __routes__:
    app.include_router(route)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Chimney Farms API is running 🚜"}

@app.get("/health", tags=["health"])
def health():
    return {"status": "healthy"}
