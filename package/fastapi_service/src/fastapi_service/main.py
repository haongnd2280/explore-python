import uvicorn
from fastapi import FastAPI

from fastapi_service.api.routes import router


app = FastAPI(title="My FastAPI Service")

# Include all the defined API endpoints
app.include_router(router)


def start():
    """Entrypoint for running the API.
    This is for registering `start` function as a CLI command in `pyproject.toml` file.
    """

    # Run the FastAPI instance (`app``) in the `main.py` function of `fastapi_service` package
    uvicorn.run("fastapi_service.main:app", host="127.0.0.1", port=8000, reload=True)



