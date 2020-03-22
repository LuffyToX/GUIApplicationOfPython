# -*- coding: utf-8 -*-
# 复利计算
# 复利计算是指每经过一个计息周期后，都要将本期所生的利息加入本金中，以计算下期的利息
#
# 复利现值：在计算复利的情况下，要达到未来某一特定的资金金额，现在必须投入的本金
# 复利终值：本金在约定期限内获得利息后，将利息加入本金中再计算利息，逐期滚算到约定
#          期末的本金之和
#
# 复利计算公式：S = P(1+i)^n


import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *


class Dialog(QDialog):

	def __init__(self, parent=None):
		super(Dialog, self).__init__(parent)

		principalLabel = QLabel("Principal:")
		self.principalSpinBox = QDoubleSpinBox()
		self.principalSpinBox.setRange(1, 1000000000)
		self.principalSpinBox.setValue(1000)
		self.principalSpinBox.setPrefix("RMB ")
		rateLabel = QLabel("Rate:")
		self.rateSpinBox = QDoubleSpinBox()
		self.rateSpinBox.setRange(1, 100)
		self.rateSpinBox.setValue(5)
		self.rateSpinBox.setSuffix(" %")
		yearsLabel = QLabel("Years:")
		self.yearsComboBox = QComboBox()
		self.yearsComboBox.addItem("1 year")
		self.yearsComboBox.addItems(["{0} years".format(x)
									 for x in range(2, 31)])
		amountLabel = QLabel("Amount")
		self.amountLabel = QLabel()

		grid = QGridLayout()
		grid.addWidget(principalLabel, 0, 0)
		grid.addWidget(self.principalSpinBox, 0, 1)
		grid.addWidget(rateLabel, 1, 0)
		grid.addWidget(self.rateSpinBox, 1, 1)
		grid.addWidget(yearsLabel, 2, 0)
		grid.addWidget(self.yearsComboBox, 2, 1)
		grid.addWidget(amountLabel, 3, 0)
		grid.addWidget(self.amountLabel, 3, 1)
		self.setLayout(grid)

		self.principalSpinBox.valueChanged.connect(self.updateUi)
		self.rateSpinBox.valueChanged.connect(self.updateUi)
		self.yearsComboBox.currentIndexChanged.connect(self.updateUi)
		
		self.setWindowTitle("Interest")
		self.updateUi()

	def updateUi(self):
		principal = self.principalSpinBox.value()
		rate = self.rateSpinBox.value()
		years = self.yearsComboBox.currentIndex() + 1
		amount = principal * ((1 + (rate / 100.0)) ** years)
		self.amountLabel.setText("RMB {0:.2f}".format(amount))


if __name__ == "__main__":
	# 下面这行代码可以确保运行界面与 Qt Designer 预览界面一致
	QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

	app = QApplication(sys.argv)
	dia = Dialog()
	dia.show()
	sys.exit(app.exec_()) 


