from aiogram import Bot, Dispatcher, F
from aiogram.types import BotCommand
from aiogram.filters import Command
from handlers.start import *
from handlers.vakansiya1 import *
from handlers.admin import *
from asyncio import run

async def main():
    bot = Bot("6960508001:AAGYOI3IMy6g8m9QBiCmEf6DcazwcFs4pk0")
    dp = Dispatcher()
    dp.message.register(start, F.text == "/start")
    dp.message.register(get_post, F.text == "Foydalanuvchilarga post jo'natish 📮")
    dp.message.register(get_admin, F.text=="🙍‍♂️ Admin qo'shish ➕")
    dp.message.register(print_admin, F.text=="🙍‍♂️ Admin o'chirish ❌")
    dp.message.register(kompaniya_answer, F.text == "🏢Kompaniya haqida")
    dp.message.register(call_filial, F.text == "🖋Vakansiya")
    dp.message.register(call_filial, Command("vakansiya"))
    dp.message.register(start_answer, F.text == "❌Bekor qilish❌")
    dp.message.register(filial_answer, vakansiya.FILIAL)
    dp.message.register(job_answer, vakansiya.JOB)
    dp.message.register(jins_answer, vakansiya.JINS) 
    dp.message.register(fio_answer, vakansiya.FIO)
    dp.message.register(birthday_answer, vakansiya.BIRTHDAY)
    dp.message.register(adres_answer, vakansiya.ADRES)
    dp.message.register(verifiy_answer, vakansiya.VERIFIY)
    dp.message.register(vaksina_answer, vakansiya.VERIFIY_Vaksina)
    dp.message.register(disability_answer, vakansiya.DISABILITY)
    dp.message.register(student_answer, vakansiya.VERIFIY_STUDENT)
    dp.message.register(language_answer, vakansiya.LANGUAGE_RU)
    dp.message.register(language_answer_uz, vakansiya.LANGUAGE_UZ)
    dp.message.register(maosh_answer, vakansiya.MAOSH)
    dp.message.register(self_answer, vakansiya.SELF)
    dp.message.register(ish_vaqti_answer, vakansiya.ISH_VAQTI)
    dp.message.register(ish_orni, vakansiya.ISH_ORNI)
    dp.message.register(tasdiqlash_answer, vakansiya.TASDIQLASH)
    dp.message.register(send_admin_answer, vakansiya.SEND_ADMIN)
    dp.message.register(make_admin, StepsForm.GET_ADMIN)      
    dp.message.register(send_post, StepsForm.GET_POST)
    dp.callback_query.register(del_admin, F.data.startswith("del_"))
      
    await bot.set_my_commands([
        BotCommand(command="/start", description="Botni ishga tushirish"),
        BotCommand(command="/vakansiya", description="ro'yxatdan o'tish"),
    ])

    await dp.start_polling(bot, polling_timeout=1)
run(main())
