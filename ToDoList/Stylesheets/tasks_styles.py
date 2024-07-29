def header_styles(isChecked):

    if isChecked:
       val = 0
    else:
        val = 10

    header_styles_template = f'''
        QWidget {{
            background-color: #360559;
            padding: 0 5px;
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
            border-bottom-left-radius: {val}px;
            border-bottom-right-radius: {val}px;
            font-weight: bold;
        }}
        
        QLabel {{
            font-size: 18px;
        }}
        
        QPushButton{{
            background-color: #E06AF9;
            color: #000;
            font-size: 16px;
            padding: 3px 5px;
            border-radius: 5px;
        }}
        
        QPushButton:hover {{
            background-color: #F198FD;
        }}
    '''

    return header_styles_template


body_styles = '''
    QWidget {
        background-color: #E06AF9;
        color: #000;
        border-bottom-left-radius: 10px;
        border-bottom-right-radius: 10px;
        padding: 0 7.5px;
    }
    
    QLabel {
        font-family: "Arial";
        font-size: 14px;
        font-weight: none;
    }
    
    QPushButton{
        background-color: #360559;
        color: #FFF;
        font-size: 14px;
        font-weight: bold;
        padding: 3px 5px;
        border-radius: 5px;
    }
        
    QPushButton:hover {
        background-color: #5E0A8B;
    }
        
'''
