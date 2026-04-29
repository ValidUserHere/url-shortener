from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi import HTTPException
from pydantic import BaseModel , HttpUrl
import random
import string

app = FastAPI()

db = {} # memo storage

def generate_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k = 6)) #formatting the link using random


@app.get("/")
def home():
    return {"status" : "ok"}

class URLRequest(BaseModel):
    url: HttpUrl                          # URL format shit, nohting else allowed

@app.post("/shorten")
def shorten_url(request : URLRequest):                     #function that runs to shorten, release and store the short url
    code = generate_code()
    db[code] = str(request.url)
    return {"short_code": code, "short_url": f"http://localhost:8000/{code}"}

@app.get("/stats")
def get_stats():
    return {"total_urls_shortened": len(db)}

@app.get("/{code}")
def redirect_url(code: str):                     #redirection fucntion
    if code not in db:
        raise HTTPException(status_code= 404, detail= "Short code not found")
    return RedirectResponse(url = db[code])

