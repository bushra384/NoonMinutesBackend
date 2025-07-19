from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return JSONResponse({"message": "Backend is running on Vercel!"})

@app.get("/search")
def search(q: str = ""):
    return JSONResponse({"query": q, "results": []})
