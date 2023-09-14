
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token='BOT_TOKEN')
dp = Dispatcher(bot)



buttonTakeTest = InlineKeyboardButton(text=" Take Test", callback_data="Take Test")
buttonLearn = InlineKeyboardButton(text="Learn", callback_data="Learn")
buttonWebinars =InlineKeyboardButton(text="Webinars", callback_data="Webinars")
buttonDriveUpdates = InlineKeyboardButton(text="Drive Updates", callback_data="Drive Updates")
buttonVerbal = InlineKeyboardButton(text="Verbal", callback_data="Verbal")
buttonNonVerbal = InlineKeyboardButton(text="Non Verbal", callback_data="Non Verbal")
buttonAptitude = InlineKeyboardButton(text="Aptitude", callback_data="Aptitude")
buttonCertifiedCourses = InlineKeyboardButton(text="Certified Courses", callback_data="Certified Courses")
buttonEntrepreneurship = InlineKeyboardButton(text="Entrepreneurship", callback_data="Entrepreneurship")
buttonITjobs = InlineKeyboardButton(text="IT jobs", callback_data="IT jobs")
buttonInvesting= InlineKeyboardButton(text="Investing", callback_data="Investing")
buttonPersonalDevelopment = InlineKeyboardButton(text="Personal Development", callback_data="Personal Development")
buttonProfitorLoss= InlineKeyboardButton(text="Profit or Loss", callback_data="Profit or Loss")
buttonPercentage= InlineKeyboardButton(text="Percentage", callback_data="Percentage")
buttonNumberSeries= InlineKeyboardButton(text="Number Series", callback_data="Number Series")
buttonTimeandWork= InlineKeyboardButton(text="Time and Work", callback_data="Time and Work")
buttonSimpleInterest= InlineKeyboardButton(text="Simple Interest", callback_data="Simple Interest")
buttonCompoundInterest= InlineKeyboardButton(text="Compound Interest", callback_data="Compound Interest")
buttonAgeProblem= InlineKeyboardButton(text="Age Problem", callback_data="Age Problem")

buttonArticles= InlineKeyboardButton(text="Articles", callback_data="Articles")
buttonTenses= InlineKeyboardButton(text="Tenses", callback_data="Tenses")
buttonPhrases= InlineKeyboardButton(text="Phrases", callback_data="Phrases")
buttonErrorSpotting= InlineKeyboardButton(text="Error Spotting", callback_data="Error Spotting")
buttonAntonymsandSynonyms= InlineKeyboardButton(text="Antonyms and Synonyms", callback_data="Antonyms and Synonyms")
buttonSentenceRearrangement= InlineKeyboardButton(text="Sentence Rearrangement", callback_data="Sentence Rearrangement")

button1=KeyboardButton('/Articles')
button2=KeyboardButton('/Phrases')
button3=KeyboardButton('/Tenses')
button4=KeyboardButton('/Synonyms&Antonyms')
button5=KeyboardButton('/SentenceRearrangement')
button6=KeyboardButton('/ErrorSpotting')
buttonprofitorLoss1=KeyboardButton('/ProfitorLoss')
buttonAgeproblem1=KeyboardButton('/AgeProblem')
buttonNumberSeries1=KeyboardButton('/NumberSeries')
buttonSimpleInterest1=KeyboardButton('/SimpleInterest')
buttonCompoundInterest1=KeyboardButton('/CompoundInterest')
buttonTimeandWork1=KeyboardButton('/TimeandWork')
buttonPercentage1=KeyboardButton('/Percentage')



buttonPython= InlineKeyboardButton(text="Python", callback_data="Python")
buttonC= InlineKeyboardButton(text="C", callback_data="C")
buttonR= InlineKeyboardButton(text="R", callback_data="R")
buttonjava= InlineKeyboardButton(text="java", callback_data="java")
buttonUX= InlineKeyboardButton(text="UX", callback_data="UX")
buttonReverseEngineering= InlineKeyboardButton(text="Reverse Engineering", callback_data="Reverse Engineering")
buttonPenetrationTest= InlineKeyboardButton(text="Penetration Testing ", callback_data="Penetration Testing")
buttonInterviewEssential= InlineKeyboardButton(text="Interview Essential", callback_data="Interview Essential")

