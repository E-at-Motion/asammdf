# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PyMDFMainWindow(object):
    def setupUi(self, PyMDFMainWindow):
        PyMDFMainWindow.setObjectName("PyMDFMainWindow")
        PyMDFMainWindow.resize(800, 723)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/asammdf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PyMDFMainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(PyMDFMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 782, 604))
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.files = QtWidgets.QTabWidget(self.page)
        self.files.setDocumentMode(False)
        self.files.setTabsClosable(True)
        self.files.setObjectName("files")
        self.verticalLayout_2.addWidget(self.files)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page, icon1, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 782, 604))
        self.page_2.setObjectName("page_2")
        self.files_layout = QtWidgets.QGridLayout(self.page_2)
        self.files_layout.setContentsMargins(0, 0, 0, 0)
        self.files_layout.setObjectName("files_layout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cs_format = QtWidgets.QComboBox(self.page_2)
        self.cs_format.setObjectName("cs_format")
        self.gridLayout_2.addWidget(self.cs_format, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        self.cs_compression = QtWidgets.QComboBox(self.page_2)
        self.cs_compression.setObjectName("cs_compression")
        self.gridLayout_2.addWidget(self.cs_compression, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)
        self.cs_split = QtWidgets.QCheckBox(self.page_2)
        self.cs_split.setObjectName("cs_split")
        self.gridLayout_2.addWidget(self.cs_split, 2, 0, 1, 1)
        self.cs_split_size = QtWidgets.QDoubleSpinBox(self.page_2)
        self.cs_split_size.setObjectName("cs_split_size")
        self.gridLayout_2.addWidget(self.cs_split_size, 3, 1, 1, 1)
        self.cs_btn = QtWidgets.QPushButton(self.page_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/stack.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cs_btn.setIcon(icon2)
        self.cs_btn.setObjectName("cs_btn")
        self.gridLayout_2.addWidget(self.cs_btn, 6, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.page_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.concatenate = QtWidgets.QRadioButton(self.groupBox)
        self.concatenate.setChecked(True)
        self.concatenate.setObjectName("concatenate")
        self.verticalLayout_3.addWidget(self.concatenate)
        self.stack = QtWidgets.QRadioButton(self.groupBox)
        self.stack.setObjectName("stack")
        self.verticalLayout_3.addWidget(self.stack)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 5, 0, 1, 1)
        self.files_layout.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.files_layout.setRowStretch(0, 1)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/list.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page_2, icon3, "")
        self.verticalLayout.addWidget(self.toolBox)
        PyMDFMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PyMDFMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        PyMDFMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PyMDFMainWindow)
        self.statusbar.setObjectName("statusbar")
        PyMDFMainWindow.setStatusBar(self.statusbar)
        self.action_memory_minimum = QtWidgets.QAction(PyMDFMainWindow)
        self.action_memory_minimum.setCheckable(True)
        self.action_memory_minimum.setObjectName("action_memory_minimum")
        self.action_memory_full = QtWidgets.QAction(PyMDFMainWindow)
        self.action_memory_full.setCheckable(True)
        self.action_memory_full.setObjectName("action_memory_full")
        self.action_memory_low = QtWidgets.QAction(PyMDFMainWindow)
        self.action_memory_low.setCheckable(True)
        self.action_memory_low.setObjectName("action_memory_low")

        self.retranslateUi(PyMDFMainWindow)
        self.toolBox.setCurrentIndex(1)
        self.files.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(PyMDFMainWindow)

    def retranslateUi(self, PyMDFMainWindow):
        _translate = QtCore.QCoreApplication.translate
        PyMDFMainWindow.setWindowTitle(_translate("PyMDFMainWindow", "asammdf"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("PyMDFMainWindow", "Single files"))
        self.label_3.setText(_translate("PyMDFMainWindow", "Compression"))
        self.label_2.setText(_translate("PyMDFMainWindow", "Split block size"))
        self.cs_split.setText(_translate("PyMDFMainWindow", "Split data blocks"))
        self.cs_split_size.setSuffix(_translate("PyMDFMainWindow", "MB"))
        self.cs_btn.setText(_translate("PyMDFMainWindow", "Concatenate"))
        self.groupBox.setTitle(_translate("PyMDFMainWindow", "Operation"))
        self.concatenate.setText(_translate("PyMDFMainWindow", "Concatenate"))
        self.stack.setText(_translate("PyMDFMainWindow", "Stack"))
        self.label.setText(_translate("PyMDFMainWindow", "Output format"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("PyMDFMainWindow", "Multiple files"))
        self.action_memory_minimum.setText(_translate("PyMDFMainWindow", "minimum"))
        self.action_memory_minimum.setToolTip(_translate("PyMDFMainWindow", "Minimal memory usage by loading only the nedded block addresses"))
        self.action_memory_full.setText(_translate("PyMDFMainWindow", "full"))
        self.action_memory_full.setToolTip(_translate("PyMDFMainWindow", "Load all blocks in the RAM"))
        self.action_memory_low.setText(_translate("PyMDFMainWindow", "low"))
        self.action_memory_low.setToolTip(_translate("PyMDFMainWindow", "Load metdata block in RAM but leave the samples on disk"))

import resource_rc
