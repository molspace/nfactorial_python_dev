# Use an official Python image
FROM python:3.9-slim

# Create a working directory
WORKDIR /app

# 1. Copy poetry configuration first
COPY pyproject.toml poetry.lock /app/

# 2. Install Poetry
RUN pip install --no-cache-dir poetry==2.1.2

# 3. Install project dependencies
# NOTE: We skip dev dependencies to keep the image smaller
RUN poetry install --without dev --no-root

# 4. Copy the rest of the project
COPY . /app

# 5. Install your project as a package (optional)
RUN poetry install --without dev

# 6. Expose port 80 (or 8000 if you prefer)
EXPOSE 80

# 7. auto-run Alembic migrations in the container
# Default command – runs uvicorn via Poetry to start the FastAPI app
CMD ["poetry", "run", "alembic", "upgrade", "head"] \
  && ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
