import uvicorn
from fastapi import FastAPI
from starlette import status
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import RedirectResponse


from controller import application
from text_sort.constant.application import APP_HOST, APP_PORT


app = FastAPI()

@app.get("/")
def read_root():
    #return {"message": "Hi...."}
    return RedirectResponse(url = "/", status_code =status.HTTP_302_FOUND )


app.include_router(application.router)

app.add_middleware(SessionMiddleware, secret_key="!secret")


if __name__ == "__main__":
    uvicorn.run(app, host=APP_HOST, port=APP_PORT)

