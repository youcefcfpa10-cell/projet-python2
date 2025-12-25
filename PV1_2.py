import tkinter as tk
from tkinter import messagebox
import PFP  # للعودة إلى نافذة PFP
import os
from save_helper1 import save_to_json_shared, load_from_json_shared

# ---------------- إعدادات الألوان ----------------
form_bg = '#D35400'
entry_bg = 'white'
label_fg = 'black'
button_bg = '#28a745'
button_fg = 'white'
exit_bg = '#FF0000'
exit_fg = 'white'

# ---------------- واجهة النموذج ----------------
def open_PV1_2_form():
    root = tk.Tk()
    root.title("الإختبار الأول")
    root.geometry('950x700')
    root.configure(bg=form_bg)

# ---------------- أيقونة شريط العنوان ----------------

    root.attributes('-alpha', 0.0)
    icon_path = os.path.join("images", "ITP1.ICO")
    if os.path.exists(icon_path):
        root.iconbitmap(icon_path)

    # ---------------- تأثير الظهور ----------------
    def fade_in():
        alpha = root.attributes('-alpha')
        if alpha < 1.0:
            alpha += 0.1
            root.attributes('-alpha', alpha)
            root.after(10, fade_in)
    fade_in()

    # ---------------- العنوان ----------------
    tk.Label(root, text="إلقاء الدرس", bg=form_bg, fg="white",
             font=("Arial", 22, "bold italic")).pack(pady=10)

    # ---------------- عنوان الدرس ----------------
    title_frame = tk.Frame(root, bg=form_bg)
    title_frame.pack(pady=5)
    tk.Label(title_frame, text="عنوان الدرس", bg=form_bg, fg="white",
             font=("Arial", 14, "bold")).pack(side='right', padx=10)
    lesson_title = tk.Entry(title_frame, font=("Arial", 14), justify='right',
                            width=50, bg="white", fg="black")
    lesson_title.pack(side='right', padx=10)

    # ---------------- عناصر التنقيط ----------------
    elements = [
        "التحضير الكتابي والمادي",
        "صياغة الأغراض البيداغوجية",
        "الخطوات البيداغوجية",
        "التنشيط – القدرات",
        "نوعية الشروحات",
        "التنقيط التحليلي والموضوعي",
        "إختيار وإستعمال الوسائل البيداغوجية",
        "تكييف محتويات التكوين و تسيير الوقت",
        "تنظيم التعليم",
        "تقييم الحصة",
        "المجموع"
    ]
    base_marks = [5, 4, 4, 5, 5, 5, 4, 2, 2, 4, 40]
    text_vars = [tk.StringVar() for _ in elements]
    notes_var = tk.StringVar(value="")

    table_frame = tk.Frame(root, bg=form_bg)
    table_frame.pack(pady=10)
    headers = ["العلامة المتحصل عليها", "العلامة القاعدية", "عناصر التنقيط"]
    col_widths = [15, 12, 40]

    # رؤوس الجدول
    for j, header in enumerate(headers):
        tk.Label(table_frame, text=header, bg=form_bg, fg="white",
                 font=("Arial", 14, "bold"), width=col_widths[j],
                 relief='ridge', padx=8, pady=8).grid(row=0, column=j, sticky="nsew")

    entries, total_label = [], None
    for i, element in enumerate(elements):
        tk.Label(table_frame, text=element, bg=form_bg, fg=label_fg,
                 font=("Arial", 13, "bold"), width=col_widths[2],
                 anchor="e").grid(row=i+1, column=2, padx=5, pady=4, sticky="e")

        tk.Label(table_frame, text=f"{base_marks[i]:.2f}", bg="white", fg="black",
                 font=("Arial", 13, "bold"), width=col_widths[1],
                 relief='solid', anchor="center").grid(row=i+1, column=1, padx=5, pady=4)

        if i < len(elements) - 1:
            entry = tk.Entry(table_frame, textvariable=text_vars[i],
                             font=("Arial", 12, "bold"), justify='center',
                             bg=entry_bg, width=col_widths[0])
            entry.grid(row=i+1, column=0, padx=5, pady=4)
            entries.append(entry)
        else:
            total_label = tk.Label(table_frame, text="0.00", bg="#FFFACD", fg="black",
                                   font=("Arial", 13, "bold"), width=col_widths[0],
                                   relief='sunken', anchor="center")
            total_label.grid(row=i+1, column=0, padx=5, pady=4)

    # ---------------- حساب المجموع ----------------
    updating = False
    _update_after = None

    def format_and_update():
        nonlocal updating
        total = 0.0
        for i, var in enumerate(text_vars[:-1]):
            val = var.get().strip().replace(",", ".").replace(" ", "")
            entry = entries[i]
            if not val:
                entry.config(bg=entry_bg)
                continue
            try:
                num = float(val)
                if num < 0:
                    entry.config(bg="#FFB6C1")
                elif num > base_marks[i]:
                    entry.config(bg="#FFCCCB")
                else:
                    entry.config(bg="white")
                    total += num
                if not updating:
                    updating = True
                    var.set(f"{num:.2f}")
                    updating = False
            except ValueError:
                entry.config(bg="#FFB6C1")
        total_label.config(text=f"{total:.2f}")
        if total < 20:
            total_label.config(bg="#FF6347")
        elif 20 <= total < 24:
            total_label.config(bg="#FFD700")
        else:
            total_label.config(bg="#32CD32")

    def delayed_update(*args):
        nonlocal _update_after
        if _update_after:
            root.after_cancel(_update_after)
        _update_after = root.after(400, format_and_update)

    for var in text_vars[:-1]:
        var.trace_add("write", delayed_update)

    # ---------------- نافذة الملاحظات ----------------
    def open_notes_window():
        notes_win = tk.Toplevel(root)
        notes_win.title("📝 التقديرات العامة حول إلقاء الدرس")
        notes_win.geometry("600x400")
        notes_win.configure(bg="#F4A460")
