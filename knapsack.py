import sys
import time
from DP import knapsack_dp
from BranchAndBound import  knapsack_BB
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui
class MyTable(QTableWidget):
	"""docstring for MyTable"""
	def __init__(self,  parent=None):
		super(MyTable, self).__init__(1, 3, parent)
		headertitle = ("Nom","Poids","Valeur")
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
	@QtCore.pyqtSlot()
	def _removerow(self):
		if self.rowCount() > 0:
			self.removeRow(self.rowCount()-1)
	def showResult(self):
		
		items=[]
		for row in range(self.rowCount()):
			name=self.item(row,0).text()
			weight=int(self.item(row,1).text())
			value=int(self.item(row,2).text())
			items.append([name,weight,value])
		print(items)
		capacity=int(a_window.capacity_text.text())
		start=time.time()
		solution=knapsack_dp(items, capacity)
		solution_items=solution[2]
		end=time.time()
		result=a_window.result_table
		result.setRowCount(0)
		for i,itemSol in enumerate(solution_items):
			row=result.rowCount()
			result.insertRow(row)
			result.setItem(i,0,QTableWidgetItem(itemSol[0]))
			result.setItem(i,1,QTableWidgetItem(str(itemSol[1])))
			print(itemSol)

		a_window.StatsTable.setItem(0,0,QTableWidgetItem(str(solution[0])))
		a_window.StatsTable.setItem(1,0,QTableWidgetItem(str(solution[1])))
		a_window.StatsTable.setItem(2,0,QTableWidgetItem(str((end-start)*1000)+"ms"))

	def showResult2(self):

		items = []
		for row in range(self.rowCount()):
			name = self.item(row, 0).text()
			weight = int(self.item(row, 1).text())
			value = int(self.item(row, 2).text())
			items.append([name, weight, value])
		print(items)
		capacity = int(a_window.capacity_text.text())
		start = time.time()
		solution = knapsack_BB(items, capacity)
		solution_items = solution[2]
		end = time.time()
		print(end - start)
		result = a_window.result_table2
		result.setRowCount(0)
		for i, itemSol in enumerate(solution_items):
			row = result.rowCount()
			result.insertRow(row)
			result.setItem(i, 0, QTableWidgetItem(itemSol[0]))
			result.setItem(i, 1, QTableWidgetItem(str(itemSol[1])))
			print(itemSol)

		a_window.StatsTable2.setItem(0, 0, QTableWidgetItem(str(solution[0])))
		a_window.StatsTable2.setItem(1, 0, QTableWidgetItem(str(solution[1])))
		a_window.StatsTable2.setItem(2, 0, QTableWidgetItem(str((end-start)*1000)+"ms"))
class ResultTable(QTableWidget):
	"""docstring for MyTable"""
	def __init__(self,  parent=None):
		super(ResultTable, self).__init__(1, 2, parent)
		headertitle = ("Objet","Nombre")
		self.setHorizontalHeaderLabels(headertitle)
		self.verticalHeader().hide()
		self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)



class StatsTable(QTableWidget):
	"""docstring for MyTable"""
	def __init__(self,  parent=None):
		super(StatsTable, self).__init__(3, 1, parent)
		headertitle = ("Valeur totale","Poids total","Temps d'éxecution")
		self.setVerticalHeaderLabels(headertitle)
		self.horizontalHeader().hide()
		self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
		self.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

class window(QWidget):
	def __init__(self):
		super().__init__()
		self.init_ui()
	def init_ui(self):
		# Capacity field
		self.capacity_label= QLabel("Donner la capacité du sac à dos : ")
		self.capacity_text=QLineEdit()
		capacity_hbox=QHBoxLayout()
		capacity_hbox.addWidget(self.capacity_label)
		capacity_hbox.addWidget(self.capacity_text)

		
		#objects table
		objects_table=MyTable()
		table_hbox=QHBoxLayout()
		table_hbox.addWidget(objects_table)
		# Vbox1
		self.add_btn = QPushButton("Ajouter un objet")
		self.add_btn.clicked.connect(objects_table._addrow)

		v_box1 = QVBoxLayout()
		v_box1.addLayout(capacity_hbox)
		v_box1.addWidget(self.add_btn)
		v_box1.addLayout(table_hbox)

		#result section
		self.show_result_btn=QPushButton("Afficher la solution")
		self.show_result_btn.clicked.connect(objects_table.showResult)

		#result table
		self.result_table=ResultTable()
		self.StatsTable=StatsTable()
		self.DP_label=QLabel("La programmation dynamique: ")
		self.DP_label.setStyleSheet("font-family: seorge; font: bold 20px")
		#Vbox2
		v_box2=QVBoxLayout()
		v_box2.addWidget(self.DP_label)
		v_box2.addWidget(self.show_result_btn)
		v_box2.addWidget(self.StatsTable,1)
		v_box2.addWidget(self.result_table,4)


		self.result_table2=ResultTable()
		self.StatsTable2=StatsTable()
		self.BB_label=QLabel("Branch and Bound ")
		self.BB_label.setStyleSheet("font-family: seorge; font: bold 20px")
		self.show_result_btn2=QPushButton("Afficher la solution")
		self.show_result_btn2.clicked.connect(objects_table.showResult2)
		#VBox3
		v_box3=QVBoxLayout()
		v_box3.addWidget(self.BB_label)
		v_box3.addWidget(self.show_result_btn2)
		v_box3.addWidget(self.StatsTable2,1)
		v_box3.addWidget(self.result_table2,4)

		#main layout
		h_box=QHBoxLayout()
		h_box.addLayout(v_box1,1)
		h_box.addLayout(v_box2,1)
		h_box.addLayout(v_box3,1)
		self.setLayout(h_box)
		self.setGeometry(0,0,1700,700)
		self.setWindowTitle("Le problème du sac à dos")
		
		self.show()

NAME, WEIGHT, VALUE = range(3)
items= []	
capacity=0
app= QApplication(sys.argv)
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
a_window=window()
sys.exit(app.exec_())