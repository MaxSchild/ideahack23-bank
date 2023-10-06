from fastapi import FastAPI
from random import uniform

app = FastAPI()

@app.post("/{n}")
async def place_bid(amount: int, use_case: str, loan_time: int):
    return { 'interest_rate' : uniform(2.5, 10.) }
