import time, random, math
def get_seconds():
    return time.localtime().tm_sec
def getListOfPrimes():
    list1 = []
    for i in range(2, 100):
        if i % 2 == 0:
            continue
        else:
            list1.append(i)
    print(list1)
    return list1
time_seconds = get_seconds()
print(time_seconds)
random_prime = random.choice(getListOfPrimes())
print(random_prime)
def getRandomNumber(n):
    # getRandomNumber()
   
    data_one = time_seconds * random_prime
    print(data_one)
    data_two = (data_one) / time.localtime().tm_yday
    print(data_two)
    str_data_two=str(data_two)
    str_arr_data_two=str_data_two.replace(".","")
    if((n>=10) and (n<=99)):
        print(random.choice(str_arr_data_two)+random.choice(str_arr_data_two))
    else:
         print(random.choice(str_arr_data_two))
    

getRandomNumber(50)
