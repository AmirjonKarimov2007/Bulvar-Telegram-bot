from aiogram.types import Message, CallbackQuery
from aiogram import Bot, types
from keyboards.repl import *
import sqlite3
from keyboards.repl import admin_panel
from aiogram.fsm.context import FSMContext
from handlers.vakansiya1 import *

db = sqlite3.connect('my_database.db')
cursor = db.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS ids (user_id INT)')  # REKLAMA
cursor.execute('CREATE TABLE IF NOT EXISTS admins (id INT)') # ADMIN
cursor.execute('CREATE TABLE IF NOT EXISTS vips (id INT)') # VIP
cursor.execute('CREATE TABLE IF NOT EXISTS channels (username TEXT)') # CHANNELS


async def start(message: Message, bot: Bot):
    cursor.execute('SELECT * FROM ids WHERE user_id = ?', (message.from_user.id,))
    result = cursor.fetchone()
    if result is None:
        cursor.execute('INSERT INTO ids VALUES (?)', (message.from_user.id,))
        db.commit()
    cursor.execute('SELECT * FROM admins WHERE id = ?', (message.from_user.id,))
    result = cursor.fetchone()
    if result is not None or message.from_user.id == 2038175209:
        await admin_reply(message)
    else:
        cursor.execute('SELECT * FROM vips WHERE id = ?', (message.from_user.id,))
        result = cursor.fetchone()
        if result is not None:
            await vip_reply(message)
        else:
            await user_reply(message, bot)

async def admin_reply(message: Message):
    await message.answer("Admin paneliga xush kelibsiz!", reply_markup=admin_panel)

async def vip_reply(message: Message):
    await message.answer("VIP foydalanuvchi paneliga xush kelibsiz!")

async def user_reply(message: Message, bot: Bot):
    photo = types.input_file.FSInputFile('photos/logo.jpg')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo, reply_markup=menu_buttons)


async def start_answer(message: Message, bot: Bot):
    photo = types.input_file.FSInputFile('photos/logo.jpg')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo, reply_markup=menu_buttons)


async def kompaniya_answer(message: Message, bot: Bot):
    photo = types.input_file.FSInputFile('photos/logo.jpg')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption="""<b>Bulvar bu siz istagan makon</b>

🍗 Bulvar bu Namangan shahridagi eng yaxshi qarsilamma tayoqchalar va stripislar tayyorlanuvchi restorant

🏢 Umumiy hisobda Namangan shahrida 3 ga yaqin filiali o’z ish faoliyatini olib boradi

<b>⏰ Bizning jamoaga qo’shiling hamda karyerangizni qurishda davom eting!</b>""", parse_mode="HTML")
     

