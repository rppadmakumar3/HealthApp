from fastapi import FastAPI, Form
import subprocess

app = FastAPI()

@app.post("/train")
async def train_model(
    dataaug: int = Form(0),
    hyperparams: int = Form(0),
    intel: int = Form(0),
):
    try:
        # Build the training command based on user input
        command = ["python3", "training.py", "-d", "data"]
        if dataaug:
            command.extend(["-a", "1"])
        if hyperparams:
            command.extend(["-hy", "1"])
        if intel:
            command.extend(["-i", "1"])

        # Execute the training command and capture the output
        result = subprocess.run(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        # Return the output as a response
        return {
            "message": "Training process initiated successfully.",
            "stdout": result.stdout,
            "stderr": result.stderr,
        }
    except Exception as e:
        return {"error": str(e)}
