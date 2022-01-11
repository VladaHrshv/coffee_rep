import sqlite3
import sys
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidgetItem, QHeaderView, QAbstractScrollArea



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        # Подключение к БД

        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        result = cur.execute("""SELECT id, 
                name_of_sort as [Сорт],
                degree_of_roasting as [Степень обжарки],
                ground_or_grain as [Молотый/Зерновой],
                description_taste as [Описание вкуса],
                cost as [Цена],
                volume as [Объем] FROM list_coffee
                """).fetchall()
        self.tableWidget.setRowCount(len(result))

        self.titles = [description[0] for description in cur.description]
        self.tableWidget.setColumnCount(len(self.titles))
        self.tableWidget.setHorizontalHeaderLabels(self.titles)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
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