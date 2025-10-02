import sqlite3

DB_NAME = "ketqua.db"

conn = sqlite3.connect(DB_NAME)
c = conn.cursor()

# Tạo bảng nhap_data
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

print(f"Đã tạo file {DB_NAME}")
