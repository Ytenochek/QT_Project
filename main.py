import os
import sqlite3
import sys

from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QInputDialog,
    QMessageBox,
    QFileDialog,
    QDialog,
)


class Ui_MainWindow(object):
    """
    Класс с настройками для главного окна
    """
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 900)
        # MainWindow.setMinimumSize(QtCore.QSize(1000, 900))
        # MainWindow.setMaximumSize(QtCore.QSize(1000, 900))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(
            88, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_3.addItem(spacerItem)

        self.choose_lesson_act = QtWidgets.QComboBox(self.centralwidget)
        self.choose_lesson_act.setMinimumSize(QtCore.QSize(200, 0))
        self.choose_lesson_act.setMaximumSize(QtCore.QSize(300, 40))
        self.choose_lesson_act.setObjectName("comboBox")

        self.horizontalLayout_3.addWidget(self.choose_lesson_act)
        spacerItem1 = QtWidgets.QSpacerItem(
            88, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_3.addItem(spacerItem1)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.choose_lesson = QtWidgets.QComboBox(self.centralwidget)
        self.choose_lesson.setMinimumSize(QtCore.QSize(200, 0))
        self.choose_lesson.setMaximumSize(QtCore.QSize(300, 40))
        self.choose_lesson.setObjectName("choose_lesson")
        self.horizontalLayout_2.addWidget(self.choose_lesson)

        self.find_label = QtWidgets.QLineEdit(self.centralwidget)
        self.find_label.setMaximumSize(QtCore.QSize(300, 50))
        self.find_label.setObjectName("find_label")
        self.horizontalLayout_2.addWidget(self.find_label)

        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setMaximumSize(QtCore.QSize(150, 60))
        self.search.setSizeIncrement(QtCore.QSize(0, 0))

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)

        self.search.setFont(font)
        self.search.setIconSize(QtCore.QSize(16, 16))
        self.search.setObjectName("find")

        self.horizontalLayout_2.addWidget(self.search)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, 40, -1, -1)
        self.gridLayout.setObjectName("gridLayout")

        self.delete_rule = QtWidgets.QPushButton(self.centralwidget)
        self.delete_rule.setMaximumSize(QtCore.QSize(16777215, 60))

        font = QtGui.QFont()
        font.setPointSize(12)

        self.delete_rule.setFont(font)
        self.delete_rule.setObjectName("delete_rule")
        self.gridLayout.addWidget(self.delete_rule, 1, 1, 1, 1)

        self.add_rule = QtWidgets.QPushButton(self.centralwidget)
        self.add_rule.setMinimumSize(QtCore.QSize(600, 0))
        self.add_rule.setMaximumSize(QtCore.QSize(500, 60))

        font = QtGui.QFont()
        font.setPointSize(12)

        self.add_rule.setFont(font)
        self.add_rule.setObjectName("add_rule")
        self.gridLayout.addWidget(self.add_rule, 0, 1, 1, 1)

        self.add_lesson = QtWidgets.QPushButton(self.centralwidget)
        self.add_lesson.setMaximumSize(QtCore.QSize(500, 60))

        font = QtGui.QFont()
        font.setPointSize(12)

        self.add_lesson.setFont(font)
        self.add_lesson.setObjectName("add_lesson")
        self.gridLayout.addWidget(self.add_lesson, 0, 0, 1, 1)

        self.change_rule = QtWidgets.QPushButton(self.centralwidget)
        self.change_rule.setMaximumSize(QtCore.QSize(100000, 60))

        font = QtGui.QFont()
        font.setPointSize(12)

        self.change_rule.setFont(font)
        self.change_rule.setObjectName("change_rule")
        self.gridLayout.addWidget(self.change_rule, 2, 1, 1, 1)

        self.delete_lesson = QtWidgets.QPushButton(self.centralwidget)
        self.delete_lesson.setMaximumSize(QtCore.QSize(16777215, 60))

        font = QtGui.QFont()
        font.setPointSize(12)

        self.delete_lesson.setFont(font)
        self.delete_lesson.setObjectName("delete_lesson")
        self.gridLayout.addWidget(self.delete_lesson, 1, 0, 1, 1)

        self.change_lesson = QtWidgets.QPushButton(self.centralwidget)
        self.change_lesson.setMaximumSize(QtCore.QSize(16777215, 60))

        font = QtGui.QFont()
        font.setPointSize(12)

        self.change_lesson.setFont(font)
        self.change_lesson.setObjectName("change_lesson")
        self.gridLayout.addWidget(self.change_lesson, 2, 0, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)
        self.detail = QtWidgets.QPushButton(self.centralwidget)
        self.detail.setMaximumSize(QtCore.QSize(16777215, 60))

        font = QtGui.QFont()
        font.setPointSize(12)

        self.detail.setFont(font)
        self.detail.setObjectName("detail")
        self.verticalLayout_2.addWidget(self.detail)

        self.find_result = QtWidgets.QTableWidget(self.centralwidget)
        self.find_result.setMaximumSize(QtCore.QSize(16777215, 400))
        self.find_result.setObjectName("tableWidget")
        self.find_result.setColumnCount(0)
        self.find_result.setRowCount(0)
        self.verticalLayout_2.addWidget(self.find_result)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Школьный справочник"))
        self.search.setText(_translate("MainWindow", "Искать"))
        self.delete_rule.setText(_translate("MainWindow", "Удалить правило"))
        self.add_rule.setText(_translate("MainWindow", "Добавить правило"))
        self.add_lesson.setText(_translate("MainWindow", "Добавить предмет"))
        self.change_rule.setText(_translate("MainWindow", "Изменить правило"))
        self.delete_lesson.setText(_translate("MainWindow", "Удалить предмет"))
        self.change_lesson.setText(_translate("MainWindow", "Изменить предмет"))
        self.detail.setText(_translate("MainWindow", "Подробнее"))


