import math

def order(list):
    
    for i in range(1, len(list)):

        current = list[i]
        position = i

        while position > 0 and list[position-1] > current:
            list[position] = new_list[position-1]
            position = position-1

        list[position] = current

def mean(list):

    acum = 0
    for i in list:
        acum += i

    return acum / len(list)

def median(list):

    order(list)
    med = (len(list) + 1) / 2

    if med % 1 == 0.5:
        return (list[int(med-0.5)] + list[int(med+0.5)]) / 2
    else:
        return list[int(med-0.5)]

def mode(list):
    
    max_count, max_val = 0, 0
    order(list)

    for i in range(len(list)):
        count = 0
        for j in range(len(list)):
            if list[j] == list[i]:
                count += 1
        if count > max_count:
            max_count = count
            max_val = list[i]
    return max_val

def max_min(list):
    
    order(list)
    return [list[0], list[-1]]

def variance(list):

    avrg = mean(list)
    add = 0

    for i in range(len(list)):
        add = add + ((list[i]-avrg) ** 2)

    return add / len(list)

def standard_dev(list):

    return math.sqrt(variance(list))

def frecuency_distribution(list):

    order(list)



def main():
    new_list = [1, 2, 3, 4, 5, 6, 5, 2, 3, 1, 4, 2, 6, 2, 1, 3, 5, 4, 4, 3, 2]
    print(new_list)
    print(mean(new_list))
    print(median(new_list))
    print(mode(new_list))
    print(max_min(new_list))
    print(variance(new_list))
    print(standard_dev(new_list))

    order(new_list)
    print(new_list)
