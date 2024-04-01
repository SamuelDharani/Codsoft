import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
        update_list_colors()

def delete_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
        update_list_colors()
    except IndexError:
        pass

def update_list_colors():
    for i in range(listbox_tasks.size()):
        if i % 2 == 0:
            listbox_tasks.itemconfig(i, bg='#f0f0f0', fg='#333333')
        else:
            listbox_tasks.itemconfig(i, bg='#e0e0e0', fg='#333333')

def confirm_delete():
    if listbox_tasks.curselection():
        response = messagebox.askyesno("Confirm", "Task will be deleted permanently?")
        if response:
            delete_task()

root = tk.Tk()
root.title("To-Do List")

frame_tasks = tk.Frame(root)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50, bg='#f0f0f0', fg='#333333', selectbackground='#d1d1d1', selectforeground='#333333')
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack()

button_add_task = tk.Button(root, text="Add Task", width=48, command=add_task, bg='#008000', fg='#ffffff')
button_add_task.pack()

button_delete_task = tk.Button(root, text="Delete Task", width=48, command=confirm_delete, bg='#ff0000', fg='#ffffff')
button_delete_task.pack()

update_list_colors()

root.mainloop()

