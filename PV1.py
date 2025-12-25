import tkinter as tk
from tkinter import messagebox
import os
import PFP
from save_helper1 import save_to_json  # استيراد دالة الحفظ في JSON
import json  # ← أضف هذا السطر

# ---------------- إعداد الألوان ----------------
form_bg = '#D35400'
entry_bg = 'white'
label_fg = 'black'
button_bg = '#28a745'
button_fg = 'white'
exit_bg = '#FF0000'
exit_fg = 'white'

def open_inspector_form():
    root = tk.Tk()
    root.title("بيانات المفتش")
    root.geometry('850x600')
    root.configure(bg=form_bg)
    root.attributes('-alpha', 0.0)  # تأثير التلاشي التدريجي

    # تعيين الأيقونة إذا كانت موجودة
    icon_path = os.path.join("images", "ITP1.ICO")
    if os.path.exists(icon_path):
        root.iconbitmap(icon_path)

    # ---------------- تعطيل زر الإغلاق X ----------------
    def disable_close():
        messagebox.showinfo("تنبيه", "❌ لا يمكن إغلاق النافذة بهذه الطريقة.\nاستخدم زر العودة فقط.")
    root.protocol("WM_DELETE_WINDOW", disable_close)

    # ---------------- تأثيرات التلاشي ----------------
    def fade_in():
        alpha = root.attributes('-alpha')
        if alpha < 1.0:
            alpha += 0.05
            root.attributes('-alpha', alpha)
            root.after(30, fade_in)

    def fade_out(callback=None):
        alpha = root.attributes('-alpha')
        if alpha > 0:
            alpha -= 0.05
            root.attributes('-alpha', alpha)
            root.after(30, lambda: fade_out(callback))
        else:
            root.destroy()
            if callback:
                callback()

    fade_in()

    # ---------------- العنوان ----------------
    title_label = tk.Label(
        root, text="بيانات خاصة بالمفتش",
        bg=form_bg, fg="white", font=("Arial", 22, "bold italic")
    )
    title_label.pack(pady=20)

    # ---------------- إطار المحتوى ----------------
    frame = tk.Frame(root, bg=form_bg)
    frame.pack(pady=10, padx=20, fill='x')

    labels_text = [
        "إسم ولقب مفتش المقاطعة",
        "إسم ورمز شعبة تخصص المفتش",
        "إسم ورقم المقاطعة",
        "ولاية المقاطعة",  # الحقل الجديد
        "المقر الإداري الخاص بالمفتش",
        "رقم الهاتف الخاص بالمفتش",
        "الإيميل الخاص بالمفتش"
    ]

    text_vars = [tk.StringVar() for _ in labels_text]

    # ---------------- ترتيب اللابلز على اليمين ----------------
    for i, label_text in enumerate(labels_text):
        entry = tk.Entry(frame, textvariable=text_vars[i],
                         font=("Arial", 12, "bold"), justify='right',
                         bg=entry_bg, width=30)
        entry.grid(row=i, column=0, padx=(10, 6), pady=8, sticky="w")

        label = tk.Label(frame, text=label_text, bg=form_bg, fg=label_fg,
                         font=("Arial", 13, "bold"), anchor="e", width=35)
        label.grid(row=i, column=1, padx=(6, 10), pady=8, sticky="e")

    # ---------------- دالة الحفظ ----------------
    def save_data():
        values = [v.get().strip() for v in text_vars]
        if not all(values):
            messagebox.showwarning("تنبيه", "⚠️ الرجاء ملء جميع الحقول قبل الحفظ.")
            return

        inspector_data = {
            "inspector_name": values[0],
            "specialty_code": values[1],
            "district": values[2],
            "district_state": values[3],  # الحقل الجديد
            "office": values[4],
            "phone": values[5],
            "email": values[6]
        }

        # قائمة الملفات لحفظ البيانات فيها
        files_to_save = ["data.json", "data1.json"]

        for file_path in files_to_save:
            all_data = {}
            if os.path.exists(file_path):
                try:
                    with open(file_path, "r", encoding="utf-8-sig") as f:
                        all_data = json.load(f)
                except:
                    all_data = {}

            # تحديث قسم المفتش فقط
            all_data["Inspector"] = inspector_data

            # حفظ البيانات في الملف
            with open(file_path, "w", encoding="utf-8-sig") as f:
                json.dump(all_data, f, ensure_ascii=False, indent=4)

        messagebox.showinfo("تم الحفظ ✅", "تم حفظ بيانات المفتش بنجاح  ")

    # ---------------- زر الحفظ ----------------
    save_btn = tk.Button(root, text="💾 حفظ",
                         font=("Arial", 14, "bold"),
                         bg=button_bg, fg=button_fg,
                         relief='raised', bd=6,
                         padx=20, pady=10,
                         command=save_data)
    save_btn.pack(pady=20)

    # ---------------- زر العودة ----------------
    def exit_app():
        if messagebox.askokcancel("الخروج", "هل تريد العودة إلى  PFP؟"):
            fade_out(lambda: PFP.open_confirmation_window())

    exit_btn = tk.Button(root, text="⬅️ العودة إلى  PFP",
                         bg=exit_bg, fg=exit_fg,
                         font=("Arial", 13, "bold"),
                         relief='raised', bd=6,
                         padx=25, pady=10,
                         command=exit_app)
    exit_btn.pack(pady=10)

    root.mainloop()


# للتجربة
if __name__ == "__main__":
    open_inspector_form()
