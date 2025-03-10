import requests
from flask import redirect, session, url_for, request
from urllib.parse import urlencode

class DiscordAuth:
    def __init__(self, client_id, client_secret, redirect_uri, scope='identify email'):
        """Инициализация с данными Discord приложения."""
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scope = scope
        self.auth_url = 'https://discord.com/api/oauth2/authorize'
        self.token_url = 'https://discord.com/api/oauth2/token'
        self.user_url = 'https://discord.com/api/users/@me'

    def get_login_url(self):
        """Генерирует URL для авторизации через Discord."""
        params = {
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri,
            'response_type': 'code',
            'scope': self.scope
        }
        return f"{self.auth_url}?{urlencode(params)}"

    def get_token(self, code):
        """Обменивает код авторизации на access token."""
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': self.redirect_uri
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.token_url, data=data, headers=headers)
        return response.json()

    def get_user_info(self, access_token):
        """Получает информацию о пользователе по access token."""
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.get(self.user_url, headers=headers)
        return response.json()

    def login_required(self, func):
        """Декоратор для защиты маршрутов, требующих авторизации."""
        def wrapper(*args, **kwargs):
            if 'user' not in session:
                return redirect(url_for('login'))
            return func(*args, **kwargs)
        wrapper.__name__ = func.__name__
        return wrapper