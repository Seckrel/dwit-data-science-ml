from typing import Union
from tensorflow.keras.models import load_model
from PIL import Image
import io
import numpy as np

from fastapi import FastAPI, File, UploadFile, HTTPException

app = FastAPI()

model = load_model("nn/models/ocr-cnn-prod.keras")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        image = Image.open(io.BytesIO(await file.read()))
        image = image.resize((8, 8))
        image = image.convert('L')  # Convert to grayscale
        
        # Convert to numpy array and normalize
        image_array = np.array(image) / 255.0
        
        # Reshape to match model's input shape: (batch_size, height, width, channels)
        image_array = image_array.reshape(1, 8, 8, 1)
        
        predictions = model.predict(image_array)
        predicted_class = np.argmax(predictions, axis=1)
        
        return {
            "predicted_class": int(predicted_class),
            "confidence": float(predictions[0][predicted_class]),
            "predictions": predictions[0].tolist()
        }

    except Exception as e:
        # Handle errors gracefully
        raise HTTPException(status_code=400, detail=f"Error processing image: {str(e)}")