import tkinter as tk

window = tk.Tk()
window.title("전북대학교 시간표")
window.geometry("500x700+100+100")

# 월화수목금 라벨 만들기
#label0 = tk.Label(window, text="", anchor='n', width=10, height=2, fg="red", relief="solid")
label1 = tk.Label(window, text="월요일", width=10, height=2, fg="red", relief="solid", bd=1)
label2 = tk.Label(window, text="화요일", width=10, height=2, fg="red", relief="solid", bd=1)
label3 = tk.Label(window, text="수요일", width=10, height=2, fg="red", relief="solid", bd=1)
label4 = tk.Label(window, text="목요일", width=10, height=2, fg="red", relief="solid", bd=1)
label5 = tk.Label(window, text="금요일", width=10, height=2, fg="red", relief="solid", bd=1)

#월화수목금 라벨 자리 배치하기
#label0.grid(row=0, column=0)
label1.grid(row=0, column=1)
label2.grid(row=0, column=2)
label3.grid(row=0, column=3)
label4.grid(row=0, column=4)
label5.grid(row=0, column=5)

# 9시, 10시 등 시간 라벨 만들기
label10 = tk.Label(window, text="9시", width=10, height=3, fg="red", relief="solid", bd=1)
label11 = tk.Label(window, text="10시", width=10, height=3, fg="red", relief="solid", bd=1)
label12 = tk.Label(window, text="11시", width=10, height=3, fg="red", relief="solid", bd=1)
label13 = tk.Label(window, text="12시", width=10, height=3, fg="red", relief="solid", bd=1)
label14 = tk.Label(window, text="13시", width=10, height=3, fg="red", relief="solid", bd=1)
label15 = tk.Label(window, text="14시", width=10, height=3, fg="red", relief="solid", bd=1)
label16 = tk.Label(window, text="15시", width=10, height=3, fg="red", relief="solid", bd=1)
label17 = tk.Label(window, text="16시", width=10, height=3, fg="red", relief="solid", bd=1)
label18 = tk.Label(window, text="17시", width=10, height=3, fg="red", relief="solid", bd=1)
label19 = tk.Label(window, text="18시", width=10, height=3, fg="red", relief="solid", bd=1)
label110 = tk.Label(window, text="19시", width=10, height=3, fg="red", relief="solid", bd=1)
label111 = tk.Label(window, text="20시", width=10, height=3, fg="red", relief="solid", bd=1)

#시간 라벨 자리배치하기
label10.grid(row=1, column=0)
label11.grid(row=2, column=0)
label12.grid(row=3, column=0)
label13.grid(row=4, column=0)
label14.grid(row=5, column=0)
label15.grid(row=6, column=0)
label16.grid(row=7, column=0)
label17.grid(row=8, column=0)
label18.grid(row=9, column=0)
label19.grid(row=10, column=0)
label110.grid(row=11, column=0)
label111.grid(row=12, column=0)

#시간표 셀 만들기
#월요일
label20 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label21 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label22 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label23 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label24 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label25 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label26 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label27 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label28 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label29 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label210 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label211 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
#화요일
label30 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label31 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label32 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label33 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label34 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label35 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label36 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label37 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label38 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label39 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label310 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label311 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
#수요일
label40 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label41 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label42 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label43 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label44 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label45 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label46 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label47 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label48 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label49 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label410 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label411 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
#목요일
label50 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label51 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label52 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label53 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label54 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label55 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label56 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label57 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label58 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label59 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label510 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label511 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
#금요일
label60 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label61 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label62 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label63 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label64 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label65 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label66 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label67 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label68 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label69 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label610 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)
label611 = tk.Label(window, text="", width=10, height=3, fg="red", relief="solid", bd=1)

