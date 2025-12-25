import tkinter as tk
from tkinter import messagebox
import os
import ADJOIN
from save_helper1 import save_to_json_shared

# ================= إعدادات الألوان =================
form_bg   = '#C9B458'     # اللون الأساسي الجديد
entry_bg  = 'white'
label_fg  = '#2F2F2F'
button_bg = '#4CAF50'     # زر الحفظ
button_fg = 'white'
exit_bg   = '#C0392B'     # زر الرجوع
exit_fg   = 'white'
# ==================================================

def open_PV2_3_form():
    root = tk.Tk()
    root.title("الإختبار الثاني")
    root.geometry("900x550")
    root.configure(bg=form_bg)
    root.resizable(False, False)

    # تعطيل زر X
    root.protocol(
        "WM_DELETE_WINDOW",
        lambda: messagebox.showwarning(
            "تنبيه",
            "الرجاء استعمال زر العودة للخروج من هذه الواجهة"
        )
    )

    # ---------------- أيقونة البرنامج ----------------
    icon_path = os.path.join("images", "ITP1.ICO")
    if os.path.exists(icon_path):
        root.iconbitmap(icon_path)

    # ---------------- العنوان ----------------
    tk.Label(root, text="تنشيط اللقاءات",
             bg=form_bg, fg=label_fg,
             font=("Arial", 22, "bold italic")).pack(pady=10)

    tk.Label(root,
             text="تنظـيم وتنشـيط اللقاءات والتظاهــرات الثقافــية والرياضــية",
             bg=form_bg, fg=label_fg,
             font=("Arial", 20, "bold")).pack(pady=5)

    # ---------------- عناصر التنقيط ----------------
    elements = [
        "المشاركة في النشاطات الثقافية",
        "المشاركة في النشاطات الرياضية",
        "المشاركة في تنظيم الإحتفالات الدينية و الوطنية",
        "روح المبادرة"
    ]

    base_marks = [5, 5, 5, 5]
    text_vars = [tk.StringVar() for _ in base_marks]

    total_var = tk.StringVar(value="0.00")
    base_total_var = tk.StringVar(value=f"{sum(base_marks):.2f}")

    table_frame = tk.Frame(root, bg=form_bg)
    table_frame.pack(pady=15)

    headers = ["العلامة المتحصل عليها", "قاعدة التنقيط", "عناصر التنقيط"]
    col_widths = [18, 14, 32]

    # ---------------- رؤوس الجدول ----------------
    for j, header in enumerate(headers):
        tk.Label(
            table_frame, text=header,
            bg=form_bg, fg=label_fg,
            font=("Arial", 14, "bold"),
            width=col_widths[j],
            relief="ridge"
        ).grid(row=0, column=j, padx=4, pady=4)

    entries = []

    # ---------------- الصفوف ----------------
    for i, element in enumerate(elements):
        tk.Label(
            table_frame, text=element,
            bg=form_bg, fg=label_fg,
            font=("Arial", 13, "bold"),
            width=col_widths[2],
            anchor="e"
        ).grid(row=i+1, column=2, padx=4, pady=4)

        tk.Label(
            table_frame, text=f"{base_marks[i]:.2f}",
            bg="white",
            fg=label_fg,
            font=("Arial", 13, "bold"),
            width=col_widths[1],
            relief="solid"
        ).grid(row=i+1, column=1, padx=4, pady=4)

        entry = tk.Entry(
            table_frame,
            textvariable=text_vars[i],
            font=("Arial", 12, "bold"),
            justify="center",
            bg=entry_bg,
            fg=label_fg,
            width=col_widths[0],
            relief="solid",
            bd=1
        )
        entry.grid(row=i+1, column=0, padx=4, pady=4)
        entries.append(entry)

    # ---------------- صف المجموع ----------------
    row_total = len(elements) + 1

    tk.Label(
        table_frame, text="المجموع",
        bg=form_bg, fg=label_fg,
        font=("Arial", 13, "bold"),
        width=col_widths[2],
        anchor="e"
    ).grid(row=row_total, column=2, padx=4, pady=4)

    tk.Entry(
        table_frame,
        textvariable=base_total_var,
        font=("Arial", 13, "bold"),
        justify="center",
        width=col_widths[1],
        state="readonly",
        readonlybackground="#EFEBD8"
    ).grid(row=row_total, column=1, padx=4, pady=4)

    tk.Entry(
        table_frame,
        textvariable=total_var,
        font=("Arial", 13, "bold"),
        justify="center",
        width=col_widths[0],
        state="readonly",
        readonlybackground="#FFFACD"
    ).grid(row=row_total, column=0, padx=4, pady=4)

    # ---------------- حساب المجموع ----------------
    def update_total(*args):
        total = 0.0
        for i, var in enumerate(text_vars):
            try:
                val = float(var.get().replace(",", "."))
                if 0 <= val <= base_marks[i]:
                    entries[i].config(bg=entry_bg)
                    total += val
                else:
                    entries[i].config(bg="#FFCCCB")
            except:
                entries[i].config(bg="#FFB6C1")

        total_var.set(f"{total:.2f}")

    for var in text_vars:
        var.trace_add("write", update_total)

    # ---------------- حفظ البيانات ----------------
    def save_data():
        data = {
            "title": "تنظيم وتنشيط اللقاءات",
            "marks1": [v.get() for v in text_vars],
            "base_total": base_total_var.get(),
            "total1": total_var.get()
        }
        save_to_json_shared("PV2_3", data, "data1.json")
        messagebox.showinfo("تم الحفظ", "تم حفظ البيانات بنجاح")

    # ---------------- الخروج ----------------
    def confirm_exit():
        if messagebox.askyesno("تأكيد", "هل تريد العودة إلى القائمة الرئيسية؟"):
            root.destroy()
            ADJOIN.open_confirmation_window()

    # ---------------- الأزرار ----------------
    btn_frame = tk.Frame(root, bg=form_bg)
    btn_frame.pack(pady=25)

    tk.Button(
        btn_frame, text="💾 حفظ النتائج",
        font=("Arial", 14, "bold"),
        bg=button_bg, fg=button_fg,
        padx=20, pady=10,
        command=save_data
    ).pack(side="right", padx=10)

    tk.Button(
        btn_frame, text="🏠 العودة للقائمة الرئيسية",
        font=("Arial", 14, "bold"),
        bg=exit_bg, fg=exit_fg,
        padx=20, pady=10,
        command=confirm_exit
    ).pack(side="right", padx=10)

    root.mainloop()


if __name__ == "__main__":
    open_PV2_3_form()
