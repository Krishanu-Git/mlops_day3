from pathlib import Path

# Prepare models directory
models_dir = Path("models")
models_dir.mkdir(exist_ok=True)

# Clean up created models
for model_path in models_dir.iterdir():
    model_path.unlink()