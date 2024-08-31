import json
import uuid

def save_Json(data, filename):
    try:
        with open(filename, 'w', encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Erro ao salvar o arquivo: {e}")


def read_Json(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def investment(name: str, price: float, quantity: int, date: str):
    investment_list = read_Json('investment.json')
    initial_length = len(investment_list)

    investment_id = str(uuid.uuid4())
    total = price * quantity

    new_investment = {
        "id": investment_id,
        "name": name,
        "price": price,
        "quantity": quantity,
        "date": date,
        "total": total,
    }

    investment_list.append(new_investment)
    read_Json(investment_list, 'investment.json')

    if len(investment_list) > initial_length:
        return {
            "status": 201,
            "message": "Investimento criado com sucesso!"
        }
    else:
        return {
            "status": 400,
            "message": "Erro ao criar investimento!"
        }
    
