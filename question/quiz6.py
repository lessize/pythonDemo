# 5)
# 이름, 나이, 국어 점수, 영어 점수를 데이터로 갖는 student 딕셔너리를 만드시오.
# 각 데이터는 키보드로 입력받아 저장하고, 저장된 데이터를 출력하시오.
# name = input('이름 : ')
# age = input('나이 : ')
# kor = input('국어 : ')
# eng = input('영어 : ')
#
# student = {'이름': name, '나이': age, '국어': kor, '영어': eng}
#
# print(student)

# 딕셔너리 생성
student = {} #dict()
student['이름'] = input('이름 : ')
student['나이'] = input('나이 : ')
student['국어'] = input('국어 : ')
student['영어'] = input('영어 : ')
print(student)


# 6)
# 5번 문제에서 만든 딕셔너리 데이터에 총점 데이터를 추가하시오.
# 총점 데이터는 국어, 영어 점수의 합으로 들어가야 합니다.

# student['총점'] = int(kor) + int(eng)
student['총점'] = int(student['국어']) + int(student['영어'])

print(student)