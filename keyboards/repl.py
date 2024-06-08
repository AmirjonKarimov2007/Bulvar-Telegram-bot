from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_panel = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Foydalanuvchilarga post jo'natish 📮")
    ],
 
    [
        KeyboardButton(text="🙍‍♂️ Admin qo'shish ➕"),
        KeyboardButton(text="🙍‍♂️ Admin o'chirish ❌")
    ],
    
], resize_keyboard=True)

menu_buttons = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="🏢Kompaniya haqida")
    ],
    [
        KeyboardButton(text="🖋Vakansiya")
    ]
],resize_keyboard=True,)

vakansiya_filial = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="📍Bulvar Ohunboboyev")
    ],
    [
        KeyboardButton(text="📍Bulvar Saydana"),
        KeyboardButton(text="📍Bulvar Go'zal")
    ],
    [
        KeyboardButton(text="❌Bekor qilish❌")
    ]
], resize_keyboard=True,)

filial_buttons = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Oshxona ishchisi")
    ],
    [
        KeyboardButton(text="Zal ishchisi"),
        KeyboardButton(text="Bar va Muzqaymoq")
    ],
    [
        KeyboardButton(text="❌Bekor qilish❌")
    ]
], resize_keyboard=True,)

job_buttons = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="👨Erkak"),
        KeyboardButton(text="👩‍🦰Ayol")
    ],
    [
        KeyboardButton(text="❌Bekor qilish❌")
    ]
], resize_keyboard=True,)

answer_buttons = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="❌Bekor qilish❌")
    ]
], resize_keyboard=True,)



reply_buttons = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="✅Ha"),
        KeyboardButton(text="❌Yoq")
    ],
    [
        KeyboardButton(text="❌Bekor qilish❌")
    ]
], resize_keyboard=True,)

language_buttons = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Mukammal"),
        KeyboardButton(text="O'rtacha")
    ],
    [
        KeyboardButton(text="Boshlang'ich"),
        KeyboardButton(text="Umuman")
    ],
    [
        KeyboardButton(text="❌Bekor qilish❌")
    ]
], resize_keyboard=True,)

maosh_buttons = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="💵1,5-2 million"),
        KeyboardButton(text="💵2-3 million"),
    ],
    [
        KeyboardButton(text="💵3-4 million"),
        KeyboardButton(text="💵5 million va ko'proq")
    ],
    [
        KeyboardButton(text="❌Bekor qilish❌")
    ]
], resize_keyboard=True)

ish_orni_buttons = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Telegram bot"),
        KeyboardButton(text="Ijtimoiy tarmoqlar")
    ],
    [
        KeyboardButton(text="Filiallardagi reklamalar"),
        KeyboardButton(text="Telegram kanallar")
    ],
    [
        KeyboardButton(text="Ish saytlari"),
        KeyboardButton(text="IshLink_uz")
    ],
    [
        KeyboardButton(text="Tashqi reklama"),
        KeyboardButton(text="Cheklardagi e'lonlar")
    ],
    [
        KeyboardButton(text="Do'stlar orqali"),
        KeyboardButton(text='\"Do\'stingli olib kel\" dasturi')
    ],
    [
        KeyboardButton(text="Ярмарка вакансий")
    ],
    [
        KeyboardButton(text="")
    ]
], resize_keyboard=True)

tasdiq_buttons = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="✅Roziman"), KeyboardButton(text="❌Bekor qilish❌")
    ]
], resize_keyboard=True)

send_admin_buttons = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Yuborish")
    ],
    [
        KeyboardButton(text="❌Bekor qilish❌")
    ]
], resize_keyboard=True)

ish_vaqti_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kunduzgi: 9:00 dan 17:00")
            
        ],
        [
            KeyboardButton(text="Kechki 17:00 dan 01:00")
        ],
        [
            KeyboardButton(text="❌Bekor qilish❌")
        ]
    ],
    resize_keyboard=True
)

grafik_buttons = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="8 soat"),
        KeyboardButton(text="12 soat")
    ],
    [
        KeyboardButton(text="❌Bekor qilish❌")
    ]
], resize_keyboard=True)
