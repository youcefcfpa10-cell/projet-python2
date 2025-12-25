# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser
import json
import os
import subprocess
import sys

class WelcomeNext(QtWidgets.QDialog):
    def __init__(self, current_user, passwords):
        super().__init__()
        self.current_user = current_user
        self.passwords = passwords
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("واجهة الترحيب")
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.resize(600, 450)
        self.setStyleSheet("background-color: #D35400; color: white;")
        icon_path = "images/ITP1.ico"
        if os.path.exists(icon_path):
            self.setWindowIcon(QtGui.QIcon(icon_path))

        self.label = QtWidgets.QLabel("تم تسجيل الدخول بنجاح ✅", self)
        self.label.setGeometry(QtCore.QRect(150, 20, 300, 50))
        self.label.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("border: 4px solid #FFFFFF; border-radius: 5px; padding: 5px;")

        self.welcome_label = QtWidgets.QLabel("بسم الله الرحمن الرحيم", self)
        self.welcome_label.setGeometry(QtCore.QRect(60, 80, 500, 55))
        self.welcome_label.setFont(QtGui.QFont("Arial", 28, QtGui.QFont.Bold))
        self.welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_label.setStyleSheet("border: 4px solid #FFFFFF; border-radius: 5px; padding: 5px;")

        self.welcome_label_2 = QtWidgets.QLabel("اللهم صل وسلم على سيدنا محمد", self)
        self.welcome_label_2.setGeometry(QtCore.QRect(60, 140, 500, 55))
        self.welcome_label_2.setFont(QtGui.QFont("Arial", 28, QtGui.QFont.Bold))
        self.welcome_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_label_2.setStyleSheet("border: 4px solid #FFFFFF; border-radius: 5px; padding: 5px;")

        self.welcome_label_3 = QtWidgets.QLabel("مرحبا بكم لا تنسوننا بخالص الدعاء", self)
        self.welcome_label_3.setGeometry(QtCore.QRect(60, 200, 500, 50))
        self.welcome_label_3.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        self.welcome_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_label_3.setStyleSheet("border: 4px solid #FFFFFF; border-radius: 5px; padding: 5px;")

        self.welcome_label_6 = QtWidgets.QLabel("روابط التواصل معنا في الأسفل", self)
        self.welcome_label_6.setGeometry(QtCore.QRect(60, 260, 500, 50))
        self.welcome_label_6.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        self.welcome_label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_label_6.setStyleSheet("border: 4px solid #FFFFFF; border-radius: 5px; padding: 5px;")

        wa_icon = QtGui.QPixmap("images/whatsap.JPEG").scaled(24, 24, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        fb_icon = QtGui.QPixmap("images/facebook.png").scaled(24, 24, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)

        self.welcome_label_4 = QtWidgets.QLabel(self)
        self.welcome_label_4.setGeometry(QtCore.QRect(60, 380, 40, 40))
        self.welcome_label_4.setPixmap(wa_icon)
        self.welcome_label_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.wa_text_label_7 = QtWidgets.QLabel(" https://wa.link/4y9xf4", self)
        self.wa_text_label_7.setGeometry(QtCore.QRect(100, 380, 150, 40))
        self.wa_text_label_7.setFont(QtGui.QFont("Arial", 10))
        self.wa_text_label_7.setStyleSheet("color: white;")
        self.wa_text_label_7.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.wa_text_label_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.wa_text_label_7.mousePressEvent = lambda event: webbrowser.open("https://wa.link/4y9xf4")

        self.welcome_label_5 = QtWidgets.QLabel(self)
        self.welcome_label_5.setGeometry(QtCore.QRect(300, 380, 40, 40))
        self.welcome_label_5.setPixmap(fb_icon)
        self.welcome_label_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.wa_text_label_8 = QtWidgets.QLabel("https://tinyurl.com/2687f245 ", self)
        self.wa_text_label_8.setGeometry(QtCore.QRect(350, 380, 150, 40))
        self.wa_text_label_8.setFont(QtGui.QFont("Arial", 10))
        self.wa_text_label_8.setStyleSheet("color: white;")
        self.wa_text_label_8.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.wa_text_label_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.wa_text_label_8.mousePressEvent = lambda event: webbrowser.open("https://tinyurl.com/2687f245")

        # زر المتابعة مع التلاشي ثم تشغيل gestion.py
        btn_continue = QtWidgets.QPushButton("المتابعة", self)
        btn_continue.setGeometry(QtCore.QRect(60, 320, 120, 40))
        btn_continue.setStyleSheet("background-color: white; color: black; font-weight: bold;")
        btn_continue.clicked.connect(self.open_next_form)

        # زر تغيير كلمة المرور
        btn_change_password = QtWidgets.QPushButton("تغيير كلمة المرور", self)
        btn_change_password.setGeometry(QtCore.QRect(450, 320, 120, 40))
        btn_change_password.setStyleSheet("background-color: white; color: black; font-weight: bold;")
        btn_change_password.clicked.connect(self.change_password)

    def change_password(self):
        text, ok = QtWidgets.QInputDialog.getText(
            self,
            "تغيير كلمة المرور",
            f"أدخل كلمة المرور الجديدة للمستخدم: {self.current_user}",
            QtWidgets.QLineEdit.Password
        )
        if ok and text:
            self.passwords[self.current_user] = text
            with open("passwords.json", "w", encoding="utf-8") as f:
                import json
                json.dump(self.passwords, f, ensure_ascii=False, indent=4)
            QtWidgets.QMessageBox.information(self, "نجاح",
                                              f"تم تغيير كلمة المرور بنجاح ✅ للمستخدم {self.current_user}")
        else:
            QtWidgets.QMessageBox.warning(self, "تنبيه", "لم يتم إدخال كلمة مرور جديدة.")

    # --- دوال التلاشي وعرض النموذج التالي ---
    def open_next_form(self):
        self.animation = QtCore.QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(500)  # نصف ثانية
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.finished.connect(self.show_next_form)
        self.animation.start()

    def show_next_form(self):
        self.hide()
        # تشغيل نافذة Tkinter كعملية مستقلة
        subprocess.Popen([sys.executable, "gestion.py"])
