from fastapi import FastAPI

from Backend.app.h9n.schemas.repe_deal import REPEDealProfile


# Creates the main FastAPI application for HANA
app = FastAPI()


# Basic endpoint used to verify that the backend is running
@app.get("/")
def root():
    return {"message": "HANA Active"}


# Test endpoint for validating REPE deal data
@app.post("/api/h9n/repe/test")
def test_repe_deal(deal: REPEDealProfile):
    return deal