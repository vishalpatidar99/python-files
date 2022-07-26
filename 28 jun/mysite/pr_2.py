{
    1: ''' input = [['str1','str1'],['str2'],['str3','str3']]  [1,2,3]

           output = [[['str1',1],['str1',1]],[['str2',2]],[['str3',3],['str3',3]]]
        ''' ,

    2: ''' input  s='aabbdeeefaa'

           output = 'a2b2d1e3f1a2'
        ''', 

    3: ''' replace first two letter with it's third consecutive letter [in only(a,b,c)]
        ex. input s='abcabc'
        first two letter of string a and b will replace c
        this will solve in this pattern
        s = 'ccabc'
        s = 'cbbc'
        s = 'abc'
        s = 'cc'
        then ouput will be 'cc'
        ''',
    
    4: '''pattern
        n=5
        ABCDE
        ZYXW
        ABC
        ZY
        A
        ''',
    
    5: '''pattern
        1 2 3 4 5
        16      6
        15      7
        14      8
        131211109
        ''',
    
    6: '''Ques3- There is a school trip and you and your friend also join the school trip and school management 
                    book a hotel for you guys to stay. The hotel has a 10-floor building and in each floor, there is 10 room 
                   and their no. are like 1 floor have “1-10” ,2nd floor “11 20”. You got an urgent call from your close friend 
                    parent. So your simple task is to find out how many floor you have to travel to reach your friend so he 
                    can talk to their parent. 
                        Input= 4 

                                    1 100 
                                    42 50 
                                    53 30 
                                    81 80 
                                    
                        Output=  
                                    9 
                                    0 
                                    3 
                                    1
        ''',
    
    7: '''Ques4= A and B were playing a game with coins. If B has more coins then he is winning, otherwise A is 
                    winning. Note that this means if both A and B have the same number of coins, then A is winning. 
                    Initially A has a coins while B has b coins. Then C came and gave his c coins to the player who is not 
                    winning currently, after which D came and repeated the same process (gave his d coins to the player who 
                    is not winning currently). 
                    Find the final winner of the game. 
                    Input = 
                            <a b c d> 
                            3 
                            2 3 4 5 
                            3 3 3 3 
                            2 3 1 2 

                    Output=  
                            B Win 
                            A win
                            B Win 
 
        ''',

    8: '''Write a Python program to find the first repeated word in a given string.
                Ex. s='Ram is good boy, Ram is friend of shyam'
                output = 'Ram'
        ''',

    9: '''Write a Python program to read a square matrix from console and print the diffrence of sum of matrix diagonal. Accept the size of the square matrix and elements for each column separated with a space (for every row) as input from the user
            Ex. Input the size of the matrix: 3
                            2 3 4
                            4 5 6
                            3 4 7

                            Sum of matrix primary diagonal: 2+5+7 = 14
                            Sum of matrix secondary diagonal: 4+5+3 = 12
                            output: 14-12 = 2
        ''',

    10: '''Write a Python program to Zip two given lists of lists. 
                            Original lists:
                            [[1, 3], [5, 7], [9, 11]]
                            [[2, 4], [6, 8], [10, 12, 14]]
                            Zipped list:
                            [[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]
        ''',

    11: '''Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. 
            Sample data : {'1':['a','b'], '2':['c','d']}
            Expected Output:
                                ac
                                ad
                                bc
                                bd    
         ''',

    12: '''Write a Python program to combine values in python list of dictionaries. 
        Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
            Expected Output: Counter({'item1': 1150, 'item2': 300})   
         ''',

    13: ''' Write a Python program to create a dictionary from a string.
                    Note: Track the count of the letters from the string.
                    Sample string : 'w3resource'
                    Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}  
         ''',

    13: ''' Write a Python program to create a dictionary from a string.
                    Note: Track the count of the letters from the string.
                    Sample string : 'w3resource'
                    Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}  
         ''',

    14: ''' Write a Python program to get the top three items in a shop. 
                    Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
                    Expected Output:
                    item4 55
                    item1 45.5
                    item3 41.3 
         ''',

    15: ''' Write a Python program to convert a list of multiple integers into a single integer.
                    Sample list: [11, 33, 50]
                    Expected Output: 113350 
         ''',
}