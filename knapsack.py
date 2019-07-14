import sys
import time
from DP import knapsack_dp
from BranchAndBound import knapsack_BB
from Greedy import greedy
from getData import  getData
from  Greedy import  greedyH2
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui


class MyTable(QTableWidget):
    """docstring for MyTable"""

    def __init__(self, parent=None):
        super(MyTable, self).__init__(1, 2, parent)
        headertitle = ("Poids", "Valeur")
        self.setHorizontalHeaderLabels(headertitle)
        self.verticalHeader().hide()
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.cellChanged.connect(self._cellclicked)

    @QtCore.pyqtSlot(int, int)
    def _cellclicked(self, r, c):
        it = self.item(r, c)
        it.setTextAlignment(QtCore.Qt.AlignCenter)

    @QtCore.pyqtSlot()
    def _addrow(self):
        rowcount = self.rowCount()
        self.insertRow(rowcount)
        a_window.nbr_text.setText(str (int(a_window.nbr_text.text())+1))

    @QtCore.pyqtSlot()
    def _removerow(self):
        if self.rowCount() > 0:
            self.removeRow(self.rowCount() - 1)

    def loadInstance(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            instance =getData(fileName)
            items = instance[0]
            print(items)
            nbr = instance[1]
            cap = instance[2]
            a_window.nbr_text.setText(str(nbr))
            a_window.capacity_text.setText(str(cap))
            self.setRowCount(0)
            for i, item in enumerate(items):
                row = self.rowCount()
                self.insertRow(row)
                self.setItem(i, 0, QTableWidgetItem(str(item[0])))
                self.setItem(i, 1, QTableWidgetItem(str(item[1])))

    def showResult(self):

        items = []
        for row in range(self.rowCount()-1):
            print(str(self.item(row, 0).text()))
            weight = int(self.item(row, 0).text())
            value = int(self.item(row, 1).text())
            items.append([weight, value])
        print(items)
        capacity = int(a_window.capacity_text.text())
        start = time.time()
        solution = knapsack_dp(items, capacity)
        solution_items = solution[2]
        end = time.time()
        result = a_window.table_widget.tab1.result_table
        result.setRowCount(0)
        for i, itemSol in enumerate(solution_items):
            row = result.rowCount()
            result.insertRow(row)
            result.setItem(i, 0, QTableWidgetItem(str(itemSol[0])))
            result.setItem(i, 1, QTableWidgetItem(str(itemSol[1])))
            print(itemSol)

        a_window.table_widget.tab1.StatsTable.setItem(0, 0, QTableWidgetItem(str(solution[0])))
        a_window.table_widget.tab1.StatsTable.setItem(1, 0, QTableWidgetItem(str(solution[1])))
        a_window.table_widget.tab1.StatsTable.setItem(2, 0, QTableWidgetItem(str((end - start) * 1000) + "ms"))

    def showResult2(self):

        items = []
        for row in range(self.rowCount()):
            weight = int(self.item(row, 0).text())
            value = int(self.item(row, 1).text())
            items.append([weight, value])
        print(items)
        capacity = int(a_window.capacity_text.text())
        start = time.time()
        solution = knapsack_BB(items, capacity)
        solution_items = solution[2]
        end = time.time()
        print(end - start)
        result = a_window.table_widget.tab1.result_table2
        result.setRowCount(0)
        for i, itemSol in enumerate(solution_items):
            row = result.rowCount()
            result.insertRow(row)
            result.setItem(i, 0, QTableWidgetItem(str(itemSol[0])))
            result.setItem(i, 1, QTableWidgetItem(str(itemSol[1])))
            print(itemSol)

        a_window.table_widget.tab1.StatsTable2.setItem(0, 0, QTableWidgetItem(str(solution[0])))
        a_window.table_widget.tab1.StatsTable2.setItem(1, 0, QTableWidgetItem(str(solution[1])))
        a_window.table_widget.tab1.StatsTable2.setItem(2, 0, QTableWidgetItem(str((end - start) * 1000) + "ms"))

    def showResultGreedy1(self):

            items = []
            for row in range(self.rowCount()):
                weight = int(self.item(row, 0).text())
                value = int(self.item(row, 1).text())
                items.append([weight, value])
            print(items)
            capacity = int(a_window.capacity_text.text())
            start = time.time()
            solution = greedy(items, capacity)
            solution_items = solution[0]
            end = time.time()
            print(end - start)
            result = a_window.table_widget.tab2.result_table
            result.setRowCount(0)
            print(solution_items)
            for i, itemSol in enumerate(solution_items):
                row = result.rowCount()
                result.insertRow(row)
                result.setItem(i, 0, QTableWidgetItem(str(itemSol[0])))
                result.setItem(i, 1, QTableWidgetItem(str(itemSol[2])))
                print(itemSol)

            a_window.table_widget.tab2.StatsTable.setItem(0, 0, QTableWidgetItem(str(solution[1])))
            a_window.table_widget.tab2.StatsTable.setItem(1, 0, QTableWidgetItem(str(solution[2])))
            a_window.table_widget.tab2.StatsTable.setItem(2, 0, QTableWidgetItem(str((end - start) * 1000) + "ms"))

    def showResultGreedy2(self):

            items = []
            for row in range(self.rowCount()):
                weight = int(self.item(row, 0).text())
                value = int(self.item(row, 1).text())
                items.append([weight, value])
            print(items)
            capacity = int(a_window.capacity_text.text())
            start = time.time()
            solution = greedyH2(items, capacity)
            solution_items = solution[0]
            print("solution "+ str(solution_items))

            end = time.time()
            print(end - start)
            result = a_window.table_widget.tab2.result_table2
            result.setRowCount(0)
            for i, itemSol in enumerate(solution_items):
                row = result.rowCount()
                result.insertRow(row)
                result.setItem(i, 0, QTableWidgetItem(str(items[i][0])))
                result.setItem(i, 1, QTableWidgetItem(str(itemSol)))
                print(itemSol)

            a_window.table_widget.tab2.StatsTable2.setItem(0, 0, QTableWidgetItem(str(solution[1])))
            a_window.table_widget.tab2.StatsTable2.setItem(1, 0, QTableWidgetItem(str(solution[2])))
            a_window.table_widget.tab2.StatsTable2.setItem(2, 0, QTableWidgetItem(str((end - start) * 1000) + "ms"))

class ResultTable(QTableWidget):
    """docstring for MyTable"""

    def __init__(self, parent=None):
        super(ResultTable, self).__init__(1, 2, parent)
        headertitle = ("Objet", "Nombre")
        self.setHorizontalHeaderLabels(headertitle)
        self.verticalHeader().hide()
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


class StatsTable(QTableWidget):
    """docstring for MyTable"""

    def __init__(self, parent=None):
        super(StatsTable, self).__init__(3, 1, parent)
        headertitle = ("Valeur totale", "Poids total", "Temps d'éxecution")
        self.setVerticalHeaderLabels(headertitle)
        self.horizontalHeader().hide()
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        super(QWidget, self).__init__(parent)

        self.layout = QVBoxLayout(self)
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tabs.resize(300, 200)
        self.tab1=ExactTab()
        self.tabs.addTab(self.tab1, "Méthodes exactes")
        self.tab2=HeuresTab()
        self.tabs.addTab(self.tab2, "heuristiques")
        self.tab3 = Metaheur()
        self.tabs.addTab(self.tab3, "Méta heuristiques")
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    @QtCore.pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

class ExactTab(QWidget):
    def __init__(self,parent=None):
        super(ExactTab,self).__init__(parent)
        h_box = QHBoxLayout()

        # result section
        self.show_result_btn = QPushButton("Afficher la solution")
        #self.show_result_btn.

        # result table
        self.result_table = ResultTable()
        self.StatsTable = StatsTable()
        self.DP_label = QLabel("La programmation dynamique: ")
        self.DP_label.setStyleSheet("font-family: seorge; font: bold 20px")
        # Vbox2
        v_box2 = QVBoxLayout()
        v_box2.addWidget(self.DP_label)
        v_box2.addWidget(self.show_result_btn)
        v_box2.addWidget(self.StatsTable, 1)
        v_box2.addWidget(self.result_table, 4)

        self.result_table2 = ResultTable()
        self.StatsTable2 = StatsTable()
        self.BB_label = QLabel("Branch and Bound ")
        self.BB_label.setStyleSheet("font-family: seorge; font: bold 20px")
        self.show_result_btn2 = QPushButton("Afficher la solution")
        # VBox3
        v_box3 = QVBoxLayout()
        v_box3.addWidget(self.BB_label)
        v_box3.addWidget(self.show_result_btn2)
        v_box3.addWidget(self.StatsTable2, 1)
        v_box3.addWidget(self.result_table2, 4)
        h_box.addLayout(v_box2, 1)
        h_box.addLayout(v_box3, 1)
        self.setLayout(h_box)


class HeuresTab(QWidget):
    def __init__(self, parent=None):
        super(HeuresTab, self).__init__(parent)
        h_box = QHBoxLayout()

        # result section
        self.show_result_btn = QPushButton("Afficher la solution")
        # self.show_result_btn.

        # result table
        self.result_table = ResultTable()
        self.StatsTable = StatsTable()
        self.DP_label = QLabel("Greedy1: ")
        self.DP_label.setStyleSheet("font-family: seorge; font: bold 20px")
        # Vbox2
        v_box2 = QVBoxLayout()
        v_box2.addWidget(self.DP_label)
        v_box2.addWidget(self.show_result_btn)
        v_box2.addWidget(self.StatsTable, 1)
        v_box2.addWidget(self.result_table, 4)

        self.result_table2 = ResultTable()
        self.StatsTable2 = StatsTable()
        self.BB_label = QLabel("Greedy2 ")
        self.BB_label.setStyleSheet("font-family: seorge; font: bold 20px")
        self.show_result_btn2 = QPushButton("Afficher la solution")
        # VBox3
        v_box3 = QVBoxLayout()
        v_box3.addWidget(self.BB_label)
        v_box3.addWidget(self.show_result_btn2)
        v_box3.addWidget(self.StatsTable2, 1)
        v_box3.addWidget(self.result_table2, 4)

        self.result_table3= ResultTable()
        self.StatsTable3 = StatsTable()
        self.greedy3_label = QLabel("Greedy3 ")
        self.greedy3_label.setStyleSheet("font-family: seorge; font: bold 20px")
        self.show_result_btn3 = QPushButton("Afficher la solution")
        v_box4 = QVBoxLayout()
        v_box4.addWidget(self.greedy3_label)
        v_box4.addWidget(self.show_result_btn3)
        v_box4.addWidget(self.StatsTable3, 1)
        v_box4.addWidget(self.result_table3, 4)

        best_label = QLabel("Meilleure heuristique:  ")
        best_text=QLineEdit()
        best_box = QHBoxLayout()
        best_box.addWidget(best_label)
        best_box.addWidget(best_text)
        h_box.addLayout(v_box2, 1)
        h_box.addLayout(v_box3, 1)
        h_box.addLayout(v_box4, 1)
        v_box=QVBoxLayout()
        v_box.addLayout(best_box)
        v_box.addLayout(h_box)
        self.setLayout(v_box)
class Metaheur(QWidget):
    def __init__(self,parent=None):
        super(Metaheur,self).__init__(parent)
        h_box = QHBoxLayout()

        # result section
        self.show_result_btn = QPushButton("Afficher la solution")
        #self.show_result_btn.

        # result table
        self.result_table = ResultTable()
        self.StatsTable = StatsTable()
        self.DP_label = QLabel("Recuit simulé: ")
        self.DP_label.setStyleSheet("font-family: seorge; font: bold 20px")
        # Vbox2
        v_box2 = QVBoxLayout()
        v_box2.addWidget(self.DP_label)
        v_box2.addWidget(self.show_result_btn)
        v_box2.addWidget(self.StatsTable, 1)
        v_box2.addWidget(self.result_table, 4)

        self.result_table2 = ResultTable()
        self.StatsTable2 = StatsTable()
        self.BB_label = QLabel("Algorithme génétique ")
        self.BB_label.setStyleSheet("font-family: seorge; font: bold 20px")
        self.param1_label=QLabel("Paramètre1 ")
        self.param1_text=QLineEdit()
        self.param1_box=QHBoxLayout()
        self.param1_box.addWidget(self.param1_label)
        self.param1_box.addWidget(self.param1_text)
        self.param2_label = QLabel("Paramètre2 ")
        self.param2_text = QLineEdit()
        self.param2_box = QHBoxLayout()
        self.param2_box.addWidget(self.param2_label)
        self.param2_box.addWidget(self.param2_text)
        self.param3_label = QLabel("Paramètre3 ")
        self.param3_text = QLineEdit()
        self.param3_box = QHBoxLayout()
        self.param3_box.addWidget(self.param3_label)
        self.param3_box.addWidget(self.param3_text)
        self.show_result_btn2 = QPushButton("Afficher la solution")
        v_box3 = QVBoxLayout()
        v_box3.addWidget(self.BB_label)
        v_box3.addLayout(self.param1_box)
        v_box3.addLayout(self.param2_box)
        v_box3.addLayout(self.param3_box)
        v_box3.addWidget(self.show_result_btn2)
        v_box3.addWidget(self.StatsTable2, 1)
        v_box3.addWidget(self.result_table2, 4)
        self.result_table3 = ResultTable()
        self.StatsTable3 = StatsTable()
        self.greedy3_label = QLabel("Algorithme génétique adaptative ")
        self.greedy3_label.setStyleSheet("font-family: seorge; font: bold 20px")

        self.show_result_btn3 = QPushButton("Afficher la solution")
        v_box4 = QVBoxLayout()
        v_box4.addWidget(self.greedy3_label)
        v_box4.addWidget(self.show_result_btn3)
        v_box4.addWidget(self.StatsTable3, 1)
        v_box4.addWidget(self.result_table3, 4)

        best_label = QLabel("Meilleure méta heuristique:  ")
        best_text = QLineEdit()
        best_box = QHBoxLayout()
        best_box.addWidget(best_label)
        best_box.addWidget(best_text)
        h_box.addLayout(v_box2, 1)
        h_box.addLayout(v_box3, 1)
        h_box.addLayout(v_box4, 1)
        v_box = QVBoxLayout()
        v_box.addLayout(best_box)
        v_box.addLayout(h_box)
        self.setLayout(v_box)



class window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Capacity field
        self.capacity_label = QLabel("Capacité: ")
        self.capacity_text = QLineEdit()
        self.nbr_label = QLabel("Nombre d'objets: ")
        self.nbr_text = QLineEdit()
        self.nbr_text.setText('0')
       # self.nbr_text.setDisabled(True)
        capacity_hbox = QHBoxLayout()
        capacity_hbox.addWidget(self.capacity_label)
        capacity_hbox.addWidget(self.capacity_text)
        nbr_hbox=QHBoxLayout()
        nbr_hbox.addWidget (self.nbr_label)
        nbr_hbox.addWidget(self.nbr_text)

        # objects table
        self.objects_table = MyTable()
        table_hbox = QHBoxLayout()
        table_hbox.addWidget(self.objects_table)
        # Vbox1
        self.add_btn = QPushButton("Ajouter un objet")
        self.add_btn.clicked.connect(self.objects_table._addrow)

        self.loadData= QPushButton("Télécharger une instance")
        self.loadData.clicked.connect(self.objects_table.loadInstance)
        v_box1 = QVBoxLayout()
        v_box1.addLayout(capacity_hbox)
        v_box1.addLayout(nbr_hbox)
        v_box1.addWidget(self.add_btn)
        v_box1.addWidget(self.loadData)
        v_box1.addLayout(table_hbox)
        v_box4 = QVBoxLayout()
        self.table_widget = MyTableWidget(self)
        v_box4.addWidget(self.table_widget)
        self.table_widget.tab1.show_result_btn.clicked.connect(self.objects_table.showResult)
        self.table_widget.tab1.show_result_btn2.clicked.connect(self.objects_table.showResult2)
        self.table_widget.tab2.show_result_btn.clicked.connect(self.objects_table.showResultGreedy1)
        self.table_widget.tab2.show_result_btn2.clicked.connect(self.objects_table.showResultGreedy2)
        # main layout
        h_box = QHBoxLayout()
        h_box.addLayout(v_box1, 1)
        h_box.addLayout(v_box4, 3)

        self.setLayout(h_box)
        self.setGeometry(0, 0, 1700, 700)
        self.setWindowTitle("Le problème du sac à dos")
        self.show()


WEIGHT, VALUE = range(2)
items = []
capacity = 0
app = QApplication(sys.argv)
app.setStyle('Fusion')
palette = QtGui.QPalette()
palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
palette.setColor(QtGui.QPalette.Base, QtGui.QColor(15, 15, 15))
palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(142, 45, 197).lighter())
palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
app.setPalette(palette)
app.setFont(QtGui.QFont("Seorge"))
a_window = window()
sys.exit(app.exec_())
