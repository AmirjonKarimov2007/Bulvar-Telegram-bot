import sqlite3
from fpdf import FPDF
from aiogram import Bot, types
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.fsm.context import FSMContext
from keyboards.repl import *
from utils.states import *



db = sqlite3.connect('my_database.db')
cursor = db.cursor()


def find_admin(user_id):
    cursor.execute("SELECT * FROM admins WHERE id=?", (user_id,))
    return cursor.fetchone() is not None

async def call_filial(message: Message, state: FSMContext):
    await message.answer("\"Bulvar\" jamoasiga qo'shiling!")
    await message.answer("Filialni tanlang:", reply_markup=vakansiya_filial)
    await state.set_state(vakansiya.FILIAL)


async def filial_answer(message: Message, state: FSMContext):
    global filial
    filial = message.text
    if message.text == "📍Bulvar Saydana":
        photo_1_filial = types.input_file.FSInputFile("photos/photo_2024-04-16_16-58-57.jpg")
        await message.answer_photo(photo=photo_1_filial,caption="Nodira ko’chasi, Mo’ljal: 7-maktab oldi")
        
        
        await message.answer_location(longitude=71.667299, latitude=40.997604)

    elif message.text == "📍Bulvar Ohunboboyev":
        photo_2_filial = types.input_file.FSInputFile("photos/photo_2024-04-16_16-18-40.jpg")
        await message.answer_photo(photo=photo_2_filial ,caption="Ohunbabayev ko’chasi, Mo’ljal Obilbalnitsa ro’parasi")
        await message.answer_location(longitude=71.658942, latitude=41.003045)

    elif message.text == "📍Bulvar Go'zal":
        photo_3_filial = types.input_file.FSInputFile("photos/photo_2024-05-04_17-08-41.jpg")
        await message.answer_photo(photo=photo_3_filial ,caption=" Chamandon ko’chasi, Mo’ljal: Go’zal fayz")
        await message.answer_location(longitude=71.660451, latitude=41.021323)

    await message.answer("💼 Sizni qiziqtirgan lavozimni tanlang:", reply_markup=filial_buttons)
    await state.set_state(vakansiya.JOB)


async def job_answer(message: Message, state: FSMContext):
    global job
    job = message.text
   
    await message.answer("Jinsni tanlang:", reply_markup=job_buttons)
    await state.set_state(vakansiya.JINS)


async def jins_answer(message: Message, state: FSMContext):
        global jins 
        jins = message.text
        await message.answer("F.I.O ingizni kiriting \nMasalan: (Иванов Иван Иванович):", reply_markup=answer_buttons)
        await state.set_state(vakansiya.FIO)


async def fio_answer(message: Message, state: FSMContext):
        if " " in message.text:
            global fio
            fio = message.text
            await message.answer("Tug'ilgan yilingizni kiriting\nMasalan: 1999.12.31:", reply_markup=answer_buttons)
            await state.set_state(vakansiya.BIRTHDAY)
        else:
            await message.answer("F.I.O ni to'liq kiriting!")


async def birthday_answer(message: Message, state: FSMContext):
     if "." in message.text or "," in message.text or " " in message.text: 
          if len(message.text) == 10:
            global birthday
            birthday = message.text
            await message.answer("🏠 Yashash manzili (Tuman, ko'cha/kvartal, uy, xonadon):", reply_markup=answer_buttons)
            await state.set_state(vakansiya.ADRES) 
          else:
            await message.answer("Tug'ilgan yili ni to'liq kiriting!")
     else:
         await message.answer("Tug'ilgan yili ni to'liq kiriting!: \n (. , probellardan foydalaning)")


async def adres_answer(message: Message, state: FSMContext):
        global adres
        adres = message.text
        await message.answer("📱 O'z telefon raqamingizni yuboring! (masalan: +998901234567)!", reply_markup=answer_buttons)
        await state.set_state(vakansiya.VERIFIY)

   
