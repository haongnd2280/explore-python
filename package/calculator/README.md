1. Init a package
- Go to the working directory
- `pip install uv`
- `uv init --no-workspace --package`

2. Write the package code (src/ directory)

3. Test the package (tests/ directory)
- Write test cases
- Run all test cases:
`uv venv`
`uv pip install pytest`
`uv run pytest`

4. Build a small app using the package
- Create a `main.py` file in the root (working directory)
- Run: `uv run main.py`

5. Build and publish the package
`uv pip install build twine`
- Build the package: `uv build` or `uv run python -m build` (slower than `uv build`)
- Upload to PyPI: `uv run twine upload dist/*`
