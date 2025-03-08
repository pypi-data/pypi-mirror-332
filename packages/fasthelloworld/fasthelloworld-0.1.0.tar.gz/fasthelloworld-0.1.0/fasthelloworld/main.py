from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def hello_from_dahuzi():
    return {"message": "Hi Hope you are well"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
