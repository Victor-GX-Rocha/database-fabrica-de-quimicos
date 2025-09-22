from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="src/static"), name="static")
templates = Jinja2Templates(directory="src/templates")

# Simulação: categorias do banco
CATEGORIAS = [
    {"id": 1, "nome": "Limpeza"},
    {"id": 2, "nome": "Químico"},
    {"id": 3, "nome": "Higiênico"},
    {"id": 4, "nome": "Sanitizante"},
    {"id": 5, "nome": "Cloreto de só ódio"}
]

from typing import Any
UNIDADES_MEDIDA: list[dict[str, Any]] = [
    {"id":1, "nome": "Litro (L)"},
    {"id":2, "nome": "Mililitro (ml)"},
    {"id":3, "nome": "Quilograma (kg)"},
    {"id":4, "nome": "Grama (g)"},
    {"id":5, "nome": "Unidade"}
]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "categorias": CATEGORIAS,  # enviando para o template
            "unidades": UNIDADES_MEDIDA
        }
    )

@app.post("/cadastrar-produto")
async def cadastrar_produto(
    product_name: str = Form(...),
    product_category: str = Form(...),
    product_quantity: int = Form(...),
    product_unit: str = Form(...),
    product_description: str = Form(None)
):
    print(f"""Produto cadastrado: 
        {product_name = }, 
        {product_category = }, 
        {product_quantity = }
        {product_unit = } 
        {product_description = }
    """)
    return RedirectResponse(url="/", status_code=303)
