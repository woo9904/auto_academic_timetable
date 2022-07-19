import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
import csv
import webbrowser

root=Tk()
root.title("시간표 자동 생성기")  

global majors_list
global lectures_list

def create_major_window():    #학과 선택하기 명령어
    def major_insert():  #입력 버튼 명령어
        mjInput=major_combobox.get()
        if mjInput in major_values:
            majors_list=[x for x in input_major_list.get(0,END)]
            if mjInput in majors_list:
                pass
            else:
                input_major_list.insert(END, mjInput)
        else:
            msgbox.showerror("에러", "리스트에 일치하는 학과 이름이 아닙니다. \n다시한번 확인해서 입력해주세요.", parent=major_window) #창 저절로 안꺼지게 만듦
            return

    def major_del():  #선택삭제 명령어
        for index in reversed(input_major_list.curselection()):
            input_major_list.delete(index)

    def major_last_input():   #최종 입력 명령어
        #파일 목록 확인
        if input_major_list.size()==0:
            msgbox.showwarning("경고", "과를 선택해 주세요", parent=major_window)
            return
        response=msgbox.askokcancel("확인/취소", "해당 학과를 입력 조건으로 넣겠습니까?", parent=major_window)
        if response==False:
            msgbox.showinfo("알림", "취소했습니다.", parent=major_window)
            return
        elif response==True:
            majors_list=[x for x in input_major_list.get(0,END)]
            input_text.config(state="normal")
            input_text.insert(INSERT,"<선택한 학과> \n")
            for i in majors_list:
                input_text.insert(END, "{}/".format(i))
            input_text.insert(END, "\n")
            input_text.insert(END, "--------------------------------\n")
            input_text.config(state="disabled")
            major_window.destroy()

    #gui 만들기
    major_window=Toplevel(root)
    major_window.title("과 검색/선택하기")
    #라벨
    Label(major_window, text="자신의 학과를 찾아 입력 조건에 넣으세요.").pack(padx=5, pady=5)
    #콤보박스 values들
    major_values=[]
    for lecture in datas:
        majors=lecture[13].split(",")
        for major in majors:
            if major not in major_values:
                major_values.append(major)
    major_values.sort()
    #sframe속 combobox, button
    major_sframe=Frame(major_window)
    major_sframe.pack(fill="x", padx=10, pady=10)
    major_combobox=ttk.Combobox(major_sframe, values=major_values) 
    major_combobox.pack(side="left", fill='y', padx=5, pady=5)
    major_combobox.set("과를 찾아 입력해주세요")
    Button(major_sframe, text="입력", width=10, pady=5, command=major_insert).pack(padx=5, pady=5)
    #input_major_label속 listbox, scrollbar, button
    input_major_label=LabelFrame(major_window, text="선택된 학과들")
    input_major_label.pack(padx=5, pady=5)

    major_scrollbar=Scrollbar(input_major_label)
    major_scrollbar.pack(fill="y", side="right",padx=5, pady=5)
    input_major_list=Listbox(input_major_label, selectmode="extended",width=40, height=15, yscrollcommand=major_scrollbar.set)
    input_major_list.pack(side="left")
    major_scrollbar.config(command=input_major_list.yview)

    major_boxframe=Frame(major_window)
    major_boxframe.pack(side="bottom", fill="x", expand=True,padx=5, pady=5)
    Button(major_boxframe, text="조건넣기", width=15, pady=5, command=major_last_input).pack(side="right", padx=20, pady=5)
    Button(major_boxframe, text="선택삭제", width=15, pady=5, command=major_del).pack(side="right", padx=20, pady=5)



