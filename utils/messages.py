'''
Билдеры сообщений
'''
# TODO Додель поддержку английского языка

# Врядли ботом будет пользоваться не говорящий
# по русски человек. Эта функция нужна больше
# для эстетики, ибо у меня, думаю как и у многих
# тг на английском и было бы приятнее получать
# ответы на английском)

# Aiogram
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Modules need to be installed
from loguru import logger

# Writed by me modules
from utils import db
from utils.load_env import GIT_URL


def start_old_user(first_name: int | str, lang_code: str | None = 'ru') -> str:
    'Начало для старых пользователей'

    if lang_code != 'ru':
        lang_code = 'en'

    return (
        f'👾 Здравствуйте, {first_name}!\n\n'
        '⭐️ Доступные комманды:\n\n'
        '/start - Начать диалог\n'
        '/me - Данные о тебе\n'
        '/cs - Классные часы\n'
        '/events - Ивенты\n'
        '/birtdays - Дни рождения\n'
        '/marks - Оценки\n'
        '/i_marks - Итоговые оценки\n'
        '/hw - Домашнее задание\n\n'
        '💡 Всегда доступны в "Меню" (нижний левый угол).'
    )


def start_new_user(first_name: int | str, lang_code: str | None = 'ru') -> str:
    'Начало для новых пользоватлей'

    if lang_code != 'ru':
        lang_code = 'en'

    return (
        f'👾 Здравствуйте, {first_name}! Вы не авторизованны в боте.\n\n'
        '⭐️ Комманды, доступные после авторизации:\n\n'
        '/start - Начать диалог\n'
        '/me - Данные о тебе\n'
        '/cs - Классные часы\n'
        '/events - Ивенты\n'
        '/birtdays - Дни рождения\n'
        '/marks - Оценки\n'
        '/i_marks - Итоговые оценки\n'
        '/hw - Домашнее задание\n\n'
        '💡 Всегда доступны в "Меню" (нижний левый угол).\n\n'
        '💬 Инструкция по регистрации в боте -> кнопка "Инструкция" ниже.'
    )


def error(e: str, lang_code: str | None = 'ru') -> str:
    'Сообщение об ошибке'

    if lang_code != 'ru':
        lang_code = 'en'

    logger.error(e)

    return (
        'Произошла непредвиденная ошибка, возможно '
        'информация ниже поможет вам понять в чем дело:\n\n'
        '<b>Ошибка:</b>\n\n'
        f'{type(e).__name__}\n\n'
        '<b>Пояснение:</b>\n\n'
        '{e}\n\n'
        '<b>Если ошибка произошла не по вашей вине напишите админу @iamlostshe</b>'
    )


def admin(lang_code: None = None) -> str:
    'Сообщение для администраторов'

    if lang_code != 'ru':
        lang_code = 'en'

    get_stat = db.get_stat()

    return (
        f'Количество пользователей в боте: {get_stat[0]}\n\n'
        'Рефералы (источники прихода аудитории, в порядке убывания):\n\n'
        f'{get_stat[1]}'
        )


def not_auth(lang_code: None = None) -> str:
    'Если этот контент не доступен без авторизациия'

    if lang_code != 'ru':
        lang_code = 'en'

    return 'Для выполнения этого действия вам необходимо зарегистрироваться.'


def not_auth_keyboard(land_code: None = None) -> InlineKeyboardMarkup:
    'Если этот контент не доступен без авторизациия (клавиатура)'
    if land_code != 'ru':
        land_code = 'en'

    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Инструкция',
                url='https://telegra.ph/Instrukciya-po-registracii-v-bote-04-25'
            )
        ]
    ])


def about(lang_code: None = None) -> str:
    'Информация о боте'
    if lang_code != 'ru':
        lang_code = 'en'

    return (
        '<b>PARS-DIARY</b> - это проект с открытым исходным кодом, направленный '
        'на улучшение успеваемости учеников путем введения современных технологий.\n\n'
        'Что отличает нас от конкурентов?\n\n'
        '- <b>Бесплатно</b>\n'
        '- <b>Открыто</b>\n'
        '- <b>Безопасно</b>\n'
        '- <b>Эффективно</b>\n'
        '- <b>Есть функционал уведомлений</b>\n'
        '- <b>Есть функционал умных уведомлений*</b>\n'
        '- <b>Есть интеграции с нейросетями и инструменты '
        'для быстрого решения домашнего задания</b>\n\n\n'
        '*<b>умные уведомления</b> - [в разработке] уникальная функция '
        'для анализа оценок и простых уведомлений, например:\n\n'
        '<blockquote>Спорная оценка по математике, необходимо исправить, иначе может выйти 4!\n\n'
        'Для настройки уведомлений используйте /notify\n'
        '</blockquote>\n'
        'или\n\n'
        '<blockquote>Вам не хватает всего 0.25 балла до оценки 5, стоит постараться!\n\n'
        'Для настройки уведомлений используйте /notify\n'
        '</blockquote>\n\n'
        'Что-то сломалось? - пиши админу @iamlostshe\n\n'
        f'<b>Исходный код</b>: {GIT_URL}'
    )
