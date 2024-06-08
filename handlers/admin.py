import sqlite3
from aiogram import Bot
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardRemove
from aiogram.enums import ChatMemberStatus
from aiogram.fsm.context import FSMContext
from utils.states import StepsForm
from keyboards.repl import admin_panel

db = sqlite3.connect('my_database.db')
cursor = db.cursor()
def find_admin(user_id):
    cursor.execute("SELECT * FROM admins WHERE id=?", (user_id,))
    return cursor.fetchone() is not None
admin_id = 2038175209

async def get_post(message: Message, state: FSMContext):
    if find_admin(message.from_user.id) or message.from_user.id == admin_id:
        await message.answer("Iltimos, foydalanuvchilarga yubormoqchi bo'lgan postni jo'nating")   
        await state.set_state(StepsForm.GET_POST)
async def send_post(message: Message, state: FSMContext, bot: Bot):
    cursor.execute("SELECT * FROM ids")
    user_ids = [row[0] for row in cursor.fetchall()]
    for n in user_ids:
        if message.text:
            try:
                await bot.send_message(chat_id = n, text=message.text)
            except:
                print("a")
        if message.voice:
            try:
                await bot.send_audio(chat_id=n, audio=message.voice.file_id, caption=message.caption)
            except:
                print("b")
        if message.video:
            try:
                await bot.send_video(chat_id=n, video=message.video.file_id, caption=message.caption)
            except:
                print("d")
        if message.photo:
            try:
                await bot.send_photo(chat_id=n, photo=message.photo[-1].file_id, caption=message.caption)
            except:
                print("c")
        if message.video_note:
            try:
                await bot.send_video_note(chat_id=n, video_note=message.video_note.file_id)
            except:
                print("e")
        if message.document:
            try:
                await bot.send_video(chat_id=n, video=message.document.file_id, caption=message.caption)
            except:
                print("f")
        if message.audio:
            try:
                await bot.send_audio(chat_id=n, audio=message.audio.file_id, caption=message.caption)
            except:
                print("g")
    await state.clear()

async def get_admin(message: Message, state: FSMContext):
    if find_admin(message.from_user.id) or message.from_user.id == admin_id:
        await message.answer("Iltimos, qo'shmoqchi bo'lgan adminni telegram ID raqamini kiriting")
        await state.set_state(StepsForm.GET_ADMIN)
async def make_admin(message: Message, state: FSMContext, bot: Bot):
        if message.text.isdigit():
            admin_id = int(message.text)
            cursor.execute("INSERT INTO admins VALUES (?)", (admin_id,))
            db.commit()
            await state.clear()
            await message.answer(f"{admin_id} ID li foydalanuvchi admin qilib qo'shildi.", reply_markup=admin_panel)
            await bot.send_message(chat_id=admin_id, text="Sizga adminlar tomonidan admin huquqi berildi!🪪", reply_markup=admin_panel)
        else:
            await message.answer("ID faqat sondan iborat bo'lishi kerak")

async def print_admin(message: Message):
    if find_admin(message.from_user.id) or message.from_user.id == admin_id:
        def get_all_admin_ids():
            cursor.execute("SELECT id FROM admins")
            admins = cursor.fetchall()
            return [admin[0] for admin in admins]
        
        admin_ids = get_all_admin_ids()
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=str(admin_id) , callback_data=f"del_{admin_id}")] for admin_id in admin_ids])
        await message.reply("Barcha adminlar:", reply_markup=keyboard)
async def del_admin(call: CallbackQuery, bot: Bot):
    admin_id = int(call.data.split("_")[1])
    cursor.execute("DELETE FROM admins WHERE id=?", (admin_id,))
    db.commit()
    await call.message.delete()
    await bot.send_message(call.from_user.id, f"Admin ID: {admin_id} o'chirildi 😊", reply_markup = admin_panel)
    await bot.send_message(chat_id=admin_id, text="Sizdan admin huquqi olindi‼️", reply_markup=ReplyKeyboardRemove())