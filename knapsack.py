import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
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
		for row in range(self.rowCount()):
			name=self.item(row,0).text()
			weight=int(self.item(row,1).text())
			value=int(self.item(row,2).text())
			items.append([name,weight,value])
		print(items)
		capacity=int(a_window.capacity_text.text())
		solution=knapsack_dp(items, capacity)[2]
		result=a_window.result_table
		result.setRowCount(0)
		for i,itemSol in enumerate(solution):
			row=result.rowCount()
			result.insertRow(row)
			result.setItem(i,0,QTableWidgetItem(itemSol[0]))
			result.setItem(i,1,QTableWidgetItem(str(itemSol[1])))
			print(itemSol)


class ResultTable(QTableWidget):
	"""docstring for MyTable"""
	def __init__(self,  parent=None):
		super(ResultTable, self).__init__(1, 2, parent)
		headertitle = ("Objet","Nombre")
		self.setHorizontalHeaderLabels(headertitle)
		self.verticalHeader().hide()
		self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

				

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

		#result section
		self.show_result_btn=QPushButton("Afficher la solution")
		result_btn=QHBoxLayout()
		result_btn.addWidget(self.show_result_btn)

		#result table
		self.result_table=ResultTable()
		result_table=QHBoxLayout()
		result_table.addWidget(self.result_table)

		#Vbox1
		self.add_btn=QPushButton("Ajouter un objet")
		self.add_btn.clicked.connect(objects_table._addrow)
		self.show_result_btn.clicked.connect(objects_table.showResult)

		v_box1=QVBoxLayout()
		v_box1.addLayout(capacity_hbox)
		v_box1.addWidget(self.add_btn)
		v_box1.addLayout(table_hbox)

		#Vbox2
		v_box2=QVBoxLayout()
		v_box2.addLayout(result_btn)
		v_box2.addLayout(result_table)


		#main layout
		h_box=QHBoxLayout()
		h_box.addLayout(v_box1,1)
		h_box.addLayout(v_box2,1)
		
		self.setLayout(h_box)
		self.setGeometry(300,100,800,200)
		self.setWindowTitle("Le problème du sac à dos")
		
		self.show()
def knapsack_dp(items, C):
    # order by max value per item weight
    items = sorted(items, key=lambda item: item[VALUE]/float(item[WEIGHT]), reverse=True)
 
    # Sack keeps track of max value so far as well as the count of each item in the tab
    tab = [(0, [0 for i in items]) for i in range(0, C+1)]   # value, [item tab]
 
    for i,item in enumerate(items):
        name, weight, value = item
        for c in range(weight, C+1):
            tabbefore = tab[c-weight]  # previous max tab to try adding this item to
            new_value = tabbefore[0] + value
            used = tabbefore[1][i]
            if tab[c][0] < new_value:
                # old max tab with this added item is better
                tab[c] = (new_value, tabbefore[1][:])
                tab[c][1][i] +=1   # use one more
 
    value, bagged = tab[C]
    numbagged = sum(bagged)
    weight = sum(items[i][1]*n for i,n in enumerate(bagged))
    # convert to (iten, count) pairs) in name order
    bagged = sorted((items[i][NAME], n) for i,n in enumerate(bagged) if n)
    return value, weight, bagged
NAME, WEIGHT, VALUE = range(3)
items= []	
capacity=0
app= QApplication(sys.argv)
app.setStyle('Fusion')
a_window=window()
sys.exit(app.exec_())