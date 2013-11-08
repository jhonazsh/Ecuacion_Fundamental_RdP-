# -*- coding: utf-8 -*- 
from PyQt4 import QtCore, QtGui 
import sys 
import re

class Mi_Programa(QtGui.QWidget): 
  
    def __init__(self, parent=None): 
    
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle('Ecuacion Fundamental')
        self.resize(891, 428) # Tamaño

        self.groupBox = QtGui.QGroupBox("Datos de Entrada", self)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 581, 381))

        self.label = QtGui.QLabel("Tamano de Matriz I/O:",self)
        self.label.setGeometry(QtCore.QRect(40, 50, 121, 16))

        self.lineEdit = QtGui.QLineEdit("",self)
        self.lineEdit.setGeometry(QtCore.QRect(160, 50, 41, 20))

        self.lineEdit_2 = QtGui.QLineEdit("",self)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 50, 41, 20))

        self.label_2 = QtGui.QLabel("Fil",self)
        self.label_2.setGeometry(QtCore.QRect(170, 30, 21, 16))

        self.label_3 = QtGui.QLabel("Col",self)
        self.label_3.setGeometry(QtCore.QRect(220, 30, 41, 16))

        self.label_4 = QtGui.QLabel("Matriz Input",self)
        self.label_4.setGeometry(QtCore.QRect(110, 80, 61, 16))

        self.pushButton_4 = QtGui.QPushButton("Aceptar",self)
        self.pushButton_4.setGeometry(QtCore.QRect(192, 75, 60, 23))

        self.label_5 = QtGui.QLabel("Matriz Output",self)
        self.label_5.setGeometry(QtCore.QRect(110, 230, 71, 16))

        #Tabla de Matriz Input
        self.tableWidget = QtGui.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(20, 90, 211, 121))
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setIconSize(QtCore.QSize(0, 0))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(4)
        item = QtGui.QTableWidgetItem("P1")
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem("P2")
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem("P3")
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem("P4")
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem("t1")
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem("t2")
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem("t3")
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem("t4")
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(25)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)

        #Tabla de Matriz Ouput
        self.tableWidget_2 = QtGui.QTableWidget(self.groupBox)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 240, 211, 121))
        self.tableWidget_2.setLineWidth(1)
        self.tableWidget_2.setAutoScrollMargin(16)
        self.tableWidget_2.setProperty("showDropIndicator", False)
        self.tableWidget_2.setIconSize(QtCore.QSize(0, 0))
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(4)
        item = QtGui.QTableWidgetItem("P1")
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem("P2")
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem("P3")
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem("P4")
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem("t1")
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem("t2")
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem("t3")
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem("t4")
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, item)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(25)
        self.tableWidget_2.horizontalHeader().setHighlightSections(True)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_2.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_2.verticalHeader().setVisible(True)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget_2.verticalHeader().setHighlightSections(True)
        self.tableWidget_2.verticalHeader().setSortIndicatorShown(True)

        self.label_6 = QtGui.QLabel("Matriz de Incidencia:",self)
        self.label_6.setGeometry(QtCore.QRect(290, 30, 111, 16))

        self.pushButton = QtGui.QPushButton("Generar",self)
        self.pushButton.setGeometry(QtCore.QRect(400, 27, 75, 23))

        self.label_7 = QtGui.QLabel("Secuencia de Transiciones:",self)
        self.label_7.setGeometry(QtCore.QRect(290, 180, 131, 16))

        self.line = QtGui.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(240, 20, 20, 351))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)

        self.spinBox = QtGui.QSpinBox(self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(270, 195, 60, 22))

        self.pushButton_5 = QtGui.QPushButton("Aceptar",self)
        self.pushButton_5.setGeometry(QtCore.QRect(360, 203, 70, 23))

        self.pushButton_6 = QtGui.QPushButton("Mostrar Vector Caract.",self)
        self.pushButton_6.setGeometry(QtCore.QRect(290, 233, 140, 23))

        self.tableWidget_7 = QtGui.QTableWidget(self.groupBox)
        self.tableWidget_7.setGeometry(QtCore.QRect(420, 173, 141, 75))
        self.tableWidget_7.setLineWidth(1)
        self.tableWidget_7.setAutoScrollMargin(16)
        self.tableWidget_7.setProperty("showDropIndicator", False)
        self.tableWidget_7.setIconSize(QtCore.QSize(0, 0))
        self.tableWidget_7.setColumnCount(1)
        self.tableWidget_7.setRowCount(4)
        item = QtGui.QTableWidgetItem("1")
        self.tableWidget_7.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem("2")
        self.tableWidget_7.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem("3")
        self.tableWidget_7.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem("4")
        self.tableWidget_7.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem("Secuencia")
        self.tableWidget_7.setHorizontalHeaderItem(0, item)
        self.tableWidget_7.horizontalHeader().setVisible(True)
        self.tableWidget_7.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_7.horizontalHeader().setDefaultSectionSize(125)
        self.tableWidget_7.horizontalHeader().setHighlightSections(True)
        self.tableWidget_7.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_7.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_7.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_7.verticalHeader().setVisible(True)
        self.tableWidget_7.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget_7.verticalHeader().setHighlightSections(True)
        self.tableWidget_7.verticalHeader().setSortIndicatorShown(True)

        self.tableWidget_3 = QtGui.QTableWidget(self.groupBox)
        self.tableWidget_3.setGeometry(QtCore.QRect(270, 260, 141, 101))
        self.tableWidget_3.setLineWidth(1)
        self.tableWidget_3.setAutoScrollMargin(16)
        self.tableWidget_3.setProperty("showDropIndicator", False)
        self.tableWidget_3.setIconSize(QtCore.QSize(0, 0))
        self.tableWidget_3.setColumnCount(1)
        self.tableWidget_3.setRowCount(4)
        item = QtGui.QTableWidgetItem("t1")
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem("t2")
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem("t3")
        self.tableWidget_3.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem("t4")
        self.tableWidget_3.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem("Vector Caract.")
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        self.tableWidget_3.horizontalHeader().setVisible(True)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(125)
        self.tableWidget_3.horizontalHeader().setHighlightSections(True)
        self.tableWidget_3.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_3.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_3.verticalHeader().setVisible(True)
        self.tableWidget_3.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget_3.verticalHeader().setHighlightSections(True)
        self.tableWidget_3.verticalHeader().setSortIndicatorShown(True)

        self.tableWidget_4 = QtGui.QTableWidget(self.groupBox)
        self.tableWidget_4.setGeometry(QtCore.QRect(420, 260, 141, 101))
        self.tableWidget_4.setLineWidth(1)
        self.tableWidget_4.setAutoScrollMargin(16)
        self.tableWidget_4.setProperty("showDropIndicator", False)
        self.tableWidget_4.setIconSize(QtCore.QSize(0, 0))
        self.tableWidget_4.setColumnCount(1)
        self.tableWidget_4.setRowCount(4)
        item = QtGui.QTableWidgetItem("1")
        self.tableWidget_4.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem("2")
        self.tableWidget_4.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem("3")
        self.tableWidget_4.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem("4")
        self.tableWidget_4.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem("Marcacion I.")
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        self.tableWidget_4.horizontalHeader().setVisible(True)
        self.tableWidget_4.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_4.horizontalHeader().setDefaultSectionSize(125)
        self.tableWidget_4.horizontalHeader().setHighlightSections(True)
        self.tableWidget_4.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_4.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_4.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_4.verticalHeader().setVisible(True)
        self.tableWidget_4.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget_4.verticalHeader().setHighlightSections(True)
        self.tableWidget_4.verticalHeader().setSortIndicatorShown(True)

        self.tableWidget_5 = QtGui.QTableWidget(self.groupBox)
        self.tableWidget_5.setGeometry(QtCore.QRect(270, 50, 291, 111))
        self.tableWidget_5.setLineWidth(1)
        self.tableWidget_5.setAutoScrollMargin(16)
        self.tableWidget_5.setProperty("showDropIndicator", False)
        self.tableWidget_5.setIconSize(QtCore.QSize(0, 0))
        self.tableWidget_5.setColumnCount(4)
        self.tableWidget_5.setRowCount(4)
        item = QtGui.QTableWidgetItem("f1")
        self.tableWidget_5.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem("f2")
        self.tableWidget_5.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem("f3")
        self.tableWidget_5.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem("f4")
        self.tableWidget_5.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem("c1")
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem("c2")
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem("c3")
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem("c4")
        self.tableWidget_5.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setItem(0, 1, item)
        self.tableWidget_5.horizontalHeader().setVisible(True)
        self.tableWidget_5.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_5.horizontalHeader().setDefaultSectionSize(25)
        self.tableWidget_5.horizontalHeader().setHighlightSections(True)
        self.tableWidget_5.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_5.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_5.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_5.verticalHeader().setVisible(True)
        self.tableWidget_5.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget_5.verticalHeader().setHighlightSections(True)
        self.tableWidget_5.verticalHeader().setSortIndicatorShown(True)

        self.groupBox_2 = QtGui.QGroupBox("Formula Ecuacion Fundamental",self)
        self.groupBox_2.setGeometry(QtCore.QRect(610, 10, 261, 101))

        self.label_8 = QtGui.QLabel("Ms = M0 + C * s",self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(20, 20, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)

        self.label_9 = QtGui.QLabel("Ms: Matriz Siguiente",self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(20, 50, 111, 16))

        self.label_10 = QtGui.QLabel("M0: Marcacion Inicial",self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(130, 50, 111, 16))
       
        self.label_11 = QtGui.QLabel("C: Matriz Incidencia",self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(20, 70, 111, 16))
        
        self.label_12 = QtGui.QLabel("s: Vector Caracterisitico",self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(130, 70, 121, 16))
        
        self.groupBox_3 = QtGui.QGroupBox("Resultado Ecuacion Fundamental",self)
        self.groupBox_3.setGeometry(QtCore.QRect(610, 120, 261, 271))

        self.tableWidget_6 = QtGui.QTableWidget(self.groupBox_3)
        self.tableWidget_6.setGeometry(QtCore.QRect(20, 30, 141, 121))
        self.tableWidget_6.setLineWidth(1)
        self.tableWidget_6.setAutoScrollMargin(16)
        self.tableWidget_6.setProperty("showDropIndicator", False)
        self.tableWidget_6.setIconSize(QtCore.QSize(0, 0))
        self.tableWidget_6.setColumnCount(1)
        self.tableWidget_6.setRowCount(4)
        item = QtGui.QTableWidgetItem("1")
        self.tableWidget_6.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem("2")
        self.tableWidget_6.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem("3")
        self.tableWidget_6.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem("4")
        self.tableWidget_6.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem("Marcacion Siguiente")
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        self.tableWidget_6.horizontalHeader().setVisible(True)
        self.tableWidget_6.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_6.horizontalHeader().setDefaultSectionSize(125)
        self.tableWidget_6.horizontalHeader().setHighlightSections(True)
        self.tableWidget_6.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_6.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_6.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_6.verticalHeader().setVisible(True)
        self.tableWidget_6.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget_6.verticalHeader().setHighlightSections(True)
        self.tableWidget_6.verticalHeader().setSortIndicatorShown(True)

        self.pushButton_1 = QtGui.QPushButton("Generar Ms",self.groupBox_3)
        self.pushButton_1.setGeometry(QtCore.QRect(170, 80, 75, 23))
        
        self.lineEdit_4 = QtGui.QLineEdit("",self.groupBox_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 170, 140, 23))
        
        self.pushButton_7 = QtGui.QPushButton("* Es Valida?",self.groupBox_3)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 170, 70, 23))
        
        self.pushButton_2 = QtGui.QPushButton("Limpiar Todo",self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 210, 221, 41))

        #funcion que conecta el evento del click al boton pushButton con una función generandoMatrizIncidencia
        self.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.generaMatrizIncidencia)
        #funcion que conecta el evento del click al boton pushButton_4 con una función generandoFilasColumnas
        self.connect(self.pushButton_4, QtCore.SIGNAL('clicked()'), self.generandoFilasColumnas)
        self.connect(self.pushButton_5, QtCore.SIGNAL('clicked()'), self.generandoSecuencia)
        self.connect(self.pushButton_6, QtCore.SIGNAL('clicked()'), self.generandoVector)
        self.connect(self.pushButton_1, QtCore.SIGNAL('clicked()'), self.generandoMs)
        self.connect(self.pushButton_7, QtCore.SIGNAL('clicked()'), self.validarMs)


    

    #función para generar filas y columnas de acuerdo al tamaño de la matriz  
    def generandoFilasColumnas(self):
        tamfila=int(self.lineEdit.text())
        tamcolumna=int(self.lineEdit_2.text())

        self.tableWidget.setColumnCount(tamcolumna)
        self.tableWidget.setRowCount(tamfila)

        self.tableWidget_2.setColumnCount(tamcolumna)
        self.tableWidget_2.setRowCount(tamfila)

        self.tableWidget_5.setColumnCount(tamcolumna)
        self.tableWidget_5.setRowCount(tamfila)

        self.tableWidget_3.setRowCount(tamcolumna)
        self.tableWidget_4.setRowCount(tamfila)
        self.tableWidget_6.setRowCount(tamfila)
        
        for i in range(tamfila):
            headerP="P"+str(i+2)
            headert="t"+str(i+2)
            headerincidenciaf="f"+str(i+2)
            headerincidenciac="c"+str(i+2)
            pri_headert = QtGui.QTableWidgetItem(headert)
            seg_headert = QtGui.QTableWidgetItem(headert)
            ter_headert = QtGui.QTableWidgetItem(headert)
            pri_headerP = QtGui.QTableWidgetItem(headerP)
            seg_headerP = QtGui.QTableWidgetItem(headerP)
            ter_headerP = QtGui.QTableWidgetItem(headerP)
            quin_headert = QtGui.QTableWidgetItem(headerincidenciaf)
            cuar_headert = QtGui.QTableWidgetItem(headerincidenciac)
            self.tableWidget.setVerticalHeaderItem(i+1, pri_headerP)
            self.tableWidget_2.setVerticalHeaderItem(i+1, seg_headerP)
            self.tableWidget.setHorizontalHeaderItem(i+1, pri_headert)
            self.tableWidget_2.setHorizontalHeaderItem(i+1, seg_headert)
            self.tableWidget_3.setVerticalHeaderItem(i+1, ter_headert)
            self.tableWidget_5.setHorizontalHeaderItem(i+1, cuar_headert)
            self.tableWidget_5.setVerticalHeaderItem(i+1, quin_headert)
      
    ####################################################################################################

    #Función para Generar la Matriz de Incidencia, mediante la resta C=O-I
    def generaMatrizIncidencia(self):
        tam_fila=int(self.lineEdit.text())
        tam_columna=int(self.lineEdit_2.text())  

        matriz_input=[]
        matriz_output=[]
        matriz_incidencia=[]
        for i in range(tam_fila):
            input_uno=[]
            input_dos=[]
            for j in range(tam_columna):
                texto_input = str(self.tableWidget.item(i,j).text())
                texto_output = str(self.tableWidget_2.item(i,j).text())
                input_uno.append(texto_input)
                input_dos.append(texto_output)
            matriz_input.append(input_uno)
            matriz_output.append(input_dos)   

        for x in range(tam_fila):
            pre_matriz_incidencia=[]
            for y in range(tam_columna):
                resta_incidencia=int(matriz_output[x][y])-int(matriz_input[x][y])
                self.tableWidget_5.setItem(x, y, QtGui.QTableWidgetItem(str(resta_incidencia)))
                pre_matriz_incidencia.append(str(resta_incidencia))
            matriz_incidencia.append(pre_matriz_incidencia)

    ####################################################################################################
  
    #Función para generar el tamaño del vector en la tabla
    def generandoSecuencia(self):     
        tamsecuencia=self.spinBox.text()
        self.tableWidget_7.setRowCount(int(tamsecuencia))

    ####################################################################################################

    #Función que genera el vector característico
    def generandoVector(self):
        tamsecuencia=int(self.spinBox.text())
        tamvector=int(self.lineEdit_2.text())

        b=[]
        for i in range(tamsecuencia):
            te=self.tableWidget_7.item(i,0).text()

            patron = re.compile('[1-9]')
            a = patron.findall(te[1])
            print a[0]
            b.append(str(a[0]))

        vector=[]
        for j in range(tamvector):
            cont=0
            for k in range(tamsecuencia):
                if str(j+1)==b[k]:
                    cont=cont+1
            print str(j+1)+" --> "+str(cont)
            vector.append(str(cont))
            self.tableWidget_3.setItem(j, 0, QtGui.QTableWidgetItem(str(cont)))

        print str(vector)
  
    ####################################################################################################
 
    #Función que genera la Marcación Siguiente
    def generandoMs(self):
        tamfila=int(self.lineEdit.text())
        tamcolumna=int(self.lineEdit_2.text())

        matrizinput=[]
        matrizoutput=[]
        matrizincidencia=[]
        for i in range(tamfila):
            inp=[]
            inp2=[]
            for j in range(tamcolumna):
                tex = self.tableWidget.item(i,j).text()
                tex1 = self.tableWidget_2.item(i,j).text()
                pal=str(tex)
                pal2=str(tex1)
                inp.append(pal)
                inp2.append(pal2)
            matrizinput.append(inp)
            matrizoutput.append(inp2)  

        for x in range(tamfila):
            prematrizincidencia=[]
            for y in range(tamcolumna):
                restaincidencia=int(matrizoutput[x][y])-int(matrizinput[x][y])
                self.tableWidget_5.setItem(x, y, QtGui.QTableWidgetItem(str(restaincidencia)))
                prematrizincidencia.append(str(restaincidencia))
            matrizincidencia.append(prematrizincidencia)
        #C
        print str(matrizincidencia)

        tamsecuencia=int(self.spinBox.text())
        tamvector=int(self.lineEdit_2.text())

        b=[]
        for i in range(tamsecuencia):
            te=self.tableWidget_7.item(i,0).text()

            patron = re.compile('[1-9]')
            a = patron.findall(te[1])
            print a[0]
            b.append(str(a[0]))

        vector=[]
        for j in range(tamvector):
            cont=0
            for k in range(tamsecuencia):
                if str(j+1)==b[k]:
                    cont=cont+1
            print str(j+1)+" --> "+str(cont)
            vector.append(str(cont))
            self.tableWidget_3.setItem(j, 0, QtGui.QTableWidgetItem(str(cont)))
        #s
        print str(vector)

        marcacion=[]
        for j in range(tamfila):
            palabra=self.tableWidget_4.item(j,0).text()
            marcacion.append(str(palabra))

        #M0
        print str(marcacion)

        print tamcolumna

        for z in range(tamfila):
            suma=0
            for a in range(tamcolumna):
                multiplicar=int(matrizincidencia[z][a])*int(vector[a])
                suma=suma+multiplicar 

            sumar=suma+int(marcacion[z])
            print str(sumar)
            self.tableWidget_6.setItem(z, 0, QtGui.QTableWidgetItem(str(sumar)))
  
    ####################################################################################################
     
    #Función para validar la Matriz Siguiente
    def validarMs(self):
        tamfila=int(self.lineEdit.text())

        ms=[]
        for i in range(tamfila):
            p=str(self.tableWidget_6.item(i,0).text())
            ms.append(p)

        mss=[]
        for j in range(tamfila):

            if(int(ms[j])>=0):
                mss.append("1")
            else:
                mss.append("0")

        multi=1
        for k in range(tamfila):
            multi=multi*int(mss[k])

        if multi==1:
            self.lineEdit_4.setText("       si es valida")
        else:
            self.lineEdit_4.setText("       no es valida")


aplicacion = QtGui.QApplication(sys.argv) 
formulario = Mi_Programa() 
formulario.show() 
aplicacion.exec_() 
