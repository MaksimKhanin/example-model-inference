import requests
import json

# URL модельного сервиса на FastAPI
url = 'http://localhost:8000/predict/'

# Параметры для предсказания
vector = [{"reqId": 111,
          "Pclass": 3,
          "Sex": 1,
          "Age": 33.0,
          "SibSp": 0,
          "Parch": 0,
          "Fare": 7.8958,
          "Embarked": 0},

         {"reqId": 222,
          "Pclass": 1,
          "Sex": 0,
          "Age": 15.0,
          "SibSp": 2,
          "Parch": 2,
          "Fare": 30.8958,
          "Embarked": 2}]



# Отправка запроса на предсказание
print(vector)

response = requests.get(url, json={'vectors': vector})
print(response.json())

# Получение предсказания из ответа
#prediction = response.json()['prediction']

#print(f"Предсказание модели: {prediction}")