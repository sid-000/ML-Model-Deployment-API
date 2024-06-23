from fastapi import FastAPI
from app.routes import predict  # import your router

app = FastAPI(
    title="ML Model Deployment API",
    description="Predict Iris flower type using a trained ML model.",
    version="1.0"
)

# Root route for welcome message
@app.get("/")
def read_root():
    return {"message": "Welcome to the ML Model Deployment API"}

# Register prediction route
app.include_router(predict.router, prefix="/api")
