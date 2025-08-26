# Grokking Dev Environment (Dockerized)

## Why this exists
- Identical Python 3.13 + Neovim/LunarVim environment on Mac (arm64) **and** Windows (amd64).
- No system pollution: all tooling is inside the container.

---

# Common actions

```bash
# Enter the dev shell (zsh + Oh My Zsh)
docker compose run --rm app zsh

# Run LunarVim directly
docker compose run --rm app lvim

# Run tests
docker compose run --rm app pytest -v

# Check arch (arm64 on M-series, x86_64 on Windows)
docker compose run --rm app python -c "import platform; print(platform.machine())
```

---

# Common docker commands

```bash
# Show current containers
docker ps -a

# Run a single command (no shell)
docker compose run --rm app python -V
docker compose run --rm app lvim README.md

# Rebuild after changing Dockerfile/requirements.txt
docker compose build --no-cache
```
