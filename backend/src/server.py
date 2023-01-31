from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return {"msg": "API is running!"}


@app.get("/products")
def get_all_products():
    return {"msg": "Listagem de produtos."}
