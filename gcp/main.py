from google.cloud import storage
import tensorflow as tf
from PIL import Image
import numpy as np
import functools

class_names = ["Early Blight", "Late Blight", "Healthy"]
BUCKET_NAME = "odicris-potate-disease"

# Use client as a global variable to avoid creating multiple clients
storage_client = storage.Client()

@functools.lru_cache(maxsize=1)
def get_model():
    try:
        bucket = storage_client.bucket(BUCKET_NAME)
        blob = bucket.blob("models/1.keras")
        model_path = "/tmp/1.keras"
        blob.download_to_filename(model_path)
        print("Model downloaded successfully")
        
        model = tf.keras.models.load_model(model_path, compile=False)
        print("Model loaded successfully")
        
        # Print model summary
        model.summary()
        
        return model
    except Exception as e:
        print(f"Error loading model: {str(e)}")
        raise

def preprocess_image(image, target_size=(256, 256)):
    img = Image.open(image).convert("RGB").resize(target_size)
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, 0)
    print(f"Preprocessed image shape: {img_array.shape}")
    return img_array

def predict(request):
    try:
        print("Getting the model")
        model = get_model()

        image = request.files["file"]
        print("Processing the received image")
        processed_image = preprocess_image(image)
        print(f"Processed image shape: {processed_image.shape}")

        print("Making the predictions")
        predictions = model.predict(processed_image)
        predicted_class = class_names[np.argmax(predictions[0])]
        confidence = round(100 * np.max(predictions[0]), 2)

        tf.keras.backend.clear_session()
        print("Clearing session and returning the results")

        return {"class": predicted_class, "confidence": confidence}
    except Exception as e:
        print(f"Error in predict function: {str(e)}")
        raise


# gcloud functions deploy predict --runtime python38 --trigger-http --memory 2048 --project long-centaur-428909-c5

# gcloud functions deploy predict --runtime python38 --trigger-http --memory 2048MB --timeout 60s --max-instances 10 --project long-centaur-428909-c5