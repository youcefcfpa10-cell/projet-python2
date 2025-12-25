import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import gestion
import PV2
import PV2_1
import PV2_2
import PV2_3
import PV2_5
import PV2_4

# ---------------- تعريف الألوان ----------------
form_bg = '#C9B458'
button_text = '#FFFFFF'

def open_confirmation_window():
    root = tk.Tk()
    root.title("محاضر التثبيت مساعد التكوين")
    root.geometry('1000x650')
    root.configure(bg=form_bg)
    root.attributes('-alpha', 1.0)

    icon_path = os.path.join("images", "ITP1.ICO")
    if os.path.exists(icon_path):
        root.iconbitmap(icon_path)

    root.protocol("WM_DELETE_WINDOW", lambda: None)
    default_font = ("Segoe UI", 11, "bold")

    content = tk.Frame(root, bg=form_bg)
    content.pack(expand=True, fill='both', padx=20, pady=20)

    # ---------------- العنوان ----------------
    title_label = tk.Label(
        content,
        text="إدخال البيانات",
        bg=form_bg,
        fg="white",
        font=("Arial", 24, "bold italic")
    )
    title_label.pack(pady=(10, 20))

    img_path = r"C:\Users\TechSpace\Desktop\Nouveau projet4\Nouveau Dossier\ITP PROJET\Images\adj.jpg"

    # ---- إطار رئيسي للصورة والأزرار ----
    main_frame = tk.Frame(content, bg=form_bg)
    main_frame.pack(expand=True, fill='both', padx=20, pady=20)

    # ---- دالة التلاشي ----
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

    # ---- وظائف الأزرار ----
    def open_teacher():
        fade_out(lambda: PV2_1.open_PV2_1_form())

    def open_inspector():
        fade_out(lambda: PV2.open_inspector_form())

    def open_committee():
        fade_out(lambda: PV2_4.open_pv2_4())

    def open_exam1():
        fade_out(lambda: PV2_2.open_PV2_2_form())

    def open_exam2():
        fade_out(lambda: PV2_3.open_PV2_3_form())

    def open_exam3():
        fade_out(lambda: PV2_5.open_PV2_5_form())

    # ---- أزرار يسار الصورة ----
    left_buttons_frame = tk.Frame(main_frame, bg=form_bg)
    left_buttons_frame.pack(side='left', padx=20, fill='y', expand=True)

    left_button_labels = ["بيانات مساعد التكوين", "بيانات المفتش", "أعضاء اللجنة"]
    left_button_commands = [open_teacher, open_inspector, open_committee]
    left_button_colors = ["#0F1E1C", "#2FA39A", "#8B008B"]

    for i, text in enumerate(left_button_labels):
        b = tk.Button(left_buttons_frame, text=text, bg=left_button_colors[i], fg=button_text,
                      font=default_font, padx=20, pady=10, width=20,
                      relief='raised', bd=5, command=left_button_commands[i])
        b.pack(pady=10)

    # ---- أزرار يمين الصورة ----
    right_buttons_frame = tk.Frame(main_frame, bg=form_bg)
    right_buttons_frame.pack(side='right', padx=20, fill='y', expand=True)

    right_button_labels = ["الإختبار الأول", "الإختبار الثاني", "الإختبار الثالث"]
    right_button_commands = [open_exam1, open_exam2, open_exam3]
    right_button_colors = ["#8A2BE2", "#FFD700", "#1E90FF"]

    for i, text in enumerate(right_button_labels):
        b = tk.Button(right_buttons_frame, text=text, bg=right_button_colors[i], fg=button_text,
                      font=default_font, padx=20, pady=10, width=20,
                      relief='raised', bd=5, command=right_button_commands[i])
        b.pack(pady=10)

    # ---- إطار الصورة والزر أسفلها ----
    center_frame = tk.Frame(main_frame, bg=form_bg)
    center_frame.pack(side='left', expand=True, fill='y')

    # ---- الصورة ----
    if os.path.exists(img_path):
        original_image = Image.open(img_path).resize((400, 180), Image.LANCZOS)
        photo = ImageTk.PhotoImage(original_image)
        img_label = tk.Label(center_frame, image=photo, bg=form_bg)
        img_label.image = photo
        img_label.pack(expand=True)
    else:
        print(f"⚠️ الصورة غير موجودة في المسار: {img_path}")

    # ---- زر العودة للقائمة الرئيسية أسفل الصورة ----
    btn_exit = tk.Button(center_frame, text="القائمة الرئيسية", bg="#FF0000", fg="white",
                         font=("Arial", 13, "bold"), padx=25, pady=10, width=25,
                         relief='raised', bd=5, command=lambda: exit_app())
    btn_exit.pack(pady=20, side='bottom')

    # ---- دالة الخروج ----
    def exit_app():
        if messagebox.askokcancel("الخروج", "هل تريد العودة للقائمة الرئيسية؟"):
            root.destroy()
            gestion.open_gestion_window()

    root.mainloop()


if __name__ == "__main__":
    open_confirmation_window()
