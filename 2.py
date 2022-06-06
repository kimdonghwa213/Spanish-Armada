from tkinter import *
from tkinter import ttk
import new

### 시간표를 만드는 프로그램###
def table_make():
        d = new.Day()

        mon = d[0]
        tue = d[1]
        wed = d[2]
        thu = d[3]
        fri = d[4]

        # 월요일

        label_11['text'] = mon[0][0]
        label_12['text'] = mon[0][1]
        label_13['text'] = mon[0][2]
        label_14['text'] = mon[0][3]
        label_15['text'] = mon[0][4]
        label_16['text'] = mon[0][5]
        label_17['text'] = mon[0][6]
        label_18['text'] = mon[0][7]
        label_19['text'] = mon[0][8]
        label_110['text'] = mon[0][9]
        label_111['text'] = mon[0][10]
        label_112['text'] = mon[0][11]

        # 화요일
        label_21['text'] = tue[0][0]
        label_22['text'] = tue[0][1]
        label_23['text'] = tue[0][2]
        label_24['text'] = tue[0][3]
        label_25['text'] = tue[0][4]
        label_26['text'] = tue[0][5]
        label_27['text'] = tue[0][6]
        label_28['text'] = tue[0][7]
        label_29['text'] = tue[0][8]
        label_210['text'] = tue[0][9]
        label_211['text'] = tue[0][10]
        label_212['text'] = tue[0][11]

        # 수요일
        label_31['text'] = wed[0][0]
        label_32['text'] = wed[0][1]
        label_33['text'] = wed[0][2]
        label_34['text'] = wed[0][3]
        label_35['text'] = wed[0][4]
        label_36['text'] = wed[0][5]
        label_37['text'] = wed[0][6]
        label_38['text'] = wed[0][7]
        label_39['text'] = wed[0][8]
        label_310['text'] = wed[0][9]
        label_311['text'] = wed[0][10]
        label_312['text'] = wed[0][11]

        # 목요일
        label_41['text'] = thu[0][0]
        label_42['text'] = thu[0][1]
        label_43['text'] = thu[0][2]
        label_44['text'] = thu[0][3]
        label_45['text'] = thu[0][4]
        label_46['text'] = thu[0][5]
        label_47['text'] = thu[0][6]
        label_48['text'] = thu[0][7]
        label_49['text'] = thu[0][8]
        label_410['text'] = thu[0][9]
        label_411['text'] = thu[0][10]
        label_412['text'] = thu[0][11]

        # 금요일
        label_51['text'] = fri[0][0]
        label_52['text'] = fri[0][1]
        label_53['text'] = fri[0][2]
        label_54['text'] = fri[0][3]
        label_55['text'] = fri[0][4]
        label_56['text'] = fri[0][5]
        label_57['text'] = fri[0][6]
        label_58['text'] = fri[0][7]
        label_59['text'] = fri[0][8]
        label_510['text'] = fri[0][9]
        label_511['text'] = fri[0][10]
        label_512['text'] = fri[0][11]

