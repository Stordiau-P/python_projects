import requests
import json


url = "https://pizzamamadjangopierre.herokuapp.com/api/GetPizzas"

data = requests.get(url)

pizzas = json.loads(data.text)

print('Liste des pizzas:')

for pizzaModel in pizzas :
    pizza = pizzaModel['fields']
    print(pizza['nom'])