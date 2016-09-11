#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from datetime import datetime, date, time, timedelta
import calendar

def calcular():
    fecha1 = datetime.now()
    fecha2 = datetime(fecha1.year + 1, 9, 15)
    b.setText("    "+str(fecha2 - fecha1)+"\n"+"para el sigiente 15 de septiembre")
    b.move(110,20)



personajes = str.format("Miguel Gregorio Antonio Ignacio Hidalgo y Costilla\n"+
                        "              Jose Maria Morelos y Pavon\n"+
                        "            Vicente Ramon Guerrero Saldaña")
app = QtGui.QApplication(sys.argv)
w = QtGui.QWidget()
b = QtGui.QLabel(w)
b.setText(personajes)
w.setGeometry(100,100,400,150)
b.move(50,20)
w.setWindowTitle("!Viva Mexico!")
w.setWindowIcon(QtGui.QIcon('icon.png'))
btn = QtGui.QPushButton('Aprietame', w)
btn.setToolTip('Hola guapa ;)')
btn.clicked.connect(calcular)
btn.resize(btn.sizeHint())
btn.move(150, 80)
w.show()
sys.exit(app.exec_())
