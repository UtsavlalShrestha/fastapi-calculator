from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

app = FastAPI(title="Simple Calculator")

APP_NAME = os.getenv("APP_NAME", "Calculator App")

class Calculation(BaseModel):
    a: float
    b: float

@app.post("/add")
def add(calc: Calculation):
    result = calc.a + calc.b
    print(f"Adding {calc.a} + {calc.b} = {result}")
    return {"result": result}

@app.post("/subtract")
def subtract(calc: Calculation):
    result = calc.a - calc.b
    print(f"Subtracting {calc.a} - {calc.b} = {result}")
    return {"result": result}

@app.post("/multiply")
def multiply(calc: Calculation):
    result = calc.a * calc.b
    print(f"Multiplying {calc.a} * {calc.b} = {result}")
    return {"result": result}

@app.post("/divide")
def divide(calc: Calculation):
    if calc.b == 0:
        print("Error: Division by zero!")
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    result = calc.a / calc.b
    print(f"Dividing {calc.a} / {calc.b} = {result}")
    return {"result": result}