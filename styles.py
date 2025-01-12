dark_style = """
QScrollBar {
background: #000000;
}

#theme_change_label {
font-size: 20px;
qproperty-alignment: AlignCenter;
}

QLabel {
color: #FFFFFF;
}

/* Стиль для кнопок с файлами и папками */
#object_button {
border: none;
background: #000000;
}

#object_button:hover {
    background-color: #1f1f1f;
}

/* Стиль для кнопки возврата в предыдущую директорию */
#back_btn {
border: none;
background: #000000;

}

#back_btn:hover {
    background-color: #1f1f1f;
    font-weight: bold;
    font-size: 20px;
}

#currentPath {
font-size: 20px;
background: #2c2c2c;
}


/* Стиль для кнопок на левой панели */
#left_side_btn {
border: none;
background: #000000;
}

#left_side_btn:hover {
    background-color: #1f1f1f;
    font-weight: bold;
    font-size: 20px;
}

QListWidget {
border: none;
background: #000000;
}

QMainWindow {
background: #000000;
}
"""

light_style = """
QScrollBar {
background: #f2f1ee;
}

#theme_change_label {
font-size: 20px;
qproperty-alignment: AlignCenter;
}


QLabel {
color: #000000;
}

/* Стиль для кнопок с файлами и папками */
#object_button {
border: none;
color: #000000;
background: #f2f1ee;
}

#object_button:hover {
    background-color: #d6d4cc;
}

/* Стиль для кнопки возврата в предыдущую директорию */
#back_btn {
border: none;
color: #000000;
background: #f2f1ee;

}

#back_btn:hover {
    background-color: #d6d4cc;
    font-weight: bold;
    font-size: 20px;
}

#currentPath {
font-size: 20px;
background: #b3b3b3;
color: #000000;
}


/* Стиль для кнопок на левой панели */
#left_side_btn {
border: none;
color: #000000;
background: #f2f1ee;
}

#left_side_btn:hover {
    background-color: #d6d4cc;
    font-weight: bold;
    font-size: 20px;
}

QListWidget {
border: none;
background: #f2f1ee;
}

QMainWindow {
background: #f2f1ee;
}
"""

styles_dict: dict = {"dark":dark_style,
                     "light":light_style}
