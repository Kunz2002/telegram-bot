# from telegram import Update
# from telegram.ext import Application, CommandHandler, ContextTypes

# TOKEN = "8470587261:AAFSLT4uWXd9iuC-r5wv1XwEHvv8L4qI-AQ"  # token bot của bạn

# # /start
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Nhập theo cú pháp: /nhap <TênNgườiDùng> <TàiKhoản> <SốNguyên>")

# # /nhap
# async def nhap(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     if len(context.args) < 3:
#         await update.message.reply_text("Sai cú pháp! /nhap <TÊN NGƯỜI DÙNG> <TÊN TK> <MỆNH GIÁ TIỀN>")
#         return
    
#     # tên người dùng luôn in hoa
#     ten_nguoi_dung = context.args[0].upper()
#     tai_khoan = context.args[1]
#     try:
#         gia_tri = int(context.args[2])
#     except ValueError:
#         await update.message.reply_text("Giá trị phải là số nguyên!")
#         return

#     ket_qua = f"/W {tai_khoan} - OWS {ten_nguoi_dung} - {gia_tri} - 5D"
#     await update.message.reply_text(ket_qua)

# def main():
#     app = Application.builder().token(TOKEN).build()
#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CommandHandler("nhap", nhap))
#     app.run_polling()

# if __name__ == "__main__":
#     main()
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from openpyxl import Workbook, load_workbook
import os

TOKEN = "8470587261:AAFSLT4uWXd9iuC-r5wv1XwEHvv8L4qI-AQ"  # token bot của bạn
EXCEL_FILE = "data.xlsx"  # file Excel lưu dữ liệu

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Nhập theo cú pháp: /nhap <TênNgườiDùng> <TàiKhoản> <SốNguyên>")

# /nhap
async def nhap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 3:
        await update.message.reply_text("Sai cú pháp! /nhap <TÊN NGƯỜI DÙNG> <TÊN TK> <MỆNH GIÁ TIỀN>")
        return
    
    # tên người dùng luôn in hoa
    ten_nguoi_dung = context.args[0].upper()
    tai_khoan = context.args[1]
    try:
        gia_tri = int(context.args[2])
    except ValueError:
        await update.message.reply_text("Giá trị phải là số nguyên!")
        return

    ket_qua = f"/W {tai_khoan} - OWS {ten_nguoi_dung} - {gia_tri} - 5D"

    # Trả lời cho user
    await update.message.reply_text(ket_qua)

    # Lưu vào file Excel
    if not os.path.exists(EXCEL_FILE):
        # Nếu file chưa tồn tại thì tạo mới
        wb = Workbook()
        ws = wb.active
        ws.title = "LichSu"
        ws.append(["TaiKhoan", "NguoiDung", "GiaTri", "CauLenh"])  # header
        wb.save(EXCEL_FILE)

    # Mở file để ghi thêm
    wb = load_workbook(EXCEL_FILE)
    ws = wb.active
    ws.append([tai_khoan, ten_nguoi_dung, gia_tri, ket_qua])
    wb.save(EXCEL_FILE)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("nhap", nhap))
    app.run_polling()

if __name__ == "__main__":
    main()
