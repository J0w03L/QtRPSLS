# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Game.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QStackedWidget, QWidget)
import rc_resources

class Ui_GameWidget(object):
    def setupUi(self, GameWidget):
        if not GameWidget.objectName():
            GameWidget.setObjectName(u"GameWidget")
        GameWidget.resize(600, 600)
        GameWidget.setMinimumSize(QSize(600, 600))
        GameWidget.setMaximumSize(QSize(600, 600))
        self.scene = QFrame(GameWidget)
        self.scene.setObjectName(u"scene")
        self.scene.setGeometry(QRect(0, 0, 601, 431))
        self.scene.setFrameShape(QFrame.Shape.StyledPanel)
        self.scene.setFrameShadow(QFrame.Shadow.Raised)
        self.sceneWidgets = QStackedWidget(self.scene)
        self.sceneWidgets.setObjectName(u"sceneWidgets")
        self.sceneWidgets.setGeometry(QRect(10, 10, 581, 411))
        self.sceneWidgets.setAutoFillBackground(False)
        self.userWidget = QWidget()
        self.userWidget.setObjectName(u"userWidget")
        self.userWidget.setStyleSheet(u"background-color:rgba(128,128,128,32);")
        self.whoIsPlayingLabel = QLabel(self.userWidget)
        self.whoIsPlayingLabel.setObjectName(u"whoIsPlayingLabel")
        self.whoIsPlayingLabel.setGeometry(QRect(10, 10, 561, 61))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(26)
        font.setBold(True)
        self.whoIsPlayingLabel.setFont(font)
        self.whoIsPlayingLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.newUserFrame = QFrame(self.userWidget)
        self.newUserFrame.setObjectName(u"newUserFrame")
        self.newUserFrame.setEnabled(True)
        self.newUserFrame.setGeometry(QRect(10, 290, 561, 61))
        self.newUserFrame.setStyleSheet(u"")
        self.newUserFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.newUserFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayoutWidget = QWidget(self.newUserFrame)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 541, 41))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.newUserNameFieldLabel = QLabel(self.formLayoutWidget)
        self.newUserNameFieldLabel.setObjectName(u"newUserNameFieldLabel")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.newUserNameFieldLabel.setFont(font1)
        self.newUserNameFieldLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.newUserNameFieldLabel)

        self.newUserNameField = QLineEdit(self.formLayoutWidget)
        self.newUserNameField.setObjectName(u"newUserNameField")
        self.newUserNameField.setEnabled(False)
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(20)
        self.newUserNameField.setFont(font2)
        self.newUserNameField.setMaxLength(100)
        self.newUserNameField.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.newUserNameField.setClearButtonEnabled(False)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.newUserNameField)

        self.userPlayButton = QPushButton(self.userWidget)
        self.userPlayButton.setObjectName(u"userPlayButton")
        self.userPlayButton.setGeometry(QRect(20, 360, 541, 41))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(18)
        font3.setBold(True)
        self.userPlayButton.setFont(font3)
        self.userList = QListWidget(self.userWidget)
        self.userList.setObjectName(u"userList")
        self.userList.setGeometry(QRect(10, 80, 561, 201))
        self.sceneWidgets.addWidget(self.userWidget)
        self.playingWidget = QWidget()
        self.playingWidget.setObjectName(u"playingWidget")
        self.sceneActionLabel = QLabel(self.playingWidget)
        self.sceneActionLabel.setObjectName(u"sceneActionLabel")
        self.sceneActionLabel.setGeometry(QRect(0, 0, 581, 411))
        self.sceneActionLabel.setScaledContents(True)
        self.sceneActionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sceneWidgets.addWidget(self.playingWidget)
        self.replayWidget = QWidget()
        self.replayWidget.setObjectName(u"replayWidget")
        self.sceneWidgets.addWidget(self.replayWidget)
        self.hud = QFrame(GameWidget)
        self.hud.setObjectName(u"hud")
        self.hud.setGeometry(QRect(10, 440, 581, 151))
        self.hud.setFrameShape(QFrame.Shape.StyledPanel)
        self.hud.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget = QWidget(self.hud)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 581, 101))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.rockButton = QPushButton(self.horizontalLayoutWidget)
        self.rockButton.setObjectName(u"rockButton")
        self.rockButton.setEnabled(True)
        self.rockButton.setMinimumSize(QSize(64, 64))
        self.rockButton.setMaximumSize(QSize(16777215, 16777215))
        self.rockButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/assets/Game/img/rock_new.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.rockButton.setIcon(icon)
        self.rockButton.setIconSize(QSize(64, 64))

        self.horizontalLayout.addWidget(self.rockButton)

        self.paperButton = QPushButton(self.horizontalLayoutWidget)
        self.paperButton.setObjectName(u"paperButton")
        self.paperButton.setMouseTracking(False)
        self.paperButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/assets/Game/img/paper_new.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.paperButton.setIcon(icon1)
        self.paperButton.setIconSize(QSize(64, 64))

        self.horizontalLayout.addWidget(self.paperButton)

        self.scissorsButton = QPushButton(self.horizontalLayoutWidget)
        self.scissorsButton.setObjectName(u"scissorsButton")
        self.scissorsButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/assets/Game/img/scissors_new.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.scissorsButton.setIcon(icon2)
        self.scissorsButton.setIconSize(QSize(64, 64))

        self.horizontalLayout.addWidget(self.scissorsButton)

        self.lizardButton = QPushButton(self.horizontalLayoutWidget)
        self.lizardButton.setObjectName(u"lizardButton")
        self.lizardButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/assets/Game/img/lizard_new.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.lizardButton.setIcon(icon3)
        self.lizardButton.setIconSize(QSize(64, 64))

        self.horizontalLayout.addWidget(self.lizardButton)

        self.spockButton = QPushButton(self.horizontalLayoutWidget)
        self.spockButton.setObjectName(u"spockButton")
        self.spockButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/assets/Game/img/spock_new.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.spockButton.setIcon(icon4)
        self.spockButton.setIconSize(QSize(64, 64))

        self.horizontalLayout.addWidget(self.spockButton)

        self.scoreLabel = QLabel(self.hud)
        self.scoreLabel.setObjectName(u"scoreLabel")
        self.scoreLabel.setGeometry(QRect(0, 100, 581, 51))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(14)
        self.scoreLabel.setFont(font4)
        self.scoreLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(GameWidget)

        self.sceneWidgets.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(GameWidget)
    # setupUi

    def retranslateUi(self, GameWidget):
        GameWidget.setWindowTitle(QCoreApplication.translate("GameWidget", u"QtRPSLS", None))
        self.whoIsPlayingLabel.setText(QCoreApplication.translate("GameWidget", u"Who is playing?", None))
        self.newUserNameFieldLabel.setText(QCoreApplication.translate("GameWidget", u"Your user name is:", None))
        self.newUserNameField.setPlaceholderText(QCoreApplication.translate("GameWidget", u"John Doe", None))
        self.userPlayButton.setText(QCoreApplication.translate("GameWidget", u"Play", None))
        self.sceneActionLabel.setText("")
