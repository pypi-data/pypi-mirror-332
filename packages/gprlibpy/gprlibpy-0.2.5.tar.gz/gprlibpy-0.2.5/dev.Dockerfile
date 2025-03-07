# Base stage with system dependencies
FROM python:3.10-slim AS base

# Copy uv package manager
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Environment variables
ARG SA_KEY_BASE64
ENV REGION=us-central1
ENV PROJECT_ID=gpr-studio
ENV REPOSITORY_ID=gprstudio-py-repo
ENV UV_SYSTEM_PYTHON=1
ARG LIB_DIR=/usr/local

# Install system dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    ffmpeg \
    libsm6 \
    libxext6 \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Builder stage for installing Python dependencies
FROM base AS builder

# Copy provided libraries instead of downloading them
COPY lib/ ${LIB_DIR}/
# Install FFTW-2.1.5
WORKDIR ${LIB_DIR}/fftw-2.1.5
RUN wget -O config.guess 'https://git.savannah.gnu.org/cgit/config.git/plain/config.guess' && \
    wget -O config.sub 'https://git.savannah.gnu.org/cgit/config.git/plain/config.sub' && \
    chmod +x config.guess config.sub && \
    ./configure --with-pic --prefix=${LIB_DIR}/fftw-2.1.5 --enable-i386-hacks --with-gcc=$(which gcc) && \
    make clean && \
    make && \
    make install

# Install CurveLab-2.1.3
WORKDIR ${LIB_DIR}/CurveLab-2.1.3
RUN make clean && make lib && make test
ENV FDCT=/usr/local/CurveLab-2.1.3
ENV FFTW=/usr/local/fftw-2.1.5

# Configure authentication for Google Artifact Registry
RUN echo $SA_KEY_BASE64 | base64 -d > /service-account.json
ENV GOOGLE_APPLICATION_CREDENTIALS=/service-account.json

# Install required authentication dependencies
RUN uv pip install keyring keyrings.google-artifactregistry-auth

# Copy source code
ADD . /app
WORKDIR /app

# Install dependencies using uv (efficient package manager)
RUN --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --no-sources --no-install-project --no-editable \
    --keyring-provider subprocess \
    --extra-index-url https://oauth2accesstoken@${REGION}-python.pkg.dev/${PROJECT_ID}/${REPOSITORY_ID}/simple/ \
    --extra gprstudio-blocks --extra gprstudio-io

# Sync the project
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen

# Remove service account credentials
RUN rm /service-account.json

# Runner stage to minimize final image size
FROM base AS runner

# Set working directory
WORKDIR /app

# Copy virtual environment and dependencies from builder stage
COPY --from=builder --chown=app:app /app/.venv /app/.venv
ENV PATH=/app/.venv/bin:$PATH

RUN pip install gprlibpy --no-cache-dir

# Set entrypoint to use Typer CLI
#ENTRYPOINT ["uv", "run", "gprlibpy"]