# ✅ إضافة الأيقونة الخاصة بالنافذة (تأكد من وجود الملف داخل مجلد images)
        icon_path = os.path.join(os.path.dirname(__file__), "images", "ITP1.ICO")
        if os.path.exists(icon_path):
            try:
                 notes_win.iconbitmap(icon_path)
            except Exception as e:
               print(f"⚠️ لم يتم تعيين الأيقونة للنافذة الفرعية: {e}")
        else:
            print(f"⚠️ ملف الأيقونة غير موجود: {icon_path}")


        tk.Label(notes_win, text="أكتب التقديرات العامة",
                 font=("Arial", 14, "bold"), bg="#F4A460", fg="black").pack(pady=10)
        text_area = tk.Text(notes_win, font=("Arial", 12), width=60, height=10)
        text_area.insert("1.0", notes_var.get())
        text_area.pack(padx=10, pady=10)

        def save_notes():
            notes_text = text_area.get("1.0", "end-1c").strip()
            notes_var.set(notes_text)

        

            # حفظ جميع القيم مع الملاحظات
            current_values = [v.get().strip() for v in text_vars[:-1]]
            data_to_save = {
                "lesson_title": lesson_title.get(),
                "marks1": current_values,
                "total": total_label.cget("text"),
                "notes": notes_var.get()
            }
            save_to_json_shared("PV1_2", data_to_save, file_path="data.json")
            messagebox.showinfo("تم الحفظ ✅", "تم حفظ الملاحظات بنجاح.")
            notes_win.destroy()

        tk.Button(notes_win, text="💾 حفظ الملاحظات", font=("Arial", 13, "bold"),
                  bg=button_bg, fg=button_fg, relief='raised', bd=5,
                  command=save_notes).pack(pady=10)

    # ---------------- زر الحفظ ----------------
    def save_data():
        values = [v.get().strip() for v in text_vars[:-1]]
        if not all(values):
            messagebox.showwarning("تنبيه", "⚠️ الرجاء ملء جميع الحقول قبل الحفظ.")
            return

        data_to_save = {
            "lesson_title": lesson_title.get(),
            "marks1": values,
            "total": total_label.cget("text"),
            "notes": notes_var.get()
        }
        save_to_json_shared("PV1_2", data_to_save, file_path="data.json")
        messagebox.showinfo("تم الحفظ ✅", "تم حفظ البيانات في ملف data.json بنجاح.")

    # ---------------- زر العودة ----------------
    def exit_app():
        nonlocal _update_after
        if _update_after:
            root.after_cancel(_update_after)
        for var in text_vars[:-1]:
            traces = var.trace_info()
            for trace in traces:
                var.trace_remove("write", trace[1])
        if messagebox.askokcancel("الخروج", "هل تريد العودة إلى PFP؟"):
            root.destroy()
            PFP.open_confirmation_window()

    # ---------------- الأزرار ----------------
    button_frame = tk.Frame(root, bg=form_bg)
    button_frame.pack(pady=20)
    tk.Button(button_frame, text="📝 التقديرات العامة", font=("Arial", 14, "bold"),
              bg="#4682B4", fg="white", relief='raised', bd=6,
              padx=10, pady=8, command=open_notes_window).pack(side="right", padx=10)
    tk.Button(button_frame, text="💾 حفظ العلامات", font=("Arial", 14, "bold"),
              bg=button_bg, fg=button_fg, relief='raised', bd=6,
              padx=10, pady=8, command=save_data).pack(side="right", padx=10)
    tk.Button(button_frame, text="⬅️ العودة إلى PFP", font=("Arial", 13, "bold"),
              bg=exit_bg, fg=exit_fg, relief='raised', bd=6,
              padx=25, pady=10, command=exit_app).pack(side="right", padx=10)

    root.mainloop()


if __name__ == "__main__":
    open_PV1_2_form()
