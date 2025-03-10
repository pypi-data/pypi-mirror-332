from flask import Flask, redirect, url_for, session, request
from src.FlaskDiscordAuth.discord_auth import DiscordAuth

# Создаем Flask приложение
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Замените на свой секретный ключ

# Настройки Discord (получите из Discord Developer Portal)
CLIENT_ID = 'your_client_id'          # Замените на ваш Client ID
CLIENT_SECRET = 'your_client_secret'  # Замените на ваш Client Secret
REDIRECT_URI = 'http://127.0.0.1:5000/callback'

# Инициализируем объект авторизации Discord
discord_auth = DiscordAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)

@app.route('/')
def home():
    """Главная страница: показывает приветствие или информацию о пользователе."""
    if 'user' in session:
        user = session['user']
        avatar_id = user.get('avatar')
        avatar_url = f"https://cdn.discordapp.com/avatars/{user['id']}/{avatar_id}.png" if avatar_id else "https://cdn.discordapp.com/embed/avatars/0.png"
        return f"""
            <img src="{avatar_url}" alt="Аватар пользователя" style="width:128px;height:128px;border-radius:50%;">
            <h1>Привет, {user['username']}#{user['discriminator']}!</h1>
            <p>Email: {user.get('email', 'Не указан')}</p>
            <p>ID: {user['id']}</p>
            <a href="/logout">Выйти</a>
        """
    return 'Добро пожаловать! <a href="/login">Войти через Discord</a>'

@app.route('/login')
def login():
    """Перенаправляет на страницу авторизации Discord."""
    return redirect(discord_auth.get_login_url())

@app.route('/callback')
def callback():
    """Обрабатывает callback от Discord и сохраняет данные пользователя."""
    code = request.args.get('code')
    token_data = discord_auth.get_token(code)
    access_token = token_data['access_token']
    user_info = discord_auth.get_user_info(access_token)
    session['user'] = user_info
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    """Удаляет данные пользователя из сессии."""
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)