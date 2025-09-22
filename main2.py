from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Agora os caminhos são relativos à pasta src/
app.mount("/static", StaticFiles(directory="src/static"), name="static")
templates = Jinja2Templates(directory="src/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/cadastrar-produto")
async def cadastrar_produto(
    product_name: str = Form(...),
    product_category: str = Form(...),
    product_quantity: int = Form(...),
    product_unit: str = Form(...),
    product_description: str = Form(None)
):
    print(f"Produto cadastrado: {product_name}, {product_category}, {product_quantity}{product_unit}")
    return RedirectResponse(url="/", status_code=303)