#if QT_CONFIG(tooltip)
        self.rockButton.setToolTip(QCoreApplication.translate("GameWidget", u"Play Rock", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.rockButton.setAccessibleName(QCoreApplication.translate("GameWidget", u"Rock", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.rockButton.setAccessibleDescription(QCoreApplication.translate("GameWidget", u"Play Rock", None))
#endif // QT_CONFIG(accessibility)
        self.rockButton.setText("")
#if QT_CONFIG(tooltip)
        self.paperButton.setToolTip(QCoreApplication.translate("GameWidget", u"Play Paper", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.paperButton.setAccessibleName(QCoreApplication.translate("GameWidget", u"Paper", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.paperButton.setAccessibleDescription(QCoreApplication.translate("GameWidget", u"Play Paper", None))
#endif // QT_CONFIG(accessibility)
        self.paperButton.setText("")
#if QT_CONFIG(tooltip)
        self.scissorsButton.setToolTip(QCoreApplication.translate("GameWidget", u"Play Scissors", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.scissorsButton.setAccessibleName(QCoreApplication.translate("GameWidget", u"Scissors", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.scissorsButton.setAccessibleDescription(QCoreApplication.translate("GameWidget", u"Play Scissors", None))
#endif // QT_CONFIG(accessibility)
        self.scissorsButton.setText("")
#if QT_CONFIG(tooltip)
        self.lizardButton.setToolTip(QCoreApplication.translate("GameWidget", u"Play Lizard", None))
#endif // QT_CONFIG(tooltip)
        self.lizardButton.setText("")
#if QT_CONFIG(tooltip)
        self.spockButton.setToolTip(QCoreApplication.translate("GameWidget", u"Play Spock", None))
#endif // QT_CONFIG(tooltip)
        self.spockButton.setText("")
        self.scoreLabel.setText(QCoreApplication.translate("GameWidget", u"You are tied at 0 v 0.", None))
    # retranslateUi

