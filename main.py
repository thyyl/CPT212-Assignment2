# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Graphs.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets

from adjacencyList import AdjacencyList
from connection import Graph
from graph import MplCanvas


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.layout = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 341, 71))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(730, 120, 171, 51))
        self.label_2.setObjectName("label_2")
        self.originBox = QtWidgets.QComboBox(self.centralwidget)
        self.originBox.setGeometry(QtCore.QRect(730, 180, 91, 41))
        self.originBox.setObjectName("originBox")
        self.originBox.addItem("")
        self.originBox.addItem("")
        self.originBox.addItem("")
        self.originBox.addItem("")
        self.originBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(870, 170, 41, 51))
        self.label_3.setObjectName("label_3")
        self.destinationBox = QtWidgets.QComboBox(self.centralwidget)
        self.destinationBox.setGeometry(QtCore.QRect(940, 180, 91, 41))
        self.destinationBox.setObjectName("destinationBox")
        self.destinationBox.addItem("")
        self.destinationBox.addItem("")
        self.destinationBox.addItem("")
        self.destinationBox.addItem("")
        self.destinationBox.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(730, 260, 211, 51))
        self.label_4.setObjectName("label_4")
        self.functionBox = QtWidgets.QComboBox(self.centralwidget)
        self.functionBox.setGeometry(QtCore.QRect(730, 320, 151, 41))
        self.functionBox.setObjectName("functionBox")
        self.functionBox.addItem("")
        self.functionBox.addItem("")
        self.functionBox.addItem("")
        self.functionBox.addItem("")
        self.functionBox.addItem("")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(730, 470, 211, 51))
        self.label_5.setObjectName("label_5")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(730, 410, 93, 28))
        self.startButton.setObjectName("startButton")
        self.scCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.scCheckBox.setGeometry(QtCore.QRect(730, 530, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.scCheckBox.setFont(font)
        self.scCheckBox.setObjectName("scCheckBox")
        self.cCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.cCheckbox.setGeometry(QtCore.QRect(730, 560, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cCheckbox.setFont(font)
        self.cCheckbox.setObjectName("cCheckbox")
        self.spCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.spCheckbox.setGeometry(QtCore.QRect(730, 590, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spCheckbox.setFont(font)
        self.spCheckbox.setObjectName("spCheckbox")
        self.remarksLabel = QtWidgets.QLabel(self.centralwidget)
        self.remarksLabel.setGeometry(QtCore.QRect(730, 690, 451, 71))
        self.remarksLabel.setObjectName("remarksLabel")
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(830, 410, 93, 28))
        self.resetButton.setObjectName("resetButton")
        self.generateButton = QtWidgets.QPushButton(self.centralwidget)
        self.generateButton.setGeometry(QtCore.QRect(930, 410, 93, 28))
        self.generateButton.setObjectName("generateButton")
        self.graphLabel = QtWidgets.QLabel(self.centralwidget)
        self.graphLabel.setGeometry(QtCore.QRect(30, 140, 651, 591))
        self.graphLabel.setText("")
        self.graphLabel.setObjectName("graphLabel")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(730, 640, 211, 51))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ''' None_PyQT5 code '''

        self.adList = AdjacencyList()
        self.canvas = MplCanvas(self.graphLabel, adList=self.adList.getOriList())
        self.startButton.pressed.connect(self.startPushed)
        self.resetButton.pressed.connect(self.resetPushed)
        self.generateButton.pressed.connect(self.generatePushed)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:26pt;\">Graphs Algorithm</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:14pt;\">Choose Vertex :</span></p></body></html>"))
        self.originBox.setItemText(0, _translate("MainWindow", "BER"))
        self.originBox.setItemText(1, _translate("MainWindow", "LDN"))
        self.originBox.setItemText(2, _translate("MainWindow", "NY"))
        self.originBox.setItemText(3, _translate("MainWindow", "SEO"))
        self.originBox.setItemText(4, _translate("MainWindow", "TKY"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:14pt;\">to</span></p></body></html>"))
        self.destinationBox.setItemText(0, _translate("MainWindow", "BER"))
        self.destinationBox.setItemText(1, _translate("MainWindow", "LDN"))
        self.destinationBox.setItemText(2, _translate("MainWindow", "NY"))
        self.destinationBox.setItemText(3, _translate("MainWindow", "SEO"))
        self.destinationBox.setItemText(4, _translate("MainWindow", "TKY"))
        self.label_4.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:14pt;\">Select a function : </span></p></body></html>"))
        self.functionBox.setItemText(0, _translate("MainWindow", "Strong Connectivity"))
        self.functionBox.setItemText(1, _translate("MainWindow", "Cycle Detection"))
        self.functionBox.setItemText(2, _translate("MainWindow", "Shortest Path"))
        self.functionBox.setItemText(3, _translate("MainWindow", "Add New Edge"))
        self.functionBox.setItemText(4, _translate("MainWindow", "Remove Edge"))
        self.label_5.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:14pt;\">Graph Status : </span></p></body></html>"))
        self.startButton.setText(_translate("MainWindow", "Check!"))
        self.scCheckBox.setText(_translate("MainWindow", "Strongly Connected"))
        self.cCheckbox.setText(_translate("MainWindow", "Cyclic"))
        self.spCheckbox.setText(_translate("MainWindow", "Shortest Path"))
        self.remarksLabel.setText(_translate("MainWindow",
                                             "<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt;\">Comment</span></p></body></html>"))
        self.resetButton.setText(_translate("MainWindow", "Reset!"))
        self.generateButton.setText(_translate("MainWindow", "Run Function!"))
        self.label_6.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:14pt;\">Remarks :</span></p></body></html>"))

    def resetPushed(self):
        self.canvas.draw_idle()
        self.canvas.plot(self.adList.getOriList())
        self.adList.resetList(self.adList.getOriList())
        self.remarksLabel.setText('Comments')

        self.scCheckBox.setChecked(False)
        self.cCheckbox.setChecked(False)
        self.spCheckbox.setChecked(False)

    def generatePushed(self):
        function = self.functionBox.currentText()

        if function == 'Add New Edge' or function == 'Remove Edge':
            src = self.originBox.currentText()
            des = self.destinationBox.currentText()

            if src == des:
                self.remarksLabel.setText(f'Source and Destination are the same.')
                return

            if function == 'Add New Edge':
                self.adList.addNewEdge(src, des)
                self.remarksLabel.setText(f'Edge {src} to {des} is added')

            elif function == 'Remove Edge':
                self.adList.removeEdge(src, des)
                self.remarksLabel.setText(f'Edge {src} to {des} is removed')

        self.drawNetwork()



    def drawNetwork(self):
        function = self.functionBox.currentText()
        self.canvas.draw_idle()
        graph = Graph()
        newGraph = graph.randomGraph(function, self.originBox.currentText(), self.destinationBox.currentText(), self.adList.getNewList())
        self.adList.updateList(newGraph)
        self.canvas.plot(self.adList.getNewList())
        self.startPushed()

    def startPushed(self):
        graph = Graph()
        function = self.functionBox.currentText()

        for origin in self.adList.getNewList():
            for destination in self.adList.getNewList()[origin]:
                graph.addEdge(origin, destination)

        self.scCheckBox.setChecked(False)
        self.cCheckbox.setChecked(False)
        self.spCheckbox.setChecked(False)
        if function == 'Strong Connectivity':
            if graph.isStrong() is True:
                self.remarksLabel.setText('The graph is strongly connected.')
                self.scCheckBox.setChecked(True)

            else:
                self.remarksLabel.setText('The graph is not strongly connected. '
                                          '\nA new adjusted graph that is strongly connected is shown.')
                self.scCheckBox.setChecked(False)

        elif function == 'Cycle Detection':
            if graph.isCyclic() is True:
                self.remarksLabel.setText('The graph is cyclic.')
                self.cCheckbox.setChecked(True)
            else:
                self.remarksLabel.setText('The graph is not cyclic. '
                                          '\nA new adjusted graph that is cyclic is shown.')
                self.cCheckbox.setChecked(False)

        elif function == 'Shortest Path':
            src = self.originBox.currentText()
            des = self.destinationBox.currentText()
            counter, dist = graph.dijkstra(src, des)
            if counter is True:
                self.remarksLabel.setText(f'Shortest path from {src} to {des} is {dist}km')
            else:
                self.remarksLabel.setText(f'There is no path from {src} to {des}')

        elif function == 'Add New Edge':
            self.remarksLabel.setText(f'Please select "Run Function!" to add new edge')

        elif function == 'Remove Edge':
            self.remarksLabel.setText(f'Please select "Run Function!" to remove edge')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
