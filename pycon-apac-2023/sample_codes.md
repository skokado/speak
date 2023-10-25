# 実装

## ORM

```python
from myapp.models import User, Book

# 1.
user = User.objects.get(username="user123@example.com")

# 2.
books = Book.objects.filter(
    author=user,
    pages__gt=100,
).order_by("published_at")
```

```sql
-- 1.
SELECT * FROM users
WHERE username = 'user123@example.com';

-- 2.
SELECT *
FROM books
WHERE
  author_id = 1
  AND pages > 100
ORDER BY published_at;
```

```sql
-- 1.
SELECT *
FROM users
WHERE email = 'user123@example.com'
;

-- 2.
SELECT *
FROM users
WHERE email = '' OR 1 = 1
;
```

## エラーハンドリング

### 例1

- Bad

```python
try:
  # ファイルが存在しない可能性のある処理
  file = open("customers.csv")

except FileNotFoundError as e:
  pass  # <===

# ファイルが存在しないのに処理が続く
...
```

- Better

```python
try:
  # ファイルが存在しない可能性のある処理
  file = open("customers.csv")

except FileNotFoundError as e:
  logger.warning("...")
  raise XXXException from e


# --- エラー発生時は処理がここまで来ない
```

### 例2

- Bad

```python
from django.http import JsonResponse


def user_view(request, user_id: int):
  try:
    user = User.objects.get(user_id=user_id)

  except UserDoesNotException:
    response =  JsonResponse(
      {"status": 404, "message": "User not found"}
    )
    print(response.status_code)
    # => 200
    return response

...
```

- Better

```python
from http import HttpStatus
from django.http import JsonResponse

def user_view(request, user_id: int):
  try:
    user = User.objects.get(user_id=user_id)

  except UserDoesNotException:
    response =  JsonResponse(
      {"status": 404, "message": "User not found"},
      status=HTTPStatus.NOT_FOUND,
    )
    print(response.status_code)
    # => 404
    return response

...
```

## Advanced

```python
# myapp/views.py
from http import Http404


def user_view(request, user_id: int):
  try:
    user = User.objects.get(user_id=user_id)

  except UserDoesNotException:
    raise Http404("User not found")


# myapp/urls.py
from http import HTTPStatus
from django.http import JsonResponse
from myapp.views import my_handler404


def my_handler404(request, exception=None):
  logger.warning(...)
  return JsonResponse(
    status=HTTPStatus.NOT_FOUND,
    {
      "message": "xxx not found.",
    }
  )


handler404 = my_handler404
```

## logging

```python
import logging

logger = logging.getLogger(__name__)


def foo():
  logger.info("...")
  logger.warning("...")
```
