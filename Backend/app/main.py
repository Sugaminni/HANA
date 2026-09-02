from fastapi import FastAPI

app = FastAPI() # Creates web application object(Will get requests from website and route them to backend)

@app.get("/") # Route when an HTTP GET request is sent to /
def root():
    return {"message": "HANA Active"}