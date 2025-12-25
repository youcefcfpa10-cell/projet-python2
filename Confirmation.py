import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import sys
import gestion
import PFP
import ADJOIN


# ---------------- تعريف الألوان ----------------
form_bg = '#D35400'
button_colors = ['#1E90FF', '#28a745', '#FF0000']  # الأزرق، الأخضر، الأحمر
button_text = '#FFFFFF'

# ---------------- تحديد base_path للصور والأيقونات ----------------
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS  # عند تحويل البرنامج إلى EXE
else:
    base_path = os.path.dirname(__file__)  # عند تشغيله ككود بايثون

def get_image_path(filename):
    """ترجع المسار الكامل للملفات داخل مجلد Images"""
    return os.path.join(base_path, "Images", filename)

def open_confirmation_window():
    root = tk.Tk()
    root.title("محاضر التثبيت")
    root.geometry('950x450')
    root.configure(bg=form_bg)
    
    # تعيين الأيقونة
    icon_path = get_image_path("ITP1.ICO")
    if os.path.exists(icon_path):
        root.iconbitmap(icon_path)
    else:
        print(f"⚠️ الأيقونة غير موجودة في المسار: {icon_path}")

    # بدء النافذة بشفافية كاملة (مخفية)
    root.attributes("-alpha", 0.0)

    default_font = ("Segoe UI", 11, "bold")

    # ---------------- الإطارات ----------------
    content = tk.Frame(root, bg=form_bg)
    content.pack(expand=True, fill='both')

    # ---------------- العنوان أعلى الفورم ----------------
    title_label = tk.Label(content, text="إختر المحضر", bg=form_bg,
                           fg="white", font=("Arial", 22, "bold italic"))
    title_label.pack(pady=(20, 20))

    center_frame = tk.Frame(content, bg=form_bg)
    center_frame.pack(side='left', padx=30, pady=30, expand=True)

    right_frame = tk.Frame(content, bg=form_bg)
    right_frame.pack(side='right', padx=30, pady=30)

    # ---------------- الصورة ----------------
    img_path = get_image_path("Confirmation1.jpeg")
    if os.path.exists(img_path):
        original_image = Image.open(img_path).resize((550, 180), Image.LANCZOS)
        photo = ImageTk.PhotoImage(original_image)
        img_label = tk.Label(center_frame, image=photo, bg=form_bg)
        img_label.image = photo
        img_label.pack(expand=True)
    else:
        print(f"⚠️ الصورة غير موجودة في المسار: {img_path}")

    # ---------------- تأثير Fade In / Fade Out ----------------
    def fade_in():
        alpha = root.attributes("-alpha")
        if alpha < 1:
            alpha += 0.05
            root.attributes("-alpha", alpha)
            root.after(25, fade_in)

    def fade_out(callback=None):
        alpha = root.attributes("-alpha")
        if alpha > 0:
            alpha -= 0.05
            root.attributes("-alpha", alpha)
            root.after(25, lambda: fade_out(callback))
        else:
            root.destroy()
            if callback:
                callback()

    fade_in()  # تشغيل تأثير الظهور عند فتح النافذة

    # ---------------- دالة التعامل مع الأزرار ----------------
    def on_button_click(button_name):
        if button_name == "PFP":
            fade_out(lambda: PFP.open_confirmation_window())
        elif button_name == "Assistant":
            fade_out(lambda:  ADJOIN.open_confirmation_window())  # استدعاء النموذج مباشرة
        elif button_name == "Exit":
            if messagebox.askokcancel("الخروج", "هل تريد العودة للقائمة الرئيسية؟"):
                fade_out(lambda: gestion.open_gestion_window())

    # ---------------- إنشاء الأزرار العمودية ----------------
    btn_pfp = tk.Button(right_frame, text="محضر تثبيت أستاذ التكوين المهني PFP", font=default_font,
                        fg=button_text, bg=button_colors[0], padx=20, pady=10,
                        width=25, command=lambda: on_button_click("PFP"))
    btn_pfp.pack(pady=20)

    btn_assistant = tk.Button(right_frame, text="محضر تثبيت مساعد التكوين", font=default_font,
                              fg=button_text, bg=button_colors[1], padx=20, pady=10,
                              width=25, command=lambda: on_button_click("Assistant"))
    btn_assistant.pack(pady=20)

    btn_exit = tk.Button(right_frame, text="القائمة الرئيسية", font=default_font,
                         fg=button_text, bg=button_colors[2], padx=20, pady=10,
                         width=25, command=lambda: on_button_click("Exit"))
    btn_exit.pack(pady=20)

    root.mainloop()
