# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'cadastro.ui'
##
# Created by: Qt User Interface Compiler version 6.2.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
                               QHBoxLayout, QHeaderView, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
                               QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
                               QToolBox, QVBoxLayout, QWidget)
import icons_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(935, 497)
        MainWindow.setStyleSheet(u"background-color: rgb(9, 9, 9);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
                                         "	\n"
                                         "	border:none;\n"
                                         "\n"
                                         "}\n"
                                         "\n"
                                         "QLabel{\n"
                                         "	color: rgb(255, 255, 255);\n"
                                         "\n"
                                         "\n"
                                         "}\n"
                                         "")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu = QFrame(self.centralwidget)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMaximumSize(QSize(9, 16777215))
        self.left_menu.setStyleSheet(u"")
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.frame_4 = QFrame(self.left_menu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Cooper Black"])
        font.setPointSize(12)
        self.label_3.setFont(font)

        self.verticalLayout_3.addWidget(self.label_3)

        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.left_menu)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet(u"QFrame{\n"
                                   "	\n"
                                   "	background-color: rgb(65, 65, 65);\n"
                                   "\n"
                                   "}\n"
                                   "\n"
                                   "QToolBox{\n"
                                   "\n"
                                   "text-align: left;\n"
                                   "	background-color: rgb(228, 254, 255);\n"
                                   "\n"
                                   "}\n"
                                   "\n"
                                   "\n"
                                   "QToolBox::tab{\n"
                                   "	border-radius: 5px;	\n"
                                   "	\n"
                                   "	background-color: rgb(194, 232, 255);\n"
                                   "	text-align: left;\n"
                                   "\n"
                                   "}\n"
                                   "")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, -1)
        self.toolBox = QToolBox(self.frame_5)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QPushButton:hover{	\n"
                                   "	background-color: rgb(65, 65, 65);\n"
                                   "	 border-top-left-radius:15px\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton{\n"
                                   "	\n"
                                   "	color: rgb(255, 255, 255);\n"
                                   "\n"
                                   "\n"
                                   "}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 67, 343))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 9, 0, -1)
        self.btn_home = QPushButton(self.page)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(12)
        self.btn_home.setFont(font1)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_menu_register = QPushButton(self.page)
        self.btn_menu_register.setObjectName(u"btn_menu_register")
        self.btn_menu_register.setMinimumSize(QSize(0, 30))
        self.btn_menu_register.setFont(font1)
        self.btn_menu_register.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_menu_register)

        self.btn_menu_contacts = QPushButton(self.page)
        self.btn_menu_contacts.setObjectName(u"btn_menu_contacts")
        self.btn_menu_contacts.setMinimumSize(QSize(0, 30))
        self.btn_menu_contacts.setFont(font1)
        self.btn_menu_contacts.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_menu_contacts)

        self.btn_menu_about = QPushButton(self.page)
        self.btn_menu_about.setObjectName(u"btn_menu_about")
        self.btn_menu_about.setMinimumSize(QSize(0, 30))
        self.btn_menu_about.setFont(font1)
        self.btn_menu_about.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_menu_about)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Menu")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 84, 360))
        self.verticalLayout_15 = QVBoxLayout(self.page_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_15 = QLabel(self.page_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_15.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.label_15)

        self.toolBox.addItem(self.page_2, u"Information")

        self.verticalLayout_5.addWidget(self.toolBox)

        self.verticalLayout_2.addWidget(self.frame_5)

        self.horizontalLayout.addWidget(self.left_menu)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_toggle = QPushButton(self.top_frame)
        self.btn_toggle.setObjectName(u"btn_toggle")
        self.btn_toggle.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu2.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon)
        self.btn_toggle.setIconSize(QSize(30, 40))

        self.horizontalLayout_2.addWidget(self.btn_toggle, 0, Qt.AlignLeft)

        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label)

        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy.setHeightForWidth(
            self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.main_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Pages = QStackedWidget(self.main_frame)
        self.Pages.setObjectName(u"Pages")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_8 = QVBoxLayout(self.pg_home)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.pg_home)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_8.addWidget(self.label_4, 0, Qt.AlignVCenter)

        self.Pages.addWidget(self.pg_home)
        self.pg_register = QWidget()
        self.pg_register.setObjectName(u"pg_register")
        self.verticalLayout_9 = QVBoxLayout(self.pg_register)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tabWidget = QTabWidget(self.pg_register)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_10 = QVBoxLayout(self.tab)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_16 = QFrame(self.tab)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy1.setHeightForWidth(
            self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy1)
        self.frame_16.setStyleSheet(u"QLineEdit{\n"
                                    "\n"
                                    "	background-color: rgb(255, 255, 255);\n"
                                    "	font: 10pt \"MS Shell Dlg 2\";\n"
                                    "}\n"
                                    "\n"
                                    "QFrame{\n"
                                    "	\n"
                                    "	\n"
                                    "	background-color: rgb(231, 231, 231);\n"
                                    "\n"
                                    "}")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_16)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.txt_complement = QLineEdit(self.frame_16)
        self.txt_complement.setObjectName(u"txt_complement")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.txt_complement.sizePolicy().hasHeightForWidth())
        self.txt_complement.setSizePolicy(sizePolicy2)
        self.txt_complement.setMinimumSize(QSize(0, 30))
        self.txt_complement.setMaximumSize(QSize(16777215, 30))
        self.txt_complement.setStyleSheet(u"")
        self.txt_complement.setMaxLength(21)

        self.gridLayout_7.addWidget(self.txt_complement, 3, 2, 1, 2)

        self.txt_phone_contr = QLineEdit(self.frame_16)
        self.txt_phone_contr.setObjectName(u"txt_phone_contr")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.txt_phone_contr.sizePolicy().hasHeightForWidth())
        self.txt_phone_contr.setSizePolicy(sizePolicy3)
        self.txt_phone_contr.setMinimumSize(QSize(0, 30))
        self.txt_phone_contr.setMaximumSize(QSize(16777215, 30))
        self.txt_phone_contr.setStyleSheet(u"")
        self.txt_phone_contr.setMaxLength(13)
        self.txt_phone_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.txt_phone_contr, 5, 0, 1, 3)

        self.txt_address = QLineEdit(self.frame_16)
        self.txt_address.setObjectName(u"txt_address")
        sizePolicy2.setHeightForWidth(
            self.txt_address.sizePolicy().hasHeightForWidth())
        self.txt_address.setSizePolicy(sizePolicy2)
        self.txt_address.setMinimumSize(QSize(0, 30))
        self.txt_address.setMaximumSize(QSize(16777215, 30))
        self.txt_address.setStyleSheet(u"")
        self.txt_address.setMaxLength(40)

        self.gridLayout_7.addWidget(self.txt_address, 2, 0, 1, 6)

        self.txt_cnpj_contr = QLineEdit(self.frame_16)
        self.txt_cnpj_contr.setObjectName(u"txt_cnpj_contr")
        sizePolicy2.setHeightForWidth(
            self.txt_cnpj_contr.sizePolicy().hasHeightForWidth())
        self.txt_cnpj_contr.setSizePolicy(sizePolicy2)
        self.txt_cnpj_contr.setMinimumSize(QSize(0, 30))
        self.txt_cnpj_contr.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setPointSize(10)
        self.txt_cnpj_contr.setFont(font2)
        self.txt_cnpj_contr.setStyleSheet(
            u"background-color: rgb(255, 255, 255);")
        self.txt_cnpj_contr.setMaxLength(14)
        self.txt_cnpj_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.txt_cnpj_contr, 1, 0, 1, 2)

        self.txt_name_contr = QLineEdit(self.frame_16)
        self.txt_name_contr.setObjectName(u"txt_name_contr")
        sizePolicy2.setHeightForWidth(
            self.txt_name_contr.sizePolicy().hasHeightForWidth())
        self.txt_name_contr.setSizePolicy(sizePolicy2)
        self.txt_name_contr.setMinimumSize(QSize(0, 30))
        self.txt_name_contr.setMaximumSize(QSize(16777215, 30))
        self.txt_name_contr.setStyleSheet(u"")
        self.txt_name_contr.setMaxLength(115)
        self.txt_name_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.txt_name_contr, 1, 2, 1, 4)

        self.txt_NUMBER = QLineEdit(self.frame_16)
        self.txt_NUMBER.setObjectName(u"txt_number")
        sizePolicy2.setHeightForWidth(
            self.txt_NUMBER.sizePolicy().hasHeightForWidth())
        self.txt_NUMBER.setSizePolicy(sizePolicy2)
        self.txt_NUMBER.setMinimumSize(QSize(0, 30))
        self.txt_NUMBER.setStyleSheet(u"")
        self.txt_NUMBER.setMaxLength(6)

        self.gridLayout_7.addWidget(self.txt_NUMBER, 3, 0, 1, 2)

        self.txt_Province = QLineEdit(self.frame_16)
        self.txt_Province.setObjectName(u"txt_Province")
        sizePolicy2.setHeightForWidth(
            self.txt_Province.sizePolicy().hasHeightForWidth())
        self.txt_Province.setSizePolicy(sizePolicy2)
        self.txt_Province.setMinimumSize(QSize(0, 0))
        self.txt_Province.setStyleSheet(u"")
        self.txt_Province.setMaxLength(2)
        self.txt_Province.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.txt_Province, 4, 4, 1, 1)

        self.txt_email_contr = QLineEdit(self.frame_16)
        self.txt_email_contr.setObjectName(u"txt_email_contr")
        sizePolicy3.setHeightForWidth(
            self.txt_email_contr.sizePolicy().hasHeightForWidth())
        self.txt_email_contr.setSizePolicy(sizePolicy3)
        self.txt_email_contr.setMinimumSize(QSize(0, 30))
        self.txt_email_contr.setMaximumSize(QSize(16777215, 30))
        self.txt_email_contr.setStyleSheet(u"")
        self.txt_email_contr.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.txt_email_contr.setMaxLength(40)
        self.txt_email_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.txt_email_contr, 5, 3, 1, 3)

        self.txt_ZipCode = QLineEdit(self.frame_16)
        self.txt_ZipCode.setObjectName(u"txt_ZipCode")
        sizePolicy3.setHeightForWidth(
            self.txt_ZipCode.sizePolicy().hasHeightForWidth())
        self.txt_ZipCode.setSizePolicy(sizePolicy3)
        self.txt_ZipCode.setMinimumSize(QSize(0, 30))
        self.txt_ZipCode.setStyleSheet(u"")
        self.txt_ZipCode.setMaxLength(8)
        self.txt_ZipCode.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.txt_ZipCode, 4, 5, 1, 1)

        self.txt_city = QLineEdit(self.frame_16)
        self.txt_city.setObjectName(u"txt_city")
        sizePolicy2.setHeightForWidth(
            self.txt_city.sizePolicy().hasHeightForWidth())
        self.txt_city.setSizePolicy(sizePolicy2)
        self.txt_city.setMinimumSize(QSize(0, 30))
        self.txt_city.setStyleSheet(u"")
        self.txt_city.setMaxLength(50)
        self.txt_city.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.txt_city, 4, 0, 1, 4)

        self.txt_neighborhood = QLineEdit(self.frame_16)
        self.txt_neighborhood.setObjectName(u"txt_neighborhood")
        sizePolicy2.setHeightForWidth(
            self.txt_neighborhood.sizePolicy().hasHeightForWidth())
        self.txt_neighborhood.setSizePolicy(sizePolicy2)
        self.txt_neighborhood.setMinimumSize(QSize(0, 0))
        self.txt_neighborhood.setStyleSheet(u"")
        self.txt_neighborhood.setMaxLength(20)
        self.txt_neighborhood.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.txt_neighborhood, 3, 4, 1, 2)

        self.label_18 = QLabel(self.frame_16)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"color: rgb(0, 99, 148);\n"
                                    "background-color: rgb(249, 249, 249);\n"
                                    "")

        self.gridLayout_7.addWidget(self.label_18, 0, 0, 1, 6)

        self.verticalLayout_10.addWidget(self.frame_16)

        self.btn_register = QPushButton(self.tab)
        self.btn_register.setObjectName(u"btn_register")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.btn_register.sizePolicy().hasHeightForWidth())
        self.btn_register.setSizePolicy(sizePolicy4)
        self.btn_register.setMinimumSize(QSize(170, 30))
        self.btn_register.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setPointSize(11)
        self.btn_register.setFont(font3)
        self.btn_register.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_register.setStyleSheet(u"QPushButton:hover{\n"
                                        "	background-color:rgb(0, 170, 255); \n"
                                        "	border-radius:15px;\n"
                                        "	color:#fff\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton{\n"
                                        "			border-radius:15px;\n"
                                        "	background-color: rgb(243, 243, 243);\n"
                                        "}")

        self.verticalLayout_10.addWidget(
            self.btn_register, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_11 = QVBoxLayout(self.tab_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 70))
        font4 = QFont()
        font4.setFamilies([u"Eras Bold ITC"])
        font4.setPointSize(14)
        self.label_11.setFont(font4)
        self.label_11.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                    "color: rgb(9, 9, 9);")

        self.verticalLayout_11.addWidget(self.label_11)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tb_company = QTableWidget(self.tab_2)
        if (self.tb_company.columnCount() < 11):
            self.tb_company.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        if (self.tb_company.rowCount() < 20):
            self.tb_company.setRowCount(20)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFlags(Qt.ItemIsSelectable | Qt.ItemIsDragEnabled |
                                      Qt.ItemIsDropEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        self.tb_company.setItem(0, 0, __qtablewidgetitem11)
        self.tb_company.setObjectName(u"tb_company")
        self.tb_company.setStyleSheet(u"\n"
                                      "QHeaderView::section {\n"
                                      "background-color: rgb(148, 148, 148);\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "	font: 10pt \"MS Shell Dlg 2\";\n"
                                      " }\n"
                                      "\n"
                                      "QTableWidget{\n"
                                      "	\n"
                                      "	background-color: rgb(252, 252, 252);\n"
                                      "\n"
                                      "}")
        self.tb_company.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tb_company.setRowCount(20)
        self.tb_company.horizontalHeader().setCascadingSectionResizes(True)
        self.tb_company.horizontalHeader().setDefaultSectionSize(170)
        self.tb_company.verticalHeader().setVisible(False)

        self.horizontalLayout_4.addWidget(self.tb_company)

        self.frame = QFrame(self.tab_2)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QPushButton{\n"
                                 "\n"
                                 "\n"
                                 "	border-radius:15px;\n"
                                 "	\n"
                                 "	background-color: rgb(255, 255, 255);\n"
                                 "	\n"
                                 "	font: 11pt \"MS Shell Dlg 2\";\n"
                                 "	\n"
                                 "	color: rgb(0, 24, 74);\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "QFrame{\n"
                                 "\n"
                                 "	background-color: rgb(230, 230, 230);\n"
                                 "\n"
                                 "}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.btn_excel = QPushButton(self.frame)
        self.btn_excel.setObjectName(u"btn_excel")
        sizePolicy4.setHeightForWidth(
            self.btn_excel.sizePolicy().hasHeightForWidth())
        self.btn_excel.setSizePolicy(sizePolicy4)
        self.btn_excel.setMinimumSize(QSize(120, 31))
        font5 = QFont()
        font5.setFamilies([u"MS Shell Dlg 2"])
        font5.setPointSize(11)
        font5.setBold(False)
        font5.setItalic(False)
        self.btn_excel.setFont(font5)
        self.btn_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excel.setStyleSheet(u"QPushButton:hover{\n"
                                     "	 color: rgb(255,255,255);\n"
                                     "	background-color: rgb(49, 147, 0)}\n"
                                     "")

        self.verticalLayout_12.addWidget(self.btn_excel)

        self.btn_update = QPushButton(self.frame)
        self.btn_update.setObjectName(u"btn_update")
        sizePolicy4.setHeightForWidth(
            self.btn_update.sizePolicy().hasHeightForWidth())
        self.btn_update.setSizePolicy(sizePolicy4)
        self.btn_update.setMinimumSize(QSize(120, 31))
        self.btn_update.setFont(font5)
        self.btn_update.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_update.setStyleSheet(u"QPushButton:hover{\n"
                                      "	background-color:rgb(255, 170, 0);\n"
                                      " 	color: rgb(255,255,255)\n"
                                      "}\n"
                                      "")

        self.verticalLayout_12.addWidget(self.btn_update)

        self.btn_delete = QPushButton(self.frame)
        self.btn_delete.setObjectName(u"btn_delete")
        sizePolicy4.setHeightForWidth(
            self.btn_delete.sizePolicy().hasHeightForWidth())
        self.btn_delete.setSizePolicy(sizePolicy4)
        self.btn_delete.setMinimumSize(QSize(120, 31))
        self.btn_delete.setFont(font5)
        self.btn_delete.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete.setStyleSheet(
            u"QPushButton:hover{background-color:rgb(199, 66, 0); color: rgb(255,255,255)}")

        self.verticalLayout_12.addWidget(self.btn_delete)

        self.verticalSpacer_7 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_7)

        self.horizontalLayout_4.addWidget(self.frame)

        self.verticalLayout_11.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_9.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_register)
        self.pg_contacts = QWidget()
        self.pg_contacts.setObjectName(u"pg_contacts")
        self.verticalLayout_14 = QVBoxLayout(self.pg_contacts)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_5 = QLabel(self.pg_contacts)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(
            self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMaximumSize(QSize(16777215, 70))

        self.verticalLayout_14.addWidget(self.label_5)

        self.frame_2 = QFrame(self.pg_contacts)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(
            self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)

        self.verticalLayout_13.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(
            self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)

        self.verticalLayout_13.addWidget(self.label_8)

        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(
            self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)

        self.verticalLayout_13.addWidget(self.label_12)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(
            self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_13.addWidget(self.label_10)

        self.verticalLayout_14.addWidget(self.frame_2, 0, Qt.AlignHCenter)

        self.Pages.addWidget(self.pg_contacts)
        self.pg_about = QWidget()
        self.pg_about.setObjectName(u"pg_about")
        self.verticalLayout_7 = QVBoxLayout(self.pg_about)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_16 = QLabel(self.pg_about)
        self.label_16.setObjectName(u"label_16")
        sizePolicy1.setHeightForWidth(
            self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy1)
        self.label_16.setMaximumSize(QSize(16777215, 70))

        self.verticalLayout_7.addWidget(self.label_16)

        self.label_17 = QLabel(self.pg_about)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.label_17)

        self.Pages.addWidget(self.pg_about)

        self.verticalLayout_6.addWidget(self.Pages)

        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.footer_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.verticalLayout.addWidget(self.footer_frame)

        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.Pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.pushButton_2.setText(QCoreApplication.translate(
            "MainWindow", u"PushButton", None))
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"Company", None))
        self.btn_home.setText(QCoreApplication.translate(
            "MainWindow", u"Home", None))
        self.btn_menu_register.setText(
            QCoreApplication.translate("MainWindow", u"Register", None))
        self.btn_menu_contacts.setText(
            QCoreApplication.translate("MainWindow", u"Contacts", None))
        self.btn_menu_about.setText(
            QCoreApplication.translate("MainWindow", u"About", None))
        self.toolBox.setItemText(self.toolBox.indexOf(
            self.page), QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Usu\u00e1rio:</span><span style=\" font-size:10pt;\"> PyTax</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Sistema: </span><span style=\" font-size:10pt;\">Cadastro</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Status:</span><span style=\" font-size:10pt;\"> Ativo</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Venc: </span><span style=\" font-size:10pt;\">12/12/2999</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate(
            "MainWindow", u"Information", None))
        self.btn_toggle.setText(QCoreApplication.translate(
            "MainWindow", u"toggle", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Registration Company System</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Registration Blenda Tocantins Company System</span></p></body></html>", None))
        self.txt_complement.setText("")
        self.txt_complement.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Complement", None))
        self.txt_phone_contr.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Phone", None))
        self.txt_address.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Address", None))
        self.txt_cnpj_contr.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.txt_name_contr.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Company Name", None))
        self.txt_NUMBER.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Number", None))
        self.txt_Province.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"State", None))
        self.txt_email_contr.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Email", None))
        self.txt_ZipCode.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"ZipCode", None))
        self.txt_city.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"city", None))
        self.txt_neighborhood.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Neighborhood", None))
        self.label_18.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Blenda Tocantins Company</span></p></body></html>", None))
        self.btn_register.setText(QCoreApplication.translate(
            "MainWindow", u"Register", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab), QCoreApplication.translate("MainWindow", u"REGISTER", None))
        self.label_11.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\">COMPANIES</p></body></html>", None))
        ___qtablewidgetitem = self.tb_company.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("MainWindow", u"CNPJ", None))
        ___qtablewidgetitem1 = self.tb_company.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("MainWindow", u"NAME", None))
        ___qtablewidgetitem2 = self.tb_company.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("MainWindow", u"ADDRESS", None))
        ___qtablewidgetitem3 = self.tb_company.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate(
            "MainWindow", u"Number", None))
        ___qtablewidgetitem4 = self.tb_company.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate(
            "MainWindow", u"COMPLEMENT", None))
        ___qtablewidgetitem5 = self.tb_company.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(
            QCoreApplication.translate("MainWindow", u"NEIGHBORHOOD", None))
        ___qtablewidgetitem6 = self.tb_company.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate(
            "MainWindow", u"city", None))
        ___qtablewidgetitem7 = self.tb_company.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(
            QCoreApplication.translate("MainWindow", u"STATE", None))
        ___qtablewidgetitem8 = self.tb_company.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(
            QCoreApplication.translate("MainWindow", u"ZIP CODE", None))
        ___qtablewidgetitem9 = self.tb_company.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(
            QCoreApplication.translate("MainWindow", u"PHONE", None))
        ___qtablewidgetitem10 = self.tb_company.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(
            QCoreApplication.translate("MainWindow", u"EMAIL", None))

        __sortingEnabled = self.tb_company.isSortingEnabled()
        self.tb_company.setSortingEnabled(False)
        self.tb_company.setSortingEnabled(__sortingEnabled)

        self.btn_excel.setText(QCoreApplication.translate(
            "MainWindow", u"Excel", None))
        self.btn_update.setText(QCoreApplication.translate(
            "MainWindow", u"Update", None))
        self.btn_delete.setText(QCoreApplication.translate(
            "MainWindow", u"Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_2), QCoreApplication.translate("MainWindow", u"COMPANIES", None))
        self.label_5.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">CONTACTS</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/whatsApp.png\"/><span style=\" font-size:18pt; vertical-align:super;\">778-791-0090</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/email.png\"/><span style=\" font-size:18pt; vertical-align:super;\">contato@blendatocantinscompany.net</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">ABOUT</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">This system queries the CNPJ using the Brazilian Federal Revenue API and registers it in a SQLITE3 database.The objective of this system is to obtain and register information from other companies that are registered with the Federal Revenue of Brazil, generating a personal and personalized database.</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"\u00a9 Blenda Tocantins Company 2023", None))
    # retranslateUi
