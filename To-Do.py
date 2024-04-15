# -*- coding: euc-kr -*-
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# �� ���� �߰��ϴ� �Լ�
def add_task():
    task = entry.get()  # �Էµ� �� �� ��������
    category = category_var.get()  # ���õ� ī�װ� ��������
    repeat = repeat_var.get()  # �ݺ� �ֱ� ��������
    priority = priority_var.get()  # ���õ� �켱���� ��������
    deadline = deadline_entry.get()  # �Էµ� ������ ��������
    if task:  # �� ���� ��� ���� ���� ��쿡�� �߰�
        task_with_info = f"{category}: {task} ({priority})" if category else f"{task} ({priority})"  # ī�װ��� �켱���� �Բ� ����
        listbox.insert(tk.END, task_with_info)  # ����Ʈ ���ڿ� �׸� �߰�
        entry.delete(0, tk.END)  # �Է� ���� ����
        deadline_date = datetime.strptime(deadline, "%Y-%m-%d") if deadline else None  # ������ ���ڿ��� datetime ��ü�� ��ȯ
        if deadline_date and deadline_date < datetime.now():  # �������� ���� ��� ��� �޽��� ǥ��
            messagebox.showwarning("������ ���", "�������� �̹� �������ϴ�!")
        elif deadline_date and deadline_date.date() == datetime.now().date():  # ���� �������� ��� �˸� ǥ��
            messagebox.showinfo("������ �˸�", "���� �������� �ִ� �� ���� �ֽ��ϴ�!")

# �� ���� �����ϴ� �Լ�
def delete_task():
    selected_task_index = listbox.curselection()  # ���õ� �׸��� �ε��� ��������
    if selected_task_index:  # ���õ� �׸��� ���� ��쿡�� ����
        listbox.delete(selected_task_index)  # ���õ� �׸� ����

# tkinter ������ ����
window = tk.Tk()
window.title("������ To-Do ����Ʈ ��")

# ���̺� �߰�
label = tk.Label(window, text="�� �� ���")
label.pack()

# ����Ʈ ���� �߰�
listbox = tk.Listbox(window)
listbox.pack()

# �� �� �Է� ���� �߰�
entry = tk.Entry(window, width=30)
entry.pack()

# ī�װ� ���̺� �߰�
category_label = tk.Label(window, text="ī�װ�:")
category_label.pack()

# ī�װ� �ɼ� �߰�
categories = ["����", "����", "�", "��Ÿ"]
category_var = tk.StringVar(window)
category_var.set(categories[0])  # �⺻ ī�װ� ����
category_option = tk.OptionMenu(window, category_var, *categories)
category_option.pack()

# �ݺ� �ֱ� ���̺� �߰�
repeat_label = tk.Label(window, text="�ݺ� �ֱ�:")
repeat_label.pack()

# �ݺ� �ֱ� �ɼ� �߰�
repeat_options = ["����", "����", "�ſ�"]
repeat_var = tk.StringVar(window)
repeat_var.set(repeat_options[0])  # �⺻ �ݺ� �ֱ� ����
repeat_option = tk.OptionMenu(window, repeat_var, *repeat_options)
repeat_option.pack()

# �켱���� ���̺� �߰�
priority_label = tk.Label(window, text="�켱����:")
priority_label.pack()

# �켱���� �ɼ� �߰�
priorities = ["����", "����", "����"]
priority_var = tk.StringVar(window)
priority_var.set(priorities[1])  # �⺻ �켱���� ����
priority_option = tk.OptionMenu(window, priority_var, *priorities)
priority_option.pack()

# ������ ���̺� �߰�
deadline_label = tk.Label(window, text="������ (�ɼ�, YYYY-MM-DD ����):")
deadline_label.pack()

# ������ �Է� ���� �߰�
deadline_entry = tk.Entry(window, width=20)
deadline_entry.pack()

# �߰� ��ư �߰�
button = tk.Button(window, text="�߰�", command=add_task)
button.pack(side=tk.LEFT)

# ���� ��ư �߰�
delete_button = tk.Button(window, text="����", command=delete_task)
delete_button.pack(side=tk.RIGHT)

# ������ ����
window.mainloop()
