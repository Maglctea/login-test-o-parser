"""
Bot messages
"""

# ---------HELP---------
BOT_COMMANDS_INFO = (
    ("start",
     "Начало работы с ботом",
     "При отправке этой команды происходит начало взаимодействие с ботом"
     ),
    ("help",
     "Помощь и справка",
     "При отправке этой команды бот покажет, какие команды доступны для взаимодействия с ним",
     ),
    # ("Список товаров",
    #  "Начать поиск товаров",
    #  "При отправке этой команды бот отправит запрос к API на начало парсинга товаров")
)

TEXT_HELP = "Помощь и справка о боте\n\n" \
            "Доступные команды:\n" \
            "- /start\n" \
            "- /help\n" \
            "- Начать парсинг"

# ---------MIDDLEWARES---------
PERMISSION_DENIED_MESSAGE = "У вас нет прав для доступа к этому боту :("

# ---------START---------
GREETING_TEXT = "Привет, это Ozon parser bot"

# ---------PARSE---------
START_PARSE = "Процедура парсинга начата"
END_PARSE = "Задача на парсинг товаров с сайта Ozon завершена.\nСохранено: {} товаров."
ERROR_PARSE = "Сервер не отвечает. Попробуйте повторить позднее"