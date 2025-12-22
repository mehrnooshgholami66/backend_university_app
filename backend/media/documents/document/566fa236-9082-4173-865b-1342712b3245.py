from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(571, 260)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 551, 241))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.itemtypelable_upload = QtWidgets.QLabel(self.groupBox)
        self.itemtypelable_upload.setGeometry(QtCore.QRect(20, 40, 55, 16))
        self.itemtypelable_upload.setObjectName("itemtypelable_upload")
        self.DacumentArticle_upload = QtWidgets.QComboBox(self.groupBox)
        self.DacumentArticle_upload.setGeometry(QtCore.QRect(80, 33, 461, 31))
        self.DacumentArticle_upload.setObjectName("DacumentArticle_upload")
        self.DacumentArticle_upload.addItem("")
        self.DacumentArticle_upload.addItem("")
        self.selectpushButton_upload = QtWidgets.QPushButton(self.groupBox)
        self.selectpushButton_upload.setGeometry(QtCore.QRect(10, 80, 121, 41))
        self.selectpushButton_upload.setObjectName("selectpushButton_upload")
        self.browselabel_uplod = QtWidgets.QLabel(self.groupBox)
        self.browselabel_uplod.setGeometry(QtCore.QRect(150, 92, 55, 16))
        self.browselabel_uplod.setObjectName("browselabel_uplod")
        self.uploadnamelabel_upload = QtWidgets.QLabel(self.groupBox)
        self.uploadnamelabel_upload.setGeometry(QtCore.QRect(23, 148, 91, 16))
        self.uploadnamelabel_upload.setObjectName("uploadnamelabel_upload")
        self.uploadnamelineEdit_upload = QtWidgets.QLineEdit(self.groupBox)
        self.uploadnamelineEdit_upload.setGeometry(QtCore.QRect(120, 140, 421, 31))
        self.uploadnamelineEdit_upload.setObjectName("uploadnamelineEdit_upload")
        self.uploadpushButton_upload = QtWidgets.QPushButton(self.groupBox)
        self.uploadpushButton_upload.setGeometry(QtCore.QRect(10, 190, 531, 41))
        self.uploadpushButton_upload.setObjectName("uploadpushButton_upload")
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "professor panel"))
        self.groupBox.setTitle(_translate("Form", "upload item"))
        self.itemtypelable_upload.setText(_translate("Form", "item type"))
        self.DacumentArticle_upload.setItemText(0, _translate("Form", "Document"))
        self.DacumentArticle_upload.setItemText(1, _translate("Form", "Article"))
        self.selectpushButton_upload.setText(_translate("Form", "select"))
        self.browselabel_uplod.setText(_translate("Form", "browse"))
        self.uploadnamelabel_upload.setText(_translate("Form", "upload name"))
        self.uploadpushButton_upload.setText(_translate("Form", "upload"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
