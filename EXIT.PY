# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import json
import os
import sys
import subprocess

class WelcomeNext(QtWidgets.QDialog):
    def __init__(self, current_user, passwords):
        super().__init__()
        self.current_user = current_user
        self.passwords = passwords
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("واجهة الخروج")
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)  # تعطيل زر X
        self.resize(600, 450)
        self.setStyleSheet("background-color: #D35400; color: white;")
        icon_path = "images/ITP1.ico"
        if os.path.exists(icon_path):
            self.setWindowIcon(QtGui.QIcon(icon_path))

        # العبارة الأولى مع علامة الاستفهام ❓
        self.label = QtWidgets.QLabel("هل تريد الخروج من البرنامج ❓", self)
        self.label.setGeometry(QtCore.QRect(150, 20, 300, 50))
        self.label.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("border: 4px solid #FFFFFF; border-radius: 5px; padding: 5px;")

        # باقي العبارات
        self.welcome_label = QtWidgets.QLabel("سيتم حفظ جميع البيانات", self)
        self.welcome_label.setGeometry(QtCore.QRect(60, 80, 500, 55))
        self.welcome_label.setFont(QtGui.QFont("Arial", 20, QtGui.QFont.Bold))
        self.welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_label.setStyleSheet("border: 4px solid #FFFFFF; border-radius: 5px; padding: 5px;")

        self.welcome_label_2 = QtWidgets.QLabel("تحياتي لكم و بالتوفيق", self)
        self.welcome_label_2.setGeometry(QtCore.QRect(60, 140, 500, 55))
        self.welcome_label_2.setFont(QtGui.QFont("Arial", 20, QtGui.QFont.Bold))
        self.welcome_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_label_2.setStyleSheet("border: 4px solid #FFFFFF; border-radius: 5px; padding: 5px;")

        self.welcome_label_3 = QtWidgets.QLabel("أخوكم المفتش سماحي يوسف", self)
        self.welcome_label_3.setGeometry(QtCore.QRect(60, 200, 500, 50))
        self.welcome_label_3.setFont(QtGui.QFont("Arial", 18, QtGui.QFont.Bold))
        self.welcome_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_label_3.setStyleSheet("border: 4px solid #FFFFFF; border-radius: 5px; padding: 5px;")

        # زر الحفظ والخروج مع التلاشي
        btn_save_exit = QtWidgets.QPushButton("💾 إغلاق", self)
        btn_save_exit.setGeometry(QtCore.QRect(150, 320, 140, 50))
        btn_save_exit.setStyleSheet("background-color: white; color: black; font-weight: bold; font-size: 14px;")
        btn_save_exit.clicked.connect(self.fade_and_save_exit)

        # زر التراجع
        btn_back = QtWidgets.QPushButton("⬅️ تراجع", self)
        btn_back.setGeometry(QtCore.QRect(310, 320, 140, 50))
        btn_back.setStyleSheet("background-color: white; color: black; font-weight: bold; font-size: 14px;")
        btn_back.clicked.connect(self.fade_and_go_back)

    # --- دوال التلاشي لكل زر ---
    def fade_and_save_exit(self):
        self.animation = QtCore.QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(500)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.finished.connect(self.save_exit)
        self.animation.start()

    def fade_and_go_back(self):
        self.animation = QtCore.QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(500)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.finished.connect(self.open_gestion)
        self.animation.start()

    # --- دوال التنفيذ النهائي لكل زر ---
    def save_exit(self):
        with open("passwords.json", "w", encoding="utf-8") as f:
            json.dump(self.passwords, f, ensure_ascii=False, indent=4)
        QtWidgets.QMessageBox.information(self, "تم الحفظ", "تم حفظ البيانات والخروج من البرنامج.")

    def open_gestion(self):
        self.close()
        subprocess.Popen([sys.executable, "GESTION.py"])

# --- تشغيل الواجهة مباشرة إذا تم فتح الملف ---
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WelcomeNext(current_user="المستخدم الحالي", passwords={})
    window.show()
    sys.exit(app.exec_())