#시간표 셀 자리배치
#월요일
label20.grid(row=1, column=1)
label21.grid(row=2, column=1)
label22.grid(row=3, column=1)
label23.grid(row=4, column=1)
label24.grid(row=5, column=1)
label25.grid(row=6, column=1)
label26.grid(row=7, column=1)
label27.grid(row=8, column=1)
label28.grid(row=9, column=1)
label29.grid(row=10, column=1)
label210.grid(row=11, column=1)
label211.grid(row=12, column=1)
#화요일
label30.grid(row=1, column=2)
label31.grid(row=2, column=2)
label32.grid(row=3, column=2)
label33.grid(row=4, column=2)
label34.grid(row=5, column=2)
label35.grid(row=6, column=2)
label36.grid(row=7, column=2)
label37.grid(row=8, column=2)
label38.grid(row=9, column=2)
label39.grid(row=10, column=2)
label310.grid(row=11, column=2)
label311.grid(row=12, column=2)
#수요일
label40.grid(row=1, column=3)
label41.grid(row=2, column=3)
label42.grid(row=3, column=3)
label43.grid(row=4, column=3)
label44.grid(row=5, column=3)
label45.grid(row=6, column=3)
label46.grid(row=7, column=3)
label47.grid(row=8, column=3)
label48.grid(row=9, column=3)
label49.grid(row=10, column=3)
label410.grid(row=11, column=3)
label411.grid(row=12, column=3)
#목요일
label50.grid(row=1, column=4)
label51.grid(row=2, column=4)
label52.grid(row=3, column=4)
label53.grid(row=4, column=4)
label54.grid(row=5, column=4)
label55.grid(row=6, column=4)
label56.grid(row=7, column=4)
label57.grid(row=8, column=4)
label58.grid(row=9, column=4)
label59.grid(row=10, column=4)
label510.grid(row=11, column=4)
label511.grid(row=12, column=4)
#금요일
label60.grid(row=1, column=5)
label61.grid(row=2, column=5)
label62.grid(row=3, column=5)
label63.grid(row=4, column=5)
label64.grid(row=5, column=5)
label65.grid(row=6, column=5)
label66.grid(row=7, column=5)
label67.grid(row=8, column=5)
label68.grid(row=9, column=5)
label69.grid(row=10, column=5)
label610.grid(row=11, column=5)
label611.grid(row=12, column=5)

#시간표 셀 안에 체크버튼 만들기
#월요일
time_check20 = tk.Checkbutton(window, text='')
time_check21 = tk.Checkbutton(window, text='')
time_check22 = tk.Checkbutton(window, text='')
time_check23 = tk.Checkbutton(window, text='')
time_check24 = tk.Checkbutton(window, text='')
time_check25 = tk.Checkbutton(window, text='')
time_check26 = tk.Checkbutton(window, text='')
time_check27 = tk.Checkbutton(window, text='')
time_check28 = tk.Checkbutton(window, text='')
time_check29 = tk.Checkbutton(window, text='')
time_check210 = tk.Checkbutton(window, text='')
time_check211 = tk.Checkbutton(window, text='')
#화요일
time_check30 = tk.Checkbutton(window, text='')
time_check31 = tk.Checkbutton(window, text='')
time_check32 = tk.Checkbutton(window, text='')
time_check33 = tk.Checkbutton(window, text='')
time_check34 = tk.Checkbutton(window, text='')
time_check35 = tk.Checkbutton(window, text='')
time_check36 = tk.Checkbutton(window, text='')
time_check37 = tk.Checkbutton(window, text='')
time_check38 = tk.Checkbutton(window, text='')
time_check39 = tk.Checkbutton(window, text='')
time_check310 = tk.Checkbutton(window, text='')
time_check311 = tk.Checkbutton(window, text='')
#수요일
time_check40 = tk.Checkbutton(window, text='')
time_check41 = tk.Checkbutton(window, text='')
time_check42 = tk.Checkbutton(window, text='')
time_check43 = tk.Checkbutton(window, text='')
time_check44 = tk.Checkbutton(window, text='')
time_check45 = tk.Checkbutton(window, text='')
time_check46 = tk.Checkbutton(window, text='')
time_check47 = tk.Checkbutton(window, text='')
time_check48 = tk.Checkbutton(window, text='')
time_check49 = tk.Checkbutton(window, text='')
time_check410 = tk.Checkbutton(window, text='')
time_check411 = tk.Checkbutton(window, text='')
#목요일
time_check50 = tk.Checkbutton(window, text='')
time_check51 = tk.Checkbutton(window, text='')
time_check52 = tk.Checkbutton(window, text='')
time_check53 = tk.Checkbutton(window, text='')
time_check54 = tk.Checkbutton(window, text='')
time_check55 = tk.Checkbutton(window, text='')
time_check56 = tk.Checkbutton(window, text='')
time_check57 = tk.Checkbutton(window, text='')
time_check58 = tk.Checkbutton(window, text='')
time_check59 = tk.Checkbutton(window, text='')
time_check510 = tk.Checkbutton(window, text='')
time_check511 = tk.Checkbutton(window, text='')
#금요일
time_check60 = tk.Checkbutton(window, text='')
time_check61 = tk.Checkbutton(window, text='')
time_check62 = tk.Checkbutton(window, text='')
time_check63 = tk.Checkbutton(window, text='')
time_check64 = tk.Checkbutton(window, text='')
time_check65 = tk.Checkbutton(window, text='')
time_check66 = tk.Checkbutton(window, text='')
time_check67 = tk.Checkbutton(window, text='')
time_check68 = tk.Checkbutton(window, text='')
time_check69 = tk.Checkbutton(window, text='')
time_check610 = tk.Checkbutton(window, text='')
time_check611 = tk.Checkbutton(window, text='')


