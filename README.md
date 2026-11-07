venv/
__pycache__/
.ipynb_checkpoints/
.DS_Store

# ignore generated/large data, keep the folder placeholders
data/raw/*
data/interim/*
data/processed/*
!data/raw/.gitkeep
!data/raw/README.md
!data/interim/.gitkeep
!data/processed/.gitkeep

# ignore model binaries
models/*
!models/.gitkeep