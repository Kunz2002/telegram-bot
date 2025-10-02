# # from telegram import Update
# # from telegram.ext import Application, CommandHandler, ContextTypes

# # TOKEN = "8470587261:AAFSLT4uWXd9iuC-r5wv1XwEHvv8L4qI-AQ"  # token bot của bạn

# # # /start
# # async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
# #     await update.message.reply_text("Nhập theo cú pháp: /nhap <TênNgườiDùng> <TàiKhoản> <SốNguyên>")

# # # /nhap
# # async def nhap(update: Update, context: ContextTypes.DEFAULT_TYPE):
# #     if len(context.args) < 3:
# #         await update.message.reply_text("Sai cú pháp! /nhap <TÊN NGƯỜI DÙNG> <TÊN TK> <MỆNH GIÁ TIỀN>")
# #         return
    
# #     # tên người dùng luôn in hoa
# #     ten_nguoi_dung = context.args[0].upper()
# #     tai_khoan = context.args[1]
# #     try:
# #         gia_tri = int(context.args[2])
# #     except ValueError:
# #         await update.message.reply_text("Giá trị phải là số nguyên!")
# #         return

# #     ket_qua = f"/W {tai_khoan} - OWS {ten_nguoi_dung} - {gia_tri} - 5D"
# #     await update.message.reply_text(ket_qua)

# # def main():
# #     app = Application.builder().token(TOKEN).build()
# #     app.add_handler(CommandHandler("start", start))
# #     app.add_handler(CommandHandler("nhap", nhap))
# #     app.run_polling()

# # if __name__ == "__main__":
# #     main()import sqlite3

import sqlite3
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8470587261:AAFSLT4uWXd9iuC-r5wv1XwEHvv8L4qI-AQ"
DB_NAME = "ketqua.db"

# Khởi tạo database và bảng nếu chưa có
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS nhap_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            thoi_gian TEXT,
            nguoi_dung TEXT,
            tai_khoan TEXT,
            gia_tri INTEGER,
            ket_qua TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Hàm lưu dữ liệu vào database
def save_to_db(nguoi_dung, tai_khoan, gia_tri, ket_qua):
    thoi_gian = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO nhap_data (thoi_gian, nguoi_dung, tai_khoan, gia_tri, ket_qua)
        VALUES (?, ?, ?, ?, ?)
    ''', (thoi_gian, nguoi_dung, tai_khoan, gia_tri, ket_qua))
    conn.commit()
    conn.close()

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Nhập theo cú pháp:\n/nhap <TênNgườiDùng> <TàiKhoản> <SốNguyên>"
    )

# /nhap
async def nhap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 3:
        await update.message.reply_text(
            "Sai cú pháp!\nVí dụ: /nhap Kunz hiha123 123"
        )
        return
    
    ten_nguoi_dung = context.args[0].upper()
    tai_khoan = context.args[1]
    
    try:
        gia_tri = int(context.args[2])
    except ValueError:
        await update.message.reply_text("❌ Giá trị phải là số nguyên!")
        return

    ket_qua = f"/W {tai_khoan} - OWS {ten_nguoi_dung} - {gia_tri} - 5D"
    await update.message.reply_text(ket_qua)

    # Lưu vào database
    save_to_db(ten_nguoi_dung, tai_khoan, gia_tri, ket_qua)

# Main
def main():
    init_db()  # Khởi tạo DB trước khi chạy bot
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("nhap", nhap))
    app.run_polling()

if __name__ == "__main__":
    main()
