1. Init the package with `uv`
- Go to the working directory
- `pip install uv`
- `uv init --no-workspace --package`

2. Write the weather fetching logic (`src/weather_cli/weather.py`)

3. Add CLI functionality
- Create a `src/weather_cli/cli.py` file

4. Configure `pyproject.toml` file
```
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "weather-cli"
version = "0.1.0"
dependencies = ["requests", "click"]

[project.scripts]
weather = "weather_cli.cli:weather"
```
This registers `weather` as a CLI command.

5. Test the package (tests/ directory)
- Write test cases
- Run all test cases:
`uv venv`
`uv pip install pytest requests click`
`uv run pytest`

6. Run in development mode
- Install package: `uv pip install -e .`
- Run CLI: `weather London` to get the result

7. Build and publish the package
- Install libraries: `uv pip install build twine`
- Build the package: `uv build` or `uv run python -m build` (slower than `uv build`)
- Upload to PyPI: `uv run twine upload dist/*`
