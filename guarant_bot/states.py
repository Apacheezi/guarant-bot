from aiogram.fsm.state import State, StatesGroup

class DealState(StatesGroup):
    game = State()
    description = State()
    price = State()
    buyer = State()
    confirm = State()
