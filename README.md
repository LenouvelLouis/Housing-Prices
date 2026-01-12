---
title: California Housing - Gradio App
emoji: 🏠
colorFrom: blue
colorTo: green
sdk: gradio
app_file: app.py
pinned: false
---

# California Housing Price Prediction

A machine learning web application that predicts California median house values using a pre-trained Random Forest model. Built with Gradio for an interactive UI and automatic REST API generation.

**[Live Demo](https://huggingface.co/spaces/LenouvelLouisDev/California-Housing-API)**

## Features

- Interactive web interface for real-time predictions
- Auto-generated REST API endpoint via Gradio
- Pre-trained RandomForestRegressor optimized with GridSearchCV
- Minimal dependencies, CPU-only inference
- Automated deployment to Hugging Face Spaces via GitHub Actions

## Project Structure

```
Housing-Prices/
├── app.py                 # Gradio web application
├── model.pkl              # Trained RandomForestRegressor model
├── House.ipynb            # Model training and analysis notebook
├── california_housing.csv # California Housing dataset
├── requirements.txt       # Python dependencies
└── .github/workflows/
    └── deploy-to-hf-space.yml  # CI/CD pipeline
```

## Installation

```bash
git clone https://github.com/LenouvelLouis/Housing-Prices.git
cd Housing-Prices
pip install -r requirements.txt
```

## Usage

### Web Interface

```bash
python app.py
```

Navigate to the local URL displayed in the terminal to access the prediction form.

### REST API

The Gradio app automatically exposes a REST API endpoint.

**Endpoint:** `POST /api/predict`

**Example Request:**

```bash
curl -X POST "https://lenouvellouisdev-california-housing-api.hf.space/api/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "data": [3.5, 5.4, 20, 2.7, 800]
  }'
```

**Response:**

```json
{
  "data": ["Predicted MedHouseVal: 1.85 (in 100k$) → $185,000"]
}
```

## Input Features

| Feature      | Description                           | Example |
|--------------|---------------------------------------|---------|
| `MedInc`     | Median income in block group          | 3.5     |
| `AveRooms`   | Average rooms per household           | 5.4     |
| `HouseAge`   | Median house age (years)              | 20      |
| `AveOccup`   | Average household occupancy           | 2.7     |
| `Population` | Block group population                | 800     |

## Model Performance

The model was trained on the California Housing dataset (20,640 samples) with hyperparameter tuning via GridSearchCV.

| Model                      | R² Score | MSE    |
|----------------------------|----------|--------|
| Linear Regression          | 0.581    | 0.549  |
| Random Forest (Base)       | 0.809    | 0.250  |
| Gradient Boosting          | 0.749    | 0.329  |
| **Random Forest (Tuned)**  | **0.764**| **0.310** |

**Optimal Hyperparameters:**
- `n_estimators`: 300
- `max_depth`: 10
- `min_samples_leaf`: 2
- `min_samples_split`: 2

## Tech Stack

- **[Gradio](https://gradio.app/)** - Web UI and API framework
- **[scikit-learn](https://scikit-learn.org/)** - Machine learning library
- **[NumPy](https://numpy.org/)** - Numerical computing
- **[Hugging Face Spaces](https://huggingface.co/spaces)** - Deployment platform

## Deployment

The project uses GitHub Actions for continuous deployment to Hugging Face Spaces. On every push to `main`, the workflow:

1. Syncs application files to the Hugging Face Space
2. Handles large model files via Git LFS
3. Automatically rebuilds the Space

To deploy your own instance:

1. Create a Hugging Face Space with Gradio SDK
2. Add `HF_TOKEN` to your GitHub repository secrets
3. Update `HF_USERNAME` and `HF_SPACE_NAME` in the workflow file

## License

This project is open source and available under the [MIT License](LICENSE).