buttonTechnical= InlineKeyboardButton(text="Technical", callback_data="Technical")
buttonNonTechnical= InlineKeyboardButton(text="Non-Technical", callback_data="Non-Technical")
buttonProgramming= InlineKeyboardButton(text="Programming", callback_data="Programming")
buttonEthicalHacking= InlineKeyboardButton(text="Ethical Hacking", callback_data="Ethical Hacking")


buttonInterviewEssential= InlineKeyboardButton(text="Interview Essential", callback_data="Interview Essential")




keyboard_start = InlineKeyboardMarkup().add(buttonTakeTest).add(buttonLearn).add(buttonWebinars).add(buttonDriveUpdates)
keyboard_learn = InlineKeyboardMarkup().add(buttonVerbal).add(buttonAptitude).add(buttonCertifiedCourses)
keyboard_Webinars = InlineKeyboardMarkup().add(buttonEntrepreneurship).add(buttonITjobs).add(buttonInvesting).add(buttonPersonalDevelopment)
keyboard_Aptitude = InlineKeyboardMarkup().add(buttonProfitorLoss).add(buttonPercentage).add(buttonNumberSeries).add(buttonTimeandWork).add(buttonSimpleInterest).add(buttonCompoundInterest).add(buttonAgeProblem)
keyboard_Verbal = InlineKeyboardMarkup().add(buttonArticles).add(buttonTenses).add(buttonPhrases).add(buttonErrorSpotting).add(buttonAntonymsandSynonyms)
keyboard_CertifiedCourses = InlineKeyboardMarkup().add(buttonTechnical).add(buttonNonTechnical)
keyboard_Technical = InlineKeyboardMarkup().add(buttonProgramming).add(buttonEthicalHacking).add(buttonUX)
keyboard_NonTechnical = InlineKeyboardMarkup().add(buttonInterviewEssential)
keyboard_Programming = InlineKeyboardMarkup().add(buttonPython).add(buttonC).add(buttonR).add(buttonjava)
keyboard_EthicalHacking = InlineKeyboardMarkup().add(buttonPenetrationTest).add(buttonReverseEngineering)

keyboardAritcles=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(button1)
keyboardPhrases=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(button2)
keyboardTenses=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(button3)
keyboardSynonymsAntonyms=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(button4)
keyboardSentenceRearrangement=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(button5)
keyboardErrorSpotting=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(button6)
keyboardProfitorLoss=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(buttonprofitorLoss1)
keyboardAgeProblem=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(buttonAgeproblem1)
keyboardPercentage=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(buttonPercentage1)
keyboardTimeandWork=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(buttonTimeandWork1)
keyboardNumberSeries=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(buttonNumberSeries1)
keyboardSimpleInterest=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(buttonSimpleInterest1)
keyboardCompoundInterest=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(buttonCompoundInterest1)





@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply("Hello I am the bot for Placement Preparation!!! welcome to the crew", reply_markup=keyboard_start)

@dp.message_handler(commands=['info'])
async def welcome(message: types.Message):
    await message.reply("Hello !! We are the open community to provide the placement for free of cost")

@dp.message_handler(commands=['contact'])
async def welcome(message: types.Message):
    await message.reply("Your feed makes us to improve \n Kindly send your feed back to the below number \n 9952780807")

"""@dp.message_handler(commands=['video'])
async def welcome(message: types.Message):
        document_id = 'BQACAgUAAxkDAAIEkWRKvuxwd_3KT1qoww9x-bSacXdSAAJVCQACiIpYVsqx9BTPS-wjLwQ'
        await bot.send_document(message.chat.id,document=document_id)"""






@dp.callback_query_handler(text=["Learn"])
async def Courses(call: types.CallbackQuery):
    if call.data == "Learn":
        await call.message.answer("Happy learning journey", reply_markup=keyboard_learn)
    await call.answer()

@dp.callback_query_handler(text=["Webinars"])
async def Courses(call: types.CallbackQuery):
    if call.data == "Webinars":
        await call.message.answer("Grow with Growbinar", reply_markup=keyboard_Webinars)
    await call.answer()

@dp.callback_query_handler(text=["Drive Updates"])
async def Courses(call: types.CallbackQuery):
    if call.data == "Drive Updates":
        await call.message.answer("https://t.me/CseTest")
    await call.answer()



