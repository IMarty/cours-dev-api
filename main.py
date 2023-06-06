from fastapi import FastAPI
app = FastAPI() #variable names for the server

@app.get("/")
async def root():
    return {"message":"coucou"}