def create_prolec_window():    #교수님/강의 선택하기 명령어
    def choose_get():
        choose_val(choose_var.get())
    def choose_val(str_name):
        choose_values=[]
        #콤보박스 values들(교수/강의에 따라 달라짐)
        if str_name=="교수":
            for lecture in datas:
                profs=lecture[7].split(",")
                for prof in profs:
                    prof=prof.strip()
                    if prof not in choose_values:
                        choose_values.append(prof)
            choose_values.sort()
            choose_combobox.config(values=choose_values)
        if str_name=="강의":
            for lecture in datas:
                lec=lecture[5]
                if lec not in choose_values:
                    choose_values.append(lec)
            choose_values.sort()
            choose_combobox.config(values=choose_values)

    def search():  #검색 버튼 명령어
        tree.delete(*tree.get_children())
        CInput=choose_combobox.get()

        if choose_var.get() =="교수":
            for lecture in datas:
                profs=lecture[7].split(",")
                for prof in profs:
                    prof=prof.strip()
                    if prof==CInput:
                        tree.insert('', 'end', values=lecture)

        if choose_var.get() =="강의":
            for lecture in datas:
                lec=lecture[5]
                if lec==CInput:
                        tree.insert('', 'end', values=lecture)

    def link_plan(): #강의 계획서 버튼 명령어
        webbrowser.open(tree.item(tree.focus(),'values')[1])

    def link_star(): #강의평 버튼 명령어
        webbrowser.open(tree.item(tree.focus(),'values')[10])

    def put_value(): #선택 입력 명령어
        put_in=True
        input_lec=tree.item(tree.focus(),'values')
        if input_lec !='':
            for parent in tree2.get_children():
                one_data=tree2.item(parent)['values'][4]
                if str(input_lec[4])==str(one_data):
                    msgbox.showwarning("경고", "이미 선택한 강의입니다.", parent=prolec_window)
                    put_in=False
                    break
            if put_in==True:
                tree2.insert('', 'end', values=input_lec)
        else:
            msgbox.showwarning("경고", "선택된 강의가 없습니다.", parent=prolec_window)

    def prolec_delete(): #선택 삭제 명령어
        selected_item=tree2.selection()
        for i in reversed(selected_item):
            tree2.delete(i)

    def prolec_last_input():   #최종 입력 명령어
        #파일 목록 확인
        if len(tree2.get_children())==0:
            msgbox.showwarning("경고", "강의를 선택해 주세요", parent=prolec_window)
            return
        response=msgbox.askokcancel("확인/취소", "해당 강의를 입력 조건으로 넣겠습니까?", parent=prolec_window)
        if response==False:
            msgbox.showinfo("알림", "취소했습니다.", parent=prolec_window)
            return
        elif response==True:
            input_text.config(state="normal")
            input_text.insert(INSERT,"<선택한 강의>(강의번호:강의명) \n")
            lectures_list=[]
            for parent in tree2.get_children():
                lec_code=tree2.item(parent)['values'][4]
                lec_name=tree2.item(parent)['values'][5]
                lectures_list.append(lec_code)
                input_text.insert(END, "{}:{},/".format(lec_code, lec_name))
            input_text.insert(END, "\n")
            input_text.insert(END, "--------------------------------\n")
            input_text.config(state="disabled")
            prolec_window.destroy()

    #gui 만들기
    prolec_window=Toplevel(root)
    prolec_window.title("교수님/강의 검색/선택하기")
    Label(prolec_window, text="듣고싶은 교수님 또는 강의를 선택하세요.").grid(row=0, column=3, columnspan=2, sticky=N+E+S+W, padx=5, pady=5)

    #p1frame속 label, radiobutton, combobox, buttons
    p1frame=LabelFrame(prolec_window, text="검색하기")
    p1frame.grid(row=1, column=0, columnspan=4, sticky=W,padx=5, pady=5)
    #->Label
    exlable=Label(p1frame, text="검색하려는 항목을 선택하고 검색해주세요.")
    exlable.grid(row=0, column=0, columnspan=4, sticky=W,padx=5, pady=5)
    #->var_frame/radiobutton, button
    var_frame=Frame(p1frame)
    var_frame.grid(row=1, column=0, rowspan=2,padx=5, pady=5)
    choose_var=StringVar()  #교수/강의 선택
    btn_prof=Radiobutton(var_frame, text="교수", value="교수", variable=choose_var)
    btn_prof.select()
    btn_lect=Radiobutton(var_frame, text="강의", value="강의", variable=choose_var)
    btn_prof.pack()
    btn_lect.pack()
    choose_btn=Button(var_frame, text="선택", command=choose_get)
    choose_btn.pack()
    #->combobox, button
    choose_values=[]
    choose_combobox=ttk.Combobox(p1frame, values=choose_values, width=40) 
    choose_combobox.grid(row=1, column=2,padx=5, pady=5)
    choose_combobox.set("선택 버튼 먼저 눌러주시고 검색해 주세요")
    Button(p1frame, text="검색", width=10, pady=5, command=search).grid(row=2, column=2, sticky=E,padx=5, pady=5)

    #p2frame속 label, buttons
    p2frame=LabelFrame(prolec_window, text="링크 확인하기")
    p2frame.grid(row=1, column=4, columnspan=4, sticky=E,padx=5, pady=5)
    #->Label
    ex2lable=Label(p2frame, text="강의 계획서/평점 내용을 확인하고 싶다면 눌러주세요.")
    ex2lable.grid(row=0, column=0, columnspan=4, sticky=W,padx=5, pady=5)
    #->buttons
    Button(p2frame, text="강의 계획서", width=10, pady=5, command=link_plan).grid(row=1, column=3, sticky=E,padx=5, pady=5)
    Button(p2frame, text="평점 내용", width=10, pady=5, command=link_star).grid(row=2, column=3, sticky=E,padx=5, pady=5)

    #table_frame속 table
    table_frame=Frame(prolec_window)
    table_frame.grid(row=2, column=0, columnspan=8,padx=5, pady=5)

    treescb=ttk.Scrollbar(table_frame)
    treescb.pack(side="right", fill="y")

    tree=ttk.Treeview(table_frame, columns=["인덱스","계획서","학년", "이수구분", "과목번호", "교과목명","학점","담당교수","강의교시/강의실", "강의평", "평점링크","담은인원","정원","수강학과","비고"],\
        displaycolumns=["학년", "이수구분", "과목번호", "교과목명","학점","담당교수","강의교시/강의실", "강의평","담은인원","정원","수강학과","비고"], yscrollcommand=treescb.set)
    tree.pack(side="left", fill='both', expand=True)
    treescb.config(command=tree.yview)

    tree.column("#0", width=20)
    tree.heading("학년", text="학년")
    tree.column("#1", width=50)
    tree.heading("이수구분", text="이수구분")
    tree.column("#2", width=75)
    tree.heading("과목번호", text="과목번호")
    tree.column("#3", width=75)
    tree.heading("교과목명", text="교과목명")
    tree.column("#4", width=100)
    tree.heading("학점", text="학점")
    tree.column("#5", width=50)
    tree.heading("담당교수", text="담당교수")
    tree.column("#6", width=100)
    tree.heading("강의교시/강의실", text="강의교시/강의실")
    tree.column("#7", width=200)
    tree.heading("강의평", text="강의평")
    tree.column("#8", width=50)
    tree.heading("담은인원", text="담은인원")
    tree.column("#9", width=75)
    tree.heading("정원", text="정원") 
    tree.column("#10", width=50)
    tree.heading("수강학과", text="수강학과")
    tree.column("#11", width=100)
    tree.heading("비고", text="비고")
    tree.column("#12", width=300)

    for i in range(1,len(datas)):  #데이터 삽입
        tree.insert('', 'end', text=i, values=datas[i], iid=str(i))

    #입력버튼
    Button(prolec_window, text="입력", width=10, padx=5, pady=5, command=put_value).grid(row=3, column=7)

    #table2_frame속 table, buttons
    table2_frame=LabelFrame(prolec_window, text="선택된 항목들")
    table2_frame.grid(row=4, column=0, columnspan=8, padx=5, pady=5)

    tree2scb=ttk.Scrollbar(table2_frame)
    tree2scb.pack(side="right", fill="y")

    tree2=ttk.Treeview(table2_frame, columns=["인덱스","계획서","학년", "이수구분", "과목번호", "교과목명","학점","담당교수","강의교시/강의실", "강의평", "평점링크","담은인원","정원","수강학과","비고"],\
        displaycolumns=["학년", "이수구분", "과목번호", "교과목명","학점","담당교수","강의교시/강의실", "강의평","담은인원","정원","수강학과","비고"], yscrollcommand=tree2scb.set, height=5)
    tree2.pack(side="left", fill='both', expand=True, padx=5, pady=5)
    tree2scb.config(command=tree2.yview)

    tree2.column("#0", width=20)
    tree2.heading("학년", text="학년")
    tree2.column("#1", width=50)
    tree2.heading("이수구분", text="이수구분")
    tree2.column("#2", width=75)
    tree2.heading("과목번호", text="과목번호")
    tree2.column("#3", width=75)
    tree2.heading("교과목명", text="교과목명")
    tree2.column("#4", width=100)
    tree2.heading("학점", text="학점")
    tree2.column("#5", width=50)
    tree2.heading("담당교수", text="담당교수")
    tree2.column("#6", width=100)
    tree2.heading("강의교시/강의실", text="강의교시/강의실")
    tree2.column("#7", width=200)
    tree2.heading("강의평", text="강의평")
    tree2.column("#8", width=50)
    tree2.heading("담은인원", text="담은인원")
    tree2.column("#9", width=75)
    tree2.heading("정원", text="정원") 
    tree2.column("#10", width=50)
    tree2.heading("수강학과", text="수강학과")
    tree2.column("#11", width=100)
    tree2.heading("비고", text="비고")
    tree2.column("#12", width=300)

    #조건 넣기 버튼
    Button(prolec_window, text="조건넣기", width=10, padx=5, pady=5, command=prolec_last_input).grid(row=5, column=7, padx=5, pady=5)
    Button(prolec_window, text="선택삭제", width=10, padx=5, pady=5, command=prolec_delete).grid(row=5, column=6, padx=5, pady=5)










