header_styles = '''
    QWidget {
        background-color: #319B05;
        max-height: 75px;
    }
    
     QLabel {
        font-family: "Avenir Next LT Pro";
        font-size: 22px;
        font-weight: bold;
    }
    
    QPushButton {
        max-width: 150px;
        height: 50px;
        font-family: "Avenir Next LT Pro";
        font-size: 18px;
        border: 0;
        background-color: #204D00;
        border-radius: 7.5px;
    }
    
    QPushButton:hover {
        background-color: #122600;
        border-radius: 7.5px;
    }
'''

dialog_styles = '''
    QDialog {
        background-color: #360559;
        font-family:"Avenir Next LT Pro"
    }
    
    QLabel{
        color: #FBC5FF;
        font-size: 18px;
        font-weight: bold;
        margin-right: 6px;
    }
                   
    QLineEdit, QTextEdit, QDateEdit{
        background-color: #F198FD;
        color: #150226;
        selection-background-color: #252226;
        selection-color: #F198FD;
        font-size: 16px;
        font-weight: bold;
    }
                   
    QLineEdit, QTextEdit {
        padding: 2px 4px;
        margin-bottom: 8px;
        border 0;
        border-radius: 5px;
    }
    
    QDateEdit {
        max-width: 180px;
    }
                   
    QDateEdit:focus, QLineEdit:focus, QTextEdit:focus {
        border: 0.6px solid #252226;
        border-radius: 5px;
    }

    QDialogButtonBox {
        margin-top: 16px;
    }
                   
    QDialogButtonBox > * {
        background-color: #F198FD;
        color: #150226;
        font-size: 18px;
        font-weight: Bold;
        padding: 4px 8px;
        border-radius: 7.5px
    }        
    
    QDialogButtonBox > *:hover, QDialogButtonBox > *:focus{
        background-color: #E06AF9;
        border: 1px solid #252226;                       
    }
'''