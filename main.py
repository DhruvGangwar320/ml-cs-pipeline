from pathlib import Path
import joblib
from fastapi import FastAPI
from pydantic import BaseModel , Field # to validate output
app = FastAPI(title ='Iris Model API')
model_dir = Path("models")
model_path = model_dir / "model.pkl"
model = joblib.load(model_path)

# threre will be four classes in the iris dataset, we will create a class to validate the input data
class IrisRequest(BaseModel):
    sepal_length: float = Field(gt=0)
    sepal_width: float = Field(gt =0)
    petal_length: float = Field(gt=0)
    petal_width: float = Field(gt=0)
    # there will be two methods for API , get and another is post

@app.get("/health")

def health_check():
    return {"status": "healthy"}
# now we have to run a command to test the API, we will use uvicorn to run the API server. The command is uvicorn mlpipeline.main:app --reload

@app.post("/predict")
def predict_iris(input_data: IrisRequest): #IrisRequest is the class we created to validate the input data , all variable should be available
    features = [
        [
            input_data.sepal_length,
            input_data.sepal_width,
            input_data.petal_length,
            input_data.petal_width
        ]
    ]
    prediction = int(model.predict(features)[0])
    return {"prediction": prediction , 'class_name': ['setosa', 'versicolor', 'virginica'][prediction]}

# we cannot run it by browser , to run it we use real time software like Postman , swagger or curl to test the API. We can also use the FastAPI documentation to test the API. The documentation is available at http://

