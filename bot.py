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
import os
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from openpyxl import Workbook, load_workbook

TOKEN = "8470587261:AAFSLT4uWXd9iuC-r5wv1XwEHvv8L4qI-AQ"
FILE_NAME = "ketqua.xlsx"

# Hàm lưu vào Excel
def save_to_excel(nguoi_dung, tai_khoan, gia_tri, ket_qua):
    thoi_gian = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Nếu file chưa tồn tại -> tạo mới với header
    if not os.path.exists(FILE_NAME):
        wb = Workbook()
        ws = wb.active
        ws.title = "Nhập dữ liệu"
        ws.append(["Thời gian", "Người dùng", "Tài khoản", "Giá trị", "Kết quả"])
        wb.save(FILE_NAME)

    # Ghi thêm dữ liệu mới
    wb = load_workbook(FILE_NAME)
    ws = wb.active
    ws.append([thoi_gian, nguoi_dung, tai_khoan, gia_tri, ket_qua])
    wb.save(FILE_NAME)

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Chào bạn! Nhập theo cú pháp:\n/nhap <TênNgườiDùng> <TàiKhoản> <SốNguyên>"
    )

# /nhap
async def nhap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 3:
        await update.message.reply_text(
            "❌ Sai cú pháp!\nVí dụ: /nhap Kunz hiha123 123"
        )
        return
    
    ten_nguoi_dung = context.args[0].upper()  # In hoa
    tai_khoan = context.args[1]

    try:
        gia_tri = int(context.args[2])
    except ValueError:
        await update.message.reply_text("❌ Giá trị phải là số nguyên!")
        return

    ket_qua = f"/W {tai_khoan} - OWS {ten_nguoi_dung} - {gia_tri} - 5D"

    # Trả lại tin nhắn vừa nhập
    tin_nhan_nhap = (
        f"Bạn vừa nhập:\n"
        f"👤 Tên: {ten_nguoi_dung}\n"
        f"💳 Tài khoản: {tai_khoan}\n"
        f"💰 Giá trị: {gia_tri}\n"
        f"📄 Kết quả: {ket_qua}"
    )
    await update.message.reply_text(tin_nhan_nhap)

    # Lưu vào Excel
    save_to_excel(ten_nguoi_dung, tai_khoan, gia_tri, ket_qua)

    # Thông báo lưu thành công
    await update.message.reply_text("✅ Đã lưu thành công vào ketqua.xlsx!")

# Main
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("nhap", nhap))
    app.run_polling()

if __name__ == "__main__":
    main()
