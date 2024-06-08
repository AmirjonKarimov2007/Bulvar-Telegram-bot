from aiogram.fsm.state import State, StatesGroup\

class vakansiya(StatesGroup):
    FILIAL = State()
    JOB = State()
    JINS = State()
    FIO = State()
    BIRTHDAY = State()  
    ADRES = State() 
    VERIFIY = State()
    VERIFIY_Vaksina = State()
    DISABILITY = State()
    VERIFIY_STUDENT = State()
    LANGUAGE_RU = State()
    LANGUAGE_UZ = State()
    MAOSH = State()
    SELF = State()
    ISH_ORNI = State()
    TASDIQLASH = State()
    SEND_ADMIN = State() 
    ISH_VAQTI = State()

class StepsForm(StatesGroup):
    GET_POST = State()
    GET_ADMIN = State()