@dp.callback_query_handler(text=["Aptitude"])
async def Courses(call: types.CallbackQuery):
    if call.data == "Aptitude":
        await call.message.answer("Choose the topic to learn", reply_markup=keyboard_Aptitude)
    await call.answer()

@dp.callback_query_handler(text=["Verbal"])
async def Courses(call: types.CallbackQuery):
    if call.data == "Verbal":
        await call.message.answer("Choose the Varbal topic to learn", reply_markup=keyboard_Verbal)
    await call.answer()

@dp.callback_query_handler(text=["Certified Courses"])
async def Courses(call: types.CallbackQuery):
    if call.data == "Certified Courses":
        await call.message.answer("Choose the Course and get start with certified courses", reply_markup=keyboard_CertifiedCourses)
    await call.answer()


@dp.callback_query_handler(text=["Technical"])
async def Courses(call: types.CallbackQuery):
    if call.data == "Technical":
        await call.message.answer("Choose the topic and start improving you Technical skills",reply_markup=keyboard_Technical)
    await call.answer()

@dp.callback_query_handler(text=["Non-Technical"])
async def Courses(call: types.CallbackQuery):
    if call.data == "Non-Technical":
        await call.message.answer("Choose the topic and start improving you Technical skills",reply_markup=keyboard_NonTechnical)
    await call.answer()

@dp.callback_query_handler(text=["Programming"])
async def Courses(call: types.CallbackQuery):
    if call.data == "Programming":
        await call.message.answer("Choose the topic and start improving you Technical skills",reply_markup=keyboard_Programming)
    await call.answer()

@dp.callback_query_handler(text=["Python"])
async def Courses(call: types.CallbackQuery):
    if call.data == "Python":
        await call.message.answer("Happy  learning journey \n https://www.udemy.com/course/python-programming-beginner-to-advanced/?couponCode=FREEAPRIL124",)
    await call.answer()

@dp.callback_query_handler(text=["C"])
async def Courses(call: types.CallbackQuery):
    if call.data == "C":
        await call.message.answer("Happy  learning journey \n https://www.udemy.com/course/lets-learn-basic-c-programming-to-advance-data-structures/",)
    await call.answer()

@dp.callback_query_handler(text=["R"])
async def Courses(call: types.CallbackQuery):
    if call.data == "R":
        await call.message.answer("Happy  learning journey \n https://www.udemy.com/course/data-sonification-using-two-tone-convert-your-data-to-music/?couponCode=APRIL002",)
    await call.answer()

@dp.callback_query_handler(text=["java"])
async def Courses(call: types.CallbackQuery):
    if call.data == "java":
        await call.message.answer("Happy  learning journey \n https://www.udemy.com/course/java-from-scratch/")
    await call.answer()

@dp.callback_query_handler(text=["UX"])
async def Courses(call: types.CallbackQuery):
    if call.data == "UX":
        await call.message.answer("Happy  learning journey \n https://www.udemy.com/course/certificate-in-ux/")
    await call.answer()

@dp.callback_query_handler(text=["Ethical Hacking"])
async def Courses(call: types.CallbackQuery):
    if call.data == "Ethical Hacking":
        await call.message.answer("Choose the topic and start improving you Hacking skills",reply_markup=keyboard_EthicalHacking)
    await call.answer()

@dp.callback_query_handler(text=["Reverse Engineering"])
async def Courses(call: types.CallbackQuery):
    if call.data == "Reverse Engineering":
        await call.message.answer("Happy  learning journey \n https://www.udemy.com/course/reverse-engineering-visual-basic/?couponCode=APR26_FREE")
    await call.answer()

@dp.callback_query_handler(text=["Penetration Testing"])
async def Courses(call: types.CallbackQuery):
    if call.data == "Penetration Testing":
        await call.message.answer("Happy  learning journey \n https://www.udemy.com/course/networking-for-ethical-hacker-and-penetration-tester/")
    await call.answer()

@dp.callback_query_handler(text=["Interview Essential"])
async def Courses(call: types.CallbackQuery):
    if call.data == "Interview Essential":
        await call.message.answer("Happy  learning journey \n https://www.udemy.com/course/interview-essentials-master-your-interview-essentials-now/?couponCode=3879764267CA2C1E677D")
    await call.answer()

