# ------------------------------------------------------------------------------
# Dockerfile — Builds a single, portable dev image for Mac (arm64) and Windows (amd64)
# Key inclusions:
# - Python 3.13 (from official multi-arch image → auto arm64 on M-series, amd64 on Windows)
# - zsh + Oh My Zsh
# - Neovim v0.9+ (from Debian bookworm-backports, which ships ≥0.9)
# - LunarVim (installed via official script)
# - git, make, pip, node, npm, cargo, ripgrep
# Notes:
# - No nano, no tzdata (per your request)
# - PATH is set so `lvim` is available immediately
# ------------------------------------------------------------------------------

ARG PYVER=3.13
FROM python:${PYVER}-slim

# Keep things non-interactive during build
ENV DEBIAN_FRONTEND=noninteractive

# Quality-of-life envs for Python & PATH
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PATH="/root/.local/bin:${PATH}"

# ---- Default working directory -----------------------------------------------
WORKDIR /app

# ---- System dependencies ------------------------------------------------------
# We install:
# - curl & ca-certificates: required for fetching install scripts over HTTPS
# - zsh: default shell we’ll use in the running container
# - git: version control + needed by many tools
# - make: build helper (also used by some tooling)
# - ripgrep: fast search (used by Telescope, LunarVim ecosystem)
# - nodejs, npm: LSP/formatters/treesitter plugins often need Node
# - cargo: Rust package manager (some Neovim plugins build via Rust)
# - build-essential: COMPILER TOOLCHAIN (recommended so pip can build native wheels)
#
# Neovim 0.9+:
# - Use Debian bookworm-backports to get a new-enough Neovim via APT for BOTH arches.
#   This avoids fragile manual tarball downloads and keeps arm64/amd64 happy.
# ------------------------------------------------------------------------------
RUN set -eux; \
    echo "deb http://deb.debian.org/debian bookworm-backports main" > /etc/apt/sources.list.d/backports.list; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
      ca-certificates curl \
      zsh git make ripgrep \
      nodejs npm cargo \
      build-essential \
    ; \
    apt-get install -y -t bookworm-backports --no-install-recommends neovim; \
    rm -rf /var/lib/apt/lists/*

# ---- Python dependencies ------------------------------------------------------
# Copy requirements first for better layer caching.
COPY requirements.txt /tmp/requirements.txt
RUN python -m pip install --upgrade pip && pip install -r /tmp/requirements.txt

# ---- Oh My Zsh ---------------------------------------------------------------
# Install Oh My Zsh without changing the default shell or launching zsh during build.
# We keep the generated .zshrc and later append our aliases.
RUN set -eux; \
    export CHSH=no RUNZSH=no KEEP_ZSHRC=yes; \
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"; \
    # Nice default plugins (safe, minimal)
    sed -i 's/^plugins=(git)$/plugins=(git)/' /root/.zshrc

# ---- LunarVim ----------------------------------------------------------------
# https://www.lunarvim.org/docs/installation
# Install LunarVim against Neovim 0.9 using the branch specified.
# The installer will place `lvim` under ~/.local/bin; we ensure PATH already includes it.
RUN set -eux; \
    LV_BRANCH='release-1.4/neovim-0.9' bash -lc \
      "curl -fsSL https://raw.githubusercontent.com/LunarVim/LunarVim/release-1.4/neovim-0.9/utils/installer/install.sh | bash"; \
    # Ensure lvim is callable from any shell (belt & suspenders):
    echo '' >> /root/.zshrc; \
    echo '# Make sure LunarVim is available as lvim' >> /root/.zshrc; \
    echo 'alias lvim="${HOME}/.local/bin/lvim"' >> /root/.zshrc; \
    echo '' >> /root/.bashrc; \
    echo 'alias lvim="${HOME}/.local/bin/lvim"' >> /root/.bashrc; \
    # Also drop a symlink into /usr/local/bin so scripts can call `lvim` without a shell RC
    ln -s /root/.local/bin/lvim /usr/local/bin/lvim || true

# The image itself doesn’t force a command; compose.yml will start a shell.
# That way you can choose bash/zsh per your preference at runtime.