filename="전체수강표.csv"
datas=[]
f=open(filename, 'r', encoding='utf-8-sig')
reader=csv.reader(f)
for line in reader:
    datas.append(line)

#학교/학기 프레임
school_semester=Frame(root)
school_semester.pack(fill="x", padx=10, pady=10)
#->학교 선택
school_label=Label(school_semester, text="학교")
school_label.pack(side="left", padx=5, pady=5)

school_values=["건국대학교"] 
school_combobox=ttk.Combobox(school_semester, height=5, values=school_values, state="readonly") 
school_combobox.pack(side="left", padx=5, pady=5)
school_combobox.current(0)
#->학기 선택
semester_values=["1학기", "2학기"] 
semester_combobox=ttk.Combobox(school_semester, height=5, values=semester_values, state="readonly") 
semester_combobox.pack(side="right", padx=5, pady=5)
semester_combobox.current(0)

semester_label=Label(school_semester, text="학기")
semester_label.pack(side="right", padx=5, pady=5)

#과/교수님/강좌명/우선순위 선택 프레임
tem_frame=Frame(root)
tem_frame.pack()
#->과
major_frame=LabelFrame(tem_frame, text="과")
major_frame.grid(row=0, column=0, rowspan=2, padx=5, pady=5)

picked_major=Entry(major_frame)
picked_major.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) #ipady-> 높이 변경

