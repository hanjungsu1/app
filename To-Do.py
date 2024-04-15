# -*- coding: euc-kr -*-
import tkinter as tk

# �� ���� �߰��ϴ� �Լ�
def add_task():
    task = entry.get()  # �Էµ� �� �� ��������
    category = category_var.get()  # ���õ� ī�װ� ��������
    if task:  # �� ���� ��� ���� ���� ��쿡�� �߰�
        task_with_category = f"{category}: {task}" if category else task  # ī�װ��� �� ���� �Բ� ����
        listbox.insert(tk.END, task_with_category)  # ����Ʈ ���ڿ� �׸� �߰�
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

# ī�װ� ���̺� �߰�
category_label = tk.Label(window, text="ī�װ�:")
category_label.pack()

# ī�װ� �ɼ� �߰�
categories = ["����", "����", "�", "��Ÿ"]
category_var = tk.StringVar(window)
category_var.set(categories[0])  # �⺻ ī�װ� ����
category_option = tk.OptionMenu(window, category_var, *categories)
category_option.pack()

# ��ư �߰�
button = tk.Button(window, text="�߰�", command=add_task)
button.pack(side=tk.LEFT)

# ���� ��ư �߰�
delete_button = tk.Button(window, text="����", command=delete_task)
delete_button.pack(side=tk.RIGHT)

# ������ ����
window.mainloop()
