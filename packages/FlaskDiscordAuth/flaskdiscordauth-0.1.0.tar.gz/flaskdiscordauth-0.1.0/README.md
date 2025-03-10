# FlaskDiscordAuth

*Read this in [English](#english-documentation) | Читайте на [русском](#русская-документация)*

---

## English Documentation

### Overview

FlaskDiscordAuth is a Python library designed to simplify Discord OAuth2 authentication integration with Flask applications. It provides an easy way to authenticate users via Discord, obtain their basic information, and protect routes that require authentication.

### Installation

```bash
pip install FlaskDiscordAuth
```

### Requirements

- Flask
- requests

### Basic Usage

Here's a simple example of how to use FlaskDiscordAuth:

```python
from flask import Flask, redirect, url_for, session, request
from FlaskDiscordAuth.discord_auth import DiscordAuth

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Discord configuration settings
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret' 
REDIRECT_URI = 'http://127.0.0.1:5000/callback'

# Initialize Discord authentication object
discord_auth = DiscordAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)

@app.route('/')
def home():
    if 'user' in session:
        user = session['user']
        return f"Hello, {user['username']}!"
    return 'Welcome! <a href="/login">Login with Discord</a>'

@app.route('/login')
def login():
    return redirect(discord_auth.get_login_url())

@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_data = discord_auth.get_token(code)
    access_token = token_data['access_token']
    user_info = discord_auth.get_user_info(access_token)
    session['user'] = user_info
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
```

### Protecting Routes

You can use the provided decorator to protect routes that require authentication:

```python
@app.route('/profile')
@discord_auth.login_required
def profile():
    user = session['user']
    return f"Profile of {user['username']}"
```

### API Reference

#### DiscordAuth

```python
DiscordAuth(client_id, client_secret, redirect_uri, scope='identify email')
```

Creates a new Discord authentication instance.

Parameters:
- `client_id` (str): Your Discord application client ID
- `client_secret` (str): Your Discord application client secret
- `redirect_uri` (str): The URI Discord will redirect to after authentication
- `scope` (str, optional): Space-separated list of OAuth2 scopes. Default is 'identify email'

#### Methods

##### get_login_url()

Generates the OAuth2 authorization URL for Discord.

Returns:
- `str`: The complete Discord authorization URL

##### get_token(code)

Exchanges an authorization code for an access token.

Parameters:
- `code` (str): The authorization code received from Discord

Returns:
- `dict`: Token data including access_token, token_type, expires_in, etc.

##### get_user_info(access_token)

Retrieves Discord user information using the provided access token.

Parameters:
- `access_token` (str): The Discord access token

Returns:
- `dict`: User information including id, username, avatar, email, etc.

##### login_required(func)

A decorator to protect routes that require Discord authentication.

Parameters:
- `func`: The route function to protect

Returns:
- `function`: A wrapper function that checks if the user is authenticated

### Complete Example

For a complete example, see the `app_example.py` file included with the library.

---

## Русская документация

### Обзор

FlaskDiscordAuth - это Python-библиотека, разработанная для упрощения интеграции аутентификации Discord OAuth2 с приложениями Flask. Она предоставляет простой способ аутентификации пользователей через Discord, получения их основной информации и защиты маршрутов, требующих аутентификации.

### Установка

```bash
pip install FlaskDiscordAuth
```

### Требования

- Flask
- requests

### Базовое использование

Вот простой пример использования FlaskDiscordAuth:

```python
from flask import Flask, redirect, url_for, session, request
from FlaskDiscordAuth.discord_auth import DiscordAuth

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Настройки Discord
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret' 
REDIRECT_URI = 'http://127.0.0.1:5000/callback'

# Инициализируем объект аутентификации Discord
discord_auth = DiscordAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)

@app.route('/')
def home():
    if 'user' in session:
        user = session['user']
        return f"Привет, {user['username']}!"
    return 'Добро пожаловать! <a href="/login">Войти через Discord</a>'

@app.route('/login')
def login():
    return redirect(discord_auth.get_login_url())

@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_data = discord_auth.get_token(code)
    access_token = token_data['access_token']
    user_info = discord_auth.get_user_info(access_token)
    session['user'] = user_info
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
```

### Защита маршрутов

Вы можете использовать предоставленный декоратор для защиты маршрутов, требующих аутентификации:

```python
@app.route('/profile')
@discord_auth.login_required
def profile():
    user = session['user']
    return f"Профиль пользователя {user['username']}"
```

### Справочник по API

#### DiscordAuth

```python
DiscordAuth(client_id, client_secret, redirect_uri, scope='identify email')
```

Создает новый экземпляр аутентификации Discord.

Параметры:
- `client_id` (str): ID клиента вашего приложения Discord
- `client_secret` (str): Секретный ключ вашего приложения Discord
- `redirect_uri` (str): URI, на который Discord перенаправит после аутентификации
- `scope` (str, опционально): Список областей OAuth2, разделенных пробелами. По умолчанию 'identify email'

#### Методы

##### get_login_url()

Генерирует URL авторизации OAuth2 для Discord.

Возвращает:
- `str`: Полный URL для авторизации Discord

##### get_token(code)

Обменивает код авторизации на токен доступа.

Параметры:
- `code` (str): Код авторизации, полученный от Discord

Возвращает:
- `dict`: Данные токена, включая access_token, token_type, expires_in и т.д.

##### get_user_info(access_token)

Получает информацию о пользователе Discord, используя предоставленный токен доступа.

Параметры:
- `access_token` (str): Токен доступа Discord

Возвращает:
- `dict`: Информация о пользователе, включая id, username, avatar, email и т.д.

##### login_required(func)

Декоратор для защиты маршрутов, требующих аутентификации Discord.

Параметры:
- `func`: Функция маршрута для защиты

Возвращает:
- `function`: Функция-обертка, которая проверяет, аутентифицирован ли пользователь

### Полный пример

Полный пример использования можно найти в файле `app_example.py`, включенном в библиотеку.