# 8755425471:AAELmQuetmmHyqfh9LKPUD3970XPotPWkGo



from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

#=============================================================================

text1 = """🟢 اطلاعیه موجود شدن کانفیگ ویژه 🟢
(ظرفیت محدود)

لوکیشن:
- هلند 🇳🇱
- اتریش 🇦🇹

🐈‍⬛ مشخصات سرویس:

• حجم پایه: 1GB

📌 1 گیگابایت | ۲۹۰,۰۰۰ تومان

📌 2 گیگابایت | ۵۶۰,۰۰۰ تومان

(سود شما در این خرید ۲۰,۰۰۰ تومان)

📌 3 گیگابایت | ۸۱۰,۰۰۰ تومان

(سود شما در این خرید ۶۰,۰۰۰ تومان)

📌 5 گیگابایت | ۱,۳۰۰,۰۰۰ تومان

(سود شما در این خرید ۱۵۰,۰۰۰ تومان)

📌 10 گیگابایت | ۲,۵۰۰,۰۰۰ تومان

(سود شما در این خرید ۴۰۰,۰۰۰ تومان)

• بدون محدودیت کاربر و زمان 🔓⌛️

⚡ توجه: به صورت لینک ساب و با پنل شخصی برای شما ارسال میشود و میتوانید حجم خود را از همان لینک استعلام بگیرید، لینک داخلی است و بدون وی پی ان باید وارد آن شوید.

✅ ضمانت اتصال
در صورتی که پس از ارسال کانفیگ برای شما وصل نشود (که احتمال بسیار پایینی دارد)، امکان بازگشت کامل وجه وجود دارد.

🔥 برای خرید و دریافت کانفیگ

🩵 @Silentline_Support 🩵
"""

#===============================================================================
#===============================================================================
text2 = ""





#===============================================================================

TOKEN = "8755425471:AAEjHGvvqe6OmCLy0suDaHPsja8NX6jjR6s"


# تابع منوی اصلی
def main_menu():
    keyboard = [
        [InlineKeyboardButton("اطلاع از قیمت ها", callback_data="btn1")],
        [InlineKeyboardButton("ثبت سفارش", callback_data="btn2")],
        [InlineKeyboardButton("تهیه اکانت تست", callback_data="btn3")],
        [InlineKeyboardButton("ارتباط با ما", callback_data="btn4")],
    ]

    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "یک گزینه را انتخاب کنید:",
        reply_markup=main_menu()
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    # اطلاع از قیمت ها
    if query.data == "btn1":

        back_keyboard = [
            [InlineKeyboardButton("🔙 بازگشت", callback_data="back")]
        ]

        await query.edit_message_text(
            text1,
            reply_markup=InlineKeyboardMarkup(back_keyboard)
        )

    # ثبت سفارش
    elif query.data == "btn2":

        order_text = """
📋 لیست حجم ها

1GB — 290,000 تومان
2GB — 560,000 تومان
3GB — 810,000 تومان
5GB — 1,300,000 تومان
10GB — 2,500,000 تومان

حجم موردنظر را انتخاب کنید:
"""

        keyboard = [
            [InlineKeyboardButton("1GB", callback_data="1gb")],
            [InlineKeyboardButton("2GB", callback_data="2gb")],
            [InlineKeyboardButton("3GB", callback_data="3gb")],
            [InlineKeyboardButton("5GB", callback_data="5gb")],
            [InlineKeyboardButton("10GB", callback_data="10gb")],
            [InlineKeyboardButton("🔙 بازگشت", callback_data="back")],
        ]

        await query.edit_message_text(
            order_text,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # انتخاب حجم ها
    elif query.data == "1gb":
        order_text2 = "✅ شما پلن 1GB را انتخاب کردید.\nقیمت ۲۹۰,۰۰۰ تومان"

        keyboard2 = [
            [InlineKeyboardButton("تایید", callback_data="confirm_1GB")],
            [InlineKeyboardButton("بازگشت", callback_data="back")],
        ]

        await query.edit_message_text(
            order_text2,
            reply_markup=InlineKeyboardMarkup(keyboard2)
        )


    elif query.data == "2gb":

        order_text3 = "✅ شما پلن 2GB را انتخاب کردید.\nقیمت ۵۶۰,۰۰۰ تومان"

        keyboard3 = [
            [InlineKeyboardButton("تایید", callback_data="confirm_2GB")],
            [InlineKeyboardButton("بازگشت", callback_data="back")],
        ]

        await query.edit_message_text(
            order_text3,
            reply_markup=InlineKeyboardMarkup(keyboard3)
        )
    elif query.data == "3gb":

        order_text4 = "✅ شما پلن 3GB را انتخاب کردید.\nقیمت ۸۱۰,۰۰۰ تومان"

        keyboard4 = [
            [InlineKeyboardButton("تایید", callback_data="confirm_3GB")],
            [InlineKeyboardButton("بازگشت", callback_data="back")],
        ]

        await query.edit_message_text(
            order_text4,
            reply_markup=InlineKeyboardMarkup(keyboard4)
        )
    elif query.data == "5gb":

        order_text5 = "✅ شما پلن 5GB را انتخاب کردید.\nقیمت ۱,۳۰۰,۰۰۰ تومان"

        keyboard5 = [
            [InlineKeyboardButton("تایید", callback_data="confirm_5GB")],
            [InlineKeyboardButton("بازگشت", callback_data="back")],
        ]

        await query.edit_message_text(
            order_text5,
            reply_markup=InlineKeyboardMarkup(keyboard5)
        )
    elif query.data == "10gb":

        order_text6 = "✅ شما پلن 10GB را انتخاب کردید.\nقیمت ۲,۵۰۰,۰۰۰ تومان"

        keyboard6 = [
            [InlineKeyboardButton("تایید", callback_data="confirm_10GB")],
            [InlineKeyboardButton("بازگشت", callback_data="back")],
        ]

        await query.edit_message_text(
            order_text6,
            reply_markup=InlineKeyboardMarkup(keyboard6)
        )
    # ارتباط با ما

    elif query.data == "btn3":

        order_text7 = "کاربر محترم به دلیل حجم درخواست هاو محدودیت ترافیک سرور در حال حاظر امکان تست رایکان فراهم نمی باشد.\nهزینه اکانت تست (100MB) / 49000 تومان میباشد."
        keyboard7 = [
            [InlineKeyboardButton("تایید", callback_data="confirm_test")],
            [InlineKeyboardButton("بازگشت", callback_data="back")],
        ]

        await query.edit_message_text(
            order_text7,
            reply_markup=InlineKeyboardMarkup(keyboard7)
        )


    elif query.data == "confirm_test":
        order_text8 = "شما درحال تهیه اکانت تست (100MB) با هزینه 49000 تومان هستید."
        keyboard8 = [
            [InlineKeyboardButton("تایید (پرداخت)", callback_data="confirm_test")],
            [InlineKeyboardButton("بازگشت", callback_data="back")],
        ]

        await query.edit_message_text(
            order_text8,
            reply_markup=InlineKeyboardMarkup(keyboard8)
        )


    elif query.data == "btn4":

        await query.edit_message_text(
            "ارتباط با ما:\n@Silentline_Support",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 بازگشت", callback_data="back")]
            ])
        )

    # بازگشت
    elif query.data == "back":

        await query.edit_message_text(
            "یک گزینه را انتخاب کنید:",
            reply_markup=main_menu()
        )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("Bot Started...")
app.run_polling()