<<<<<<< HEAD
Userin = input("Enter the statement: ")
#Userin ="Test1 test2 test3 coded and tested test test"
=======
#Userin = input("Enter the statement: ")
Userin ="Testing the program for character and word manipulation. This is a test statement for testing purposes"
>>>>>>> ramp_up_python/master
print("The Total number of characters in the statement: ",len(Userin))
Userin=Userin.lower()
lC = Userin.lower()
def t1():
    dup=""
    dupchar=""
    for i in lC:
        if i not in dup:
                dup=dup+i
        else:
            if i not in dupchar:
                dupchar+=i
    count_dup=len(lC)-len(dup)
    print(f"Duplicates in the Statement are: {dupchar}")
    print(f"The Total number of duplicates in the statement:{count_dup}")

#task2
def t2():
    # Userin = input("enter the characters")
    words = Userin.split()
    Words_count = len(words)
    print(f"No of words in the given Statement is: {Words_count}")

#task3
def t3():
    words = Userin.split()
    Dup = []
    Dup_words = []
    for i in words:
        if i not in Dup:
            Dup.append(i)
        else:
            if i not in Dup_words:
                Dup_words.append(i)
    #print(Dup_words)
    Words_count = len(Dup_words)
<<<<<<< HEAD
    print(f"No of Duplicate words in the given Statement: {Words_count}")
=======
    print(f"No of words in the given input is: {Words_count}")
>>>>>>> ramp_up_python/master
#task4
def t4():
    reversed_char = Userin[::-1]
    print(f"The Statement after reversing the characters: {reversed_char}")
#task5
def t5():
    Words = Userin.split()
    revers = Words[::-1]
    reverss = " ".join(revers)
    # print(Words)
    print(f"The statement after the reversing the order of the words: {reverss}")
<<<<<<< HEAD
#task6 To romve the dups
    dup = ""
    dupchar = ""
    for i in reverss:
=======
#task6
def t6():
    dup = ""
    dupchar = ""
    for i in Userin:
>>>>>>> ramp_up_python/master
        if i not in dup:
            dup = dup + i
        else:
            if i not in dupchar:
                dupchar += i
    count_dup = len(lC) - len(dup)
    #print(dupchar)
    print(f"The latest statment after remove the the duplicates char from statement: {dup}")
<<<<<<< HEAD
def main():
    t1()
    t2()
    t3()
    t4()
    t5()


main()
=======
t1()
t2()
t3()
t4()
t5()
t6()
>>>>>>> ramp_up_python/master
