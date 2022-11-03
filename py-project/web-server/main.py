import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3,4,5,65,234423,423432,432,32,4,234234,234,234,324324,234,324,2]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
        <h1>Hola<\h1>
        <p>parrafo<\p>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()