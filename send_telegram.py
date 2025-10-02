import pandas as pd
from telegram import Bot
import asyncio

# -------------------- CẤU HÌNH --------------------
EXCEL_FILE = 'bc.xlsx'   # File Excel chứa dữ liệu
START_ROW = 3                # Bắt đầu từ D4 (Python index 3)
COLUMN_INDEX = 3             # Cột D trong Excel (Python index 3)
BOT_TOKEN = "8470587261:AAFSLT4uWXd9iuC-r5wv1XwEHvv8L4qI-AQ"
# ---------------------------------------------------

# 1. Đọc Excel (không dùng header)
df = pd.read_excel(EXCEL_FILE, header=None)

# 2. Khởi tạo bot
bot = Bot(token=BOT_TOKEN)

# 3. Hàm async lấy chat_id từ tin nhắn gần nhất (có message thật)
async def get_chat_id():
    updates = await bot.get_updates()
    messages = [u.message for u in updates if u.message is not None]
    if messages:
        return messages[-1].chat.id
    else:
        print("Bạn chưa nhắn /start với bot trên Telegram.")
        return None

# 4. Hàm async gửi tin nhắn từ D4 trở xuống
async def send_messages():
    chat_id = await get_chat_id()
    if not chat_id:
        return

    for row in df.iloc[START_ROW:, COLUMN_INDEX]:
        text = str(row)
        if text.strip():  # bỏ qua ô trống
            await bot.send_message(chat_id=chat_id, text=text)

    print("Đã gửi xong tất cả tin nhắn từ D4 trở xuống!")

# 5. Chạy async
asyncio.run(send_messages())
