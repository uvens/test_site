from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def get_site():
    return """<html><body><h1>Hello World</h1></body></html>"""


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
