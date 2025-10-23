import tkinter as tk  # 匯入 tkinter 用於建立圖形介面
import sqlite3         # 匯入 sqlite3（目前尚未使用，預留給後續資料庫功能）

# initial environment
root = tk.Tk()                   # 建立主視窗（root）
root.title('INTEGRATION')        # 設定視窗標題
root.geometry('300x350')         # 設定視窗初始大小（寬 x 高）

# new label and input
label_id = tk.Label(root, text='Student ID', font=('Arial', 12))  # Student ID 標籤
label_id.pack(pady=(15,5))                                         # pack 佈局並設定上下邊距

entry_id = tk.Entry(root, font=('Arial', 11), width=25)  # Student ID 輸入欄位
entry_id.pack(pady=(0,10))                              # pack 佈局，設定與下一元素間距

# 新增 Student Name 欄位
label_name = tk.Label(root, text='Student Name', font=('Arial', 12))  # Student Name 標籤
label_name.pack(pady=(10,5))                                          # pack 佈局並設定上下邊距
entry_name = tk.Entry(root, font=('Arial', 11), width=25)             # Student Name 輸入欄位
entry_name.pack()                                                     # pack 佈局

def print_student():
    student_id = entry_id.get()      # 取得 Student ID 輸入值
    student_name = entry_name.get()   # 取得 Student Name 輸入值
    print(f'Student ID: {student_id}, Student Name: {student_name}')  # 印出學生資訊


# 按鈕出來

botton_print = tk.Button(root, text='Print ', command=print_student)  # 印出學生資訊按鈕
botton_print.pack(pady=20)  # pack 佈局並設定上下邊距




#連資料庫

conn = sqlite3.connect('Student.db')  # 連接到 SQLite 資料庫（若無則建立）
cursor = conn.cursor()                  # 建立游標物件以執行 SQL 指

#
def create_student():
    student_id = entry_id.get()      # 取得 Student ID 輸入值
    student_name = entry_name.get().lower()  # 取得 Student Name 輸入值
    cursor.execute('INSERT INTO  DB_student (db_student_id, db_student_name) VALUES (?, ?)', (student_id, student_name))  # 插入學生資料
    conn.commit()  # 提交變更
    print('Student ID:{}. '.format(student_id))  # 印出確認訊息
    print('Student Name:{}. '.format(student_name))  # 印出確認訊息
    print('-'*30)  # 印出分隔線

          
button_create = tk.Button(root, text='Create ', command=create_student)  # 建立學生按鈕
button_create.pack(padx=30)  # pack 佈局

#incopleted
def overview_student():
    cursor.execute('''SELECT * FROM DB_student''')  # 查詢所有學生資料
    overview = cursor.fetchall()  # 取得所有查詢結果
    print(overview)  # 印出標題
button_overview = tk.Button(root, text='Overview ', command=overview_student)  # 檢視學生按鈕
button_overview.pack(pady=40)  # pack 佈局並設定上下邊距

root.mainloop()  # 進入主事件迴圈，等待使用者互動（此行必須放在程式最後）