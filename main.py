import sqlite3
import sys
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidgetItem, QHeaderView, QAbstractScrollArea



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(2)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        # Подключение к БД
        con = sqlite3.connect("coffee.db")

        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        result = cur.execute("""SELECT id, 
        name_of_sort as [Сорт],
        degree_of_roasting as [Степень обжарки],
        ground_or_grain as [Молотый/Зерновой],
        description_taste as [Описание вкуса],
        cost as [Цена],
        volume as [Объем] FROM list_coffee
        """).fetchall()

        for i in range(len(result)):
            for j in range(7):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(result[i][j])))
        self.tableWidget.resizeColumnsToContents()

        con.close()




def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())