@dp.callback_query_handler(text=["Take Test"])
async def Courses(call: types.CallbackQuery):
    if call.data == "Take Test":
        await call.message.answer("Join the group to get more updates about the FAQ's \n https://t.me/+6OC6BsReQ7ExMDM1")
    await call.answer()


@dp.callback_query_handler(text=["Articles"])
async def Courses(call: types.CallbackQuery):
    if call.data == "Articles":
        await call.message.answer("Click the below button to receive the notes",reply_markup=keyboardAritcles)
    await call.answer()

@dp.callback_query_handler(text=["Phrases"])
async def Courses(call: types.CallbackQuery):
    if call.data == "Phrases":
        await call.message.answer("Click the below button to receive the notes",reply_markup=keyboardPhrases)
    await call.answer()

@dp.callback_query_handler(text=["Error Spotting"])
async def Courses(call: types.CallbackQuery):
    if call.data == "Error Spotting":
        await call.message.answer("Click the below button to receive the notes",reply_markup=keyboardErrorSpotting)
    await call.answer()

@dp.callback_query_handler(text=["Tenses"])
async def Courses(call: types.CallbackQuery):
    if call.data == "Tenses":
        await call.message.answer("Click the below button to receive the notes",reply_markup=keyboardTenses)
    await call.answer()

@dp.callback_query_handler(text=["Antonyms and Synonyms"])
async def Courses(call: types.CallbackQuery):
    if call.data == "Antonyms and Synonyms":
        await call.message.answer("Click the below button to receive the notes",reply_markup=keyboardSynonymsAntonyms)
    await call.answer()

@dp.callback_query_handler(text=["Sentance Rearrangement"])
async def Courses(call: types.CallbackQuery):
    if call.data == "Sentance Rearrangement":
        await call.message.answer("Click the below button to receive the notes",reply_markup=keyboardSentenceRearrangement)
    await call.answer()

@dp.callback_query_handler(text=["Profit or Loss"])
async def Courses(call: types.CallbackQuery):
    if call.data == "Profit or Loss":
        await call.message.answer("Click the below button to receive the notes",reply_markup=keyboardProfitorLoss)
    await call.answer()

@dp.callback_query_handler(text=["Age Problem"])
async def Courses(call: types.CallbackQuery):
    if call.data == "Age Problem":
        await call.message.answer("Click the below button to receive the notes",reply_markup=keyboardAgeProblem)
    await call.answer()

@dp.callback_query_handler(text=["Percentage"])
async def Courses(call: types.CallbackQuery):
    if call.data == "Percentage":
        await call.message.answer("Click the below button to receive the notes",reply_markup=keyboardPercentage)
    await call.answer()

@dp.callback_query_handler(text=["Number Series"])
async def Courses(call: types.CallbackQuery):
    if call.data == "Number Series":
        await call.message.answer("Click the below button to receive the notes",reply_markup=keyboardNumberSeries)
    await call.answer()
@dp.callback_query_handler(text=["Time and Work"])
async def Courses(call: types.CallbackQuery):
    if call.data == "Time and Work":
        await call.message.answer("Click the below button to receive the notes",reply_markup=keyboardTimeandWork)
    await call.answer()

@dp.callback_query_handler(text=["Simple Interest"])
async def Courses(call: types.CallbackQuery):
    if call.data == "Simple Interest":
        await call.message.answer("Click the below button to receive the notes",reply_markup=keyboardSimpleInterest)
    await call.answer()

@dp.callback_query_handler(text=["Compound Interest"])
async def Courses(call: types.CallbackQuery):
    if call.data == "Compound Interest":
        await call.message.answer("Click the below button to receive the notes",reply_markup=keyboardCompoundInterest)
    await call.answer()


@dp.callback_query_handler(text=["Non Verbal"])
async def Courses(call: types.CallbackQuery):
    if call.data == "Non Verbal":
        await call.message.answer("Click the interested topics to learn more about in",reply_markup=keyboardCompoundInterest)
    await call.answer()



@dp.message_handler(commands=['Articles'])
async def welcome(message: types.Message):
        document_id = 'BQACAgUAAxkDAAIEkWRKvuxwd_3KT1qoww9x-bSacXdSAAJVCQACiIpYVsqx9BTPS-wjLwQ'
        await bot.send_document(message.chat.id,document=document_id)

