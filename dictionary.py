import re, json

dictionary = {}

# json 형식으로 파일에 저장
with open("dictionary.json", mode="w", encoding="utf-8") as f:
  json.dump(dictionary, f, ensure_ascii=False, indent=4)

# 예외 처리
class ErrorExecption(Exception):
  def __init__(self, errmsg):
    self.errmsg = errmsg
  def __str__(self):
    return self.errmsg

# 단어장
stop = False
while not stop :
  try:
    print("=" * 45)
    print("1.저장 2.검색 3.수정 4.삭제 5.목록 6.통계 7.종료")
    print("=" * 45)
    menu = input("메뉴 선택 : ")

    match menu :
      # 단어 등록
      case "1" :
        dict_eng = input("단어 : ")
        dict_kor = input("뜻 : ")

        # 대문자로 입력받더라도 소문자로 변환
        dict_eng = dict_eng.lower()

        if dict_eng in dictionary :
          print("이미 등록되었습니다.")
          continue

        if len(dictionary) >= 5 :
          raise ErrorExecption("최대 5단어만 저장할 수 있습니다.")

        dictionary[dict_eng] = dict_kor

        with open("dictionary.json", mode="w", encoding="utf-8") as f:
          json.dump(dictionary, f, ensure_ascii=False, indent=4)
        continue  # 파일에 기록하고 나서 메뉴 선택으로 다시 이동

      # 단어 검색
      case "2":
        search_word = input("검색할 단어 : ")
        search_word = search_word.lower()

        # 일치하는 키 값 찾기
        pattern = r'^' + re.escape(search_word)
        matching_keys = [key for key in dictionary.keys() if re.search(pattern, key)]

        if matching_keys :
          for key in matching_keys:
            print(key, dictionary[key])
        else:
          print("단어를 검색할 수 없습니다.")

      # 단어 수정
      case "3":
        edit_word = input("단어 선택 : ")
        edit_word = edit_word.lower()

        # 일치하는 키 값 찾기
        pattern = r'^' + re.escape(edit_word)
        matching_keys = [key for key in dictionary.keys() if re.search(pattern, key)]

        if matching_keys :
          for key in matching_keys :
            dictionary.pop(key)
            dictionary[key] = input("수정할 뜻 : ")
            print("단어의 뜻을 수정하였습니다.")
        else :
          print("단어를 검색할 수 없습니다.")

      # 단어 삭제
      case "4":
        del_word = input("단어 선택 : ")
        del_word = del_word.lower()

        # 일치하는 키 값 찾기
        pattern = r'^' + re.escape(del_word)
        matching_keys = [key for key in dictionary.keys() if re.search(pattern, key)]

        if matching_keys:
          for key in matching_keys:
            del dictionary[key]
            print("단어를 삭제하였습니다.")
        else :
          print("단어를 검색할 수 없습니다.")

      case "5":
        print("1.오름차순 2.내림차순")
        order = input("정렬 방식을 고르세요 : ")

        li = list(dictionary.items())

        match order :
          case "1" :
            li.sort(key = lambda x: x[0])
            for key, value in li :
              print(key, value)
            continue
          case "2" :
            li.sort(key=lambda x: x[0])
            li.reverse()
            for key, value in li:
              print(key, value)
            continue
          case _ :
            print("1~2 중에서 고르세요.")

      # 통계
      case "6":
        print("1.저장된 단어 갯수 2.단어의 문자 수가 가장 많은 단어 3.단어 글자 수 내림차순 출력")
        stats = input("확인할 통계 : ")

        stats_flag = False
        while not stats_flag :
          match stats :

            # 저장된 단어 갯수
            case "1" :
              dict_len = len(dictionary)
              print(dict_len, "개")
              break

            # 단어의 문자 수가 가장 많은 단어
            case "2" :
              max_len = 0
              longest_word = ""
              for key in dictionary.keys() :
                cnt = len(key)
                if cnt > max_len :
                  max_len = cnt
                  longest_word = key
              print("단어의 문자 수가 가장 많은 단어 : ", longest_word)

              break

            # 단어 글자 수 내림차순 출력
            case "3" :
              keys_list = list(dictionary.keys())
              keys_list.sort(key = lambda leng : len(leng))
              keys_list.reverse()
              for key in keys_list:
                print(key)
              break

            case _ :
              print("1~3 중에서 고르세요.")

      case "7":
        stop = True

      case _ :
        print("1~7 중에서 고르세요.")
  except ErrorExecption as e :
    print(e)
  else :
    continue
