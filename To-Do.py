# -*- coding: euc-kr -*-
import tkinter as tk
from tkcalendar import Calendar
from tkinter import messagebox
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ������ ���� �Լ�
def select_deadline():
    def set_deadline():
        selected_date = cal.selection_get()  # ������ ��¥ ��������
        deadline_entry.delete(0, tk.END)  # ������ �Էµ� ��¥ �����
        deadline_entry.insert(0, selected_date.strftime("%Y-%m-%d"))  # ������ ��¥�� �Է� ���ڿ� �ֱ�
        top.destroy()  # Ķ���� â �ݱ�

    top = tk.Toplevel(window)  # ���ο� ������ ����
    cal = Calendar(top, selectmode="day", date_pattern="yyyy-mm-dd")  # �޷� ���� ����
    cal.pack()

    # Ȯ�� ��ư �߰�
    confirm_button = tk.Button(top, text="Ȯ��", command=set_deadline)
    confirm_button.pack()

# �� ���� �߰��ϴ� �Լ�
def add_task():
    task = entry.get()  # �Էµ� �� �� ��������
    category = category_var.get()  # ���õ� ī�װ� ��������
    repeat = repeat_var.get()  # �ݺ� �ֱ� ��������
    priority = priority_var.get()  # ���õ� �켱���� ��������
    deadline = deadline_entry.get()  # �Էµ� ������ ��������
    if task:  # �� ���� ��� ���� ���� ��쿡�� �߰�
        task_with_info = f"{category}: {task} ({priority})" if category else f"{task} ({priority})"  # ī�װ��� �켱���� �Բ� ����
        if deadline:  # �������� �Էµ� ��쿡�� �߰�
            task_with_info += f" - ������: {deadline}"  # �������� �Բ� ����
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

# �̸��� ���� �Լ�
def send_email(to_email, subject, body):
    from_email = "your_email@example.com"  # ������ �̸��� �ּ�
    password = "your_email_password"  # ������ �̸��� ��й�ȣ

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.example.com', 587)  # SMTP ���� ���� �Է�
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

# �� ���� �����ϴ� �Լ�
def share_task():
    selected_index = listbox.curselection()  # ���õ� �׸��� �ε��� ��������
    if selected_index:  # ���õ� �׸��� �ִ� ��쿡�� ����
        selected_task = listbox.get(selected_index)  # ���õ� �׸� ��������
        # ���⼭ �� ���� �����ϴ� �ڵ带 �ۼ��ϸ� �˴ϴ�.
        # �̸��Ϸ� �����ϴ� ����
        to_email = "recipient@example.com"  # ������ �̸��� �ּ�
        subject = "�� �� ����"
        body = f"�� ��: {selected_task}"
        send_email(to_email, subject, body)
        messagebox.showinfo("����", "�� ���� �̸��Ϸ� �����߽��ϴ�!")

# tkinter ������ ����
window = tk.Tk()
window.title("To-Do ����Ʈ ��")

# ���̺� �߰�
label = tk.Label(window, text="�� �� ���")
label.pack()

# ����Ʈ ���� �߰�
listbox = tk.Listbox(window, width=50)
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
deadline_label = tk.Label(window, text="������ (�ɼ�):")
deadline_label.pack()

# ������ �Է� ���� �߰�
deadline_entry = tk.Entry(window, width=20)
deadline_entry.pack()

# ������ ���� ��ư �߰�
select_deadline_button = tk.Button(window, text="������ ����", command=select_deadline)
select_deadline_button.pack()

# �߰� ��ư �߰�
button = tk.Button(window, text="�߰�", command=add_task)
button.pack(side=tk.LEFT)

# ���� ��ư �߰�
delete_button = tk.Button(window, text="����", command=delete_task)
delete_button.pack(side=tk.RIGHT)

# ���� ��ư �߰�
share_button = tk.Button(window, text="����", command=share_task)
share_button.pack()

# ������ ����
window.mainloop()
