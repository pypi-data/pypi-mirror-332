# 🎩 metricks

metricks is a tool for creating and managing metrics that can be consumed
via snowpark.

## Installation

```bash
uv sync --all-extras
```

## Tests

```bash
uv run pytest
```

## Example usage

```bash
uv run example_usage/example.py
```

## Streamlit app:

Run locally with:

```bash
cd example_usage
uv run streamlit run example_usage/streamlit_app.py
```

Deploy to SiS with:

```bash
cd example_usage
./deploy-app.sh
```
