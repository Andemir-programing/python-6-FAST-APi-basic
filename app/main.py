import uvicorn
from fastapi import FastAPI

from api.employee.views import router_employee
from api.product.views import router_product
from api.users.views import router_user

app = FastAPI()
app.include_router(router_product)
app.include_router(router_user)
app.include_router(router_employee)


@app.get("/")
def root():
    return {"message": "Hello FAST_API"}


#uvicorn.run(app, host="0.0.0.0", port=80)