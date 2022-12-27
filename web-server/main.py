from fastapi.responses import HTMLResponse
import store
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def get_list():
    return [1, 2, 3]


@app.get('/hola', response_class=HTMLResponse)
def get_list():
    return """
    <h1>This is a page from python</h1>
    """


def run():
    store.get_categories()


if __name__ == '__main__':
    run()

# fastapi: https://fastapi.tiangolo.com
# uvicorn: https://www.uvicorn.org