btn_major_search=Button(major_frame, text="검색/입력", width=10, command=create_major_window)
btn_major_search.pack(side="right", padx=5, pady=5)
#->교수님/강의
professor_frame=LabelFrame(tem_frame, text="교수님/강의")
professor_frame.grid(row=2, column=0, rowspan=2, padx=5, pady=5)

picked_professor=Entry(professor_frame)
picked_professor.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) #ipady-> 높이 변경

btn_professor_search=Button(professor_frame, text="검색/입력", width=10, command=create_prolec_window)
btn_professor_search.pack(side="right", padx=5, pady=5)
#->영역
lesson_frame=LabelFrame(tem_frame, text="영역")
lesson_frame.grid(row=4, column=0, rowspan=2, padx=5, pady=5)

picked_lesson=Entry(lesson_frame)
picked_lesson.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) #ipady-> 높이 변경

btn_lesson_search=Button(lesson_frame, text="검색/입력", width=10)
btn_lesson_search.pack(side="right", padx=5, pady=5)

#->우선순위 선택 프레임
priority_frame=LabelFrame(tem_frame, text="우선순위")
priority_frame.grid(row=6, column=0, rowspan=2, padx=5, pady=5)

pick_values=["최대한 공강 없이", "강의당 30분 텀", "오전 수업 최대한 배제", "평점", "전공 우선", "학점 채우기 우선"] 
pick_combobox=ttk.Combobox(priority_frame, height=5, values=pick_values, state="readonly") 
pick_combobox.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)
pick_combobox.set("우선 순위 선택해주세요.") 

btn_priority=Button(priority_frame, text="선택하기")
btn_priority.pack(side="right", fill="x", expand=True, padx=5, pady=5, ipady=4)

#-> 입력조건 표시 창
input_list_frame=Frame(tem_frame)
input_list_frame.grid(row=0, column=1, rowspan=7, columnspan=2, padx=5, pady=5)

input_label=Label(input_list_frame, text="   <입력된 조건>   ")
input_label.pack(fill="both")

scrollbar=Scrollbar(input_list_frame)
scrollbar.pack(side="right", fill="y")

input_text=Text(input_list_frame, state="disabled",width=40, height=15, yscrollcommand=scrollbar.set)
input_text.pack(side="left", fill="both", expand=True)
scrollbar.config(command=input_text.yview)


#->버튼
btn_del=Button(tem_frame, text="선택삭제", width=10)
btn_del.grid(row=7, column=1, padx=5, pady=5)

btn_ok=Button(tem_frame, text="최종 입력", width=10)
btn_ok.grid(row=7, column=2, padx=5, pady=5, sticky=N+E+W+S)


#진행 상황 progress bar
frame_progress=LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var=DoubleVar()
progress_bar=ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

#1순위 결과물
output_frame=LabelFrame(root, text="1순위 결과물")
output_frame.pack(fill="both", padx=5, pady=5, ipady=5)

output=Entry(output_frame, state="readonly")
output.pack(side="left", fill="both", expand=True, padx=5, pady=5, ipady=5) #ipady-> 높이 변경

#다른 방안 확인하기/닫기
end_frame=Frame(root)
end_frame.pack(fill="x", padx=5, pady=5)

btn_close=Button(end_frame, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)
btn_down=Button(end_frame, padx=5, pady=5, text="다른 방안 다운하기")
btn_down.pack(side="right", padx=5, pady=5)

root.resizable(False, False) 
root.mainloop()