# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialogButtonBox,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(850, 670)
        self.loginWindowBox = QGroupBox(Widget)
        self.loginWindowBox.setObjectName(u"loginWindowBox")
        self.loginWindowBox.setEnabled(False)
        self.loginWindowBox.setGeometry(QRect(210, 0, 241, 201))
        self.loginWindowBox.setAlignment(Qt.AlignCenter)
        self.userInputLogin = QLineEdit(self.loginWindowBox)
        self.userInputLogin.setObjectName(u"userInputLogin")
        self.userInputLogin.setGeometry(QRect(70, 100, 141, 23))
        self.userInputLogin.setMaxLength(20)
        self.login = QDialogButtonBox(self.loginWindowBox)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(20, 150, 191, 24))
        self.login.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.user_label = QLabel(self.loginWindowBox)
        self.user_label.setObjectName(u"user_label")
        self.user_label.setGeometry(QRect(20, 110, 53, 16))
        self.user_label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.device_label = QLabel(self.loginWindowBox)
        self.device_label.setObjectName(u"device_label")
        self.device_label.setGeometry(QRect(30, 70, 53, 16))
        self.deviceSerialNumberInput = QComboBox(self.loginWindowBox)
        self.deviceSerialNumberInput.addItem("")
        self.deviceSerialNumberInput.setObjectName(u"deviceSerialNumberInput")
        self.deviceSerialNumberInput.setGeometry(QRect(70, 60, 141, 24))
        self.login.raise_()
        self.user_label.raise_()
        self.device_label.raise_()
        self.userInputLogin.raise_()
        self.deviceSerialNumberInput.raise_()
        self.RightTipWindow = QScrollArea(Widget)
        self.RightTipWindow.setObjectName(u"RightTipWindow")
        self.RightTipWindow.setGeometry(QRect(630, 10, 211, 521))
        self.RightTipWindow.setWidgetResizable(True)
        self.RightTipContentWidget = QWidget()
        self.RightTipContentWidget.setObjectName(u"RightTipContentWidget")
        self.RightTipContentWidget.setGeometry(QRect(0, 0, 209, 519))
        self.verticalLayoutWidget = QWidget(self.RightTipContentWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 191, 501))
        self.RightTipContentWidgetTipTextLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.RightTipContentWidgetTipTextLayout.setObjectName(u"RightTipContentWidgetTipTextLayout")
        self.RightTipContentWidgetTipTextLayout.setContentsMargins(0, 0, 0, 0)
        self.RightTipWindow.setWidget(self.RightTipContentWidget)
        self.LeftTipWindow = QScrollArea(Widget)
        self.LeftTipWindow.setObjectName(u"LeftTipWindow")
        self.LeftTipWindow.setGeometry(QRect(10, 10, 181, 451))
        self.LeftTipWindow.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 179, 449))
        self.loginWindowShowButton = QPushButton(self.scrollAreaWidgetContents)
        self.loginWindowShowButton.setObjectName(u"loginWindowShowButton")
        self.loginWindowShowButton.setEnabled(False)
        self.loginWindowShowButton.setGeometry(QRect(10, 420, 71, 24))
        self.loginWindowShowButton.setCheckable(False)
        self.verticalLayoutWidget_2 = QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 30, 161, 371))
        self.devicesGroupBox = QVBoxLayout(self.verticalLayoutWidget_2)
        self.devicesGroupBox.setObjectName(u"devicesGroupBox")
        self.devicesGroupBox.setContentsMargins(0, 0, 0, 0)
        self.scrollAreaWidgetContentsTitle = QLabel(self.scrollAreaWidgetContents)
        self.scrollAreaWidgetContentsTitle.setObjectName(u"scrollAreaWidgetContentsTitle")
        self.scrollAreaWidgetContentsTitle.setGeometry(QRect(10, 10, 53, 16))
        font = QFont()
        font.setPointSize(9)
        self.scrollAreaWidgetContentsTitle.setFont(font)
        self.reloadDeviceListButton = QPushButton(self.scrollAreaWidgetContents)
        self.reloadDeviceListButton.setObjectName(u"reloadDeviceListButton")
        self.reloadDeviceListButton.setEnabled(True)
        self.reloadDeviceListButton.setGeometry(QRect(100, 420, 71, 24))
        self.LeftTipWindow.setWidget(self.scrollAreaWidgetContents)
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(390, 530, 451, 131))
        self.restartAppButton = QPushButton(self.groupBox)
        self.restartAppButton.setObjectName(u"restartAppButton")
        self.restartAppButton.setGeometry(QRect(10, 30, 80, 24))
        self.QuickTextsOptionBox = QGroupBox(self.groupBox)
        self.QuickTextsOptionBox.setObjectName(u"QuickTextsOptionBox")
        self.QuickTextsOptionBox.setGeometry(QRect(10, 60, 161, 61))
        self.quickTextsAllRoomSelectOption = QComboBox(self.QuickTextsOptionBox)
        self.quickTextsAllRoomSelectOption.addItem("")
        self.quickTextsAllRoomSelectOption.addItem("")
        self.quickTextsAllRoomSelectOption.addItem("")
        self.quickTextsAllRoomSelectOption.addItem("")
        self.quickTextsAllRoomSelectOption.setObjectName(u"quickTextsAllRoomSelectOption")
        self.quickTextsAllRoomSelectOption.setGeometry(QRect(10, 30, 141, 22))
        self.QuickTextsInputBox = QGroupBox(self.groupBox)
        self.QuickTextsInputBox.setObjectName(u"QuickTextsInputBox")
        self.QuickTextsInputBox.setGeometry(QRect(190, 60, 191, 61))
        self.sendQuickTextAllRoomInputButton = QPushButton(self.QuickTextsInputBox)
        self.sendQuickTextAllRoomInputButton.setObjectName(u"sendQuickTextAllRoomInputButton")
        self.sendQuickTextAllRoomInputButton.setGeometry(QRect(130, 30, 51, 24))
        self.sendAllLiveRoomTextInput = QLineEdit(self.QuickTextsInputBox)
        self.sendAllLiveRoomTextInput.setObjectName(u"sendAllLiveRoomTextInput")
        self.sendAllLiveRoomTextInput.setGeometry(QRect(10, 30, 111, 21))
        self.inLiveRoomBox = QWidget(self.groupBox)
        self.inLiveRoomBox.setObjectName(u"inLiveRoomBox")
        self.inLiveRoomBox.setGeometry(QRect(90, 20, 171, 41))
        self.inLiveRoomButton = QPushButton(self.inLiveRoomBox)
        self.inLiveRoomButton.setObjectName(u"inLiveRoomButton")
        self.inLiveRoomButton.setGeometry(QRect(119, 10, 41, 24))
        self.inLiveRoomNameInput = QLineEdit(self.inLiveRoomBox)
        self.inLiveRoomNameInput.setObjectName(u"inLiveRoomNameInput")
        self.inLiveRoomNameInput.setGeometry(QRect(10, 10, 101, 23))

        self.retranslateUi(Widget)
        self.login.rejected.connect(self.loginWindowBox.close)
        self.loginWindowShowButton.clicked.connect(self.loginWindowBox.show)
        self.quickTextsAllRoomSelectOption.currentTextChanged.connect(self.sendAllLiveRoomTextInput.setText)
        self.loginWindowShowButton.clicked.connect(self.login.show)
        self.sendAllLiveRoomTextInput.returnPressed.connect(self.sendQuickTextAllRoomInputButton.animateClick)
        self.inLiveRoomNameInput.returnPressed.connect(self.inLiveRoomButton.animateClick)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"\u6296\u97f3\u76f4\u64ad\u52a9\u624b", None))
