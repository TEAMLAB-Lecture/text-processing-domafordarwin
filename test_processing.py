#######################
# Test Processing I   #
#######################

"""
NLP에서 흔히하는 전처리는 소문자 변환, 앞뒤 필요없는 띄어쓰기를 제거하는 등의 텍스트 정규화 (text normalization)입니다. 
"""


def normalize(input_string):
    """
     인풋으로 받는 스트링에서 정규화된 스트링을 반환함
     아래의 요건들을 충족시켜야함
    * 모든 단어들은 소문자로 되어야함
    * 띄어쓰기는 한칸으로 되어야함
    * 앞뒤 필요없는 띄어쓰기는 제거해야함

         Parameters:
             input_string (string): 영어로 된 대문자, 소문자, 띄어쓰기, 문장부호, 숫자로 이루어진 string
             ex - "This is an example.", "   EXTRA   SPACE   "

         Returns:
             normalized_string (string): 위 요건을 충족시킨 정규회된 string
             ex - 'this is an example.'

         Examples:
             >>> import text_processing as tp
             >>> input_string1 = "This is an example."
             >>> tp.normalize(input_string1)
             'this is an example.'
             >>> input_string2 = "   EXTRA   SPACE   "
             >>> tp.normalize(input_string2)
             'extra space'
    """
    normalized_string = None
    
    #소문자로 만들기
    normalized_string=input_string.lower()
    
    
    #모든 공백을 제거한 후 한 칸의 공백을 넣기
    pre_string = normalized_string.split()
    
    temp = " "
    for i in pre_string:
        temp = temp + " " + i
    normalized_string = temp
    
    # 앞 뒤의 공백 지우기
    
    normalized_string=normalized_string.lstrip()
    normalized_string=normalized_string.rstrip()
    
    # 결과 반환하기
    return normalized_string


def no_vowels(input_string):
    """
    인풋으로 받는 스트링에서 모든 모음 (a, e, i, o, u)를 제거시킨 스트링을 반환함

        Parameters:
            input_string (string): 영어로 된 대문자, 소문자, 띄어쓰기, 문장부호로 이루어진 string
            ex - "This is an example."

        Returns:
            no_vowel_string (string): 모든 모음 (a, e, i, o, u)를 제거시킨 스트링
            ex - "Ths s n xmpl."

        Examples:
            >>> import text_processing as tp
            >>> input_string1 = "This is an example."
            >>> tp.normalize(input_string1)
            "Ths s n xmpl."
            >>> input_string2 = "We love Python!"
            >>> tp.normalize(input_string2)
            ''W lv Pythn!'
    """
    no_vowel_string = None
    eliminate_string_list = ["a", "e", "i", "o", "u"]
    temp = input_string
    
    for i in eliminate_string_list:
        #print(f'{i}를 {temp.count(i)}번 제거합니다.')
        temp = temp.replace(i, "" ,temp.count(i))
        #print(temp)
    
    no_vowel_string = temp
    
    return no_vowel_string


'''
    ### test part

input_string1 = "This is an example."
input_string2 = "   EXTRA   SPACE   "
input_string3 = "We love Python!"

post_string = normalize(input_string2)

post_string2 = no_vowels(input_string3)

print(post_string)

print(post_string2)

'''
