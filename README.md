# 🍕 Pizza API Challenge

## Project Structure (MVC)

```
server/
  app.py                # App setup
  config.py             # DB config
  models/               # SQLAlchemy models
    __init__.py
    restaurant.py
    pizza.py
    restaurant_pizza.py
  controllers/          # Route handlers
    __init__.py
    restaurant_controller.py
    pizza_controller.py
    restaurant_pizza_controller.py
  seed.py               # Seed data
migrations/             # DB migrations
challenge-1-pizzas.postman_collection.json
README.md
```

## Setup Instructions

1. **Install dependencies:**
   ```bash
   pipenv install flask flask_sqlalchemy flask_migrate flask-cors
   pipenv shell
   ```
2. **Database setup:**
   ```bash
   export FLASK_APP=server/app.py
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```
3. **Seed the database:**
   ```bash
   python server/seed.py
   ```

## API Routes

### Restaurants
- `GET /restaurants` — List all restaurants
- `GET /restaurants/<id>` — Get a restaurant and its pizzas
- `DELETE /restaurants/<id>` — Delete a restaurant (cascades to RestaurantPizzas)

### Pizzas
- `GET /pizzas` — List all pizzas

### RestaurantPizzas
- `POST /restaurant_pizzas` — Create a new RestaurantPizza

## Example Requests & Responses

### GET /restaurants
```json
[
  { "id": 1, "name": "Domino's", "address": "123 Pizza St" },
  ...
]
```

### GET /restaurants/1
```json
{
  "id": 1,
  "name": "Domino's",
  "address": "123 Pizza St",
  "pizzas": [
    { "id": 1, "name": "Pepperoni", "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni" }
  ]
}
```

### DELETE /restaurants/1
- Success: `204 No Content`
- Not found: `{ "error": "Restaurant not found" }`

### GET /pizzas
```json
[
  { "id": 1, "name": "Pepperoni", "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni" },
  ...
]
```

### POST /restaurant_pizzas
**Request:**
```json
{ "price": 10, "pizza_id": 1, "restaurant_id": 1 }
```
**Success Response:**
```json
{
  "id": 4,
  "price": 10,
  "pizza_id": 1,
  "restaurant_id": 1,
  "pizza": { "id": 1, "name": "Pepperoni", "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni" },
  "restaurant": { "id": 1, "name": "Domino's", "address": "123 Pizza St" }
}
```
**Error Response:**
```json
{ "errors": ["Price must be between 1 and 30"] }
```

## Validation Rules
- `RestaurantPizza.price` must be between 1 and 30 (inclusive).
- `pizza_id` and `restaurant_id` must reference existing records.

## Postman Usage
- Import `challenge-1-pizzas.postman_collection.json` into Postman.
- Test all routes as described above.

---

Happy coding! 🍕