@dp.message_handler(commands=['Phrases'])
async def welcome(message: types.Message):
        document_id = 'BQACAgUAAxkDAAIEsGRKy3__RS1b--mK_6Q6zQ4-hliKAAJfCAACGN5ZVvw4XDkIOYNDLwQ'
        await bot.send_document(message.chat.id,document=document_id)

@dp.message_handler(commands=['ErrorSpotting'])
async def welcome(message: types.Message):
        document_id = 'BQACAgUAAxkDAAIE0WRK1NUelz4aIao8Kkmmbw_H4wuAAAJgCAACGN5ZVgm8Ej-yggdwLwQ'
        await bot.send_document(message.chat.id,document=document_id)

@dp.message_handler(commands=['Tenses'])
async def welcome(message: types.Message):
        document_id = 'BQACAgUAAxkDAAIE9WRK2fwKDu_mVkJ9UOG0KhgdyCHtAAJjCAACGN5ZVut8tsvkYTlsLwQ'
        await bot.send_document(message.chat.id,document=document_id)

@dp.message_handler(commands=['Synonyms&Antonyms'])
async def welcome(message: types.Message):
        document_id = 'BQACAgUAAxkDAAIE4WRK14hZy8DcGJaIrfynfL5gDt5rAAJhCAACGN5ZVs3X5iRxMXEBLwQ'
        await bot.send_document(message.chat.id,document=document_id)

@dp.message_handler(commands=['SentanceRearrangement'])
async def welcome(message: types.Message):
        document_id = 'BQACAgUAAxkDAAIE0WRK1NUelz4aIao8Kkmmbw_H4wuAAAJgCAACGN5ZVgm8Ej-yggdwLwQ'
        await bot.send_document(message.chat.id,document=document_id)

@dp.message_handler(commands=['ProfitorLoss'])
async def welcome(message: types.Message):
        document_id = 'BAACAgUAAxkDAAIFEGRLWSSk4D0p6Xrzg4lHveS3zqoiAALqCAACGN5ZVgP1BBHugWGULwQ'
        await bot.send_document(message.chat.id,document=document_id)


@dp.message_handler(commands=['AgeProblem'])
async def welcome(message: types.Message):
    document_id = 'BAACAgUAAxkDAAIFemRLuWepZKg4LjZmmMqpkgTlSiUDAALnBwACGN5hVmjxa2Rw0hOOLwQ'
    await bot.send_document(message.chat.id, document=document_id)

@dp.message_handler(commands=['Percentage'])
async def welcome(message: types.Message):
    document_id = 'BAACAgUAAxkDAAIFf2RLv3ej2B8zGA95qGoG4FL_mhKTAALwBwACGN5hVlfYrtk7s3ALLwQ'
    await bot.send_document(message.chat.id, document=document_id)

@dp.message_handler(commands=['NumberSeries'])
async def welcome(message: types.Message):
    document_id = 'BAACAgUAAxkDAAIFhGRLwny-C5dvlLR6g8X6u6xFQgbBAALyBwACGN5hVv7Hz1wRAcWVLwQ'
    await bot.send_document(message.chat.id, document=document_id)

@dp.message_handler(commands=['TimeandWork'])
async def welcome(message: types.Message):
    document_id = 'BAACAgUAAxkDAAIFjWRLxIA3wlSw_xB8234xalFogbVNAALzBwACGN5hVik7diiAP6RrLwQ'
    await bot.send_document(message.chat.id, document=document_id)

@dp.message_handler(commands=['SimpleInterest'])
async def welcome(message: types.Message):
    document_id = 'BAACAgUAAxkDAAIFlmRLyOyXV_SF58Xx5IikDTCTdkubAAL-BwACGN5hVoWZdrd2raTILwQ'
    await bot.send_document(message.chat.id, document=document_id)

@dp.message_handler(commands=['CompoundInterest'])
async def welcome(message: types.Message):
    document_id = 'BAACAgUAAxkDAAIFm2RLy0jYS6nS1ZgTY6KuJU3PmOqjAAILCAACGN5hVlgcrQGI-N3GLwQ'
    await bot.send_document(message.chat.id, document=document_id)




if name == 'main':
    executor.start_polling(dp, skip_updates=True)
