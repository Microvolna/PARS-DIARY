# TODO Добавить докстроки
# TODO Додель поддержку английского языка
# 
# if lang_code != 'ru':
#     lang_code = 'en'
# 
# Врядли ботом будет пользоваться не говорящий
# по русски человек. Эта функция нужна больше
# для эстетики, ибо у меня, думаю как и у многих
# тг на английском и было бы приятнее получать
# ответы на английском)

# Aiogram
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Writed by me modules
from utils import db
from utils.load_env import GIT_URL


def start_old_user(first_name: int | str, lang_code: str | None = 'ru') -> str:
    if lang_code != 'ru':
        lang_code = 'en'

    return f'''👾 Здравствуйте, {first_name}!

⭐️ Доступные комманды:

/start - Начать диалог
/me - Данные о тебе
/cs - Классные часы
/events - Ивенты
/birtdays - Дни рождения
/marks - Оценки
/i_marks - Итоговые оценки
/hw - Домашнее задание

💡 Всегда доступны в "Меню" (нижний левый угол).'''


def start_new_user(first_name: int | str, lang_code: str | None = 'ru') -> str:
    if lang_code != 'ru':
        lang_code = 'en'

    return f'''👾 Здравствуйте, {first_name}! Вы не авторизованны в боте.

⭐️ Комманды, доступные после авторизации:

/start - Начать диалог
/me - Данные о тебе
/cs - Классные часы
/events - Ивенты
/birtdays - Дни рождения
/marks - Оценки
/i_marks - Итоговые оценки
/hw - Домашнее задание

💡 Всегда доступны в "Меню" (нижний левый угол).

💬 Инструкция по регистрации в боте -> кнопка "Инструкция" ниже.'''


def error(e: str, lang_code: str | None = 'ru') -> str:
    # TODO В случае возникновения некоторых ошибок
    # стоит выдавать инструкцию по регестрации
    
    if lang_code != 'ru':
        lang_code = 'en'

    logger.error(e)

    return f'''Произошла непредвиденная ошибка, возможно информация ниже поможет вам понять в чем дело:
    
<b>Ошибка:</b>

{str(type(e).__name__)}

<b>Пояснение:</b>

{e}

<b>Если ошибка произошла не по вашей вине напишите админу @iamlostshe</b>'''


def admin(lang_code: None = None) -> str:
    if lang_code != 'ru':
        lang_code = 'en'

    get_stat = db.get_stat()

    return f'''Количество пользователей в боте: {get_stat[0]}
            
Рефералы (источники прихода аудитории, в порядке убывания):
            
{get_stat[1]}'''


def not_auth(lang_code: None = None) -> str:
    if lang_code != 'ru':
        lang_code = 'en'

    return 'Для выполнения этого действия вам необходимо зарегистрироваться.'


def not_auth_keyboard(land_code: None = None) -> InlineKeyboardMarkup:
    if land_code != 'ru':
        land_code = 'en'

    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Инструкция', url='https://telegra.ph/Instrukciya-po-registracii-v-bote-04-25')]])


def about(lang_code: None = None) -> str:
    if lang_code != 'ru':
        lang_code = 'en'

    return f'''<b>PARS-DIARY</b> - это проект с открытым исходным кодом, направленный на улучшение успеваемости учеников путем введения современных технологий.

Что отличает нас от конкурентов?

- <b>Бесплатно</b>
- <b>Открыто</b>
- <b>Безопасно</b>
- <b>Эффективно</b>
- <b>Есть функционал уведомлений</b>
- <b>Есть функционал умных уведомлений*</b>
- <b>Есть интеграции с нейросетями и инструменты для быстрого решения домашнего задания</b>


*<b>умные уведомления</b> - [в разработке] уникальная функция для анализа оценок и простых уведомлений, например:

<blockquote>Спорная оценка по математике, необходимо исправить, иначе может выйти 4!

Для настройки уведомлений используйте /notify
</blockquote>
или

<blockquote>Вам не хватает всего 0.25 балла до оценки 5, стоит постараться!

Для настройки уведомлений используйте /notify
</blockquote>

Что-то сломалось? - пиши админу @iamlostshe

<b>Исходный код</b>: {GIT_URL}'''