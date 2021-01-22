from environs import Env

env = Env()
# Read .env into os.environ
env.read_env()


# Constant
TELEGRAM_BOT_TOKEN= env.str('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHANNEL_ID= env.str('TELEGRAM_CHANNEL_ID')
URL_WEB = 'https://www.crossfit.com'
CONTENT_CLASS = '_6zX5t4v71r1EQ1b1O0nO2 jYZW249J9cFebTPrzuIl0'