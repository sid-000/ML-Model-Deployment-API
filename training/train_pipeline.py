import logging
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from training.config import MODEL_PATH, PREPROCESSOR_PATH, TEST_SIZE, RANDOM_STATE
from training.utils import save_object, setup_logging

def train_and_save():
    setup_logging()
    logging.info("Loading Iris dataset")
    iris = load_iris()
    X, y = iris.data, iris.target

    logging.info("Splitting dataset")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE)

    logging.info("Creating preprocessing pipeline")
    preprocessor = StandardScaler()

    logging.info("Creating classifier pipeline")
    model = Pipeline([
        ("scaler", preprocessor),
        ("classifier", RandomForestClassifier(n_estimators=100, random_state=RANDOM_STATE))
    ])

    logging.info("Training model")
    model.fit(X_train, y_train)

    logging.info("Saving model to %s", MODEL_PATH)
    save_object(model, MODEL_PATH)

    logging.info("Training complete")

if __name__ == "__main__":
    train_and_save()
