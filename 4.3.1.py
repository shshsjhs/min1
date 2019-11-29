while True:
    try:
        target =int(input())
        list = input()
        list = list.split(" ")
        flag = 0
        for index, value in enumerate(list):
            list[index] = int(value)
        for index,value in  enumerate(list):
            for index_1, value_1 in  enumerate(list):
                if ((value + value_1)==target and index != index_1):
                    print(index, index_1)
                    flag = 1
                    break
            if (flag == 1):
                break
    except:
        break