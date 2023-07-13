# Inforce Python Task 

Django REST API application that helps employees make decisions of the restaurant to have lunch today.

### make sure to install all necessary packaged and libraries:
```bash
  pip install -r requirements.txt
```

## DataBase setup

Inside `settings.py` file there is the option of two DB configurations:

    1. SQLite DB 
    2. Postgres DB

If you have chosen Postgres you need to configure Postgres Server.
The easiest way is to install Docker on your machine and run following commands inside `app/` folder:

```bash
  docker-compose up -d
  cd ..
  make migrate
```


## Project shortcuts


Run server

```bash
  make run
```
Prepare migrations

```bash
  make makemigrations
```

Migrate

```bash
  make migrate
```

Open ORM shell

```bash
  make shell
```

## Running Tests

To run tests, proceed the following instruction:
#### 1. Remove or comment provided below attribute inside every view.py file of apps you want to test
```code
  authentication_classes = [SessionAuthentication, BasicAuthentication]
```
#### 2. Go to app/ filter
```bash
  cd app/
  ls
  authentication/  dish/  manage.py*  menu/  pytest.ini  restaurants/  settings/  tests/  vote/
```
#### 3. Run tests
```bash
  pytest
```


# Main API endpoints

## Authentication
#### Register:

```http
  POST /api/register/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required** |
| `password` | `string` | **Required** |

#### Log In:

```http
  POST /api/login/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required** |
| `password` | `string` | **Required** |

#### Log Out:

```http
  POST /api/logout/
```
GET will not be supported from Django v5.0
```http
  GET /api/logout/ 
```

#### JWT verify token:

```http
  GET /api/token/verify/
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Required** |

#### JWT refresh token:

```http
  GET /api/token/refresh/
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Required** |


### Restaurant app

#### List of restaurants:

```http
  GET /api/restaurant/list/
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id`      | integer | **Optional** |
| `delivery`| boolean | **Optional** |

#### Create restaurant:

```http
  POST /api/restaurant/create/
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name`     | string | **Required** |
| `address`| string | **Optional** |
| `delivery`| boolean | **Optional (False is default)** |
| `phone_number`| string | **Optional** |

#### Update restaurant:

```http
  PUT /api/restaurant/update/<int:pk>/
```
| Parameter | Type     |
| :-------- | :------- | 
| `name`     | string | 
| `address`| string | 
| `delivery`| boolean | 
| `phone_number`| string | 

#### Delete restaurant:

```http
  DELETE /api/restaurant/delete/<int:pk>/
```

### Dish app

#### List of dishes:

```http
  GET /api/dish/list/
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id`      | integer | **Optional** |


#### Create the dish:

```http
  POST /api/dish/create/
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name`     | string | **Required** |


#### Update dish:

```http
  PUT /api/dish/update/<int:pk>/
```
| Parameter | Type     |
| :-------- | :------- | 
| `name`     | string | 


#### Delete dish:

```http
  DELETE /api/dish/delete/<int:pk>/
```

### Menu app

#### List of menus:

```http
  GET /api/menu/list/
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id`      | integer | **Optional** |
| `restaurant_id` | integer | **Optional** |
| `day` | integer / (today/tomorrow) | **Optional** |



#### Create menu:

```http
  POST /api/menu/create/
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `restaurant` | integer | **Required** |
| `day` | integer | **Optional (default - 0 Monday)** |
| `dishes` | list | **Required** |


#### Update menu:

```http
  PUT /api/menu/update/<int:pk>/
```
| Parameter | Type     | 
| :-------- | :------- | 
| `restaurant` | integer | 
| `day` | integer | 
| `dishes` | list | 


#### Delete menu:

```http
  DELETE /api/menu/delete/<int:pk>/
```

### Vote app

#### List of votes:

```http
  GET /api/vote/list/
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id`      | integer | **Optional** |


#### Vote:

```http
  POST /api/vote/create/
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `employee` | integer | **Required** |
| `model` | integer | **Required** |


#### Change vote:

```http
  PUT /api/vote/update/<int:pk>/
```
| Parameter | Type     | 
| :-------- | :------- | 
| `employee` | integer | 
| `model` | integer | 


#### Delete vote:

```http
  DELETE /api/vote/delete/<int:pk>/
```


### Admin GIU panel

#### 1. Create superuser
```code
  cd app/
  python3 manage.py createsuperuser
```
#### 2. Provide username and password and press `yes`

#### 3. Go buy this url and provide your credentials

```http
  GET /admin/
```