---
title: California Housing – Gradio App
emoji: 🏠
colorFrom: blue
colorTo: green
sdk: gradio
app_file: app.py
pinned: false
---

# California Housing Prediction (Gradio)

A simple web app and API that serves a pre-trained **RandomForestRegressor** (scikit-learn) to predict the median house value (`MedHouseVal`) on the **California Housing** dataset from scikit-learn.

- ✅ Zero-setup UI via **Gradio**
- ✅ Auto-generated **HTTP API** (see examples below)
- ✅ Minimal dependencies, CPU-only
- ✅ Model serialized as `model.pkl` (scikit-learn **1.6.1**)

---

## ✨ What this Space does

Given **five input features**:

| Feature      | Description                                   |
|--------------|-----------------------------------------------|
| `MedInc`     | Median income in block group                  |
| `AveRooms`   | Average number of rooms per household         |
| `HouseAge`   | Median house age                              |
| `AveOccup`   | Average household occupancy                    |
| `Population` | Population of the block group                 |

The app returns a prediction of `MedHouseVal` in:
- `100k$` units (dataset original unit)
- Absolute dollars (`$`), for convenience

---

## 🚀 Try it

- **Web UI:** open the Space and use the form to predict  
- **Swagger/Docs:** not applicable (Gradio app), but an API endpoint is provided by Gradio (see below)

---

## 🧪 API (via Gradio)

Gradio automatically exposes a REST API for the app.  
You can access it directly from your Space or programmatically.

From your Space page, click the **🪲 Inspect** icon → **Use via API** to see the live endpoint path and input schema.

Here’s an example `curl` request using your deployed Space:

```bash
curl -X POST "https://lenouvellouisdev-california-housing-api.hf.space/api/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "data": [3.5, 5.4, 20, 2.7, 800]
  }'
