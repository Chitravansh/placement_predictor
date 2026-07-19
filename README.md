# Placement Predictor

A full-stack machine learning web application that predicts whether a student will get placed based on their **CGPA** and **IQ** score.

## Project Structure

```
Placement_predictor/
├── main.py                  # FastAPI backend server
├── model.pkl                # Trained ML model (pickle)
├── scaler.pkl               # StandardScaler (pickle)
├── placement(1).ipynb       # Model training notebook (Google Colab)
├── LICENSE                  # MIT License
├── code.txt                 # Earlier version of main.py (no scaler)
├── requirements.txt         # Python dependencies
└── templates/
    ├── index.html           # Frontend UI
    ├── script.js            # API call logic
    └── style.css            # Styling
```

## How It Works

1. A classifier is trained on a dataset of 100 student records containing **CGPA**, **IQ**, and **placement status**.
2. The trained model and scaler are serialized as `model.pkl` and `scaler.pkl`.
3. A **FastAPI** server loads these artifacts and exposes a `POST /predict` endpoint.
4. A vanilla HTML/CSS/JS frontend sends user input to the API and displays the result.

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the backend

```bash
uvicorn main:app --reload
```

### 3. Open the frontend

Navigate to `http://127.0.0.1:8000` in your browser.

## API

### `POST /predict`

**Request:**

```json
{
  "cgpa": 7.4,
  "iq": 132.0
}
```

**Response:**

```json
{
  "placement": 1
}
```

- `placement = 1` → Student is likely to get placed
- `placement = 0` → Placement chances are low

### `GET /`

Serves the frontend page.

### `GET /api`

Returns a basic health check response.

## Deployment on Render

1. Push your repo to GitHub
2. Go to [render.com](https://render.com) → **New Web Service**
3. Connect your GitHub repo
4. Configure:

| Setting | Value |
|---------|-------|
| Language | Python 3 |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `uvicorn main:app --host 0.0.0.0 --port $PORT` |

5. Click **Deploy**

Once live, your app will be available at:

- `https://your-app.onrender.com/docs` — Swagger UI
- `https://your-app.onrender.com/home` — Frontend
- `https://your-app.onrender.com/predict` — API endpoint

**Note:** Free tier apps sleep after 15 minutes of inactivity. First request after idle takes 30-60s to cold start.

## Tech Stack

- **Backend:** FastAPI, Uvicorn
- **ML:** scikit-learn, NumPy, pandas
- **Serialization:** pickle
- **Frontend:** HTML, CSS, JavaScript

## Retraining the Model

Open `placement(1).ipynb` in Google Colab (or Jupyter), run all cells. The notebook:

- Loads `placement.csv`
- Performs EDA (scatter plot of CGPA vs IQ)
- Splits data (90% train / 10% test)
- Trains a classifier
- Exports `model.pkl` and `scaler.pkl`

Place the updated pickles in the project root before restarting the server.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
