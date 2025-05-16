# Simple FastAPI Calculator
Link: https://www.youtube.com/watch?v=lm8Y7FGO7xA

A beginner-friendly FastAPI app that does addition, subtraction, multiplication, and division.

## What It Does
This app provides a web API to:
- Add two numbers (`/add`)
- Subtract two numbers (`/subtract`)
- Multiply two numbers (`/multiply`)
- Divide two numbers (`/divide`)

## Requirements
- Python 3.11
- Docker (optional, to run in a container)
- Git

## ✅ How to Run It Locally

### 1 Clone the Repository
```bash
   git clone https://github.com/UtsavlalShrestha/fastapi-calculator.git
   cd fastapi-calculator
```
### 2 Clone the Repository
```bash
   pipenv install
   pipenv shell
```
### 3 Clone the Repository
   APP_NAME=MyCalculator

### 4 Run the applicaion
```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
```
   
