# api id, hash
API_ID = 22522686
API_HASH = '3776efcbe8ca722437998cf5a625ecce'

DELAYS = {
    'ACCOUNT': [5, 15],  # delay between connections to accounts (the more accounts, the longer the delay)
    'PLAY': [0, 0],   # delay between play in seconds
    'ERROR_PLAY': [60, 180],    # delay between errors in the game in seconds
}

BOMBS = [2, 6, 1] # первое число - всего бомбочек, второе число - количество игр для использования бомбочек, третье число, максимум бомбочек за игру
SNOWFLAKES = [7, 7, 2] # первое число - всего снежинок, второе число - количество игр для использования снежинок, третье число, максимум снежинок за игру
POINTS = [240, 280]

PROXY_TYPE = "socks5"  # "socks4", "socks5" and "http" are supported

# title blacklist tasks (do not change)
BLACKLIST_TASKS = ['Farm points']

# session folder (do not change)
WORKDIR = "sessions/"
