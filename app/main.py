from fastapi import FastAPI

#create application instance
app = FastAPI()


#define endpoint for GET request
@app.get("/")
def read_root():
  return {"message": "Welcome to the analytics backend."}

read_root()