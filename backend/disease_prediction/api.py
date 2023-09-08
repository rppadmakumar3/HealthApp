from fastapi import FastAPI
from fastapi import HTTPException
import subprocess
from pathlib import Path  # Import Path from pathlib

app = FastAPI()

# Create directories if they don't exist
Path("../logs/stock").mkdir(parents=True, exist_ok=True)
Path("../saved_models/stock").mkdir(parents=True, exist_ok=True)
Path("../data/disease-prediction").mkdir(parents=True, exist_ok=True)

@app.post("/train")
async def train_model(epochs: int):
    try:
        # Construct the training command
        training_command = [
            "python3",
            "run_training.py",
            "--logfile",
            "../logs/stock.log",
            "--save_model_dir",
            "../saved_models/stock",
            "--data_dir",
            "../data/disease-prediction",
            "--epochs",
            str(epochs)  # Pass the selected epochs as an argument
        ]

        # Run the training script using subprocess
        process = subprocess.Popen(training_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            return {"message": "Model training completed successfully."}
        else:
            error_message = stderr.decode() if stderr else "Unknown error"
            return {"error": error_message}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
