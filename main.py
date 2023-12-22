import cv2
import json
import numpy as np
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import StreamingResponse
from ultralytics import YOLO
from io import BytesIO

app = FastAPI()

# Dictionary mapping fruit names to their corresponding YOLO model files
fruit_models = {
    "apple": "Model/Apple-YoloV8L.pt",
    "banana": "Model/Banana-YoloV8N.pt",
    "chili": "Model/Chili-YoloV8N.pt",
    "pokchoy": "Model/Pokcoy-YoloV8L.pt",
    "orange": "Model/Orange-YoloV8N.pt",
}

def load_model(model_path):
    return YOLO(model_path)

def yolo(img, model):
    # Assuming you have a YOLO model loaded
    # Perform inference on the image
    results = model.predict(img)
    # Get the results in JSON format
    result_json = results[0].tojson()
    # Convert the JSON to a Python dictionary
    result_json = json.loads(result_json)
    # Get the annotated image
    annotated_img = img.copy()
    # Create an empty list to store the results
    output_list = []
    # Loop through the results and draw bounding boxes
    for i, item in enumerate(result_json, 1):
        label = item["name"]
        confidence = item["confidence"]
        box = item["box"]
        x1, y1, x2, y2 = box["x1"], box["y1"], box["x2"], box["y2"]
        # Convert the bounding box coordinates to integers
        bbox = {
            "x1": x1,
            "y1": y1,
            "x2": x2,
            "y2": y2
        }
        # Append the results to the output list
        output_list.append({
            "name": label,
            "bounding_box": bbox,
            "confidence": confidence
        })
        # Draw bounding box on the image
        cv2.rectangle(annotated_img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(annotated_img, f"{label} {confidence:.2f}", (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 2)
    # Return the results and annotated image
    return output_list, annotated_img

@app.post("/predict")
async def predict(
    file: UploadFile = File(...),
    model_name: str = Form(...),
):
    # Check if the specified fruit model exists
    if model_name not in fruit_models:
        return {"error": "Invalid model name"}

    # Load the YOLO model dynamically based on the selected fruit model
    model_path = fruit_models[model_name]
    model = load_model(model_path)

    # Load and process the image
    contents = await file.read()
    img = cv2.imdecode(np.frombuffer(contents, np.uint8), cv2.IMREAD_COLOR)
    img = cv2.resize(img, (416, 416))

    # Run YOLO on the image and get annotated image
    yolo_results, annotated_img = yolo(img, model)

    # Convert annotated image to stream
    _, img_stream = cv2.imencode('.jpg', annotated_img)

    # Return the results and annotated image as JSON
    return {"results": yolo_results, "annotated_image": StreamingResponse(BytesIO(img_stream.tobytes()), media_type="image/jpeg")}

# Testing Deployment