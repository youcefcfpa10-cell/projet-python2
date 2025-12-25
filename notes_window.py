# ✅ notes_window.py
import tkinter as tk
import json
import os


def save_to_json(data, filename="data.json"):
    """Save updated data back to JSON."""
    with open(filename, "w", encoding="utf-8-sig") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def open_notes_window(root, all_data, on_save_callback=None, icon_path=None):
    """
    يفتح نافذة الملاحظات (Modal) ويتيح كتابة الملاحظات RTL
    عند الضغط على "حفظ" يتم تخزينها داخل all_data["PV1_4"]["notesg"]
    ثم يتم استدعاء on_save_callback من الملف الرئيسي
    """

    notes_win = tk.Toplevel(root)
    notes_win.title("إضافة الملاحظات العامة")
    notes_win.geometry("700x380")
    notes_win.configure(bg="#D35400")
    notes_win.transient(root)   # يجعلها فوق النافذة الرئيسية
    notes_win.grab_set()        # Modal

    # إضافة الأيقونة إذا موجودة
    if icon_path and os.path.exists(icon_path):
        try:
            notes_win.iconbitmap(icon_path)
        except Exception:
            pass

    tk.Label(
        notes_win,
        text="📝  أدخل الملاحظات و التقديرات العامة النهائية",
        bg="#D35400",
        fg="white",
        font=("Arial", 15, "bold")
    ).pack(pady=(12, 6))

    notes_text = tk.Text(notes_win, font=("Arial", 13), width=78, height=12, wrap='word')
    notes_text.pack(padx=12, pady=(0, 8), expand=True, fill="both")

    # ✅ إعداد اتجاه النص Right-To-Left
    notes_text.tag_configure("rtl", justify="right")

    def apply_rtl(event=None):
        notes_text.tag_add("rtl", "1.0", "end")

    notes_text.bind("<KeyRelease>", apply_rtl)

    # ✅ جلب الملاحظات السابقة إن وجدت (notesg)
    existing_notes = all_data.get("PV1_4", {}).get("notesg", "")
    if existing_notes:
        notes_text.insert("1.0", existing_notes)
        apply_rtl()

    def save_notes_only():
        notes = notes_text.get("1.0", "end").strip()

        # إذا لم يكن هناك PV1_4 نعمل إنشاء له
        if "PV1_4" not in all_data:
            all_data["PV1_4"] = {}

        # ✅ حفظ الملاحظات بالمفتاح الجديد notesg
        all_data["PV1_4"]["notesg"] = notes
        save_to_json(all_data)

        notes_win.grab_release()
        notes_win.destroy()

        # 🔁 إكمال العملية في الملف الرئيسي
        if on_save_callback:
            on_save_callback()

    tk.Button(
        notes_win,
        text="💾 حفظ الملاحظات ",
        bg="#4CAF50",
        fg="white",
        font=("Arial", 12, "bold"),
        command=save_notes_only
    ).pack(pady=(0, 12))
