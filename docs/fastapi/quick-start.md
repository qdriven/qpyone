# FastAPI quick start

## 1. FastAPI setup

```shell
poetry add fastapi
```

## 2. First API and OpenAPI Spec

```shell
from fastapi import FastAPI

app = FastAPI()


@app.get("/demo")
def demo():
    return {"message": "Hello World"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
```

Run it , and see the API Working.

## 3. Add Middleware in FastAPI

```shell

```
