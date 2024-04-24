<div align="center">
  <h1>grocery_store_sarafan</h1>
  
  <h3>Описание</h3>
  <p>Backend проекта "магазин продуктов".</p>

<hr>

  <h3>Эндпоинты</h3>
</div>
<details>
  <p><summary align="center"><ins>Получение категорий</ins></summary></p>
  
  ```JSON
    method: GET
    Authorization: No Auth
    URL: http://domaine:port/api/v1/categories/
    Status: 200 OK
    Response:
              {
                  "count": 1,
                  "next": "http://domaine:port/api/v1/categories/?page={int}",
                  "previous": "http://domaine:port/api/v1/categories/?page={int}",
                  "results": [
                      {
                          "title": "str",
                          "slug": "str",
                          "image": "http://domaine:port/media/images/{str}.png",
                          "subcategories": [
                              {
                                  "title": "str",
                                  "slug": "str",
                                  "image": "http://domaine:port/media/images/{str}.png"
                              }
                          ]
                      }
                  ]
              }
  ```
</details>
<details>
  <p><summary align="center"><ins>Получение продуктов</ins></summary></p>

  ```JSON
    method: GET
    Authorization: No Auth
    URL: http://domaine:port/api/v1/products/
    Status: 200 OK
    Response:
              {
                  "count": 1,
                  "next": "http://domaine:port/api/v1/products/?page={int}",
                  "previous": "http://domaine:port/api/v1/products/?page={int}",
                  "results": [
                      {
                          "title": "str",
                          "slug": "str",
                          "image": [
                              "http://domaine:port/media/images/{str}.png",
                              "http://domaine:port/media/images/{str}.png",
                              "http://domaine:port/media/images/{str}.png"
                          ],
                          "price": 1,
                          "category": "str",
                          "subcategory": "str"
                      }
                  ]
              }
```
</details>
<details>
  <p><summary align="center"><ins>Регистрация пользователя</ins></summary></p>
  
  ```JSON
    method: POST
    Authorization: No Auth
    URL: http://domaine:port/api/v1/auth/users/
    Status: 201 Created
    Request:
              {
                  "username": "str",
                  "password": "str"
              }
    Response:
              {
                  "email": "str",
                  "username": "str",
                  "id": 1
              }
  ```
</details>
<details>
  <p><summary align="center"><ins>Получение токена</ins></summary></p>

  ```JSON
    method: POST
    Authorization: No Auth
    URL: http://domaine:port/api/v1/auth/jwt/create/
    Status: 200 OK
    Request:
              {
                  "username": "str",
                  "password": "str"
              }
    Response:
              {
                  "refresh": "str",
                  "access": "str"
              }
  ```
</details>
<details>
  <p><summary align="center"><ins>Добавление/изменение/удаление товара из корзины</ins></summary></p>
  
  ```JSON
    method: POST
    Authorization: Bearer Token
    URL: http://domaine:port/api/v1/basket/
    Status: 201 Create
    Request:
              {
                  "product": "str",
                  "count":  1
              }
    Response:
              {
                  "product": {
                      "title": "str",
                      "slug": "str",
                      "image": [
                          "http://domaine:port/media/images/{str}.png",
                          "http://domaine:port/media/images/{str}.png",
                          "http://domaine:port/media/images/{str}.png"
                      ],
                      "price": 1,
                      "category": "str",
                      "subcategory": "str"
                  },
                  "count": 1,
                  "total_price_product": 1
              }
  ```
  ```JSON
    method: PUT, PATCH
    Authorization: Bearer Token
    URL: http://domaine:port/api/v1/basket/
    Status: 200 OK
    Request:
              {
                  "product": "str",
                  "count":  1
              }
    Response:
              {
                  "product": {
                      "title": "str",
                      "slug": "str",
                      "image": [
                          "http://domaine:port/media/images/{str}.png",
                          "http://domaine:port/media/images/{str}.png",
                          "http://domaine:port/media/images/{str}.png"
                      ],
                      "price": 1,
                      "category": "str",
                      "subcategory": "str"
                  },
                  "count": 1,
                  "total_price_product": 1
              }
  ```
  ```JSON
    method: DELETE
    Authorization: Bearer Token
    URL: http://domaine:port/api/v1/basket/
    Status: 204 No Content
    Request:
              {
                  "product": "str",
                  "count":  1
              }
  ```
</details>
<details>
  <p><summary align="center"><ins>Получение информации по корзине</ins></summary></p>
  
  ```JSON
    method: GET
    Authorization: Bearer Token
    URL: http://domaine:port/api/v1/basket/info/
    Status: 200 OK
    Response:
              {
                  "products": [
                      {
                          "product": {
                              "title": "str",
                              "slug": "str",
                              "image": [
                                  "http://domaine:port/media/images/{str}.png",
                                  "http://domaine:port/media/images/{str}.png",
                                  "http://domaine:port/media/images/{str}.png"
                              ],
                              "price": 1,
                              "category": "str",
                              "subcategory": "str"
                          },
                          "count": 1,
                          "total_price_product": 1
                      }
                  ],
                  "total_count": 1011,
                  "total_price_products": 6066
              }
  ```
