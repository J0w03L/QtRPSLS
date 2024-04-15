# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainMenu.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        if not MainMenu.objectName():
            MainMenu.setObjectName(u"MainMenu")
        MainMenu.resize(600, 600)
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        MainMenu.setFont(font)
        self.bg = QFrame(MainMenu)
        self.bg.setObjectName(u"bg")
        self.bg.setEnabled(True)
        self.bg.setGeometry(QRect(0, 0, 0, 0))
        self.bg.setStyleSheet(u"")
        self.bg.setFrameShape(QFrame.StyledPanel)
        self.bg.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.bg)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bgImg = QLabel(self.bg)
        self.bgImg.setObjectName(u"bgImg")
        self.bgImg.setStyleSheet(u"")
        self.bgImg.setLineWidth(0)
        self.bgImg.setScaledContents(True)
        self.bgImg.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.bgImg, 0, 0, 1, 1)

        self.content = QFrame(MainMenu)
        self.content.setObjectName(u"content")
        self.content.setGeometry(QRect(0, 0, 600, 600))
        self.content.setStyleSheet(u"background-color: rgba(128,128,128,16);")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.content)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widgets = QStackedWidget(self.content)
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"padding:.1em;")
        self.mainWidget = QWidget()
        self.mainWidget.setObjectName(u"mainWidget")
        self.verticalLayoutWidget = QWidget(self.mainWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(-1, -1, 601, 601))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.mainTitle = QLabel(self.verticalLayoutWidget)
        self.mainTitle.setObjectName(u"mainTitle")
        palette = QPalette()
        self.mainTitle.setPalette(palette)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.mainTitle.setFont(font1)
        self.mainTitle.setStyleSheet(u"background:none;")
        self.mainTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.mainTitle)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.mainPlayButton = QPushButton(self.verticalLayoutWidget)
        self.mainPlayButton.setObjectName(u"mainPlayButton")
        self.mainPlayButton.setMinimumSize(QSize(300, 0))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(18)
        self.mainPlayButton.setFont(font2)

        self.verticalLayout_2.addWidget(self.mainPlayButton)

        self.mainHighScoresButton = QPushButton(self.verticalLayoutWidget)
        self.mainHighScoresButton.setObjectName(u"mainHighScoresButton")
        self.mainHighScoresButton.setFont(font2)

        self.verticalLayout_2.addWidget(self.mainHighScoresButton)

        self.mainGuideButton = QPushButton(self.verticalLayoutWidget)
        self.mainGuideButton.setObjectName(u"mainGuideButton")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(18)
        font3.setBold(False)
        font3.setItalic(False)
        self.mainGuideButton.setFont(font3)

        self.verticalLayout_2.addWidget(self.mainGuideButton)

        self.mainAboutButton = QPushButton(self.verticalLayoutWidget)
        self.mainAboutButton.setObjectName(u"mainAboutButton")
        self.mainAboutButton.setFont(font2)

        self.verticalLayout_2.addWidget(self.mainAboutButton)

        self.mainExitButton = QPushButton(self.verticalLayoutWidget)
        self.mainExitButton.setObjectName(u"mainExitButton")
        self.mainExitButton.setFont(font2)

        self.verticalLayout_2.addWidget(self.mainExitButton)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.widgets.addWidget(self.mainWidget)
        self.aboutWidget = QWidget()
        self.aboutWidget.setObjectName(u"aboutWidget")
        self.verticalLayoutWidget_3 = QWidget(self.aboutWidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 632, 601))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.aboutTitle = QLabel(self.verticalLayoutWidget_3)
        self.aboutTitle.setObjectName(u"aboutTitle")
        self.aboutTitle.setMaximumSize(QSize(600, 64))
        self.aboutTitle.setFont(font1)
        self.aboutTitle.setStyleSheet(u"padding: .5em;")
        self.aboutTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.aboutTitle)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.aboutInfo = QLabel(self.verticalLayoutWidget_3)
        self.aboutInfo.setObjectName(u"aboutInfo")
        self.aboutInfo.setMaximumSize(QSize(600, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(11)
        self.aboutInfo.setFont(font4)
        self.aboutInfo.setStyleSheet(u"padding: .5em;background: none;")
        self.aboutInfo.setScaledContents(False)
        self.aboutInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.aboutInfo.setWordWrap(True)
        self.aboutInfo.setOpenExternalLinks(True)

        self.verticalLayout_4.addWidget(self.aboutInfo)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_7)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.aboutBackButton = QPushButton(self.verticalLayoutWidget_3)
        self.aboutBackButton.setObjectName(u"aboutBackButton")
        self.aboutBackButton.setMinimumSize(QSize(320, 0))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(18)
        font5.setBold(False)
        self.aboutBackButton.setFont(font5)
        self.aboutBackButton.setStyleSheet(u"margin-bottom: 1.5em;")

        self.horizontalLayout_3.addWidget(self.aboutBackButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.widgets.addWidget(self.aboutWidget)

        self.gridLayout_3.addWidget(self.widgets, 0, 0, 1, 1)


        self.retranslateUi(MainMenu)

        self.widgets.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainMenu)
    # setupUi

    def retranslateUi(self, MainMenu):
        MainMenu.setWindowTitle(QCoreApplication.translate("MainMenu", u"QtRPSLS", None))
        self.bgImg.setText("")
        self.mainTitle.setText(QCoreApplication.translate("MainMenu", u"Rock Paper Scissors Lizard Spock", None))
        self.mainPlayButton.setText(QCoreApplication.translate("MainMenu", u"Play", None))
        self.mainHighScoresButton.setText(QCoreApplication.translate("MainMenu", u"Highscores", None))
        self.mainGuideButton.setText(QCoreApplication.translate("MainMenu", u"How to Play", None))
        self.mainAboutButton.setText(QCoreApplication.translate("MainMenu", u"About", None))
        self.mainExitButton.setText(QCoreApplication.translate("MainMenu", u"Exit", None))
        self.aboutTitle.setText(QCoreApplication.translate("MainMenu", u"About", None))
        self.aboutInfo.setText(QCoreApplication.translate("MainMenu", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; text-decoration: underline;\">Project</span></p><p><span style=\" font-size:10pt;\">QtRPSLS is a game that I wrote for one of my university assignments. Built using Python and Qt 6, this project follows Sam Kass's and Karen Bryla's twist on the classic &quot;Rock Paper Scissors&quot;, letting you play a game of &quot;Rock Paper Scissors Lizard Spock&quot; against the computer!</span></p><p><span style=\" font-size:10pt;\">Once that assignment has been submitted and graded, you may view the code online at </span><a href=\"https://github.com/J0w03L/QtRPSLS\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">this GitHub repository</span></a><span style=\" font-size:10pt;\">.</span></p><p><br/><span style=\" font-size:16pt; font-weight:700; text-decoration: underline;\">Credits</span></p><p><span style=\" font-size:10pt;\">This software was written by </span><a href=\"https://github.com/J0w03L\"><span style=\" font-size"
                        ":10pt; text-decoration: underline; color:#0000ff;\">J0w03L</span></a><span style=\" font-size:10pt;\">, with the use of these open-source projects:</span></p><p><span style=\" font-size:10pt;\">- </span><a href=\"https://www.qt.io/product/development-tools\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">Qt Creator</span></a></p><p><span style=\" font-size:10pt;\">- </span><a href=\"https://www.python.org/\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">Python</span></a></p><p><span style=\" font-size:10pt;\">Additionally, this software contains some third-party media, for which attribution is given below:</span></p><p><span style=\" font-size:10pt;\">- </span><a href=\"https://en.wikipedia.org/wiki/File:Pierre_ciseaux_feuille_l%C3%A9zard_spock_aligned.svg\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">Moves diagram</span></a><span style=\" font-size:10pt;\">, licensed under </span><a href=\"https://creativecommons.org/li"
                        "censes/by-sa/3.0/deed.en\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">CC-BY-SA-3.0</span></a><span style=\" font-size:10pt;\"> by </span><a href=\"https://commons.wikimedia.org/wiki/User:DMacks\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">DMacks</span></a><span style=\" font-size:10pt;\">.</span></p><p><span style=\" font-size:10pt;\">- </span><a href=\"https://youtu.be/6s9k5rwBWB4?t=67\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">&quot;Rock Paper Scissors Lizard Spock&quot; callout audio</span></a><span style=\" font-size:10pt;\">, voice clip from &quot;The Big Bang Theory, Season 2 Episode 8: The Lizard-Spock Expansion&quot;</span></p></body></html>", None))
        self.aboutBackButton.setText(QCoreApplication.translate("MainMenu", u"Back to Main Menu", None))
    # retranslateUi

