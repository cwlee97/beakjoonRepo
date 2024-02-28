import sys

input = sys.stdin.readline

def getInput():
    cases = int(input())
    string_array = list()

    for _ in range(cases):
        string_array.append(input()[:-1])

    return string_array

def solution():
    res_dict = dict()
    res_array = list()
    for string in string_array:
        pushed = False
        word_array = string.split(" ")
        for word in word_array:
            if word[0].lower() not in res_dict.keys():
                res_dict[word[0].lower()] = string
                res_array.append(string[:string.find(word)]+"["+word[0]+"]"+string[string.find(word)+1:])
                pushed = True
                break
        if pushed == False:
            for char in string:
                if char != " " and char.lower() not in res_dict.keys():
                    res_dict[char.lower()] = string
                    res_array.append(string[:string.find(char)]+"["+char+"]"+string[string.find(char)+1:])
                    pushed = True
                    break
                               
        if pushed == False:
            res_array.append(string)
    
    for i in res_array:
        print(i)

if __name__ == "__main__":
    string_array = getInput()
    solution()