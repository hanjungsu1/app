# -*- coding: euc-kr -*-
import tkinter as tk

# 할 일을 추가하는 함수
def add_task():
    task = entry.get()  # 입력된 할 일 가져오기
    category = category_var.get()  # 선택된 카테고리 가져오기
    if task:  # 할 일이 비어 있지 않은 경우에만 추가
        task_with_category = f"{category}: {task}" if category else task  # 카테고리와 할 일을 함께 저장
        listbox.insert(tk.END, task_with_category)  # 리스트 상자에 항목 추가
        entry.delete(0, tk.END)  # 입력 상자 비우기

# 할 일을 삭제하는 함수
def delete_task():
    selected_task_index = listbox.curselection()  # 선택된 항목의 인덱스 가져오기
    if selected_task_index:  # 선택된 항목이 있을 경우에만 삭제
        listbox.delete(selected_task_index)  # 선택된 항목 삭제

# tkinter 윈도우 생성
window = tk.Tk()
window.title("간단한 To-Do 리스트 앱")

# 레이블 추가
label = tk.Label(window, text="할 일 목록")
label.pack()

# 리스트 상자 추가
listbox = tk.Listbox(window)
listbox.pack()

# 할 일 입력 상자 추가
entry = tk.Entry(window, width=30)
entry.pack()

# 카테고리 레이블 추가
category_label = tk.Label(window, text="카테고리:")
category_label.pack()

# 카테고리 옵션 추가
categories = ["업무", "개인", "운동", "기타"]
category_var = tk.StringVar(window)
category_var.set(categories[0])  # 기본 카테고리 설정
category_option = tk.OptionMenu(window, category_var, *categories)
category_option.pack()

# 버튼 추가
button = tk.Button(window, text="추가", command=add_task)
button.pack(side=tk.LEFT)

# 삭제 버튼 추가
delete_button = tk.Button(window, text="삭제", command=delete_task)
delete_button.pack(side=tk.RIGHT)

# 윈도우 실행
window.mainloop()
