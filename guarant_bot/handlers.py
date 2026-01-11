from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from states import DealState
from keyboards import games_kb, confirm_kb
from config import COMMISSION
import re

router = Router()

@router.message(F.text == "/start")
async def start(msg: Message):
    await msg.answer("🔐 Гарант сделок\n\nНапиши /create для создания сделки")

@router.message(F.text == "/create")
async def create(msg: Message, state: FSMContext):
    await state.set_state(DealState.game)
    await msg.answer("🎮 Выберите игру:", reply_markup=games_kb())

@router.callback_query(DealState.game)
async def game(call: CallbackQuery, state: FSMContext):
    await state.update_data(game=call.data)
    await state.set_state(DealState.description)
    await call.message.answer("✏️ Опишите аккаунт")
    await call.answer()

@router.message(DealState.description)
async def description(msg: Message, state: FSMContext):
    await state.update_data(description=msg.text)
    await state.set_state(DealState.price)
    await msg.answer("💰 Введите цену (только цифры)")

@router.message(DealState.price)
async def price(msg: Message, state: FSMContext):
    if not msg.text.isdigit():
        return await msg.answer("❌ Введите цену цифрами")

    price = int(msg.text)
    commission = int(price * COMMISSION)

    await state.update_data(price=price, commission=commission)
    await state.set_state(DealState.buyer)

    await msg.answer(
        f"💰 Цена: {price}\n"
        f"🔐 Комиссия (10%): {commission}\n\n"
        f"👤 Введите @username покупателя"
    )

@router.message(DealState.buyer)
async def buyer(msg: Message, state: FSMContext):
    if not re.match(r"^@[a-zA-Z0-9_]{5,32}$", msg.text):
        return await msg.answer("❌ Неверный username")

    await state.update_data(buyer=msg.text)
    data = await state.get_data()
    await state.set_state(DealState.confirm)

    await msg.answer(
        f"🔎 Проверьте данные сделки:\n\n"
        f"🎮 {data['game']}\n"
        f"📄 {data['description']}\n"
        f"💰 {data['price']}\n"
        f"🔐 Комиссия {data['commission']}",
        reply_markup=confirm_kb()
    )