class Ui_Dialog(object):
    """
    Класс с настройками для окна с картинками
    """
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        Dialog.setMinimumSize(QtCore.QSize(640, 480))

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.image = QtWidgets.QLabel(Dialog)
        self.image.setMinimumSize(QtCore.QSize(600, 400))
        self.image.setText("")
        self.image.setObjectName("label")
        self.verticalLayout_2.addWidget(self.image)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 90, -1, -1)
        self.horizontalLayout.setSpacing(100)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.previous_picture = QtWidgets.QPushButton(Dialog)
        self.previous_picture.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.previous_picture)

        self.exit_button = QtWidgets.QPushButton(Dialog)
        self.exit_button.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.exit_button)

        self.next_picture = QtWidgets.QPushButton(Dialog)
        self.next_picture.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.next_picture)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Картинки"))
        self.previous_picture.setText(_translate("Dialog", "<"))
        self.exit_button.setText(_translate("Dialog", "Выход"))
        self.next_picture.setText(_translate("Dialog", ">"))


class Main(QMainWindow, Ui_MainWindow):
    """
    Класс, описывающий функциональность виджетов главного окна приложения и логику взаимодействия с базой данных
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("reading-book.ico"))

        self.db = sqlite3.connect("Handbook.db")  # TODO: Сделать проверку на наличие базы данных
        self.db.cursor().execute("PRAGMA foreign_keys=ON")  # Фикс бага с БД (не работал CASCADE)

        # Связь функций с виджетами
        self.search.clicked.connect(self.update_lesson_list)
        self.delete_lesson.clicked.connect(self.delete_lesson_f)
        self.add_lesson.clicked.connect(self.add_lesson_f)
        self.change_lesson.clicked.connect(self.change_lesson_f)
        self.delete_rule.clicked.connect(self.delete_rule_f)
        self.add_rule.clicked.connect(self.add_rule_f)
        self.change_rule.clicked.connect(self.change_rule_f)
        self.detail.clicked.connect(self.detail_f)
        self.choose_lesson.currentIndexChanged.connect(self.update_lesson_list)

        self.refresh()

    def keyPressEvent(self, event):
        """
        Горячие клавиши:
        esc - выход

        ctrl + N - добавить правило
        ctrl + C - изменить правило
        ctrl + Delete - удалить правило
        ctrl + Alt - подробности правила

        ctrl + shift + N - добавить урок
        ctrl + shift + C - изменить урок
        ctrl + shift + Delete - удалить урок
        """
        if event.key() == Qt.Key_Escape:
            self.close()

        if int(event.modifiers()) == Qt.ControlModifier:

            if event.key() == Qt.Key_N:
                self.add_rule_f()

            if event.key() == Qt.Key_C:
                self.change_rule_f()

            if event.key() == Qt.Key_Delete:
                self.delete_rule_f()

            if event.key() == Qt.Key_Alt:
                self.detail_f()

        if int(event.modifiers()) == (Qt.ControlModifier + Qt.ShiftModifier):

            if event.key() == Qt.Key_N:
                self.add_lesson_f()

            if event.key() == Qt.Key_C:
                self.change_lesson_f()

            if event.key() == Qt.Key_Delete:
                self.delete_lesson_f()

    def update_lesson_list(self):
        """
        Обновление списка правил по уроку
        """
        cur = self.db.cursor()
        lesson_id = cur.execute(
            f"""SELECT id FROM Lessons WHERE Name=?""",
            (self.choose_lesson.currentText(),),
        ).fetchall()

        res = []

        if lesson_id:
            res = cur.execute(
                f"""SELECT * FROM main WHERE Short_rule LIKE ? AND Lesson_id = ?""",
                ("%" + self.find_label.text() + "%", lesson_id[0][0]),
            ).fetchall()  # Результат поиска

        # Отображение результата в таблице
        if res:
            self.find_result.setRowCount(len(res))
            self.find_result.setColumnCount(2)

            for i, elem in enumerate(res):
                self.find_result.setItem(i, 0, QtWidgets.QTableWidgetItem(str(elem[0])))
                self.find_result.setItem(i, 1, QtWidgets.QTableWidgetItem(str(elem[2])))

            self.find_result.setHorizontalHeaderLabels(("id", "Правило"))
            self.find_result.resizeColumnsToContents()
            self.find_result.resizeRowsToContents()

        else:
            self.clear_result()

    def clear_result(self):
        """
        Очистка таблицы
        """
        self.find_result.setRowCount(0)
        self.find_result.setColumnCount(0)
        self.find_result.clear()

    def refresh(self):
        """
        Обновление списки уроков
        """
        self.choose_lesson_act.clear()
        self.choose_lesson.clear()

        cur = self.db.cursor()
        res = cur.execute("SELECT Name FROM Lessons").fetchall()

        for lesson in res:
            self.choose_lesson_act.addItem(str(lesson[0]))
            self.choose_lesson.addItem(str(lesson[0]))

    def delete_lesson_f(self):
        """
        Удаление урока
        """
        cur = self.db.cursor()
        valid = QMessageBox.question(
            self,
            "Удалить",
            f"Действительно удалить пердмет: {self.choose_lesson_act.currentText()}",
            QMessageBox.Yes,
            QMessageBox.No,
        )

        if valid == QMessageBox.Yes:
            cur.execute(
                f"DELETE FROM Lessons WHERE Name = ?",
                (self.choose_lesson_act.currentText(),),
            )
            self.db.commit()
            self.refresh()

    def add_lesson_f(self):
        """
        Добавление урока
        """
        cur = self.db.cursor()
        name, ok_pressed = QInputDialog.getText(
            self, "Введите название предмета", "Название предмета:"
        )

        if ok_pressed:
            cur.execute(f"INSERT INTO Lessons(Name) VALUES(?)", (name,))
            self.db.commit()
            self.refresh()

    def change_lesson_f(self):
        """
        Изменение урока
        """
        cur = self.db.cursor()
        name, ok_pressed = QInputDialog.getText(
            self,
            "Введите название предмета",
            "Название предмета:",
            text=f"{self.choose_lesson_act.currentText()}",
        )

        if ok_pressed:
            cur.execute(
                f"""UPDATE Lessons SET Name = ? WHERE Name = ?""",
                (name, self.choose_lesson_act.currentText()),
            )
            self.db.commit()
            self.refresh()

    def delete_rule_f(self):
        """
        Удаление правила
        """
        cur = self.db.cursor()
        msg = QMessageBox()

        msg.setWindowTitle("Удалить")
        rows = list(set([i.row() for i in self.find_result.selectedItems()]))

        if rows:
            ids = [self.find_result.item(i, 0).text() for i in rows]
            valid = QMessageBox.question(
                self,
                "",
                "Действительно удалить правила с id " + ",".join(ids),
                QMessageBox.Yes,
                QMessageBox.No,
            )  # Подтверждение

            if valid == QMessageBox.Yes:
                cur.execute(
                    "DELETE FROM main WHERE id IN (" + ", ".join("?" * len(ids)) + ")",
                    ids,
                )
                self.db.commit()

            self.update_lesson_list()

    def add_rule_f(self):
        """
        Добавление правило
        """
        cur = self.db.cursor()
        res = cur.execute("SELECT Name FROM Lessons").fetchall()
        res = list(map(lambda x: str(x[0]), res))

        lesson, ok_pressed = QInputDialog.getItem(
            self,
            "Добавить правило",
            "Название предмета:",
            res,
            res.index(self.choose_lesson.currentText()),
            False,
        )  # Выбрать предмет

        if ok_pressed:
            answer1, ok_pressed = QInputDialog.getText(
                self,
                "Добавить правило",
                "Название правила:",
                text=self.find_label.text(),
            )  # Ввести название

            if ok_pressed:
                answer2, ok_pressed = QInputDialog.getMultiLineText(
                    self, "Добавить правило", "Полное правило:"
                )  # Ввести полное правило

                if ok_pressed:
                    file_dialog = QFileDialog()
                    file_dialog.setFileMode(QFileDialog.ExistingFiles)
                    filt = "JPEG (*.jpg);;PNG (*.png);;Все файлы (*)"
                    fnames = file_dialog.getOpenFileNames(
                        self, "Выбрать файлы", "C://Desktop", filt
                    )[0]  # Выбрать картинки

                    if not fnames:
                        fnames = None

                    else:
                        fnames = "|".join(fnames)

                    cur.execute(
                        f"""INSERT INTO main(Lesson_id, Short_rule, Full_rule, Picture_path) VALUES((SELECT id FROM Lessons WHERE Name = ?), ?, ?, ?)""",
                        (lesson, answer1, answer2, fnames),
                    )  # Сохранить в БД
                    self.db.commit()

        self.update_lesson_list()

    def change_rule_f(self):
        """
        Изменение правила
        """
        cur = self.db.cursor()
        rows = list(set([i.row() for i in self.find_result.selectedItems()]))
        ids = [self.find_result.item(i, 0).text() for i in rows][0]
        for id_ in ids:
            lessons = cur.execute("SELECT Name FROM Lessons").fetchall()
            lessons = list(map(lambda x: x[0], lessons))

            lesson, ok_pressed = QInputDialog.getItem(
                self,
                "Изменить правило",
                "Название предмета:",
                lessons,
                lessons.index(self.choose_lesson.currentText()),
                False,
            )
            current_rule = cur.execute("SELECT * FROM main WHERE id = ?", (id_,)).fetchone()

            if ok_pressed:
                answer1, ok_pressed = QInputDialog.getText(
                    self, "Изменить правило", "Название правила:", text=current_rule[2]
                )

                if ok_pressed:
                    answer2, ok_pressed = QInputDialog.getMultiLineText(
                        self, "Изменить правило", "Полное правило:", text=current_rule[3]
                    )

                    if ok_pressed:
                        file_dialog = QFileDialog()
                        file_dialog.setFileMode(QFileDialog.ExistingFiles)
                        filt = "JPEG (*.jpg);;PNG (*.png);;Все файлы (*)"
                        fnames = file_dialog.getOpenFileNames(
                            self, "Выбрать файлы", current_rule[4].split("|")[0], filt
                        )[0]

                        if not fnames:
                            fnames = None
                        else:
                            fnames = "|".join(fnames)

                        cur.execute(
                            f"""UPDATE main 
                        SET Lesson_id = (SELECT id FROM Lessons WHERE Name = ?),
                            Short_rule = ?,
                            Full_rule = ?,
                            Picture_path = ?
                        WHERE id = ?""",
                            (lesson, answer1, answer2, fnames, id_),
                        )
                        self.db.commit()

        self.update_lesson_list()

    def detail_f(self):
        """
        Получение подробной информации о правиле (получиние и отображение данных из БД)
        """
        cur = self.db.cursor()
        rows = list(set([i.row() for i in self.find_result.selectedItems()]))

        if rows:
            ids = [self.find_result.item(i, 0).text() for i in rows]
            for id_ in ids:
                res = cur.execute(f"SELECT * FROM main WHERE id = ?", (id_,)).fetchone()
                lesson = cur.execute(
                    f"SELECT Name FROM Lessons WHERE id = ?", (res[1],)
                ).fetchone()

                # Окно с информацией
                dialog = QMessageBox()
                dialog.setWindowTitle("Подробности")
                dialog.setWindowIcon(QtGui.QIcon("reading-book.ico"))
                dialog.setText(
                    f"Пердмет: {lesson[0]}\nНазвание правила: {res[2]}\nПолное правило: \n{res[3]}"
                )
                dialog.addButton(QtWidgets.QPushButton("Закрыть"), QMessageBox.NoRole)
                dialog.addButton(
                    QtWidgets.QPushButton("Показать картинку"), QMessageBox.YesRole
                )
                show_pic = dialog.exec_()

                if show_pic:  # Если пользователь захочет посмотреть картинки
                    self.show_pictures(res[4])

        self.update_lesson_list()

    def show_pictures(self, paths):
        """
        Открытие окна для просмотра картинок
        """
        pic_dialog = PictureShow(self, paths=paths.split("|"))
        pic_dialog.exec_()


class PictureShow(QDialog, Ui_Dialog):
    """
    Окно для отображения картинок
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.setupUi(self)

        self.paths = kwargs["paths"]
        self.ending = self.paths[0].split(".")[-1].replace("jpg", "jpeg")

        self.setWindowIcon(QtGui.QIcon("reading-book.ico"))

        self.previous_picture.clicked.connect(self.prev)
        self.next_picture.clicked.connect(self.nxt)
        self.exit_button.clicked.connect(self.close_window)

        self.show_image()

    def keyPressEvent(self, event):
        """
        Горячие клавиши:
        esc - выход

        Правая стрелка - следующая картинка
        Левая стрелка - предыдущая картинка
        """
        if event.key() == Qt.Key_Escape:
            self.close_window()

        if event.key() == Qt.RightArrow:
            self.nxt()

        if event.key() == Qt.LeftArrow:
            self.prev()

    def close_window(self):
        """
        Закрытие окна
        """
        os.remove(f"tmp.{self.ending}")
        self.close()

    def prev(self):
        """
        Выбрать предыдущую картинку
        """
        self.paths.insert(0, self.paths.pop(-1))
        self.show_image()

    def nxt(self):
        """
        Выбрать следующую картинку
        """
        self.paths.append(self.paths.pop(0))  # Картинки повторяются по кругу
        self.show_image()

    def show_image(self):
        """
        Отображение картинки
        """
        try:
            Image.open(self.paths[0]).resize((600, 400)).save(
                f"tmp.{self.ending}", f"{self.ending.upper()}"
            )  # Создаём временную картинку для отображения
            self.image.setPixmap(QPixmap(f"tmp.{self.ending}"))
        except FileNotFoundError:
            self.paths = ["Pictures/Nothing.jpg"]  # Картинка по умолчанию
            Image.open(self.paths[0]).resize((600, 400)).save(
                f"tmp.{self.ending}", f"{self.ending.upper()}"
            )
            self.image.setPixmap(QPixmap(f"tmp.{self.ending}"))


def except_hook(cls, exception, traceback):
    """
    Отображение исключений
    """
    sys.__excepthook__(cls, exception, traceback)


# Запуск программы
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
