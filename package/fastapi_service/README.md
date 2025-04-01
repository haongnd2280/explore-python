1. Init the package
- `mkdir fastapi_service`
- `cd fastapi_service`
- `uv init --no-workspace --package`

2. Write the application
- Create a FastAPI instance (`src/fastapi_service/main.py`)
- Add API routes (`src/fastapi_service/api/routes.py`)

3. Configure `pyproject.toml`
```
[project]
name = "fastapi-service"
version = "0.1.0"
description = "My first FastAPI service package"
readme = "README.md"
authors = [
    { name = "haongnd2280", email = "hao.ngnd2285@gmail.com" }
]
requires-python = ">=3.10"
dependencies = [
    "fastapi",
    "uvicorn"
]

[project.scripts]
fastapi-service = "fastapi_service.main:start"      # Register `fastapi-service` as a CLI command

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

4. Test the package
- Write test cases (`tests/test_routes.py`)
- Install dependencies: `uv pip install fastapi uvicorn pytest`
- Run test: `uv run pytest`

5. Build the package
- `uv build`

6. Publish the package
- `uv publish dist/*`

7. Install & use the service
- Install the package: `pip install fastapi_service` (or `pip install -e .` to install package in development mode)
- Run CLI: `fastapi-service` to start the service
- Test API: `curl http://127.0.0.1:8000/`
