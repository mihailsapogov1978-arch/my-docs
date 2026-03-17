## Шаг 1. Краткое описание
DELETE /api/v1/watchlist/:symbol - удаляем (метод DELETE) параметр :symbol в /api/v1/watchlist/ из watchlist

## шаг 2. Таблица с метаданными

| Поле | Значение |
|------|----------|
| **Метод** | `DELETE` |
| **Путь** | `/api/v1/swatchlist/:symbol` |
| **Обработчик** | `handlers.DeletWatchList` |
| **Авторизация** | ❌ Не требуется (публичный маршрут) |
| **Параметры в пути** | `:symbol` |

## Шаг 3. Что делает этот ресурс?
Удаляет параметр пути :symbol используя метод Delete

## Шаг 4. Техническое описание запроса

handlers.DeletWatchList - нужно смотреть в этом обработчике, но у меня его нет, поэтому напишу 

http
DELETE /api/v1/watchlist/:symbol
Host: localhost:3000

## Шаг 5. Пример запроса json

```json
    {
        ....
    }


```

## Шаг 6. Пример успешного ответа json
```json
 {
  "message": ":symbol удален из watchlist",
  "status": "success"
  "Code": 200
 }   
```
 ## Шаг 7. Пример ответа с ошибками (json)
```json
 [
 {
  "message": ":symbol не удален из watchlist, отсутствует запрашиваемая страница",
  "status": "error"
  "Code": 404
 }   
,
 {
  "message": ":symbol не удален из watchlist, доступ запрещен",
  "status": "error"
  "Code": 403
 },

 {
  "message": ":symbol не удален из watchlist, ошибка сервера",
  "status": "error"
  "Code": 500
 }   
 ]   
```

### `GET /api/v1/portfolio` — Получить портфолио пользователя

Статус: Стабильно | Обновлено: {{ git_revision_date }}

#### Метаданные

| Поле | Значение | Подтверждение |
|------|----------|---------------|
| **Метод** | `GET` | `main.go` |
| **Путь** | `/api/v1/portfolio` | `main.go` |
|**Обработчик**|`handlers.PortfolioHandler`|`main.go`
|**Авторизация**|`Требуется - protected`|`main.go`|
|**Параметр пути**|`нет`|`main.go`|
|**Порт**|`8000`|`main.go`|

#### Пример запроса

```http
GET /api/v1/portfolio HTTP/1.1
Host: localhost:8000
Authorization: Bearer <your_token>
```