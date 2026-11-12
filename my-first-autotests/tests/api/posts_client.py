import requests
from requests import Session

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10 

def get_post(session:Session, post_id:int) -> dict:
    """Получить пост по ID. Возвращает JSON или вызывает исключение."""
    url= f"{BASE_URL}/posts/{post_id}"
    response = session.get(url, timeout=TIMEOUT)
    response.raise_for_status() # выбросит HTTPError при кодах 4xx / 5xx
    return response.json()

def create_post(session:Session, title:str, body:str, userID:int) -> dict:
    """Создать новый пост на сервере с обработкой ошибок."""
    url = f"{BASE_URL}/posts"
    payload = {"title": title, "body": body, "userID": userID}
    try:
        response = session.post(url, json=payload, timeout=TIMEOUT)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        raise RuntimeError("Сервер не ответил за 10 секунд") from None
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 400:
            raise ValueError("Некорректные данные поста") from e
        raise

if __name__ == "__main__":
    with requests.Session() as session:
        # 1. Проверяем получение поста
        post = get_post(session, 1)
        print("Получен пост:", post["title"])

        # 2. Проверяем создание поста
        new_post = create_post(
            session, 
            "AQA Python", 
            "My dear frends, it is realy interesting! I can program all day (sike)", 
            1
        )
        print("Создан пост с ID:", new_post["id"])