async def verifiy_answer(message: Message, state: FSMContext):
    if message.text != "+998901234567" and len(message.text) == 13 and message.text[1:].isdigit() and message.text.startswith("+998"):
        global verifiy
        verifiy = message.text
        await message.answer("Ishga kuniga qancha vaqt ajrata olasiz?:",reply_markup=grafik_buttons)
        await state.set_state(vakansiya.VERIFIY_Vaksina)
    else:
            await message.answer("To'g'ri raqam yuboring!\nEslatma: +998 bilan boshlanishi shart‼️")


async def vaksina_answer(message: Message, state: FSMContext):
        global vaksina
        vaksina = message.text
        await message.answer("Nogironligingiz bormi ?",reply_markup=reply_buttons)
        await state.set_state(vakansiya.DISABILITY)


async def disability_answer(message: Message, state: FSMContext):
        global disability
        disability = message.text
        await message.answer("Hozir studentmisiz",reply_markup=reply_buttons)
        await state.set_state(vakansiya.VERIFIY_STUDENT)


async def student_answer(message: Message, state: FSMContext):
        global student
        student = message.text

        await message.answer("Rus tilini qay darajada bilasiz:",reply_markup=language_buttons)
        await state.set_state(vakansiya.LANGUAGE_RU)


async def language_answer(message: Message, state: FSMContext):
        global language_ru
        language_ru = message.text
        await message.answer("O'zbek tilini qay darajada bilasiz:",reply_markup=language_buttons)
        await state.set_state(vakansiya.LANGUAGE_UZ)


async def language_answer_uz(message: Message, state: FSMContext): 
        global language_uz
        language_uz = message.text
       
        await message.answer("💵 Kutilayotgan oylik maos:", reply_markup=maosh_buttons)
        await state.set_state(vakansiya.MAOSH)


async def maosh_answer(message: Message, state: FSMContext):
        global maosh
        maosh = message.text
        await message.answer("Rasmingizni yuboring:", reply_markup=answer_buttons)
        await state.set_state(vakansiya.SELF)


async def self_answer(message: Message, state: FSMContext, bot: Bot):
        if message.photo:
            global photo1
        
            photo1 = message.photo[-1].file_id
            file_profile = await bot.get_file(message.photo[-1].file_id)
            await image_saver(message, bot)
            await message.answer("Sizga Qaysi grafikda ishlash qulay?:", reply_markup=ish_vaqti_buttons)
            await state.set_state(vakansiya.ISH_VAQTI)
        else:
            await message.answer("Siz rasm yubormadingiz")


async def ish_vaqti_answer(message: Message, state: FSMContext):
        global ish_vaqti
        ish_vaqti = message.text
        await message.answer("❓ Bo'sh ish o'rni haqida qayerdan eshitdingiz?", reply_markup=ish_orni_buttons)
        await state.set_state(vakansiya.ISH_ORNI)


async def ish_orni(message: Message, state: FSMContext):
        global ish_ornii
        ish_ornii = message.text
        
        await message.answer("Shaxsiy ma'lumotlaringizni qayta ishlashga rozilik bildirasizmi?", reply_markup=tasdiq_buttons)
        await state.set_state(vakansiya.TASDIQLASH)
  

async def tasdiqlash_answer(message: Message, state: FSMContext):
        global tasdiq
        tasdiq = message.text
        pdf_maker()
        await message.answer_photo(photo=photo1, caption=f"""
Filial: {filial}
💼Bo'sh o'rin: {job}
jins: {jins}
👤 Toʻliq ismi: {fio}
📅 Tug'ilgan sana: {birthday}
Manzil: {adres}
📱 Aloqa uchun shaxs: {verifiy}
Ajratilan vaqt: {vaksina}
nogironlik: {disability}
Talaba: {student}
Trening shakli: {ish_vaqti}
🗣 Rus tili darajasi?: {language_ru}
🗣O'zbek tili darajasi: {language_uz}
Ish haqi: {maosh}
Grafik: {ish_vaqti}
Manbalar: {ish_ornii}
Shaxsiy ma'lumotlar: {tasdiq}.""")
        await message.answer("✅Siz barcha ma'lumotlar to'g'ri to'ldirilganligini tasdiqlaysizmi?", reply_markup=send_admin_buttons)

        await state.set_state(vakansiya.SEND_ADMIN)
        anketa_pdf = types.input_file.FSInputFile("anketa_pdf.pdf")
        await message.answer_document(document=anketa_pdf)

