"""Билдеры клавиатур."""

from __future__ import annotations

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from utils.pars import get_regions


def not_auth_keyboard(land_code: str | None = None) -> InlineKeyboardMarkup:
    """Если этот контент не доступен без авторизациия (клавиатура)."""
    if land_code != "ru":
        land_code = "en"

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Инструкция",
                    url="https://telegra.ph/Instrukciya-po-registracii-v-bote-04-25",
                ),
            ],
        ],
    )


def reg_0(land_code: str | None = None) -> InlineKeyboardMarkup:
    """Нулевая стадия регистрации."""
    if land_code != "ru":
        land_code = "en"

    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="Начнём!", callback_data="reg_0")]],
    )


def reg_1(land_code: str | None = None) -> InlineKeyboardMarkup:
    """Нулевая стадия регистрации."""
    if land_code != "ru":
        land_code = "en"

    result = []
    regions = get_regions()

    for r, u in regions.items():
        result.append(
            [
                InlineKeyboardButton(
                    text=r,
                    callback_data=f"reg_1_{u}",
                ),
            ],
        )

    return InlineKeyboardMarkup(inline_keyboard=result)


def reg_2(land_code: str | None = None) -> InlineKeyboardMarkup:
    """Нулевая стадия регистрации."""
    if land_code != "ru":
        land_code = "en"

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Инструкция",
                    url="https://telegra.ph/Instrukciya-po-registracii-v-bote-04-25",
                ),
            ],
        ],
    )