#if QT_CONFIG(tooltip)
        Widget.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.loginWindowBox.setToolTip(QCoreApplication.translate("Widget", u"\u767b\u5f55\u7a97\u53e3", None))
#endif // QT_CONFIG(tooltip)
        self.loginWindowBox.setTitle(QCoreApplication.translate("Widget", u"\u767b\u5f55\u6296\u97f3", None))
        self.userInputLogin.setText("")
        self.userInputLogin.setPlaceholderText(QCoreApplication.translate("Widget", u"\u767b\u5f55\u8d26\u53f7", None))
        self.user_label.setText(QCoreApplication.translate("Widget", u"\u8d26\u53f7:", None))
        self.device_label.setText(QCoreApplication.translate("Widget", u"\u8bbe\u5907:", None))
        self.deviceSerialNumberInput.setItemText(0, "")

        self.loginWindowShowButton.setText(QCoreApplication.translate("Widget", u"\u767b\u5f55", None))
        self.scrollAreaWidgetContentsTitle.setText(QCoreApplication.translate("Widget", u"\u8bbe\u5907\u5217\u8868", None))
#if QT_CONFIG(tooltip)
        self.reloadDeviceListButton.setToolTip(QCoreApplication.translate("Widget", u"<html><head/><body><p>\u5237\u65b0\u8bbe\u5907\u5217\u8868</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.reloadDeviceListButton.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.reloadDeviceListButton.setText(QCoreApplication.translate("Widget", u"\u5237\u65b0", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"\u6279\u91cf\u64cd\u4f5c", None))
#if QT_CONFIG(tooltip)
        self.restartAppButton.setToolTip(QCoreApplication.translate("Widget", u"<html><head/><body><p>\u6279\u91cf\u91cd\u542f\u6296\u97f3app</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.restartAppButton.setText(QCoreApplication.translate("Widget", u"\u542f\u52a8/\u91cd\u542f", None))
        self.QuickTextsOptionBox.setTitle(QCoreApplication.translate("Widget", u"\u9009\u62e9\u5feb\u6377\u8bed", None))
        self.quickTextsAllRoomSelectOption.setItemText(0, "")
        self.quickTextsAllRoomSelectOption.setItemText(1, QCoreApplication.translate("Widget", u"666", None))
        self.quickTextsAllRoomSelectOption.setItemText(2, QCoreApplication.translate("Widget", u"\u597d", None))
        self.quickTextsAllRoomSelectOption.setItemText(3, QCoreApplication.translate("Widget", u"1", None))

        self.QuickTextsInputBox.setTitle(QCoreApplication.translate("Widget", u"\u53d1\u5f39\u5e55", None))
        self.sendQuickTextAllRoomInputButton.setText(QCoreApplication.translate("Widget", u"\u53d1\u9001", None))
#if QT_CONFIG(tooltip)
        self.inLiveRoomButton.setToolTip(QCoreApplication.translate("Widget", u"<html><head/><body><p>\u6279\u91cf\u8fdb\u5165\u9ed8\u8ba4\u76f4\u64ad\u95f4</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inLiveRoomButton.setText(QCoreApplication.translate("Widget", u"\u8fdb\u5165", None))
        self.inLiveRoomNameInput.setPlaceholderText(QCoreApplication.translate("Widget", u"\u76f4\u64ad\u95f4\u540d\u79f0", None))
    # retranslateUi

