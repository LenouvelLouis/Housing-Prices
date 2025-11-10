import pickle
import numpy as np
import gradio as gr
import os

MODEL_PATH = os.getenv("MODEL_PATH", "model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

FEATURES = ["MedInc", "AveRooms", "HouseAge", "AveOccup", "Population"]

def predict(medinc, averooms, houseage, aveoccup, population):
    X = np.array([[medinc, averooms, houseage, aveoccup, population]], dtype=float)
    y = model.predict(X)[0]
    return {
        "MedHouseVal (100k$)": float(y),
        "MedHouseVal ($)": round(float(y) * 100_000, 2),
    }

with gr.Blocks(title="California Housing – RandomForestRegressor") as demo:
    gr.Markdown("## 🏠 California Housing Prediction")

    gr.Markdown(
        "**Enter the five input variables** (UI order doesn’t matter):\n\n"
        "1. `MedInc` — Median income in block group\n"
        "2. `AveRooms` — Average number of rooms per household\n"
        "3. `HouseAge` — Median house age\n"
        "4. `AveOccup` — Average household occupancy\n"
        "5. `Population` — Block group population\n\n"
        "The model returns **MedHouseVal** (median house value):\n"
        "- in **100k$ units** (original dataset scale), and\n"
        "- in **dollars ($)** for convenience.\n\n"
        "_Example: a prediction of `1.85` equals `$185,000`._"
    )

    with gr.Row():
        medinc = gr.Number(label="MedInc (median income)", value=3.5)
        averooms = gr.Number(label="AveRooms", value=5.4)
        houseage = gr.Number(label="HouseAge", value=20)
    with gr.Row():
        aveoccup = gr.Number(label="AveOccup", value=2.7)
        population = gr.Number(label="Population", value=800)

    btn = gr.Button("Predict")
    out = gr.JSON(label="Prediction")

    btn.click(
        fn=predict,
        inputs=[medinc, averooms, houseage, aveoccup, population],
        outputs=out
    )

    gr.Examples(
        examples=[
            [3.5, 5.4, 20, 2.7, 800],
            [2.1, 4.3, 15, 2.2, 1200],
            [6.0, 6.8, 30, 3.0, 600],
        ],
        inputs=[medinc, averooms, houseage, aveoccup, population],
        outputs=out,
        fn=predict,
        label="Examples"
    )

if __name__ == "__main__":
    demo.launch()
