import pandas as pd

def load_face_gest(model_type: str):
    print(f"Loading dataset for {model_type}...")
    if model_type == "Deep-Features-Mediapipe":
        url = "https://raw.githubusercontent.com/yaseen21khan/FaceGest_Repo/main/FaceGest_mediapipe.csv"
    elif model_type == "Deep-Features-Inception":
        url = "https://raw.githubusercontent.com/yaseen21khan/FaceGest_Repo/main/FaceGest_inception.csv"
    else:
        print("Invalid model type.")
        return None

    try:
        print(f"Trying to load from {url}")
        df = pd.read_csv(url)
        print("Data loaded successfully")
        return df
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None