async def send_admin_answer(message: Message, state: FSMContext, bot: Bot):
        if message.text == "Yuborish":
                await message.answer("Ma'lumotlar yuborildi!")
                photo = types.input_file.FSInputFile('photos/logo.jpg')
                await message.answer_photo(photo=photo, reply_markup=menu_buttons)
                print(filial)
                await bot.send_photo(chat_id="@vakansiya_private_channel", photo=photo1, caption=f"""
Filial: {filial}
💼Bo'sh o'rin: {job}
jins: {jins}
👤 Toʻliq ismi: {fio}
📅 Tug'ilgan sana: {birthday}
Manzil: {adres}
📱 Aloqa uchun shaxs: {verifiy}
Ajratilgan vaqt: {vaksina}
nogironlik: {disability}
Talaba: {student}
🗣 Rus tili darajasi?: {language_ru}
🗣O'zbek tili darajasi: {language_uz}
Ish haqi: {maosh}
Grafik: {ish_vaqti}
Manbalar: {ish_ornii}
Shaxsiy ma'lumotlar: {tasdiq}.
bog'lanish uchun: {message.from_user.mention_html("User")}""", parse_mode="HTML")
                    
                anketa_pdf = types.input_file.FSInputFile("anketa_pdf.pdf")
                    
                await bot.send_document(chat_id="@vakansiya_private_channel", document=anketa_pdf)
                    
                    
                await state.clear()

def safe_text(text):
    try:
        return text.encode('latin-1', 'replace').decode('latin-1')
    except UnicodeEncodeError:
        return text.encode('latin-1', 'ignore').decode('latin-1')

