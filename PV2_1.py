import tkinter as tk
from tkinter import messagebox
import ADJOIN
import os
from save_helper1 import save_to_json

# ---------------- إعدادات الألوان ----------------
form_bg = '#145E57'          # أخضر
entry_bg = 'white'
label_fg = 'white'
button_bg = '#C9B458'
button_fg = 'white'
exit_bg = '#8B0000'
exit_fg = 'white'


def open_PV2_1_form():
    root = tk.Tk()
    root.title("بيانات مساعد التكوين")
    root.geometry('800x800')
    root.configure(bg=form_bg)
    root.attributes('-alpha', 0.0)

    # أيقونة
    icon_path = os.path.join("images", "ITP1.ICO")
    if os.path.exists(icon_path):
        root.iconbitmap(icon_path)

    # تعطيل زر X
    def disable_close():
        messagebox.showinfo("تنبيه", "الرجاء استخدام زر العودة إلى القائمة الرئيسية.")
    root.protocol("WM_DELETE_WINDOW", disable_close)

    # ---------------- تأثيرات ----------------
    def fade_in():
        alpha = root.attributes('-alpha')
        if alpha < 1.0:
            root.attributes('-alpha', alpha + 0.05)
            root.after(30, fade_in)

    def fade_out(callback=None):
        alpha = root.attributes('-alpha')
        if alpha > 0:
            root.attributes('-alpha', alpha - 0.05)
            root.after(30, lambda: fade_out(callback))
        else:
            root.destroy()
            if callback:
                callback()

    fade_in()

    # ---------------- العنوان ----------------
    title_label = tk.Label(
        root,
        text="بيانات خاصة بمساعد التكوين المعني بإمتحان التثبيت",
        bg=form_bg,
        fg="white",
        font=("Arial", 22, "bold italic")
    )
    title_label.pack(pady=20)

    # ---------------- الإطار ----------------
    frame = tk.Frame(root, bg=form_bg)
    frame.pack(pady=10, padx=50, fill='x')

    # ---------------- الحقول ----------------
    labels_text = [
        "لقب الممتحن",
        "إسم الممتحن",
        "الإسم و اللقب باللغة اللاتينية",
        "تاريخ إزدياد الممتحن",
        "مكان الإزدياد",
        "ولاية الإزدياد",
        "تاريخ تنصيب الممتحن",
        "مؤسسة التعيين",
        "مؤسسة الإمتحان",
        "المؤسسة الممارس بها النشاط",
        "تاريخ الإمتحان"
    ]

    keys = [
        "last_name",
        "first_name",
        "latin_full_name",
        "birth_date",
        "birth_place",
        "birth_state",
        "install_date",
        "assignment_institution",
        "exam_institution",
        "activity_institution",
        "exam_date"
    ]

    text_vars = [tk.StringVar() for _ in labels_text]

    # السماح فقط بالحروف اللاتينية
    def latin_only(P):
        return all((c.isascii() and c.isalpha()) or c.isspace() for c in P)

    # إنشاء الحقول
    for i, label_text in enumerate(labels_text):
        if i == 2:
            vcmd = (root.register(latin_only), '%P')
            entry = tk.Entry(
                frame,
                textvariable=text_vars[i],
                font=("Arial", 12, "bold"),
                justify='right',
                bg=entry_bg,
                width=35,
                validate='key',
                validatecommand=vcmd
            )
        else:
            entry = tk.Entry(
                frame,
                textvariable=text_vars[i],
                font=("Arial", 12, "bold"),
                justify='right',
                bg=entry_bg,
                width=35
            )

        entry.grid(row=i, column=0, padx=10, pady=5, sticky="w")

        label = tk.Label(
            frame,
            text=label_text,
            bg=form_bg,
            fg=label_fg,
            font=("Arial", 13, "bold"),
            anchor="e",
            width=35
        )
        label.grid(row=i, column=1, pady=5, sticky="e")

    # ---------------- حفظ البيانات ----------------
    def save_data():
        values = [v.get().strip() for v in text_vars]

        if not all(values):
            messagebox.showwarning("تنبيه", "⚠️ الرجاء ملء جميع الحقول قبل الحفظ.")
            return

        ADJOIN_data = dict(zip(keys, values))

        save_to_json({"ADJOIN": ADJOIN_data}, "data1.json")
        messagebox.showinfo("تم الحفظ ✅", "تم حفظ بيانات مساعد التكوين بنجاح")

    save_btn = tk.Button(
        root,
        text="💾 حفظ البيانات",
        font=("Arial", 14, "bold"),
        bg=button_bg,
        fg=button_fg,
        relief='raised',
        bd=6,
        padx=20,
        pady=10,
        command=save_data
    )
    save_btn.pack(pady=(30, 10))

    # ---------------- رجوع ----------------
    def exit_app():
        if messagebox.askokcancel("الخروج", "هل تريد العودة إلى القائمة الرئيسية؟"):
            fade_out(lambda: ADJOIN.open_confirmation_window())

    exit_btn = tk.Button(
        root,
        text="⬅️    العودة للنافذة السابقة",
        bg=exit_bg,
        fg=exit_fg,
        font=("Arial", 13, "bold"),
        relief='raised',
        bd=6,
        padx=25,
        pady=10,
        command=exit_app
    )
    exit_btn.pack(pady=(10, 20))

    root.mainloop()


if __name__ == "__main__":
    open_PV2_1_form()