#시간표 셀 자리배치
#월요일
time_check20.grid(row=1, column=1)
time_check21.grid(row=2, column=1)
time_check22.grid(row=3, column=1)
time_check23.grid(row=4, column=1)
time_check24.grid(row=5, column=1)
time_check25.grid(row=6, column=1)
time_check26.grid(row=7, column=1)
time_check27.grid(row=8, column=1)
time_check28.grid(row=9, column=1)
time_check29.grid(row=10, column=1)
time_check210.grid(row=11, column=1)
time_check211.grid(row=12, column=1)
#회요일
time_check30.grid(row=1, column=2)
time_check31.grid(row=2, column=2)
time_check32.grid(row=3, column=2)
time_check33.grid(row=4, column=2)
time_check34.grid(row=5, column=2)
time_check35.grid(row=6, column=2)
time_check36.grid(row=7, column=2)
time_check37.grid(row=8, column=2)
time_check38.grid(row=9, column=2)
time_check39.grid(row=10, column=2)
time_check310.grid(row=11, column=2)
time_check311.grid(row=12, column=2)
#수요일
time_check40.grid(row=1, column=3)
time_check41.grid(row=2, column=3)
time_check42.grid(row=3, column=3)
time_check43.grid(row=4, column=3)
time_check44.grid(row=5, column=3)
time_check45.grid(row=6, column=3)
time_check46.grid(row=7, column=3)
time_check47.grid(row=8, column=3)
time_check48.grid(row=9, column=3)
time_check49.grid(row=10, column=3)
time_check410.grid(row=11, column=3)
time_check411.grid(row=12, column=3)
#목요일
time_check50.grid(row=1, column=4)
time_check51.grid(row=2, column=4)
time_check52.grid(row=3, column=4)
time_check53.grid(row=4, column=4)
time_check54.grid(row=5, column=4)
time_check55.grid(row=6, column=4)
time_check56.grid(row=7, column=4)
time_check57.grid(row=8, column=4)
time_check58.grid(row=9, column=4)
time_check59.grid(row=10, column=4)
time_check510.grid(row=11, column=4)
time_check511.grid(row=12, column=4)
#금요일
time_check60.grid(row=1, column=5)
time_check61.grid(row=2, column=5)
time_check62.grid(row=3, column=5)
time_check63.grid(row=4, column=5)
time_check64.grid(row=5, column=5)
time_check65.grid(row=6, column=5)
time_check66.grid(row=7, column=5)
time_check67.grid(row=8, column=5)
time_check68.grid(row=9, column=5)
time_check69.grid(row=10, column=5)
time_check610.grid(row=11, column=5)
time_check611.grid(row=12, column=5)

#만들기버튼
build_but = tk.Button(window, text='만들기')
build_but.grid(column=3, row=15, padx=5, pady=5)

#리로드버튼
right_arrow = tk.Button(window, text='Reload', width=10)
right_arrow.grid(column=4, row=15)

window.mainloop()