def pdf_maker():
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    # Sarlavha
    pdf.set_font("Arial", size=30, style="B")
    pdf.cell(200, 10, txt=safe_text("Anketa"), ln=True, align='C')

    # Sarlavha ramka
    pdf.set_draw_color(0, 0, 0)
    pdf.rect(30, 30, 150, 40)

    # Ramka
    pdf.set_draw_color(0, 255, 255)
    pdf.rect(30, 100, 150, 85)

    # Yarim ramka
    pdf.set_draw_color(0, 255, 255)
    pdf.rect(30, 100, 75, 85)

    # Savol-javob ramka
    pdf.set_draw_color(0, 255, 255)
    pdf.rect(30, 100, 150, 10)

    # Ism
    pdf.set_xy(32, 32)
    pdf.set_font("Arial", size=16)
    pdf.cell(0, 10, safe_text(fio), 0, 1, 'L')

    # Ish turi
    pdf.set_xy(32, 42)
    pdf.cell(0, 10, safe_text(job), 0, 1, 'L')

    # Telefon raqam
    pdf.set_xy(32, 52)
    pdf.cell(0, 10, safe_text(f"Telefon raqam: {verifiy}"), 0, 1, 'L')

    # Profil rasmi
    pdf.image(f"profile.jpg", 142, 33, 30, 30)

    # Savolga javob
    pdf.set_xy(30, 80)
    pdf.set_font("Arial", size=30, style="B")
    pdf.cell(200, 10, safe_text("Savollarga javoblar"))

    # Savol
    pdf.set_xy(59, 100)
    pdf.set_font("Arial", size=11)
    pdf.cell(0, 10, safe_text("Savollar"))

    # Javob
    pdf.set_xy(135, 100)
    pdf.cell(0, 10, safe_text("Javoblar"))

    # Shahar
    pdf.set_xy(34, 110)
    pdf.cell(0, 10, safe_text("Shahar"))

    # Filial
    pdf.set_xy(34, 115)
    pdf.cell(0, 10, safe_text("Filial"))

    # Jins
    pdf.set_xy(34, 120)
    pdf.cell(0, 10, safe_text("Jins"))

    # Tug'ilgan kun
    pdf.set_xy(34, 125)
    pdf.cell(0, 10, safe_text("Tug'ilgan kun"))

    # Manzil
    pdf.set_xy(34, 130)
    pdf.cell(0, 10, safe_text("Manzil"))

    # Vaksina
    pdf.set_xy(34, 135)
    pdf.cell(0, 10, safe_text("Ishga ajratilgan vaqt"))

    # Noogironlik
    pdf.set_xy(34, 140)
    pdf.cell(0, 10, safe_text("Noogironlik"))

    # Talaba
    pdf.set_xy(34, 145)
    pdf.cell(0, 10, safe_text("Talaba"))

    # Ishlash vaqti
    pdf.set_xy(34, 150)
    pdf.cell(0, 10, safe_text("Grafik turi"))

    # Rus tili bilish darajasi
    pdf.set_xy(34, 155)
    pdf.cell(0, 10, safe_text("Rus tili bilish darajasi"))

    # O'zbek tili bilish darajasi
    pdf.set_xy(34, 160)
    pdf.cell(0, 10, safe_text("O'zbek tili bilish darajasi"))

    # Oylik maosh
    pdf.set_xy(34, 165)
    pdf.cell(0, 10, safe_text("Oylik maosh"))

    # Ish joyini eshitgan joyi
    pdf.set_xy(34, 170)
    pdf.cell(0, 10, safe_text("Ish joyini eshitgan joyi"))

    # Shaxsiy ma'lumotlarni qayta ishlash
    pdf.set_xy(34, 175)
    pdf.cell(0, 10, safe_text("Shaxsiy ma'lumotlarni qayta ishlash"))

    # Shahar qiymati
    pdf.set_xy(110, 110)
    pdf.cell(0, 10, safe_text("Namangan"))

    # Filial qiymati
    pdf.set_xy(110, 115)
    pdf.cell(0, 10, safe_text(filial[1:]))

    # Jins qiymati
    pdf.set_xy(110, 120)
    pdf.cell(0, 10, safe_text(jins[1:]))

    # Tug'ilgan kun qiymati
    pdf.set_xy(110, 125)
    pdf.cell(0, 10, safe_text(birthday))

    # Manzil qiymati
    pdf.set_xy(110, 130)
    pdf.cell(0, 10, safe_text(adres))

    # Vaksina qiymati
    pdf.set_xy(110, 135)
    pdf.cell(0, 10, safe_text(vaksina))

    # Noogironlik qiymati
    pdf.set_xy(110, 140)
    pdf.cell(0, 10, safe_text(disability[1:]))

    # Talaba qiymati
    pdf.set_xy(110, 145)
    pdf.cell(0, 10, safe_text(student[1:]))

    # Ishlash vaqti qiymati
    pdf.set_xy(110, 150)
    pdf.cell(0, 10, safe_text(ish_vaqti))

    # Rus tili bilish darajasi qiymati
    pdf.set_xy(110, 155)
    pdf.cell(0, 10, safe_text(language_ru))

    # O'zbek tili bilish darajasi qiymati
    pdf.set_xy(110, 160)
    pdf.cell(0, 10, safe_text(language_uz))

    # Oylik maosh qiymati
    pdf.set_xy(110, 165)
    pdf.cell(0, 10, safe_text(maosh[1:]))

    # Ish joyini eshitgan joyi qiymati
    pdf.set_xy(110, 170)
    pdf.cell(0, 10, safe_text(ish_ornii))

    # Shaxsiy ma'lumotlarni qayta ishlash qiymati
    pdf.set_xy(110, 175)
    pdf.cell(0, 10, safe_text(tasdiq[1:]))

    # PDFni saqlash
    pdf.output("anketa_pdf.pdf")

async def image_saver(message: Message, bot: Bot):
    global change_fio
    change_fio = fio.replace(" ", "_")
    photo = message.photo[-1].file_id
    file_path = await bot.get_file(photo)
    file_path = file_path.file_path
    downloaded_file = await bot.download_file(file_path)
    with open(f'profile.jpg', 'wb') as new_file:
        new_file.write(downloaded_file.read())
