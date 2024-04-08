# 2)
# 키보드로 세 문자열을 입력받고, 입력받은 세 문자열을 리스트에 저장하시오.
# 그 후 리스트에 저장된 문자열 중 가장 긴 문자열과 가장 짧은 문자열의 글자 수 차이를 출력하시오.

str1 = input('문자열1 : ')
str2 = input('문자열2 : ')
str3 = input('문자열3 : ')

strs = [len(str1), len(str2), len(str3)]

print(f'가장 긴 문자열과 가장 짧은 문자열의 글자 수 차이 : {abs(max(strs)-min(strs))}')

