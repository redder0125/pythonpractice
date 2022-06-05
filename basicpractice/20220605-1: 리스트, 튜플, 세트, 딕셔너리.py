print ("Hello, world!")

#List, 대괄호를 이용한다
your_list = ["바둑","오목","알까기"]

#값 찾아내기(단수)
print (your_list[0])
print (your_list[1])
print (your_list[2])

#Tuple, 소괄호를 이용한다
your_tuple = ("장기","쇼기","체스") #문맥상 느그 튜플이라고 해석하지는 않는다.

#값 찾아내기(복수)
print (your_tuple[0:2])

#포함 여부 확인
print ("바둑" in your_tuple)
print ("체스" in your_tuple)

#길이 확인
print (len(your_tuple))

#Set, 중괄호를 이용한다
your_set = {"스도쿠", "카쿠라스", "피크로스"}

#Dictionary, 중괄호와 콜론을 이용한다
your_dictionary = {
    "key":"value", #key는 중복되면 안 된다.
    "김레더":"물리법사 해파리",
    "지존":"조세",
    "오늘안할거":your_list
    }
print (your_dictionary["key"])
print (your_dictionary["김레더"])
