import db

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

    return f'''Произошла непредвиденная ошибка:
    
{e}

Пожалуйста попробуйте выполнить действие снова.

Если предидущий шаг не помог напишите админу @iamlostshe'''

def admin(lang_code: None = None) -> str:
    if lang_code != 'ru':
        lang_code = 'en'

    get_stat = db.get_stat()

    return f'''Количество пользователей в боте: {get_stat[0]}
            
Рефералы (источники прихода аудитории, в порядке убывания):
            
{get_stat[1]}'''