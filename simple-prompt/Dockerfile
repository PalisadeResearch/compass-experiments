FROM python:3.13-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy dependency files
COPY pyproject.toml ./
COPY uv.lock* ./
COPY src/ src/

# Install dependencies
RUN uv sync --frozen --no-dev

RUN useradd -m experimentuser
RUN chown -R experimentuser:experimentuser /app
USER experimentuser

CMD ["uv", "run", "python", "-m", "simple_prompt.run"]

