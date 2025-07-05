from aiogram.fsm.state import State, StatesGroup


class CurtainCalculation(StatesGroup):
    waiting_for_fabric_type = State()
    waiting_for_height = State()
    waiting_for_width = State()
    waiting_for_zipper = State()


FABRIC_PRICES = {
    "Брезент": 500,
    "Оксфорд": 450
}

ZIPPER_PRICE_PER_METER = 300
WIDTH_OVERLAP = 0.1