if __name__ == '__main__':
    win = Tk()
    win.title("전북대학교 시간표")

    # choice_time = IntVar() # 시간표 선택 값을 입력받는 문자열 변수

    choice_time1 = IntVar() # 해당 시간이 선택되면 1, 선택 안되면 0을 입력 받는 정수 변수
    choice_time2 = IntVar()
    choice_time3 = IntVar()
    choice_time4 = IntVar()
    choice_time5 = IntVar()
    choice_time6 = IntVar()
    choice_time7 = IntVar()
    choice_time8 = IntVar()
    choice_time9 = IntVar()
    choice_time10 = IntVar()
    choice_time11 = IntVar()
    choice_time12 = IntVar()
    choice_time13 = IntVar()
    choice_time14 = IntVar()
    choice_time15 = IntVar()
    choice_time16 = IntVar()
    choice_time17 = IntVar()
    choice_time18 = IntVar()
    choice_time19 = IntVar()
    choice_time20 = IntVar()
    choice_time21 = IntVar()
    choice_time22 = IntVar()
    choice_time23 = IntVar()
    choice_time24 = IntVar()
    choice_time25 = IntVar()
    choice_time26 = IntVar()
    choice_time27 = IntVar()
    choice_time28 = IntVar()
    choice_time29 = IntVar()
    choice_time30 = IntVar()
    choice_time31 = IntVar()
    choice_time32 = IntVar()
    choice_time33 = IntVar()
    choice_time34 = IntVar()
    choice_time35 = IntVar()
    choice_time36 = IntVar()
    choice_time37 = IntVar()
    choice_time38 = IntVar()
    choice_time39 = IntVar()
    choice_time40 = IntVar()
    choice_time41 = IntVar()
    choice_time42 = IntVar()
    choice_time43 = IntVar()
    choice_time44 = IntVar()
    choice_time45 = IntVar()
    choice_time46 = IntVar()
    choice_time47 = IntVar()
    choice_time48 = IntVar()
    choice_time49 = IntVar()
    choice_time50 = IntVar()
    choice_time51 = IntVar()
    choice_time52 = IntVar()
    choice_time53 = IntVar()
    choice_time54 = IntVar()
    choice_time55 = IntVar()
    choice_time56 = IntVar()
    choice_time57 = IntVar()
    choice_time58 = IntVar()
    choice_time59 = IntVar()
    choice_time60 = IntVar()



    choice_level = IntVar()  # 학년 선택 값을 입력받는 정수 변수

    choice_num = IntVar()  # 들을 전공 수의 선택 값을 입력 받는 정수 변수

    choice_major = StringVar()  # 전공 선택 값을 입력받는 문자열 변수

    choice_lib = IntVar()  # 들을 교양 수의 선택 값을 입력 받는 정수 변수

    choice_lib1 = IntVar()  # 교양 난이도 1이 선택되면 1, 선택 안되면 0을 입력 받는 정수 변수
    choice_lib2 = IntVar()  # 교양 난이도 2이 선택되면 1, 선택 안되면 0을 입력 받는 정수 변수
    choice_lib3 = IntVar()  # 교양 난이도 3이 선택되면 1, 선택 안되면 0을 입력 받는 정수 변수
    choice_lib4 = IntVar()  # 교양 난이도 4이 선택되면 1, 선택 안되면 0을 입력 받는 정수 변수

    choice_1 = StringVar()  # 교양 선택 값을 입력받는 문자열 변수

    #########label로 표 셀 만들기###########

    row_title_label1 = Label(win, text='월', font=('맑은 고딕', 10), bg='#FFB2F5',
                             relief='ridge', width=13)
    row_title_label2 = Label(win, text='화', font=('맑은 고딕', 10), bg='#FFB2F5',
                             relief='ridge', width=13)
    row_title_label3 = Label(win, text='수', font=('맑은 고딕', 10), bg='#FFB2F5',
                             relief='ridge', width=13)
    row_title_label4 = Label(win, text='목', font=('맑은 고딕', 10), bg='#FFB2F5',
                             relief='ridge', width=13)
    row_title_label5 = Label(win, text='금', font=('맑은 고딕', 10), bg='#FFB2F5',
                             relief='ridge', width=13)

    col_title_label1 = Label(win, text='9시', font=('맑은 고딕', 10), bg='#FFB2F5',
                             relief='ridge', width=6, height=3)
    col_title_label2 = Label(win, text='10시', font=('맑은 고딕', 10), bg='#FFB2F5',
                             relief='ridge', width=6, height=3)
    col_title_label3 = Label(win, text='11시', font=('맑은 고딕', 10), bg='#FFB2F5',
                             relief='ridge', width=6, height=3)
    col_title_label4 = Label(win, text='12시', font=('맑은 고딕', 10), bg='#FFB2F5',
                             relief='ridge', width=6, height=3)
    col_title_label5 = Label(win, text='13시', font=('맑은 고딕', 10), bg='#FFB2F5',
                             relief='ridge', width=6, height=3)
    col_title_label6 = Label(win, text='14시', font=('맑은 고딕', 10), bg='#FFB2F5',
                             relief='ridge', width=6, height=3)
    col_title_label7 = Label(win, text='15시', font=('맑은 고딕', 10), bg='#FFB2F5',
                             relief='ridge', width=6, height=3)
    col_title_label8 = Label(win, text='16시', font=('맑은 고딕', 10), bg='#FFB2F5',
                             relief='ridge', width=6, height=3)
    col_title_label9 = Label(win, text='17시', font=('맑은 고딕', 10), bg='#FFB2F5',
                             relief='ridge', width=6, height=3)
    col_title_label10 = Label(win, text='18시', font=('맑은 고딕', 10), bg='#FFB2F5',
                              relief='ridge', width=6, height=3)
    col_title_label11 = Label(win, text='19시', font=('맑은 고딕', 10), bg='#FFB2F5',
                              relief='ridge', width=6, height=3)
    col_title_label12 = Label(win, text='20시', font=('맑은 고딕', 10), bg='#FFB2F5',
                              relief='ridge', width=6, height=3)
    # 월요일
    label_11 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_12 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_13 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_14 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_15 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_16 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_17 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_18 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_19 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_110 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_111 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_112 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)

    # 화요일
    label_21 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_22 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_23 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_24 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_25 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_26 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_27 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_28 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_29 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_210 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_211 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_212 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)

    # 수요일
    label_31 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_32 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_33 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_34 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_35 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_36 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_37 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_38 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_39 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_310 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_311 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_312 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)

    # 목요일
    label_41 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_42 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_43 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_44 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_45 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_46 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_47 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_48 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_49 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_410 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_411 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_412 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)

    # 금요일
    label_51 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_52 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_53 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_54 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_55 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_56 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_57 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_58 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_59 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_510 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_511 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)
    label_512 = Label(win, text='', font=('맑은 고딕', 10), relief='ridge', width=13, height=3, wraplength=120)

    ##########화살표 버튼###########
    right_arrow = Button(win, text='Reload', width=10, command=table_make)
    # capture = Button(win, text='캡쳐', command=capture)

    #########전공##########
    major_label = Label(win, text='학과', font=('맑은 고딕', 11), padx=2, pady=2)

    combo_major = ttk.Combobox(win, textvariable=choice_major)

    ########### 시간 선택 ##############
    time_box1 = Checkbutton(win, text='', variable=choice_time1, onvalue=1, offvalue=0)
    time_box2 = Checkbutton(win, text='', variable=choice_time2, onvalue=1, offvalue=0)
    time_box3 = Checkbutton(win, text='', variable=choice_time3, onvalue=1, offvalue=0)
    time_box4 = Checkbutton(win, text='', variable=choice_time4, onvalue=1, offvalue=0)
    time_box5 = Checkbutton(win, text='', variable=choice_time5, onvalue=1, offvalue=0)
    time_box6 = Checkbutton(win, text='', variable=choice_time6, onvalue=1, offvalue=0)
    time_box7 = Checkbutton(win, text='', variable=choice_time7, onvalue=1, offvalue=0)
    time_box8 = Checkbutton(win, text='', variable=choice_time8, onvalue=1, offvalue=0)
    time_box9 = Checkbutton(win, text='', variable=choice_time9, onvalue=1, offvalue=0)
    time_box10 = Checkbutton(win, text='', variable=choice_time10, onvalue=1, offvalue=0)
    time_box11 = Checkbutton(win, text='', variable=choice_time11, onvalue=1, offvalue=0)
    time_box12 = Checkbutton(win, text='', variable=choice_time12, onvalue=1, offvalue=0)
    time_box13 = Checkbutton(win, text='', variable=choice_time13, onvalue=1, offvalue=0)
    time_box14 = Checkbutton(win, text='', variable=choice_time14, onvalue=1, offvalue=0)
    time_box15 = Checkbutton(win, text='', variable=choice_time15, onvalue=1, offvalue=0)
    time_box16 = Checkbutton(win, text='', variable=choice_time16, onvalue=1, offvalue=0)
    time_box17 = Checkbutton(win, text='', variable=choice_time17, onvalue=1, offvalue=0)
    time_box18 = Checkbutton(win, text='', variable=choice_time18, onvalue=1, offvalue=0)
    time_box19 = Checkbutton(win, text='', variable=choice_time19, onvalue=1, offvalue=0)
    time_box20 = Checkbutton(win, text='', variable=choice_time20, onvalue=1, offvalue=0)
    time_box21 = Checkbutton(win, text='', variable=choice_time21, onvalue=1, offvalue=0)
    time_box22 = Checkbutton(win, text='', variable=choice_time22, onvalue=1, offvalue=0)
    time_box23 = Checkbutton(win, text='', variable=choice_time23, onvalue=1, offvalue=0)
    time_box24 = Checkbutton(win, text='', variable=choice_time24, onvalue=1, offvalue=0)
    time_box25 = Checkbutton(win, text='', variable=choice_time25, onvalue=1, offvalue=0)
    time_box26 = Checkbutton(win, text='', variable=choice_time26, onvalue=1, offvalue=0)
    time_box27 = Checkbutton(win, text='', variable=choice_time27, onvalue=1, offvalue=0)
    time_box28 = Checkbutton(win, text='', variable=choice_time28, onvalue=1, offvalue=0)
    time_box29 = Checkbutton(win, text='', variable=choice_time29, onvalue=1, offvalue=0)
    time_box30 = Checkbutton(win, text='', variable=choice_time30, onvalue=1, offvalue=0)
    time_box31 = Checkbutton(win, text='', variable=choice_time31, onvalue=1, offvalue=0)
    time_box32 = Checkbutton(win, text='', variable=choice_time32, onvalue=1, offvalue=0)
    time_box33 = Checkbutton(win, text='', variable=choice_time33, onvalue=1, offvalue=0)
    time_box34 = Checkbutton(win, text='', variable=choice_time34, onvalue=1, offvalue=0)
    time_box35 = Checkbutton(win, text='', variable=choice_time35, onvalue=1, offvalue=0)
    time_box36 = Checkbutton(win, text='', variable=choice_time36, onvalue=1, offvalue=0)
    time_box37 = Checkbutton(win, text='', variable=choice_time37, onvalue=1, offvalue=0)
    time_box38 = Checkbutton(win, text='', variable=choice_time38, onvalue=1, offvalue=0)
    time_box39 = Checkbutton(win, text='', variable=choice_time39, onvalue=1, offvalue=0)
    time_box40 = Checkbutton(win, text='', variable=choice_time40, onvalue=1, offvalue=0)
    time_box41 = Checkbutton(win, text='', variable=choice_time41, onvalue=1, offvalue=0)
    time_box42 = Checkbutton(win, text='', variable=choice_time42, onvalue=1, offvalue=0)
    time_box43 = Checkbutton(win, text='', variable=choice_time43, onvalue=1, offvalue=0)
    time_box44 = Checkbutton(win, text='', variable=choice_time44, onvalue=1, offvalue=0)
    time_box45 = Checkbutton(win, text='', variable=choice_time45, onvalue=1, offvalue=0)
    time_box46 = Checkbutton(win, text='', variable=choice_time46, onvalue=1, offvalue=0)
    time_box47 = Checkbutton(win, text='', variable=choice_time47, onvalue=1, offvalue=0)
    time_box48 = Checkbutton(win, text='', variable=choice_time48, onvalue=1, offvalue=0)
    time_box49 = Checkbutton(win, text='', variable=choice_time49, onvalue=1, offvalue=0)
    time_box50 = Checkbutton(win, text='', variable=choice_time50, onvalue=1, offvalue=0)
    time_box51 = Checkbutton(win, text='', variable=choice_time51, onvalue=1, offvalue=0)
    time_box52 = Checkbutton(win, text='', variable=choice_time52, onvalue=1, offvalue=0)
    time_box53 = Checkbutton(win, text='', variable=choice_time53, onvalue=1, offvalue=0)
    time_box54 = Checkbutton(win, text='', variable=choice_time54, onvalue=1, offvalue=0)
    time_box55 = Checkbutton(win, text='', variable=choice_time55, onvalue=1, offvalue=0)
    time_box56 = Checkbutton(win, text='', variable=choice_time56, onvalue=1, offvalue=0)
    time_box57 = Checkbutton(win, text='', variable=choice_time57, onvalue=1, offvalue=0)
    time_box58 = Checkbutton(win, text='', variable=choice_time58, onvalue=1, offvalue=0)
    time_box59 = Checkbutton(win, text='', variable=choice_time59, onvalue=1, offvalue=0)
    time_box60 = Checkbutton(win, text='', variable=choice_time60, onvalue=1, offvalue=0)

    build_but = Button(win, text='만들기', command=table_make)

    ######## 시간표 셀 배치###########
    row_title_label1.grid(column=1, row=0)
    row_title_label2.grid(column=2, row=0)
    row_title_label3.grid(column=3, row=0)
    row_title_label4.grid(column=4, row=0)
    row_title_label5.grid(column=5, row=0)

    col_title_label1.grid(column=0, row=1)
    col_title_label2.grid(column=0, row=2)
    col_title_label3.grid(column=0, row=3)
    col_title_label4.grid(column=0, row=4)
    col_title_label5.grid(column=0, row=5)
    col_title_label6.grid(column=0, row=6)
    col_title_label7.grid(column=0, row=7)
    col_title_label8.grid(column=0, row=8)
    col_title_label9.grid(column=0, row=9)
    col_title_label10.grid(column=0, row=10)
    col_title_label11.grid(column=0, row=11)
    col_title_label12.grid(column=0, row=12)


    # 월요일
    label_11.grid(column=1, row=1)
    label_12.grid(column=1, row=2)
    label_13.grid(column=1, row=3)
    label_14.grid(column=1, row=4)
    label_15.grid(column=1, row=5)
    label_16.grid(column=1, row=6)
    label_17.grid(column=1, row=7)
    label_18.grid(column=1, row=8)
    label_19.grid(column=1, row=9)
    label_110.grid(column=1, row=10)
    label_111.grid(column=1, row=11)
    label_112.grid(column=1, row=12)

    # 화요일
    label_21.grid(column=2, row=1)
    label_22.grid(column=2, row=2)
    label_23.grid(column=2, row=3)
    label_24.grid(column=2, row=4)
    label_25.grid(column=2, row=5)
    label_26.grid(column=2, row=6)
    label_27.grid(column=2, row=7)
    label_28.grid(column=2, row=8)
    label_29.grid(column=2, row=9)
    label_210.grid(column=2, row=10)
    label_211.grid(column=2, row=11)
    label_212.grid(column=2, row=12)

    # 수요일
    label_31.grid(column=3, row=1)
    label_32.grid(column=3, row=2)
    label_33.grid(column=3, row=3)
    label_34.grid(column=3, row=4)
    label_35.grid(column=3, row=5)
    label_36.grid(column=3, row=6)
    label_37.grid(column=3, row=7)
    label_38.grid(column=3, row=8)
    label_39.grid(column=3, row=9)
    label_310.grid(column=3, row=10)
    label_311.grid(column=3, row=11)
    label_312.grid(column=3, row=12)

    # 목요일
    label_41.grid(column=4, row=1)
    label_42.grid(column=4, row=2)
    label_43.grid(column=4, row=3)
    label_44.grid(column=4, row=4)
    label_45.grid(column=4, row=5)
    label_46.grid(column=4, row=6)
    label_47.grid(column=4, row=7)
    label_48.grid(column=4, row=8)
    label_49.grid(column=4, row=9)
    label_410.grid(column=4, row=10)
    label_411.grid(column=4, row=11)
    label_412.grid(column=4, row=12)

    # 금요일
    label_51.grid(column=5, row=1)
    label_52.grid(column=5, row=2)
    label_53.grid(column=5, row=3)
    label_54.grid(column=5, row=4)
    label_55.grid(column=5, row=5)
    label_56.grid(column=5, row=6)
    label_57.grid(column=5, row=7)
    label_58.grid(column=5, row=8)
    label_59.grid(column=5, row=9)
    label_510.grid(column=5, row=10)
    label_511.grid(column=5, row=11)
    label_512.grid(column=5, row=12)

    ######### 시간표 선택 위치 #############

    time_box1.grid(column=1, row=1)
    time_box2.grid(column=2, row=1)
    time_box3.grid(column=3, row=1)
    time_box4.grid(column=4, row=1)
    time_box5.grid(column=5, row=1)
    time_box6.grid(column=1,row=2)
    time_box7.grid(column=2, row=2)
    time_box8.grid(column=3, row=2)
    time_box9.grid(column=4, row=2)
    time_box10.grid(column=5, row=2)
    time_box11.grid(column=1, row=3)
    time_box12.grid(column=2, row=3)
    time_box13.grid(column=3, row=3)
    time_box14.grid(column=4, row=3)
    time_box15.grid(column=5, row=3)
    time_box16.grid(column=1, row=4)
    time_box17.grid(column=2, row=4)
    time_box18.grid(column=3, row=4)
    time_box19.grid(column=4, row=4)
    time_box20.grid(column=5, row=4)
    time_box21.grid(column=1, row=5)
    time_box22.grid(column=2, row=5)
    time_box23.grid(column=3, row=5)
    time_box24.grid(column=4, row=5)
    time_box25.grid(column=5, row=5)
    time_box26.grid(column=1, row=6)
    time_box27.grid(column=2, row=6)
    time_box28.grid(column=3, row=6)
    time_box29.grid(column=4, row=6)
    time_box30.grid(column=5, row=6)
    time_box31.grid(column=1, row=7)
    time_box32.grid(column=2, row=7)
    time_box33.grid(column=3, row=7)
    time_box34.grid(column=4, row=7)
    time_box35.grid(column=5, row=7)
    time_box36.grid(column=1, row=8)
    time_box37.grid(column=2, row=8)
    time_box38.grid(column=3, row=8)
    time_box39.grid(column=4, row=8)
    time_box40.grid(column=5, row=8)
    time_box41.grid(column=1, row=9)
    time_box42.grid(column=2, row=9)
    time_box43.grid(column=3, row=9)
    time_box44.grid(column=4, row=9)
    time_box45.grid(column=5, row=9)
    time_box46.grid(column=1, row=10)
    time_box47.grid(column=2, row=10)
    time_box48.grid(column=3, row=10)
    time_box49.grid(column=4, row=10)
    time_box50.grid(column=5, row=10)
    time_box51.grid(column=1, row=11)
    time_box52.grid(column=2, row=11)
    time_box53.grid(column=3, row=11)
    time_box54.grid(column=4, row=11)
    time_box55.grid(column=5, row=11)
    time_box56.grid(column=1, row=12)
    time_box57.grid(column=2, row=12)
    time_box58.grid(column=3, row=12)
    time_box59.grid(column=4, row=12)
    time_box60.grid(column=5, row=12)

    ######### 화살표 위치선정##############
    right_arrow.grid(column=4, row=15) #리롤버튼

    build_but.grid(column=3, row=15, padx=5, pady=5)

    win.mainloop()
