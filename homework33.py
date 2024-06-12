from random import random

def random_lists():
    # number = random()
    my_list1 = []
    my_list2 = []
    
    for i in range(5):
        my_list1.append(round(random()*10)) 
        my_list2.append(round(random()*10)) 

    my_list3 = my_list1+my_list2
    my_list4 = list(set(my_list3))
    
    my_list5 = []
    i = 0
    while i < len(my_list1):
        if my_list1[i] in my_list2 and my_list1[i] not in my_list5:
            my_list5.append(my_list1[i])
        i+=1
        
    my_list6 = list(set(my_list1)) + list(set(my_list2))
    
    my_list7 = max(my_list1), min(my_list1), max(my_list2), min(my_list2)
    my_list7 = list(my_list7)
        
    print(my_list1)
    print(my_list2)
    print(my_list3)
    print(my_list4)
    print(my_list5)
    print(my_list6)
    print(my_list7)
    
    
random_lists()