import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import json
from datetime import datetime
from save_helper1 import save_to_json, fill_template_with_check
import gestion
import PV1
import PV1_1
import PV1_2
import PV1_3
import PV1_4

# ---------------- تعريف الألوان ----------------
form_bg = '#D35400'  # لون الخلفية
button_colors = ['#1E90FF', '#28a745', '#8A2BE2', '#FFD700']
button_text = '#FFFFFF'

def open_confirmation_window():
    root = tk.Tk()
    root.title("محاضر التثبيتPFP")
    root.geometry('800x600')
    root.configure(bg=form_bg)
    root.attributes('-alpha', 1.0)

    # تعيين الأيقونة إذا كانت موجودة
    icon_path = os.path.join("images", "ITP1.ICO")
    if os.path.exists(icon_path):
        root.iconbitmap(icon_path)

    # تعطيل زر الإغلاق X
    root.protocol("WM_DELETE_WINDOW", lambda: None)

    default_font = ("Segoe UI", 11, "bold")

    # ---------------- المحتوى ----------------
    content = tk.Frame(root, bg=form_bg)
    content.pack(expand=True, fill='both')

    # ---------------- العنوان ----------------
    title_label = tk.Label(
        content,
        text=" إدخال البيانات",
        bg=form_bg,
        fg="white",
        font=("Arial", 24, "bold italic")
    )
    title_label.pack(pady=(20, 10))

    # ---------------- الأزرار العلوية ----------------
    top_buttons_frame = tk.Frame(content, bg=form_bg)
    top_buttons_frame.pack(pady=(10, 20))

    labels = [
        " بيانات الأستاذ ",
        " بيانات المفتش ",
        " الإختبار الأول إلقاء الدرس ",
        " الإختبار الثاني المحادثة "
    ]

    # تأثير التلاشي (Fade Out)
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

    # دالة فتح النوافذ
    def on_button_click(i):
        if i == 0:
            fade_out(lambda: PV1_1.open_PV1_1_form())
        elif i == 1:
            fade_out(lambda: PV1.open_inspector_form())
        elif i == 2:
            fade_out(lambda: PV1_2.open_PV1_2_form())
        elif i == 3:
            fade_out(lambda: PV1_3.open_PV1_3_form())

    # إنشاء الأزرار (2 × 2)
    for i in range(2):
        b = tk.Button(top_buttons_frame, text=labels[i], font=default_font,
                      fg=button_text, bg=button_colors[i], relief='raised', bd=5,
                      padx=20, pady=10, width=25,
                      command=lambda i=i: on_button_click(i))
        b.grid(row=0, column=i, padx=20, pady=10)

    for i in range(2, 4):
        b = tk.Button(top_buttons_frame, text=labels[i], font=default_font,
                      fg=button_text, bg=button_colors[i], relief='raised', bd=5,
                      padx=20, pady=10, width=25,
                      command=lambda i=i: on_button_click(i))
        b.grid(row=1, column=i - 2, padx=20, pady=10)

    # ---------------- الصورة ----------------
    img_path = r"C:\Users\TechSpace\Desktop\Nouveau projet4\Nouveau Dossier\ITP PROJET\Images\Confirmation.jpeg"
    if os.path.exists(img_path):
        original_image = Image.open(img_path).resize((550, 180), Image.LANCZOS)
        photo = ImageTk.PhotoImage(original_image)
        img_label = tk.Label(content, image=photo, bg=form_bg)
        img_label.image = photo
        img_label.pack(pady=(30, 30))
    else:
        print(f"⚠️ الصورة غير موجودة في المسار: {img_path}")

    # ---------------- الأزرار السفلية ----------------
    bottom_frame = tk.Frame(content, bg=form_bg)
    bottom_frame.pack(pady=(0, 20))

    # فتح نموذج أعضاء اللجنة
    def open_committee():
        fade_out(lambda: PV1_4.open_pv1_4())

    # العودة للقائمة الرئيسية
    def exit_app():
        if messagebox.askokcancel("الخروج", "هل تريد العودة للقائمة الرئيسية؟"):
            root.destroy()
            gestion.open_gestion_window()

    # ---------------- الأزرار السفلية ----------------
    btn_committee = tk.Button(bottom_frame, text="أعضاء اللجنة", bg="#28a745", fg="white",
                              font=("Arial", 13, "bold"), padx=25, pady=10, width=18, command=open_committee)
    btn_committee.grid(row=0, column=0, padx=20)

    btn_exit = tk.Button(bottom_frame, text="القائمة الرئيسية", bg="#FF0000", fg="white",
                         font=("Arial", 13, "bold"), padx=25, pady=10, width=18, command=exit_app)
    btn_exit.grid(row=0, column=1, padx=20)

    root.mainloop()

# ---------------- دالة فتح القائمة الرئيسية ----------------
def open_main_menu():
    import PFP
    PFP.PFP()
