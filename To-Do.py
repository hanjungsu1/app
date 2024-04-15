# -*- coding: euc-kr -*-
import tkinter as tk

# �� ���� �߰��ϴ� �Լ�
def add_task():
    task = entry.get()  # �Էµ� �� �� ��������
    if task:  # �� ���� ��� ���� ���� ��쿡�� �߰�
        listbox.insert(tk.END, task)  # ����Ʈ ���ڿ� �׸� �߰�
        entry.delete(0, tk.END)  # �Է� ���� ����

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

# ��ư �߰�
button = tk.Button(window, text="�߰�", command=add_task)
button.pack(side=tk.LEFT)

# ���� ��ư �߰�
delete_button = tk.Button(window, text="����", command=delete_task)
delete_button.pack(side=tk.RIGHT)

# ������ ����
window.mainloop()
