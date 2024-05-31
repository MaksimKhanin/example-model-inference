import pandas as pd
from fastapi import FastAPI
import uvicorn
import pickle

app = FastAPI()


@app.get("/predict/")
async def predict(data: dict):
    data = data['vectors']
    input_vector = pd.DataFrame(data)
    index = input_vector["reqId"].values
    input_vector = input_vector.drop(columns="reqId")
    prediction = model.predict(input_vector)
    response_data = []
    for i in range(0, len(prediction)):
        response_data.append({"reqId": index[i].item(),
                              "prediction": prediction[i].item()})
    return {"prediction": response_data}

if __name__ == "__main__":
    # Загрузка модели
    with open('Model.pkl', 'rb') as f:
        model = pickle.load(f)

    uvicorn.run(app, host="0.0.0.0", port=8000)