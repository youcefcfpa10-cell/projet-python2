import tkinter as tk
from tkinter import messagebox
import PFP  # للعودة إلى نافذة PFP
import os
import json
from save_helper1 import save_to_json

# ---------------- إعدادات الألوان ----------------
form_bg = '#D35400'
entry_bg = 'white'
label_fg = 'black'
button_bg = '#28a745'
button_fg = 'white'
exit_bg = '#FF0000'
exit_fg = 'white'

def open_PV1_1_form():
    root = tk.Tk()
    root.title("بيانات الأستاذ")
    root.geometry('800x800')
    root.configure(bg=form_bg)
    root.attributes('-alpha', 0.0)

    icon_path = os.path.join("images", "ITP1.ICO")
    if os.path.exists(icon_path):
        root.iconbitmap(icon_path)

    def disable_close():
        messagebox.showinfo("تنبيه", "الرجاء استخدام زر العودة إلى القائمة الرئيسية.")
    root.protocol("WM_DELETE_WINDOW", disable_close)

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

    title_label = tk.Label(
        root, text="بيانات خاصة بالأستاذ المعني بإمتحان التثبيت",
        bg=form_bg, fg="white", font=("Arial", 22, "bold italic")
    )
    title_label.pack(pady=20)

    frame = tk.Frame(root, bg=form_bg)
    frame.pack(pady=10, padx=50, fill='x')

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
        "رمز الشعبة المهنية للتخصص القاعدي",
        "التخصص المدرس",
        "بداية التربص البيداغوجي",
        "نهاية التربص البيداغوجي",
        "الحجم الساعي الأسبوعي"
    ]

    text_vars = [tk.StringVar() for _ in labels_text]

    # ✅ Validation function للأسم اللاتيني
    def latin_only(P):
        # يسمح فقط بالحروف الإنجليزية والمسافات
        return all((c.isascii() and c.isalpha()) or c.isspace() for c in P)

    # إنشاء Entry مع Validation
    for i, label_text in enumerate(labels_text):
        if i == 2:
            vcmd = (root.register(latin_only), '%P')
            entry = tk.Entry(frame, textvariable=text_vars[i],
                             font=("Arial", 12, "bold"), justify='right',
                             bg=entry_bg, width=35, validate='key', validatecommand=vcmd)
        else:
            entry = tk.Entry(frame, textvariable=text_vars[i],
                             font=("Arial", 12, "bold"), justify='right',
                             bg=entry_bg, width=35)

        entry.grid(row=i, column=0, padx=10, pady=5, sticky="w")

        label = tk.Label(frame, text=label_text, bg=form_bg, fg=label_fg,
                         font=("Arial", 13, "bold"), anchor="e", width=35)
        label.grid(row=i, column=1, pady=5, sticky="e")

    def save_data():
        values = [v.get().strip() for v in text_vars]
        if not all(values):
            messagebox.showwarning("تنبيه", "⚠️ الرجاء ملء جميع الحقول قبل الحفظ.")
            return

        teacher_data = {
            "last_name": values[0],
            "first_name": values[1],
            "latin_first_name": values[2],
            "birth_date": values[3],
            "birth_place": values[4],
            "birth_state": values[5],
            "install_date": values[6],
            "assignment_institution": values[7],
            "exam_institution": values[8],
            "specialty_code": values[9],
            "taught_specialty": values[10],
            "start_training": values[11],
            "end_training": values[12],
            "weekly_hours": values[13],
        }

        save_to_json({"Teacher": teacher_data})
        messagebox.showinfo("تم الحفظ ✅", "تم حفظ بيانات الأستاذ بنجاح ")

    save_btn = tk.Button(root, text="💾 حفظ البيانات",
                         font=("Arial", 14, "bold"),
                         bg=button_bg, fg=button_fg,
                         relief='raised', bd=6,
                         padx=20, pady=10,
                         command=save_data)
    save_btn.pack(pady=(30, 10))

    def exit_app():
        if messagebox.askokcancel("الخروج", "هل تريد العودة إلى PFP؟"):
            fade_out(lambda: PFP.open_confirmation_window())

    exit_btn = tk.Button(root, text="⬅️ العودة إلى PFP",
                         bg=exit_bg, fg=exit_fg,
                         font=("Arial", 13, "bold"),
                         relief='raised', bd=6,
                         padx=25, pady=10,
                         command=exit_app)
    exit_btn.pack(pady=(10, 20))

    root.mainloop()


if __name__ == "__main__":
    open_PV1_1_form()
