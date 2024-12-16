from utils import db
from loguru import logger

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
    if lang_code != 'ru':
        lang_code = 'en'

    logger.error(e)

    return f'''Произошла непредвиденная ошибка, возможно информация ниже поможет вам понять в чем дело:
    
<b>Ошибка:</b>

{str(str(type(e).__name__))}

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