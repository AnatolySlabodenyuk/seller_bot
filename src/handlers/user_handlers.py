from aiogram import types, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from src.config_data.config import CurtainCalculation
from src.lexicon.lexicon import LEXICON
from src.keyboards.inline import fabric_keyboard, zipper_keyboard, restart_keyboard
from src.services.calculator import calculate_curtain_cost

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(LEXICON["start"], reply_markup=fabric_keyboard())
    await state.set_state(CurtainCalculation.waiting_for_fabric_type)


@router.callback_query(lambda c: c.data.startswith("fabric_"))
async def process_fabric_selection(callback_query: types.CallbackQuery, state: FSMContext):
    fabric_type = callback_query.data.replace("fabric_", "")
    await state.update_data(fabric_type=fabric_type)
    await callback_query.answer()
    await callback_query.message.edit_text(
        LEXICON["height"].format(fabric=fabric_type)
    )
    await state.set_state(CurtainCalculation.waiting_for_height)


@router.message(CurtainCalculation.waiting_for_height)
async def process_height_input(message: types.Message, state: FSMContext):
    try:
        height = float(message.text.replace(",", "."))
        if height <= 0:
            raise ValueError
        await state.update_data(height=height)
        await message.answer(
            LEXICON["width"].format(height=height)
        )
        await state.set_state(CurtainCalculation.waiting_for_width)
    except ValueError:
        await message.answer(LEXICON["input_error"].format(example="3 или 3.5"))


@router.message(CurtainCalculation.waiting_for_width)
async def process_width_input(message: types.Message, state: FSMContext):
    try:
        width = float(message.text.replace(",", "."))
        if width <= 0:
            raise ValueError
        await state.update_data(width=width)
        await message.answer(
            LEXICON["zipper"].format(width=width),
            reply_markup=zipper_keyboard()
        )
        await state.set_state(CurtainCalculation.waiting_for_zipper)
    except ValueError:
        await message.answer(LEXICON["input_error"].format(example="3.8 или 4"))


@router.callback_query(lambda c: c.data.startswith("zipper_"))
async def process_zipper_selection(callback_query: types.CallbackQuery, state: FSMContext):
    zipper_count = int(callback_query.data.replace("zipper_", ""))
    data = await state.get_data()
    result = calculate_curtain_cost(
        data["fabric_type"], data["height"], data["width"], zipper_count
    )
    result["fabric"] = result["fabric_type"]
    await callback_query.message.edit_text(
        LEXICON["result"].format(**result)
    )
    await callback_query.answer()
    await state.clear()
    await callback_query.message.answer(
        LEXICON["restart"], reply_markup=restart_keyboard()
    )


@router.callback_query(lambda c: c.data == "restart")
async def process_restart(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await cmd_start(callback_query.message, state)


@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(LEXICON["help"])
