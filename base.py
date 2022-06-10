import csv
from typing import List

from PyQt5.QtCore import endl


def read_data(filename) -> (List[str], List[str], List[str]): # 자료를 읽어서 과목 이름, 교양 영역, 시간을 리스트로 출력
    title_list = []
    category_list = []
    time_list = []
    credit_list = []
    subject_list = []
    with open(filename, encoding="UTF-8") as f:
        csv_reader = csv.reader(f)

        for _ in range(12):
            next(csv_reader)
        for tokens in csv_reader:
            title_list.append(tokens[6])
            category_list.append(tokens[12])
            time_list.append(tokens[19])
            credit_list.append(tokens[8])
        for i in range(805):
            subject_list.append([title_list[i], category_list[i], time_list[i], credit_list[i]])
    return title_list, category_list, time_list, credit_list, subject_list

#같은 이름, 같은 시간끼리 묶어서 리스트 만들기
#


def main():
    filename = "./개설교과목목록_1654420364753.csv"
    title, category, time, credit, subject = read_data(filename)

    print(title)
    print(category)
    print(time)
    print(credit)
    print(subject)



if __name__ == "__main__":
    main()