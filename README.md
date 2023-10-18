# quiz-api

this is a simple quiz api.

## Database Design

![Database Design](db-design.png)

## Project Structure

```
.
├── manage.py
├── core
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── quiz
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
|   └── migrations
```

## API Endpoints

### Quiz

- `GET /api/quiz/` - List all quiz
- `POST /api/quiz/` - Create a new quiz
- `GET /api/quiz/<int:pk>/` - Retrieve a quiz
- `PUT /api/quiz/<int:pk>/` - Update a quiz
- `DELETE /api/quiz/<int:pk>/` - Delete a quiz

### Question

- `GET /api/quiz/<int:quiz_id>/question/` - List all question
- `POST /api/quiz/<int:quiz_id>/question/` - Create a new question
- `GET /api/quiz/<int:quiz_id>/question/<int:pk>/` - Retrieve a question
- `PUT /api/quiz/<int:quiz_id>/question/<int:pk>/` - Update a question
- `DELETE /api/quiz/<int:quiz_id>/question/<int:pk>/` - Delete a question

### Option

- `GET /api/quiz/<int:quiz_id>/question/<int:question_id>/option/` - List all option
- `POST /api/quiz/<int:quiz_id>/question/<int:question_id>/option/` - Create a new option
- `GET /api/quiz/<int:quiz_id>/question/<int:question_id>/option/<int:pk>/` - Retrieve a option
- `PUT /api/quiz/<int:quiz_id>/question/<int:question_id>/option/<int:pk>/` - Update a option
- `DELETE /api/quiz/<int:quiz_id>/question/<int:question_id>/option/<int:pk>/` - Delete a option

## Take

- `POST /api/quiz/<int:quiz_id>/take/` - Take a quiz

## Answer

- `POST /api/quiz/take/<int:take_id>/answer/` - Answer a question