</details>
<details>
  <p><summary align="center"><ins>Очистка корзины</ins></summary></p>
  
  ```JSON
    method: DELETE
    Authorization: Bearer Token
    URL: http://domaine:port/api/v1/basket/clean/
    Status: 204 No Content
  ```
</details>
<hr>

<h3 align="center">Как запустить</h3>
<details>
  <p align="center"><summary align="center"><ins>Через Docker</ins></summary></p>
  <ul>
    <li align="center">1. Создать и заполнить файл <code>.env</code> в папке 
      <a href="https://github.com/VladislavYar/grocery_store_sarafan/tree/main/infra"><code>infra</code></a> по шаблону 
        <a href="https://github.com/VladislavYar/grocery_store_sarafan/blob/main/infra/.env.example"><code>.env.example</code></a>.
    </li>
    <li align="center">
      <p>2. Если имеется утилита <code>Make</code>, в корне проекта выполнить команду <code>make project-init</code>,</p>
      <p>иначе</p>
      <p>выполнить команду <code>docker compose -f ./infra/docker-compose.yml --env-file ./infra/.env up -d</code>.</p>
      <p><code>Docker</code> соберёт контейнеры с <code>postgreSQL</code>, <b>приложением</b>, выполнит миграцию,</p>
      <p>заполнит БД тестовыми <i>категориями</i>, <i>подкатегориями</i> и <i>продуктами</i>, создаст superuser-a.</p>
      <p>После сервер будет доступен по адрессу: <code>http://127.0.0.1:8000/</code>.</p>
    </li>
    <li align="center">
      <p><b>Примечание</b></p>
      <p>3. В контейнер с приложением проброшен <code>volume</code> с кодом, изменение кода в проекте обновляет его в контейнере и перезапускает сервер.</p>
    </li>
    <li align="center">
      <p>4. Последующие запуски проекта осуществляются через команду <code>make project-start</code></p>
      <p>или</p>
      <p><code>docker compose -f ./infra/docker-compose-start.yml --env-file ./infra/.env up -d</code></p>
    </li>
  </ul>
</details>

<details>
  <p align="center"><summary align="center"><ins>Через консоль</ins></summary></p>
  <ul>
    <li align="center">1. Создать и заполнить файл <code>.env</code> в папке 
      <a href="https://github.com/VladislavYar/grocery_store_sarafan/tree/main/infra"><code>infra</code></a> по шаблону 
        <a href="https://github.com/VladislavYar/grocery_store_sarafan/blob/main/infra/.env.example"><code>.env.example</code></a>.
    </li>
    <li align="center">
      <p>2. Создать БД в <code>postgreSQL</code>.</p>
    </li>
    <li align="center">
      <p>3. Перейти в корень проекта и создать виртуальное окружение <code>python -m venv venv</code>.</p>
    </li>
    <li align="center">
      <p>4. Активировать виртуальное окружение <code>source venv/Scripts/activate</code>.</p>
    </li>
    <li align="center">
      <p>5. Установить зависимости <code>pip install -r requirements.txt</code>.</p>
    </li>
    <li align="center">
      <p>6. Выполнить миграцию БД <code>python src/manage.py migrate</code>.</p>
    </li>
        <li align="center">
      <p>7. Создать superuser-a <code>python src/manage.py createsuperuser --noinput</code>.</p>
    </li>
    </li>
        <li align="center">
      <p>8. Заполнить БД тестовыми данными(<i>категории, подкатегории, продукты</i>) <code>python src/manage.py test_data</code>.</p>
    </li>
    </li>
        <li align="center">
      <p>9. Запустить сервер <code>python src/manage.py runserver</code>.</p>
    </li>
        </li>
        <li align="center">
      <p>10. Сервер будет доступен по адрессу: <code>http://127.0.0.1:8000/</code>.</p>
    </li>
  </ul>
</details>
<hr>

<h3 align="center">Стек</h3>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12.3-red?style=flat&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Django-5.0.4-red?style=flat&logo=django&logoColor=white">
  <img src="https://img.shields.io/badge/DjangoRestFramework-3.15.2-red?style=flat">
  <img src="https://img.shields.io/badge/PostgreSQL-Latest-red?style=flat&logo=postgresql&logoColor=white">
  <img src="https://img.shields.io/badge/Docker-Latest-red?style=flat&logo=docker&logoColor=white">
</p>
<hr>

