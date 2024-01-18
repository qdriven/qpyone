FROM python:3.11-slim-bullseye

# Set environment variables.
ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Set working directory.
WORKDIR /app

# Copy dependencies.
COPY pyproject.toml /app/

# Install dependencies.
RUN poetry install

# Copy project.
COPY . /app/

EXPOSE 5000

ENTRYPOINT [ "gunicorn", "app.main:app", "--workers", "2", "--worker-class", \
        "uvicorn.workers.UvicornWorker",  "-b", "0.0.0.0:5000" ]
