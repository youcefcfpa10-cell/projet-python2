import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os, sys
import subprocess
from search_word import open_word_search_window
import Confirmation      # فتح الفورم الثاني
import Etablissement     # بيانات المؤسسات
import ADJOIN     # محضر  تثبيت مساعد التكوين

# ---------------- إعدادات الألوان ----------------
form_bg = '#D35400'
button_colors = ['#1E90FF', '#28a745', '#FF4500', '#8A2BE2', '#FFD700', '#00CED1']
button_text = '#FFFFFF'

# ---------------- تحديد المسار الأساسي للصور ----------------
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(__file__)

def get_image_path(filename):
    return os.path.join(base_path, "images", filename)

# ---------------- دالة فتح نافذة الإدارة ----------------
def open_gestion_window():
    root = tk.Tk()
    root.title("برنامج النشاط")
    root.geometry('700x550')
    root.configure(bg=form_bg)

    default_font = ("Segoe UI", 11, "bold")

    # ---------------- أيقونة النافذة ----------------
    icon_path = get_image_path("ITP1.ico")
    if os.path.exists(icon_path):
        root.iconbitmap(icon_path)

    # ---------------- إطار علوي (العنوان + الصورة) ----------------
    top_frame = tk.Frame(root, bg=form_bg)
    top_frame.pack(pady=(5, 2), fill='x')   # ✅ تقليص المسافة أسفل العنوان

    # إعداد الأعمدة للتوسيط
    top_frame.columnconfigure(0, weight=1)
    top_frame.columnconfigure(1, weight=0)
    top_frame.columnconfigure(2, weight=0)
    top_frame.columnconfigure(3, weight=1)

    # العنوان
    title_label = tk.Label(
        top_frame,
        text="إدارة المهام",
        bg=form_bg,
        fg="white",
        font=("Arial", 22, "bold italic")
    )
    title_label.grid(row=0, column=1, padx=5, pady=2)

    # الصورة بجانب العنوان (نفس السطر)
    right_img = ImageTk.PhotoImage(
        Image.open(get_image_path("ITP10.PNG")).resize((90, 60))
    )
    right_label = tk.Label(top_frame, image=right_img, bg=form_bg)
    right_label.grid(row=0, column=2, padx=5, pady=2)

    # ---------------- إطار المحتوى (الأزرار + الصورة) ----------------
    content_frame = tk.Frame(root, bg=form_bg)
    content_frame.pack(expand=True, fill='both', pady=(2, 0))  # ✅ تقليص المسافة العمودية

    # أزرار يسار
    left_frame = tk.Frame(content_frame, bg=form_bg)
    left_frame.pack(side='left', padx=20, pady=5)

    # أزرار يمين
    right_frame = tk.Frame(content_frame, bg=form_bg)
    right_frame.pack(side='right', padx=20, pady=5)

    # الصورة في الوسط
    center_frame = tk.Frame(content_frame, bg=form_bg)
    center_frame.pack(expand=True, pady=5)

    main_img = ImageTk.PhotoImage(
        Image.open(get_image_path("téléchargement.jpeg")).resize((350, 200))
    )
    img_label = tk.Label(center_frame, image=main_img, bg=form_bg)
    img_label.pack()

    # ---------------- تأثير Hover للأزرار ----------------
    def make_hover_effect(btn, base_color):
        def hex_to_rgb(h): return tuple(int(h[i:i+2], 16) for i in (1, 3, 5))
        def rgb_to_hex(rgb): return '#{:02x}{:02x}{:02x}'.format(*rgb)

        def adjust_color(hex_color, factor):
            r, g, b = hex_to_rgb(hex_color)
            clamp = lambda x: max(0, min(255, int(x)))
            if factor >= 0:
                r = clamp(r + (255 - r) * factor)
                g = clamp(g + (255 - g) * factor)
                b = clamp(b + (255 - b) * factor)
            else:
                r = clamp(r * (1 + factor))
                g = clamp(g * (1 + factor))
                b = clamp(b * (1 + factor))
            return rgb_to_hex((r, g, b))

        hover_color = adjust_color(base_color, 0.15)
        active_color = adjust_color(base_color, -0.25)

        btn.bind("<Enter>", lambda e: btn.config(bg=hover_color))
        btn.bind("<Leave>", lambda e: btn.config(bg=base_color))
        btn.bind("<ButtonPress-1>", lambda e: btn.config(bg=active_color))
        btn.bind("<ButtonRelease-1>", lambda e: btn.config(bg=hover_color))

    # ---------------- أسماء الأزرار ----------------
    labels = [
        " الأهداف و النشاطات ",
        "محاضر التثبيت",
        "بيانات المؤسسات",
        "معطيات الدخول",
        "وضعية الأساتذة",
        "جدول الكفاءات"
    ]

    # ---------------- دالة الضغط على الأزرار ----------------
    def on_button_click(i):
        if i == 0:
            open_word_search_window(root)
        elif i == 1:
            root.destroy()
            Confirmation.open_confirmation_window()
        elif i == 2:
            root.destroy()
            Etablissement.open_Etablissement_window()
        else:
            messagebox.showinfo("تنبيه", f"لا يزال قيد التطوير للنسخة القادمة: {labels[i]}")

    # ---------------- إنشاء الأزرار اليسرى ----------------
    for i in range(3):
        b = tk.Button(
            left_frame, text=labels[i], font=default_font,
            fg=button_text, bg=button_colors[i],
            relief='raised', bd=6, padx=20, pady=8,
            command=lambda i=i: on_button_click(i)
        )
        b.pack(pady=6, fill='x')
        make_hover_effect(b, button_colors[i])

    # ---------------- إنشاء الأزرار اليمنى ----------------
    for i in range(3, 6):
        b = tk.Button(
            right_frame, text=labels[i], font=default_font,
            fg=button_text, bg=button_colors[i],
            relief='raised', bd=6, padx=20, pady=8,
            command=lambda i=i: on_button_click(i)
        )
        b.pack(pady=6, fill='x')
        make_hover_effect(b, button_colors[i])

    # ---------------- زر الخروج ----------------
    def exit_app():
        exit_path = os.path.join(os.path.dirname(__file__), "EXIT.py")
        subprocess.Popen([sys.executable, exit_path], shell=False)
        root.destroy()

    exit_btn = tk.Button(
        root, text="خروج",
        bg="#FF0000", fg="white",
        font=("Arial", 14, "bold"),
        command=exit_app
    )
    exit_btn.place(relx=0.5, rely=0.95, anchor='s')

    # ---------------- منع الإغلاق بزر X ----------------
    def on_close():
        messagebox.showinfo("تنبيه", "استخدم زر الخروج لإغلاق النموذج بشكل صحيح.")

    root.protocol("WM_DELETE_WINDOW", on_close)

    # ---------------- الاحتفاظ بالصور ----------------
    root.right_img = right_img
    root.main_img = main_img

    root.mainloop()


if __name__ == "__main__":
    open_gestion_window()
