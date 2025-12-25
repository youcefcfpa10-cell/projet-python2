# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import json
# تحديد المسار الحالي للملف
current_dir = os.getcwd()
password_file = os.path.join(current_dir, "passwords.json")

# التحقق إن كان الملف موجودًا، وإذا لم يكن، يتم إنشاؤه تلقائيًا
if not os.path.exists(password_file):
    with open(password_file, "w", encoding="utf-8") as f:
        json.dump({}, f, ensure_ascii=False, indent=4)
    print("✅ تم إنشاء ملف passwords.json في:", password_file)
else:
    print("📂 الملف موجود بالفعل:", password_file)

# تحميل محتوى الملف
with open(password_file, "r", encoding="utf-8") as f:
    passwords = json.load(f)

print("Loaded passwords:", passwords)
# ✅ إضافة دالة إدخال المستخدمين
def add_password(username, password):
    # قراءة البيانات الموجودة حاليًا
    with open(password_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # إضافة المستخدم الجديد أو تحديثه
    data[username] = password

    # حفظ البيانات في الملف من جديد
    with open(password_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"✅ تم حفظ كلمة المرور للمستخدم: {username}")


# --- اختبار عملي ---
add_password("IFEP", "1234")
add_password("ITP", "12345")
from welcome_next import WelcomeNext  # استدعاء النافذة الثانية

class Ui_welcom(object):
    def setupUi(self, welcom):
        welcom.setObjectName("welcom")
        welcom.resize(950, 800)
        welcom.setStyleSheet("QDialog { background-color: #D35400; }")

        icon_path = os.path.join("images", "ITP1.ICO")
        if os.path.exists(icon_path):
            welcom.setWindowIcon(QtGui.QIcon(icon_path))
        welcom.setWindowTitle("واجهة الدخول")

        self.attempts = 0

        # ======= تحميل كلمات المرور من الملف =======
        self.load_passwords()  # استدعاء دالة التحميل

        # ===== العناوين =====
        self.label = QtWidgets.QLabel(welcom)
        self.label.setGeometry(QtCore.QRect(150, 10, 651, 41))
        font = QtGui.QFont("Arial", 14, QtGui.QFont.Bold)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("تم تصميم هذا التطبيق من طرف المفتش التقني و البيداغوجي")

        self.label_2 = QtWidgets.QLabel(welcom)
        self.label_2.setGeometry(QtCore.QRect(560, 50, 120, 41))
        self.label_2.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        self.label_2.setText("سماحي يوسف")

        self.label_3 = QtWidgets.QLabel(welcom)
        self.label_3.setGeometry(QtCore.QRect(200, 50, 300, 41))
        self.label_3.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setText("المقاطعة البيداغوجية رقم:45")

        # ===== الصور =====
        self.label_4 = QtWidgets.QLabel(welcom)
        self.label_4.setGeometry(QtCore.QRect(840, 5, 100, 110))
        self.label_4.setPixmap(QtGui.QPixmap("images/drapo.jpg"))
        self.label_4.setScaledContents(True)

        self.label_5 = QtWidgets.QLabel(welcom)
        self.label_5.setGeometry(QtCore.QRect(10, 5, 100, 110))
        self.label_5.setPixmap(QtGui.QPixmap("images/logo.jpg"))
        self.label_5.setScaledContents(True)

        self.label_6 = QtWidgets.QLabel(welcom)
        self.label_6.setGeometry(QtCore.QRect(10, 135, 920, 380))
        self.label_6.setPixmap(QtGui.QPixmap("images/CFPA.jpg"))
        self.label_6.setScaledContents(True)

        # ===== إطار تسجيل الدخول =====
        self.frame = QtWidgets.QFrame(welcom)
        self.frame.setGeometry(QtCore.QRect(260, 530, 481, 140))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setStyleSheet("background-color: #d2b48c; border: 4px solid #4682B4; border-radius: 10px;")

        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(350, 5, 125, 130))
        self.label_7.setPixmap(QtGui.QPixmap("images/cle.jpg"))
        self.label_7.setScaledContents(True)

        font12 = QtGui.QFont("Arial", 12, QtGui.QFont.Bold)
        font10 = QtGui.QFont("Arial", 10, QtGui.QFont.Bold)

        self.label_8 = QtWidgets.QLabel("إسم المستخدم:", self.frame)
        self.label_8.setGeometry(QtCore.QRect(220, 10, 120, 31))
        self.label_8.setFont(font12)

        self.label_9 = QtWidgets.QLabel("كلمة المرور:", self.frame)
        self.label_9.setGeometry(QtCore.QRect(220, 50, 120, 31))
        self.label_9.setFont(font12)

        self.label_10 = QtWidgets.QLabel("إظهار كلمة المرور:", self.frame)
        self.label_10.setGeometry(QtCore.QRect(100, 90, 140, 31))
        self.label_10.setFont(font10)

        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 201, 31))
        self.comboBox.setFont(font12)
        self.comboBox.addItems(["إختر إسم المستخدم", "IFEP", "ITP"])
        self.comboBox.setStyleSheet("background-color: white; color: black;")

        self.lineEdit_password = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_password.setGeometry(QtCore.QRect(13, 50, 191, 31))
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.returnPressed.connect(lambda: self.on_ok_clicked(welcom))
        self.lineEdit_password.setStyleSheet("background-color: white; color: black;")
        self.lineEdit_password.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))

        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(40, 100, 21, 20))
        self.checkBox.stateChanged.connect(self.toggle_password)
        self.checkBox.setStyleSheet("background-color: white;")

        self.label_11 = QtWidgets.QLabel(welcom)
        self.label_11.setGeometry(QtCore.QRect(50, 530, 131, 140))
        self.label_11.setPixmap(QtGui.QPixmap("images/enter.jpg"))
        self.label_11.setScaledContents(True)
        self.label_11.mousePressEvent = lambda event: self.on_ok_clicked(welcom)

        self.label_15 = QtWidgets.QLabel("أدخل إسم المستخدم و كلمة المرور ثم إضغط الزر enter", welcom)
        self.label_15.setGeometry(QtCore.QRect(200, 680, 550, 31))
        self.label_15.setFont(font10)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)

        self.progressBar = QtWidgets.QProgressBar(welcom)
        self.progressBar.setGeometry(QtCore.QRect(50, 710, 850, 20))
        self.progressBar.setValue(0)
        self.progressBar.hide()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_progress)

        self.progress_value = 0
        self.welcom_window = welcom

    # ===== دالة تحميل كلمات المرور =====
    def load_passwords(self):
        print("Current working directory:", os.getcwd())  # 👈 أضفه هنا
        if os.path.exists("passwords.json"):
            with open("passwords.json", "r", encoding="utf-8") as f:
                self.passwords = json.load(f)
        else:
            # القيم الافتراضية إذا لم يوجد الملف
            self.passwords = {"IFEP": "1234", "ITP": "12345"}
        print("Loaded passwords:", self.passwords)  # 👈 أضف هذا

    def toggle_password(self, state):
        self.lineEdit_password.setEchoMode(
            QtWidgets.QLineEdit.Normal if state == QtCore.Qt.Checked else QtWidgets.QLineEdit.Password
        )

    def on_ok_clicked(self, welcom):
        username = self.comboBox.currentText()
        password = self.lineEdit_password.text()

        if username in self.passwords and password == self.passwords[username]:
            self.current_user = username
            self.progress_value = 0
            self.progressBar.setValue(0)
            self.progressBar.show()
            self.timer.start(30)
        else:
            self.attempts += 1
            remaining = 3 - self.attempts
            if remaining > 0:
                QtWidgets.QMessageBox.warning(welcom, "خطأ",
                    f"إسم المستخدم أو كلمة المرور غير صحيحة ❌\nتبقى لديك {remaining} محاولات.")
            else:
                QtWidgets.QMessageBox.critical(welcom, "فشل",
                    "لقد تجاوزت عدد المحاولات المسموح بها ❌\nسيتم إغلاق البرنامج.")
                QtCore.QCoreApplication.quit()

    def update_progress(self):
        if self.progress_value < 100:
            self.progress_value += 2
            self.progressBar.setValue(self.progress_value)
        else:
            self.timer.stop()
            self.progressBar.hide()
            self.open_next_form()

    def save_passwords(self):
        with open("passwords.json", "w", encoding="utf-8") as f:
            json.dump(self.passwords, f, ensure_ascii=False, indent=4)

    def open_next_form(self):
        self.welcom_window.close()
        self.next_dialog = WelcomeNext(self.current_user, self.passwords)
        self.next_dialog.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    welcom = QtWidgets.QDialog()
    ui = Ui_welcom()
    ui.setupUi(welcom)
    welcom.show()
    sys.exit(app.exec_())
