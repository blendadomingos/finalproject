from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidgetItem)
from ui_main import Ui_MainWindow
import sys
from ui_functions import *
from database import Data_base
import pandas as pd
import sqlite3


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Company Registration System")
        appIcon = QIcon(u"icons/logo4.png")
        self.setWindowIcon(appIcon)

        ################################################
        # TOGGLE BUTTON
        self.btn_toggle.clicked.connect(self.leftMenu)
        ################################################

        ##############################################################################################
        # Páginas do Sistema
        self.btn_home.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_menu_register.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_register))
        self.btn_menu_about.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_about))
        self.btn_menu_contacts.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_contacts))
        ###############################################################################################

        ###############################################################################################
        # PREENCHER AUTOMATICAMENTE OS DADOS DO CNPJ
        self.txt_cnpj_contr.editingFinished.connect(self.consult_api)
        ###############################################################################################

        self.btn_register.clicked.connect(self.register_company)
        self.btn_update.clicked.connect(self.update_company)
        self.btn_delete.clicked.connect(self.delete_company)
        self.btn_excel.clicked.connect(self.excel_2)

        self.search_company()

    def leftMenu(self):

        width = self.left_menu.width()

        if width == 9:
            newWidth = 200
        else:
            newWidth = 9

        self.animation = QtCore.QPropertyAnimation(
            self.left_menu, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def consult_api(self):
        campos = consulta_cnpj(self.txt_cnpj_contr.text())

        self.txt_name_contr.setText(campos[0])
        self.txt_address.setText(campos[1])
        self.txt_NUMBER.setText(campos[2])
        self.txt_complement.setText(campos[3])
        self.txt_neighborhood.setText(campos[4])
        self.txt_city.setText(campos[5])
        self.txt_Province.setText(campos[6])
        self.txt_ZipCode.setText(campos[7].replace('.', '').replace('-', ''))
        self.txt_phone_contr.setText(campos[8].replace(
            '(', '').replace('-', '').replace(')', ''))
        self.txt_email_contr.setText(campos[9])

    def register_company(self):
        db = Data_base()
        db.connect()

        fullDataSet = (

            self.txt_cnpj_contr.text(), self.txt_name_contr.text(),
            self.txt_address.text(), self.txt_NUMBER.text(),
            self.txt_complement.text(), self.txt_neighborhood.text(),
            self.txt_city.text(), self.txt_Province.text(),
            self.txt_ZipCode.text(), self.txt_phone_contr.text().strip(),
            self.txt_email_contr.text()
        )

      # UPDATE DATA IN THE BANK
        resp = db.register_company(fullDataSet)

        if resp == "OK":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Registration Completed")
            msg.setText("Registration completed successfully")
            msg.exec()
            db.close_connection()
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(
                "Error registering, check if the information was filled in correctly!")
            msg.exec()
            db.close_connection()
            return

    def search_company(self):

        db = Data_base()
        db.connect()
        result = db.select_all_companies()

        self.tb_company.clearContents()
        self.tb_company.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tb_company.setItem(
                    row, column, QTableWidgetItem(str(data)))

        db.close_connection()

    def update_company(self):

        dados = []
        update_dados = []

        for row in range(self.tb_company.rowCount()):
            for column in range(self.tb_company.columnCount()):
                dados.append(self.tb_company.item(row, column).text())
            update_dados.append(dados)
            dados = []

         # REGISTER IN THE DATABASE
        db = Data_base()
        db.connect()

        for emp in update_dados:
            db.update_company(tuple(emp))

        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Data update")
        msg.setText("Data updated successfully!")
        msg.exec()

        self.tb_company.reset()
        self.search_company()

    def delete_company(self):

        db = Data_base()
        db.connect()

        msg = QMessageBox()
        msg.setWindowTitle("Delete")
        msg.setText("This record will be deleted.")
        msg.setInformativeText("Are you sure you want to delete?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            cnpj = self.tb_company.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = db.delete_companies(cnpj)
            self.search_company()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("COMPANY")
            msg.setText(result)
            msg.exec()

        db.close_connection()

    def excel(self):

        dados = []
        all_dados = []

        for row in range(self.tb_company.rowCount()):
            for column in range(self.tb_company.columnCount()):
                dados.append(self.tb_company.item(row, column).text())

            all_dados.append(dados)
            dados = []

        columns = ['CNPJ', 'NAME', 'ADDRESS', 'NUMBER', 'COMPLEMENT',
                   'NEIGHBORHOOD', 'CITY', 'PROVINCE', 'ZIP_CODE', 'PHONE', 'EMAIL']

        empresas = pd.DataFrame(all_dados, columns=columns)
        empresas.to_excel("COMPANIES.xlsx",
                          sheet_name='companies', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excel")
        msg.setText("Excel report generated successfully!")
        msg.exec()

    def excel_2(self):

        cnx = sqlite3.connect("system.db")

        empresas = pd.read_sql_query("""SELECT * FROM companies""", cnx)

        empresas.to_excel("COMPANIES.xlsx",
                          sheet_name='companies', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excel")
        msg.setText("Excel report generated successfully!")
        msg.exec()


if __name__ == "__main__":

    db = Data_base()
    db.connect()
    db.create_table_company()
    db.close_connection()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
