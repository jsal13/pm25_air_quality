set shell := ["zsh", "-cu"]

default:
  just --list

venv: 
  pip install --upgrade uv
  uv venv \
    && source .venv/bin/activate \
    && uv pip install -r requirements.txt \
    && uv pip install -r requirements-dev.txt

test:
  python -m pytest --doctest-modules ./tests

emulator:
  docker run -it --rm -p 2222:2222 -v $PWD/dist:/dist ptrsr/pi-ci start

ssh:
   ssh root@localhost -p 2222