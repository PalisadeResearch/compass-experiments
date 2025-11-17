FROM python:3.11-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy dependency files
COPY pyproject.toml ./
COPY uv.lock ./
COPY src/ src/

# Install dependencies
RUN uv sync --frozen --no-dev

RUN useradd -m experimentuser

# Set user to experimentuser
USER experimentuser

CMD ["uv", "run", "python", "-m", "what_is_capital_of_france.run"]

