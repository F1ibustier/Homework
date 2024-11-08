from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
button1_1 = KeyboardButton(text='Информация')
button1_2 = KeyboardButton(text='Рассчитать')
kb1.row(button1_1, button1_2)

kb2 = InlineKeyboardMarkup()
button2_1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button2_2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb2.row(button2_1, button2_2)

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.\n'
                         'Чтобы узнать, сколько тебе нужно потреблять калорий в сутки набери "Рассчитать"',
                         reply_markup=kb1)

@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup=kb2)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Упрощенная формула Миффлина-Сан-Жеора позволяет рассчитать базовую норму калорий (BMR)'
                              ' с учётом пола, возраста, роста и веса человека\n'
                              'Для мужчин: BMR = 10 x вес (кг) + 6,25 x рост (см) — 5 x возраст (лет) + 5;\n'
                              'Для женщин: BMR = 10 x вес (кг) + 6,25 x рост (см) — 5 x возраст (лет) — 161.')
    await call.answer()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer('Информация о боте')

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_growth(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    norma = 10 * int(data['weight']) + 6.25 * int(data['growth']) + 5 * int(data['age']) + 5
    await message.answer(f'Ваша норма: {norma} калорий')
    await state.finish()

@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
