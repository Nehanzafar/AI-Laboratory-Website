from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# Add your React frontend URL(s)
origins = [
    "http://localhost:5173",  # Vite default port
    "http://localhost:3000",  # Alternative React port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],  # Allows all headers
)

@app.get("/api/items")
async def get_items():
    return [{"id": 1, "name": "1st Item"},
            {"id": 2, "name": "2nd Item"},
            {"id": 3, "name": "3rd Item"},
            {"id": 4, "name": "4th Item"}
            
            ]