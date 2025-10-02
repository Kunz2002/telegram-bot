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
# #     main()
# from telegram import Update
# from telegram.ext import Application, CommandHandler, ContextTypes
# import pandas as pd
# from openpyxl import Workbook, load_workbook
# import os
# from datetime import datetime

# TOKEN = "8470587261:AAFSLT4uWXd9iuC-r5wv1XwEHvv8L4qI-AQ"
# FILE_NAME = "ketqua.xlsx"

# # Hàm lưu vào Excel
# def save_to_excel(nguoi_dung, tai_khoan, gia_tri, ket_qua):
#     thoi_gian = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     if not os.path.exists(FILE_NAME):
#         # Tạo file mới nếu chưa có
#         wb = Workbook()
#         ws = wb.active
#         ws.append(["Thời gian", "Người dùng", "Tài khoản", "Giá trị", "Kết quả"])
#         wb.save(FILE_NAME)

#     # Ghi thêm dữ liệu
#     wb = load_workbook(FILE_NAME)
#     ws = wb.active
#     ws.append([thoi_gian, nguoi_dung, tai_khoan, gia_tri, ket_qua])
#     wb.save(FILE_NAME)

# # /start
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Nhập theo cú pháp: /nhap <TênNgườiDùng> <TàiKhoản> <SốNguyên>")

# # /nhap
# async def nhap(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     if len(context.args) < 3:
#         await update.message.reply_text("Sai cú pháp! /nhap <TÊN NGƯỜI DÙNG> <TÊN TK> <MỆNH GIÁ TIỀN>")
#         return
    
#     ten_nguoi_dung = context.args[0].upper()
#     tai_khoan = context.args[1]
#     try:
#         gia_tri = int(context.args[2])
#     except ValueError:
#         await update.message.reply_text("Giá trị phải là số nguyên!")
#         return

#     ket_qua = f"/W {tai_khoan} - OWS {ten_nguoi_dung} - {gia_tri} - 5D"
#     await update.message.reply_text(ket_qua)

#     # Lưu vào Excel
#     save_to_excel(ten_nguoi_dung, tai_khoan, gia_tri, ket_qua)

# def main():
#     app = Application.builder().token(TOKEN).build()
#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CommandHandler("nhap", nhap))
#     app.run_polling()

# if __name__ == "__main__":
#     main()
