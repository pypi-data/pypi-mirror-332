# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'email_splitter.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(377, 286)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.layoutInputFile = QHBoxLayout()
        self.layoutInputFile.setObjectName(u"layoutInputFile")
        self.lblInputFile = QLabel(self.centralwidget)
        self.lblInputFile.setObjectName(u"lblInputFile")

        self.layoutInputFile.addWidget(self.lblInputFile)

        self.btnSelectInput = QPushButton(self.centralwidget)
        self.btnSelectInput.setObjectName(u"btnSelectInput")

        self.layoutInputFile.addWidget(self.btnSelectInput)


        self.verticalLayout.addLayout(self.layoutInputFile)

        self.layoutOutputFile = QHBoxLayout()
        self.layoutOutputFile.setObjectName(u"layoutOutputFile")
        self.lblOutputFile = QLabel(self.centralwidget)
        self.lblOutputFile.setObjectName(u"lblOutputFile")

        self.layoutOutputFile.addWidget(self.lblOutputFile)

        self.btnSelectOutput = QPushButton(self.centralwidget)
        self.btnSelectOutput.setObjectName(u"btnSelectOutput")

        self.layoutOutputFile.addWidget(self.btnSelectOutput)


        self.verticalLayout.addLayout(self.layoutOutputFile)

        self.layoutSheetName = QHBoxLayout()
        self.layoutSheetName.setObjectName(u"layoutSheetName")
        self.lblSheetName = QLabel(self.centralwidget)
        self.lblSheetName.setObjectName(u"lblSheetName")

        self.layoutSheetName.addWidget(self.lblSheetName)

        self.txtSheetName = QLineEdit(self.centralwidget)
        self.txtSheetName.setObjectName(u"txtSheetName")

        self.layoutSheetName.addWidget(self.txtSheetName)


        self.verticalLayout.addLayout(self.layoutSheetName)

        self.layoutEmailColumn = QHBoxLayout()
        self.layoutEmailColumn.setObjectName(u"layoutEmailColumn")
        self.lblEmailColumn = QLabel(self.centralwidget)
        self.lblEmailColumn.setObjectName(u"lblEmailColumn")

        self.layoutEmailColumn.addWidget(self.lblEmailColumn)

        self.txtEmailColumn = QLineEdit(self.centralwidget)
        self.txtEmailColumn.setObjectName(u"txtEmailColumn")

        self.layoutEmailColumn.addWidget(self.txtEmailColumn)


        self.verticalLayout.addLayout(self.layoutEmailColumn)

        self.btnProcess = QPushButton(self.centralwidget)
        self.btnProcess.setObjectName(u"btnProcess")

        self.verticalLayout.addWidget(self.btnProcess)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Email Splitter", None))
        self.lblInputFile.setText(QCoreApplication.translate("MainWindow", u"Select Input File:", None))
        self.btnSelectInput.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.lblOutputFile.setText(QCoreApplication.translate("MainWindow", u"Select Output File:", None))
        self.btnSelectOutput.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.lblSheetName.setText(QCoreApplication.translate("MainWindow", u"Sheet Name:", None))
        self.lblEmailColumn.setText(QCoreApplication.translate("MainWindow", u"Email Column Name:", None))
        self.btnProcess.setText(QCoreApplication.translate("MainWindow", u"Process File", None))
    # retranslateUi

