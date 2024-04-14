import tkinter as tk

# tkinter 윈도우 생성
window = tk.Tk()
window.title("간단한 To-Do 리스트 앱")

# 레이블 추가
label = tk.Label(window, text="할 일 목록")
label.pack()

# 버튼 추가
button = tk.Button(window, text="추가")
button.pack()

# 윈도우 실행
window.mainloop()
