import tkinter as tk
from tkinter import ttk, messagebox
import os
import sys
import json
import openpyxl
import gestion  # ✅ استدعاء الواجهة الرئيسية للعودة إليها

# -------------------- إعداد الألوان --------------------
form_bg = "#D35400"          # بني داكن (الخلفية الرئيسية)
frame_bg = "#d2b48c"         # بني فاتح للإطارات
entry_bg = "#D7CCC8"         # بيج فاتح لمربعات النص
list_bg = "#FFF8E1"          # بيج ناعم للقوائم
select_bg = "#8D6E63"        # بني رمادي متوسط لتحديد العناصر
button_bg = "#A47551"        # بني فاتح للأزرار
button_hover = "#5D4037"     # بني داكن عند الضغط
exit_button_bg = "#FF0000"   # أحمر لزر الخروج

# -------------------- تحديد base_path --------------------
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS  # عند تحويل البرنامج إلى EXE
else:
    base_path = os.path.dirname(__file__)

# -------------------- ملفات البيانات --------------------
excel_file = os.path.join(base_path, "PROJET.xlsx")  # ضع PROJET.xlsx في نفس مجلد البرنامج
json_file = os.path.join(base_path, "etablissement_data.json")

# -------------------- تحميل البيانات --------------------
if os.path.exists(json_file):
    # إذا تم حفظ JSON مسبقًا، استخدمه
    with open(json_file, "r", encoding="utf-8") as f:
        etablissement_data = json.load(f)
else:
    # قراءة من Excel وحفظها في JSON
    wb = openpyxl.load_workbook(excel_file)
    ws = wb["REG1"]  # اسم الشيت
    etablissement_data = [list(row) for row in ws.iter_rows(min_row=11, values_only=True)]
    
    # حفظ نسخة JSON للاستخدام لاحقًا
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(etablissement_data, f, ensure_ascii=False)

# -------------------- فتح نافذة المؤسسات --------------------
def open_Etablissement_window():
    root = tk.Tk()
    root.title("بيانات المؤسسات")
    root.geometry("1200x800")
    root.configure(bg=form_bg)

    # أيقونة
    icon_path = os.path.join(base_path, "Images", "ITP1.ICO")
    if os.path.exists(icon_path):
        root.iconbitmap(icon_path)

    # منع الإغلاق بزر X
    def on_close():
        messagebox.showinfo("تنبيه", "استخدم زر الخروج لإغلاق النموذج.")
    root.protocol("WM_DELETE_WINDOW", on_close)

    # -------------------- ComboBox --------------------
    tk.Label(
        root,
        text="اختر إسم الولاية من القائمة",
        bg=form_bg,
        fg="white",
        font=("Arial", 22, "bold")
    ).pack(pady=10)

    combo_var = tk.StringVar()
    combo_box = ttk.Combobox(
        root,
        textvariable=combo_var,
        font=("Arial", 14, "bold"),
        state="readonly",
        justify="center"
    )
    combo_box.pack(pady=5)

    # استخراج القيم من العمود B بدون تكرار
    unique_values = []
    for row in etablissement_data:
        if row[1] is not None and row[1] not in unique_values:
            unique_values.append(row[1])
    combo_box['values'] = unique_values

    # -------------------- TextBoxes --------------------
    labels_text = [
        "رمز الولاية", "إسم المؤسسة", "إسم الشهرة", "نوع المؤسسة",
        "اسم الملحقة", "عنوان المؤسسة", "رقم هاتف المؤسسة",
        "إسم ولقب مدير المؤسسة", "رقم هاتف المدير"
    ]

    frame_textboxes = tk.Frame(root, bg=frame_bg)
    frame_textboxes.pack(pady=10)

    text_vars = [tk.StringVar() for _ in range(9)]
    text_entries = []

    for i, label_text in enumerate(labels_text):
        label = tk.Label(frame_textboxes, text=label_text, bg=form_bg, fg="white",
                         font=("Arial", 12, "bold"), anchor="e")
        label.grid(row=(i//3)*2, column=i%3, padx=10, pady=(5, 0), sticky="e")

        entry = tk.Entry(frame_textboxes, textvariable=text_vars[i],
                         font=("Arial", 12, "bold"), justify='right',
                         bg="white", fg="black", width=25)
        entry.grid(row=(i//3)*2+1, column=i%3, padx=10, pady=(0,10), sticky="e")
        text_entries.append(entry)

    # -------------------- ListBox --------------------
    frame_list = tk.Frame(root, bg=frame_bg)
    frame_list.pack(pady=20, fill='both', expand=True)

    scrollbar_y = tk.Scrollbar(frame_list, orient='vertical')
    listbox = tk.Listbox(frame_list, width=120, height=15,
                         font=("Arial", 12, "bold"), bg=list_bg, fg="black",
                         selectbackground=select_bg, selectforeground="white",
                         yscrollcommand=scrollbar_y.set, justify='center')
    listbox.pack(side='left', fill='both', expand=True)
    scrollbar_y.config(command=listbox.yview)
    scrollbar_y.pack(side='right', fill='y')

    # -------------------- الوظائف --------------------
    def update_listbox(event):
        selected = combo_var.get()
        listbox.delete(0, tk.END)
        for idx, row in enumerate(etablissement_data):
            if str(row[1]) == str(selected):
                display_values = []
                if row[1] is not None:
                    display_values.append(str(row[1]))
                for col in range(2, 10):
                    if col < len(row) and row[col] is not None:
                        display_values.append(str(row[col]))
                display_text = " | ".join(display_values)
                listbox.insert(tk.END, f"{idx+1} | {display_text}")

    combo_box.bind("<<ComboboxSelected>>", update_listbox)

    def fill_textboxes(event):
        idx = listbox.curselection()
        if not idx:
            return
        selected_row = listbox.get(idx).split("|")[0].strip()
        row_idx = int(selected_row) - 1
        row_data = etablissement_data[row_idx]
        columns_order = [0, 2, 3, 4, 5, 6, 7, 8, 9]
        for i, col_idx in enumerate(columns_order):
            if col_idx < len(row_data) and row_data[col_idx] is not None:
                text_vars[i].set(str(row_data[col_idx]))
            else:
                text_vars[i].set("")

    listbox.bind("<<ListboxSelect>>", fill_textboxes)

    # -------------------- زر الخروج --------------------
    def exit_form():
        if messagebox.askyesno("خروج", "هل تريد العودة إلى القائمة الرئيسية؟"):
            root.destroy()
            gestion.open_gestion_window()

    exit_btn = tk.Button(root, text="⬅️ القائمة الرئيسية",
                         font=("Arial", 14, "bold"), bg=exit_button_bg, fg="white",
                         relief='raised', bd=6, padx=25, pady=10,
                         command=exit_form, activebackground=button_hover)
    exit_btn.pack(pady=20)

    # -------------------- تشغيل الواجهة --------------------
    root.mainloop()


# ✅ إذا تم تشغيل الملف مباشرة
if __name__ == "__main__":
    open_Etablissement_window()
