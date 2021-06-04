#создай приложение для запоминания информации
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,QHBoxLayout,
QVBoxLayout,QLabel,QMessageBox,QRadioButton,QGroupBox,QButtonGroup)
from random import randint,shuffle

class Questions():
    def __init__(self,question, right_answer,wrong1,wrong2,wrong3):
        self.question=question
        self.right_answer=right_answer
        self.wrong1=wrong1
        self.wrong2=wrong2
        self.wrong3=wrong3       

questions_list=[]
questions_list.append(Questions("Какого цвета нету на флаге Франции","розовый","красный","синий","белый"))
questions_list.append(Questions("Какого цвета нету на флаге Казахстана","красный","золотой","синий","желтый"))
questions_list.append(Questions("Какого цвета нету на флаге России","желтый","красный","синий","белый"))
questions_list.append(Questions("Сколько будет 2*(2+2)/4","2","6","4","8"))
questions_list.append(Questions("Как переводиться слово light","Свет","не переводиться","тьма","лайм"))
questions_list.append(Questions("Какое из ниже перечисленный произведений написал А.С.Пушкин","Золотая рыбка","Зимнее утро","Дядюшка Том","Гарри Поттер"))
questions_list.append(Questions("Какого цвета крокодил","зеленый","красный","синий","белый"))
questions_list.append(Questions("Какой формы планета Земля","шара","она плоская","квадрат","круг"))
questions_list.append(Questions("Сколько будет 12/12","1","0","12","6"))
questions_list.append(Questions("Что лишнее","машина","птица","самолет","пчела"))
questions_list.append(Questions("Выбери НЕ хищное животное","слон","богомол","морской котик","лев"))
questions_list.append(Questions("да или да","да","нет","конечно нет","no"))
questions_list.append(Questions("сколько видно пальцев, если один из них загнуть и повернуть лицевой стороной к вам","5","4","3","6"))
questions_list.append(Questions("Сколько будет 6*0","0","6","12","60"))
questions_list.append(Questions("Что будет если горящую свечу накрыть стаканом","она погаснет","ничего","загориться сильнее","будет большой бум"))
questions_list.append(Questions("Назови ездовую породу собак","хаски","такса","чихуахуа","авчарка"))
questions_list.append(Questions("Сколько материков на Земле","6","5","7","8"))
questions_list.append(Questions("Самая глубокая впадина в океане","Марианская","Маринская","Восточная","Западная"))
questions_list.append(Questions("Температура плавления стела","425-600","200-300","70-100","230-300"))
questions_list.append(Questions("При какой температуре замерзает вода","0","-1","-5","-10"))

app=QApplication([])

window=QWidget()
window.setWindowTitle('memo card')

btn_OK=QPushButton("Ответить")
Ib_Question=QLabel("В каком году была основана Москва?")

RadioGroupBox = QGroupBox("Варианты ответов")

rbtn_1=QRadioButton("1147")
rbtn_2=QRadioButton("1242")
rbtn_3=QRadioButton("1861")
rbtn_4=QRadioButton("1943")

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1=QHBoxLayout()
layout_ans2=QVBoxLayout()
layout_ans3=QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox=QGroupBox("Результат теста")
Ib_Result=QLabel("правильно/неправильно")
Ib_Correct=QLabel("Ответ будет тут!")
layout_res=QVBoxLayout()
layout_res.addWidget(Ib_Result,alignment=(Qt.AlignLeft | Qt.AlignVCenter))
layout_res.addWidget(Ib_Correct,alignment=Qt.AlignHCenter,stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1=QHBoxLayout()
layout_line2=QHBoxLayout()
layout_line3=QHBoxLayout()

layout_line1.addWidget(Ib_Question,alignment=(Qt.AlignHCenter | Qt.AlignVCenter ))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK,stretch=2)
layout_line3.addStretch(1)

layout_card=QVBoxLayout()

layout_card.addLayout(layout_line1,stretch=2)
layout_card.addLayout(layout_line2,stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3,stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.hide()
    btn_OK.setText("Следующий вопрос")

def show_questions():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
answer=[rbtn_1,rbtn_2,rbtn_3,rbtn_4]
def ask(q: Questions):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    Ib_Question.setText(q.question)
    Ib_Correct.setText(q.right_answer)
    show_questions()

def show__correct(res):
    Ib_Result.setText(res)
    show_result()

def check_answer():
    if answer[0].isChecked():
        show__correct("Правильно!")
        window.score+=1
        print("Статистика/n-Всего вопросов: ", window.total, "/n-Правильных ответов: ", window.score)
        print("Рейтинг: ",(window.score/window.total*100),"%")
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show__correct("Неверно!")
            print("Рейтинг: ",(window.score/window.total*100),"%")

def next_question():
    window.total+=1
    print("Статистика/n-Всего вопросов: ", window.total, "/n-Правильных ответов: ", window.score)
    cur_question=randint(0,len(questions_list)-1)
    q=questions_list[cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window.setLayout(layout_card)
window.score=0
window.total=0
btn_OK.clicked.connect(click_OK)
next_question()
window.resize(400,300)
window.show()
app.exec_()