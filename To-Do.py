# -*- coding: euc-kr -*-
import tkinter as tk
from tkcalendar import Calendar
from tkinter import messagebox
from datetime import datetime

# 마감일 선택 함수
def select_deadline():
    def set_deadline():
        selected_date = cal.selection_get()  # 선택한 날짜 가져오기
        deadline_entry.delete(0, tk.END)  # 이전에 입력된 날짜 지우기
        deadline_entry.insert(0, selected_date.strftime("%Y-%m-%d"))  # 선택한 날짜를 입력 상자에 넣기
        top.destroy()  # 캘린더 창 닫기

    top = tk.Toplevel(window)  # 새로운 윈도우 생성
    cal = Calendar(top, selectmode="day", date_pattern="yyyy-mm-dd")  # 달력 위젯 생성
    cal.pack()

    # 확인 버튼 추가
    confirm_button = tk.Button(top, text="확인", command=set_deadline)
    confirm_button.pack()

# 할 일을 추가하는 함수
def add_task():
    task = entry.get()  # 입력된 할 일 가져오기
    category = category_var.get()  # 선택된 카테고리 가져오기
    repeat = repeat_var.get()  # 반복 주기 가져오기
    priority = priority_var.get()  # 선택된 우선순위 가져오기
    deadline = deadline_entry.get()  # 입력된 마감일 가져오기
    if task:  # 할 일이 비어 있지 않은 경우에만 추가
        task_with_info = f"{category}: {task} ({priority})" if category else f"{task} ({priority})"  # 카테고리와 우선순위 함께 저장
        listbox.insert(tk.END, task_with_info)  # 리스트 상자에 항목 추가
        entry.delete(0, tk.END)  # 입력 상자 비우기
        deadline_date = datetime.strptime(deadline, "%Y-%m-%d") if deadline else None  # 마감일 문자열을 datetime 객체로 변환
        if deadline_date and deadline_date < datetime.now():  # 마감일이 지난 경우 경고 메시지 표시
            messagebox.showwarning("마감일 경고", "마감일이 이미 지났습니다!")
        elif deadline_date and deadline_date.date() == datetime.now().date():  # 오늘 마감일인 경우 알림 표시
            messagebox.showinfo("마감일 알림", "오늘 마감일이 있는 할 일이 있습니다!")

# 할 일을 삭제하는 함수
def delete_task():
    selected_task_index = listbox.curselection()  # 선택된 항목의 인덱스 가져오기
    if selected_task_index:  # 선택된 항목이 있을 경우에만 삭제
        listbox.delete(selected_task_index)  # 선택된 항목 삭제

# tkinter 윈도우 생성
window = tk.Tk()
window.title("To-Do 리스트 앱")

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

# 반복 주기 레이블 추가
repeat_label = tk.Label(window, text="반복 주기:")
repeat_label.pack()

# 반복 주기 옵션 추가
repeat_options = ["매일", "매주", "매월"]
repeat_var = tk.StringVar(window)
repeat_var.set(repeat_options[0])  # 기본 반복 주기 설정
repeat_option = tk.OptionMenu(window, repeat_var, *repeat_options)
repeat_option.pack()

# 우선순위 레이블 추가
priority_label = tk.Label(window, text="우선순위:")
priority_label.pack()

# 우선순위 옵션 추가
priorities = ["낮음", "보통", "높음"]
priority_var = tk.StringVar(window)
priority_var.set(priorities[1])  # 기본 우선순위 설정
priority_option = tk.OptionMenu(window, priority_var, *priorities)
priority_option.pack()

# 마감일 레이블 추가
deadline_label = tk.Label(window, text="마감일 (옵션):")
deadline_label.pack()

# 마감일 입력 상자 추가
deadline_entry = tk.Entry(window, width=20)
deadline_entry.pack()

# 마감일 선택 버튼 추가
select_deadline_button = tk.Button(window, text="마감일 선택", command=select_deadline)
select_deadline_button.pack()

# 추가 버튼 추가
button = tk.Button(window, text="추가", command=add_task)
button.pack(side=tk.LEFT)

# 삭제 버튼 추가
delete_button = tk.Button(window, text="삭제", command=delete_task)
delete_button.pack(side=tk.RIGHT)

# 윈도우 실행
window.mainloop()
