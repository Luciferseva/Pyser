# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/MainWindow.ui'
#
# Created: Tue Jan 05 11:36:50 2016
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(910, 611)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(190, 530))
        self.groupBox.setMaximumSize(QtCore.QSize(190, 530))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.sendType_comboBox = QtGui.QComboBox(self.groupBox)
        self.sendType_comboBox.setObjectName(_fromUtf8("sendType_comboBox"))
        self.sendType_comboBox.addItem(_fromUtf8(""))
        self.sendType_comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_8.addWidget(self.sendType_comboBox)
        self.asciiTail_comboBox = QtGui.QComboBox(self.groupBox)
        self.asciiTail_comboBox.setObjectName(_fromUtf8("asciiTail_comboBox"))
        self.asciiTail_comboBox.addItem(_fromUtf8(""))
        self.asciiTail_comboBox.addItem(_fromUtf8(""))
        self.asciiTail_comboBox.addItem(_fromUtf8(""))
        self.asciiTail_comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_8.addWidget(self.asciiTail_comboBox)
        self.gridLayout.addLayout(self.horizontalLayout_8, 11, 0, 1, 2)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.autoLF_checkBox = QtGui.QCheckBox(self.groupBox)
        self.autoLF_checkBox.setObjectName(_fromUtf8("autoLF_checkBox"))
        self.horizontalLayout_7.addWidget(self.autoLF_checkBox)
        self.hideSRFlag_checkBox = QtGui.QCheckBox(self.groupBox)
        self.hideSRFlag_checkBox.setChecked(True)
        self.hideSRFlag_checkBox.setObjectName(_fromUtf8("hideSRFlag_checkBox"))
        self.horizontalLayout_7.addWidget(self.hideSRFlag_checkBox)
        self.gridLayout.addLayout(self.horizontalLayout_7, 9, 0, 1, 2)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.inc_checkBox = QtGui.QCheckBox(self.groupBox)
        self.inc_checkBox.setObjectName(_fromUtf8("inc_checkBox"))
        self.horizontalLayout_9.addWidget(self.inc_checkBox)
        self.resetStartVal_pushButton = QtGui.QPushButton(self.groupBox)
        self.resetStartVal_pushButton.setObjectName(_fromUtf8("resetStartVal_pushButton"))
        self.horizontalLayout_9.addWidget(self.resetStartVal_pushButton)
        self.gridLayout.addLayout(self.horizontalLayout_9, 12, 0, 1, 2)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.autoSend_checkBox = QtGui.QCheckBox(self.groupBox)
        self.autoSend_checkBox.setObjectName(_fromUtf8("autoSend_checkBox"))
        self.horizontalLayout_10.addWidget(self.autoSend_checkBox)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_10.addWidget(self.label_2)
        self.gridLayout.addLayout(self.horizontalLayout_10, 15, 0, 1, 2)
        self.showSent_checkBox = QtGui.QCheckBox(self.groupBox)
        self.showSent_checkBox.setObjectName(_fromUtf8("showSent_checkBox"))
        self.gridLayout.addWidget(self.showSent_checkBox, 14, 0, 1, 2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.parity_comboBox = QtGui.QComboBox(self.groupBox)
        self.parity_comboBox.setMinimumSize(QtCore.QSize(121, 0))
        self.parity_comboBox.setObjectName(_fromUtf8("parity_comboBox"))
        self.parity_comboBox.addItem(_fromUtf8(""))
        self.parity_comboBox.addItem(_fromUtf8(""))
        self.parity_comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.parity_comboBox)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 2)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 2)
        self.open_pushButton = QtGui.QPushButton(self.groupBox)
        self.open_pushButton.setMinimumSize(QtCore.QSize(0, 51))
        self.open_pushButton.setObjectName(_fromUtf8("open_pushButton"))
        self.gridLayout.addWidget(self.open_pushButton, 5, 0, 1, 2)
        self.clearSentText_checkBox = QtGui.QCheckBox(self.groupBox)
        self.clearSentText_checkBox.setChecked(False)
        self.clearSentText_checkBox.setObjectName(_fromUtf8("clearSentText_checkBox"))
        self.gridLayout.addWidget(self.clearSentText_checkBox, 13, 0, 1, 2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_4.addWidget(self.label_6)
        self.bytesize_comboBox = QtGui.QComboBox(self.groupBox)
        self.bytesize_comboBox.setMinimumSize(QtCore.QSize(121, 0))
        self.bytesize_comboBox.setObjectName(_fromUtf8("bytesize_comboBox"))
        self.bytesize_comboBox.addItem(_fromUtf8(""))
        self.bytesize_comboBox.addItem(_fromUtf8(""))
        self.bytesize_comboBox.addItem(_fromUtf8(""))
        self.bytesize_comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.bytesize_comboBox)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.port_comboBox = QtGui.QComboBox(self.groupBox)
        self.port_comboBox.setMinimumSize(QtCore.QSize(121, 0))
        self.port_comboBox.setObjectName(_fromUtf8("port_comboBox"))
        self.horizontalLayout.addWidget(self.port_comboBox)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.sendInterval_spinBox = QtGui.QSpinBox(self.groupBox)
        self.sendInterval_spinBox.setMinimum(1)
        self.sendInterval_spinBox.setMaximum(10000)
        self.sendInterval_spinBox.setSingleStep(1)
        self.sendInterval_spinBox.setProperty("value", 1000)
        self.sendInterval_spinBox.setObjectName(_fromUtf8("sendInterval_spinBox"))
        self.gridLayout.addWidget(self.sendInterval_spinBox, 16, 0, 1, 2)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 10, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_5.addWidget(self.label_7)
        self.stopbits_comboBox = QtGui.QComboBox(self.groupBox)
        self.stopbits_comboBox.setMinimumSize(QtCore.QSize(121, 0))
        self.stopbits_comboBox.setObjectName(_fromUtf8("stopbits_comboBox"))
        self.stopbits_comboBox.addItem(_fromUtf8(""))
        self.stopbits_comboBox.addItem(_fromUtf8(""))
        self.stopbits_comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.stopbits_comboBox)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 2)
        self.recvType_comboBox = QtGui.QComboBox(self.groupBox)
        self.recvType_comboBox.setObjectName(_fromUtf8("recvType_comboBox"))
        self.recvType_comboBox.addItem(_fromUtf8(""))
        self.recvType_comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.recvType_comboBox, 8, 0, 1, 2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.baud_comboBox = QtGui.QComboBox(self.groupBox)
        self.baud_comboBox.setMinimumSize(QtCore.QSize(121, 0))
        self.baud_comboBox.setObjectName(_fromUtf8("baud_comboBox"))
        self.baud_comboBox.addItem(_fromUtf8(""))
        self.baud_comboBox.addItem(_fromUtf8(""))
        self.baud_comboBox.addItem(_fromUtf8(""))
        self.baud_comboBox.addItem(_fromUtf8(""))
        self.baud_comboBox.addItem(_fromUtf8(""))
        self.baud_comboBox.addItem(_fromUtf8(""))
        self.baud_comboBox.addItem(_fromUtf8(""))
        self.baud_comboBox.addItem(_fromUtf8(""))
        self.baud_comboBox.addItem(_fromUtf8(""))
        self.baud_comboBox.addItem(_fromUtf8(""))
        self.baud_comboBox.addItem(_fromUtf8(""))
        self.baud_comboBox.addItem(_fromUtf8(""))
        self.baud_comboBox.addItem(_fromUtf8(""))
        self.baud_comboBox.addItem(_fromUtf8(""))
        self.baud_comboBox.addItem(_fromUtf8(""))
        self.baud_comboBox.addItem(_fromUtf8(""))
        self.baud_comboBox.addItem(_fromUtf8(""))
        self.baud_comboBox.addItem(_fromUtf8(""))
        self.baud_comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.baud_comboBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)
        self.updatePort_pushButton = QtGui.QPushButton(self.groupBox)
        self.updatePort_pushButton.setObjectName(_fromUtf8("updatePort_pushButton"))
        self.gridLayout.addWidget(self.updatePort_pushButton, 6, 0, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 2, 1)
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setMinimumSize(QtCore.QSize(691, 0))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.recv_TextBrowser = Ui_TextView(self.splitter)
        self.recv_TextBrowser.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 0);"))
        self.recv_TextBrowser.setFrameShape(QtGui.QFrame.NoFrame)
        self.recv_TextBrowser.setObjectName(_fromUtf8("recv_TextBrowser"))
        self.send_TextEdit = QtGui.QTextEdit(self.splitter)
        self.send_TextEdit.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 0);"))
        self.send_TextEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.send_TextEdit.setLineWrapColumnOrWidth(-2)
        self.send_TextEdit.setObjectName(_fromUtf8("send_TextEdit"))
        self.gridLayout_2.addWidget(self.splitter, 0, 1, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_6.addWidget(self.label_3)
        self.rx_lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.rx_lcdNumber.setMinimumSize(QtCore.QSize(120, 0))
        self.rx_lcdNumber.setMaximumSize(QtCore.QSize(50, 30))
        self.rx_lcdNumber.setStyleSheet(_fromUtf8(""))
        self.rx_lcdNumber.setFrameShape(QtGui.QFrame.Box)
        self.rx_lcdNumber.setLineWidth(1)
        self.rx_lcdNumber.setSmallDecimalPoint(True)
        self.rx_lcdNumber.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.rx_lcdNumber.setProperty("value", 0.0)
        self.rx_lcdNumber.setProperty("intValue", 0)
        self.rx_lcdNumber.setObjectName(_fromUtf8("rx_lcdNumber"))
        self.horizontalLayout_6.addWidget(self.rx_lcdNumber)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_6.addWidget(self.label_8)
        self.tx_lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.tx_lcdNumber.setMinimumSize(QtCore.QSize(120, 0))
        self.tx_lcdNumber.setMaximumSize(QtCore.QSize(50, 30))
        self.tx_lcdNumber.setStyleSheet(_fromUtf8(""))
        self.tx_lcdNumber.setSmallDecimalPoint(True)
        self.tx_lcdNumber.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.tx_lcdNumber.setProperty("value", 0.0)
        self.tx_lcdNumber.setProperty("intValue", 0)
        self.tx_lcdNumber.setObjectName(_fromUtf8("tx_lcdNumber"))
        self.horizontalLayout_6.addWidget(self.tx_lcdNumber)
        self.clearLcdNumber_pushButton = QtGui.QPushButton(self.centralwidget)
        self.clearLcdNumber_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.clearLcdNumber_pushButton.setMaximumSize(QtCore.QSize(60, 30))
        self.clearLcdNumber_pushButton.setObjectName(_fromUtf8("clearLcdNumber_pushButton"))
        self.horizontalLayout_6.addWidget(self.clearLcdNumber_pushButton)
        self.clear_pushButton = QtGui.QPushButton(self.centralwidget)
        self.clear_pushButton.setMaximumSize(QtCore.QSize(60, 30))
        self.clear_pushButton.setObjectName(_fromUtf8("clear_pushButton"))
        self.horizontalLayout_6.addWidget(self.clear_pushButton)
        self.send_pushButton = QtGui.QPushButton(self.centralwidget)
        self.send_pushButton.setMinimumSize(QtCore.QSize(131, 30))
        self.send_pushButton.setMaximumSize(QtCore.QSize(100, 30))
        self.send_pushButton.setObjectName(_fromUtf8("send_pushButton"))
        self.horizontalLayout_6.addWidget(self.send_pushButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.about_action = QtGui.QAction(MainWindow)
        self.about_action.setObjectName(_fromUtf8("about_action"))
        self.saveData_action = QtGui.QAction(MainWindow)
        self.saveData_action.setObjectName(_fromUtf8("saveData_action"))
        self.quit_action = QtGui.QAction(MainWindow)
        self.quit_action.setObjectName(_fromUtf8("quit_action"))
        self.settings_action = QtGui.QAction(MainWindow)
        self.settings_action.setObjectName(_fromUtf8("settings_action"))
        self.menu.addAction(self.saveData_action)
        self.menu.addAction(self.settings_action)
        self.menu.addSeparator()
        self.menu.addAction(self.quit_action)
        self.menuHelp.addAction(self.about_action)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.quit_action, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Pyser", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "串口设置", None, QtGui.QApplication.UnicodeUTF8))
        self.sendType_comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "ASCII", None, QtGui.QApplication.UnicodeUTF8))
        self.sendType_comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "HEX", None, QtGui.QApplication.UnicodeUTF8))
        self.asciiTail_comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "CR+LF", None, QtGui.QApplication.UnicodeUTF8))
        self.asciiTail_comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "LF", None, QtGui.QApplication.UnicodeUTF8))
        self.asciiTail_comboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "CR", None, QtGui.QApplication.UnicodeUTF8))
        self.asciiTail_comboBox.setItemText(3, QtGui.QApplication.translate("MainWindow", "NONE", None, QtGui.QApplication.UnicodeUTF8))
        self.autoLF_checkBox.setText(QtGui.QApplication.translate("MainWindow", "自动换行", None, QtGui.QApplication.UnicodeUTF8))
        self.hideSRFlag_checkBox.setText(QtGui.QApplication.translate("MainWindow", "隐藏收发标志", None, QtGui.QApplication.UnicodeUTF8))
        self.inc_checkBox.setText(QtGui.QApplication.translate("MainWindow", "自增前缀", None, QtGui.QApplication.UnicodeUTF8))
        self.resetStartVal_pushButton.setText(QtGui.QApplication.translate("MainWindow", "前缀归零", None, QtGui.QApplication.UnicodeUTF8))
        self.autoSend_checkBox.setText(QtGui.QApplication.translate("MainWindow", "自动发送", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "间隔（毫秒）", None, QtGui.QApplication.UnicodeUTF8))
        self.showSent_checkBox.setText(QtGui.QApplication.translate("MainWindow", "显示发送数据", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "校验位", None, QtGui.QApplication.UnicodeUTF8))
        self.parity_comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "N", None, QtGui.QApplication.UnicodeUTF8))
        self.parity_comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "E", None, QtGui.QApplication.UnicodeUTF8))
        self.parity_comboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "O", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "接收设置", None, QtGui.QApplication.UnicodeUTF8))
        self.open_pushButton.setText(QtGui.QApplication.translate("MainWindow", "打开", None, QtGui.QApplication.UnicodeUTF8))
        self.clearSentText_checkBox.setText(QtGui.QApplication.translate("MainWindow", "发送后清空发送框数据", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "数据位", None, QtGui.QApplication.UnicodeUTF8))
        self.bytesize_comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.bytesize_comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.bytesize_comboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.bytesize_comboBox.setItemText(3, QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "串  口", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "发送设置", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "停止位", None, QtGui.QApplication.UnicodeUTF8))
        self.stopbits_comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.stopbits_comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "1.5", None, QtGui.QApplication.UnicodeUTF8))
        self.stopbits_comboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.recvType_comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "ASCII", None, QtGui.QApplication.UnicodeUTF8))
        self.recvType_comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "HEX", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "波特率", None, QtGui.QApplication.UnicodeUTF8))
        self.baud_comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "75", None, QtGui.QApplication.UnicodeUTF8))
        self.baud_comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "110", None, QtGui.QApplication.UnicodeUTF8))
        self.baud_comboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "134", None, QtGui.QApplication.UnicodeUTF8))
        self.baud_comboBox.setItemText(3, QtGui.QApplication.translate("MainWindow", "150", None, QtGui.QApplication.UnicodeUTF8))
        self.baud_comboBox.setItemText(4, QtGui.QApplication.translate("MainWindow", "300", None, QtGui.QApplication.UnicodeUTF8))
        self.baud_comboBox.setItemText(5, QtGui.QApplication.translate("MainWindow", "600", None, QtGui.QApplication.UnicodeUTF8))
        self.baud_comboBox.setItemText(6, QtGui.QApplication.translate("MainWindow", "1200", None, QtGui.QApplication.UnicodeUTF8))
        self.baud_comboBox.setItemText(7, QtGui.QApplication.translate("MainWindow", "1800", None, QtGui.QApplication.UnicodeUTF8))
        self.baud_comboBox.setItemText(8, QtGui.QApplication.translate("MainWindow", "2400", None, QtGui.QApplication.UnicodeUTF8))
        self.baud_comboBox.setItemText(9, QtGui.QApplication.translate("MainWindow", "4800", None, QtGui.QApplication.UnicodeUTF8))
        self.baud_comboBox.setItemText(10, QtGui.QApplication.translate("MainWindow", "7200", None, QtGui.QApplication.UnicodeUTF8))
        self.baud_comboBox.setItemText(11, QtGui.QApplication.translate("MainWindow", "9600", None, QtGui.QApplication.UnicodeUTF8))
        self.baud_comboBox.setItemText(12, QtGui.QApplication.translate("MainWindow", "14400", None, QtGui.QApplication.UnicodeUTF8))
        self.baud_comboBox.setItemText(13, QtGui.QApplication.translate("MainWindow", "19200", None, QtGui.QApplication.UnicodeUTF8))
        self.baud_comboBox.setItemText(14, QtGui.QApplication.translate("MainWindow", "38400", None, QtGui.QApplication.UnicodeUTF8))
        self.baud_comboBox.setItemText(15, QtGui.QApplication.translate("MainWindow", "57600", None, QtGui.QApplication.UnicodeUTF8))
        self.baud_comboBox.setItemText(16, QtGui.QApplication.translate("MainWindow", "115200", None, QtGui.QApplication.UnicodeUTF8))
        self.baud_comboBox.setItemText(17, QtGui.QApplication.translate("MainWindow", "128000", None, QtGui.QApplication.UnicodeUTF8))
        self.baud_comboBox.setItemText(18, QtGui.QApplication.translate("MainWindow", "230400", None, QtGui.QApplication.UnicodeUTF8))
        self.updatePort_pushButton.setText(QtGui.QApplication.translate("MainWindow", "刷新", None, QtGui.QApplication.UnicodeUTF8))
        self.recv_TextBrowser.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'新宋体\';\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.send_TextEdit.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'新宋体\';\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", " RX", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "TX", None, QtGui.QApplication.UnicodeUTF8))
        self.clearLcdNumber_pushButton.setText(QtGui.QApplication.translate("MainWindow", "统计清零", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_pushButton.setText(QtGui.QApplication.translate("MainWindow", "清空", None, QtGui.QApplication.UnicodeUTF8))
        self.send_pushButton.setText(QtGui.QApplication.translate("MainWindow", "        发送        ", None, QtGui.QApplication.UnicodeUTF8))
        self.menu.setTitle(QtGui.QApplication.translate("MainWindow", "文件", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "帮助", None, QtGui.QApplication.UnicodeUTF8))
        self.about_action.setText(QtGui.QApplication.translate("MainWindow", "关于", None, QtGui.QApplication.UnicodeUTF8))
        self.saveData_action.setText(QtGui.QApplication.translate("MainWindow", "保存接收区数据", None, QtGui.QApplication.UnicodeUTF8))
        self.quit_action.setText(QtGui.QApplication.translate("MainWindow", "退出", None, QtGui.QApplication.UnicodeUTF8))
        self.settings_action.setText(QtGui.QApplication.translate("MainWindow", "数据合并", None, QtGui.QApplication.UnicodeUTF8))

from Ui_TextView import Ui_TextView
