# 🍕 Pizza API Challenge

## Project Description

This application is a RESTful Pizza API built with Flask, following the MVC (Model–View–Controller) architecture. It manages restaurants, pizzas, and the relationships between them, allowing users to:

- List, create, and delete restaurants.
- List all pizzas.
- Create and list restaurant-pizza relationships, including price validation.
- Cascade delete all related restaurant-pizza records when a restaurant is deleted.

The API is designed for easy integration with frontend clients and supports robust validation and error handling. It includes a database seeding script, migration support, and a Postman collection for testing all endpoints. The project is ideal for learning or demonstrating best practices in Flask API development, database relationships, and clean project structure.

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

---

## Setup Instructions

1. **Install dependencies:**
   ```bash
   pipenv install flask flask_sqlalchemy flask_migrate flask-cors
   pipenv shell
   ```
2. **Database setup:**
   ```bash
   export FLASK_APP=server.app
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```
3. **Seed the database:**
   ```bash
   pipenv run python -m server.seed
   ```

---

## API Routes

### Restaurants
- `GET /restaurants` — List all restaurants
- `GET /restaurants/<id>` — Get a restaurant and its pizzas
- `POST /restaurants` — Create a new restaurant
- `DELETE /restaurants/<id>` — Delete a restaurant (cascades to RestaurantPizzas)

### Pizzas
- `GET /pizzas` — List all pizzas

### RestaurantPizzas
- `GET /restaurant_pizzas` — List all restaurant-pizza relationships
- `POST /restaurant_pizzas` — Create a new RestaurantPizza

---

## Example Requests & Responses

### GET /restaurants
```json
[
  { "id": 1, "name": "Domino's", "address": "123 Pizza St" },
  { "id": 2, "name": "Kiki's Pizza", "address": "456 Cheese Ave" }
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

### POST /restaurants
**Request:**
```json
{ "name": "New Place", "address": "789 New St" }
```
**Response:**
```json
{ "id": 3, "name": "New Place", "address": "789 New St" }
```

### DELETE /restaurants/1
- Success: `204 No Content`
- Not found: `{ "error": "Restaurant not found" }`

### GET /pizzas
```json
[
  { "id": 1, "name": "Pepperoni", "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni" },
  { "id": 2, "name": "Veggie", "ingredients": "Dough, Tomato Sauce, Cheese, Peppers, Olives, Onions" }
]
```

### GET /restaurant_pizzas
```json
[
  {
    "id": 1,
    "price": 10,
    "pizza_id": 1,
    "restaurant_id": 1,
    "pizza": { "id": 1, "name": "Pepperoni", "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni" },
    "restaurant": { "id": 1, "name": "Domino's", "address": "123 Pizza St" }
  },
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
  "id": 3,
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

---

## Validation Rules
- `RestaurantPizza.price` must be between 1 and 30 (inclusive).
- `pizza_id` and `restaurant_id` must reference existing records.
- `name` and `address` are required for creating a restaurant.

---

## Postman Usage
- Import `challenge-1-pizzas.postman_collection.json` into Postman.
- Test all routes as described above.
- Use valid IDs from `/restaurants` and `/pizzas` for POST/DELETE requests.

---

## Submission Checklist
- [x] MVC folder structure
- [x] Models with validations and relationships
- [x] All required routes implemented
- [x] Postman tests passing
- [x] Well-written README.md

---

## Dependencies

This project uses the following main dependencies:

- **flask**: The main web framework for building the API.
- **flask_sqlalchemy**: SQLAlchemy integration for Flask, used for ORM/database models.
- **flask_migrate**: Database migration tool for SQLAlchemy and Flask.
- **flask-cors**: For handling Cross-Origin Resource Sharing (CORS) in Flask APIs.

All dependencies are managed via Pipenv and listed in the `Pipfile`.

---

Joyrose Kinuthia
