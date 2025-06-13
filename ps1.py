
# Problem -1 # checking number of vowels
def problem1():
    s = "azcbobobegghakl" # string of lower case characters

    list_vowels = ["a","e","i","o","u"]
    num_vowels = 0


    for i in s:
        if i in list_vowels:
            num_vowels +=1

    print("Number of vowels: ",num_vowels)

#Problem-2 #  number of occurances of a string
def problem2():
    s = "azcbobobobgghakl" # string of lower case characters
    num_bob = 0
    num_exception = 0
    for i in range(len(s)):
        try:
            if s[i:i+3] == "bob":
                num_bob +=1
        except Exception as e:
            print("Exception hit:",e)
            num_exception +=1
        else:
            #print("Test")
            pass
    print("Number of times bob occurs: ",num_bob)
    print("Number of times exception hit:",num_exception)

# Problem -3: # longest substring
def problem3():
    s = 'abcbcd'
    sub_string= ""
    lexical_order = "abcdefghijklmnopqrstuvwxyz"
    dict_substrings = {}
    run_count = 0
    for i in range(len(s)):
        try:
            if lexical_order.index(s[i]) <= lexical_order.index(s[i+1]):# the next letter is above the current one; 
                
                print(s[i])
                print(s[i+1])
                if len(sub_string) != 0: # string has something; add only the next character you encounter
                    sub_string +=s[i+1] # the index() method is the error, when there are multiple instances of the same character, it returns the index of the first one.
                else: # string is empty, add both the characters
                    sub_string +=s[i]
                    sub_string +=s[i+1]
                
            else: # if the current on is above the next one;
                if len(sub_string)!= 0:# just to add fruitful substrings to dict
                    dict_substrings[(len(dict_substrings)+1)] = sub_string # adding substring as a key value pair
                    sub_string = "" # we have to reset for new checks

        except Exception as e: # if the last character was the one that was checked; we have to close and add the substring to dict;
            print(f"At position {i}, with the character {s[i]}, the exception {e} has been thrown.")
            dict_substrings[(len(dict_substrings)+1)] = sub_string # adding substring as a key value pair
            sub_string = "" # we have to reset for new checks
        run_count +=1

    # print out the longest substring 
    list_substrings = list(dict_substrings.values())
    largest_substring = max(list_substrings,key=len)
    print("Longest substring in alphabetical order is:",largest_substring)
    print(dict_substrings)

def problem3_v2():
    s = 'azcbobobegghakl'
    sub_string= ""
    lexical_order = "abcdefghijklmnopqrstuvwxyz"
    dict_substrings = {}
    def check_continuity(i,a,b):
                """
                returns true if the next letter is lexicographically above the current one
                in case of an error, an exception is printed and special type None is returned"""
                try:
                    if b.index(i) < b.index(a[a.index(i)+1]):
                        return True
                    else:
                        return False
                except Exception as e:
                    print(e)
                    return False
    for i in s:
        if check_continuity(i,s,lexical_order):
            sub_string +=i
        else: # not in order; or last one checking; save and reset sub_string
            dict_substrings[(len(dict_substrings)+1)] = sub_string # adding substring as a key value pair
            sub_string = "" # resetting

    # print out the longest substring 
    list_substrings = list(dict_substrings.values())
    largest_substring = max(list_substrings,key=len)
    print(dict_substrings)
    print("Longest substring in alphabetical order is:",largest_substring)
    

if __name__ == "__main__":
    problem3()
    """print("testing:")
    s = 'azcbobobegghakl'
    sub_string= ""
    lexical_order = "abcdefghijklmnopqrstuvwxyz"
    dict_substrings = {}

    for i in s:
        try:
            if lexical_order.index(i) < lexical_order.index(s[s.index(i)+1]):

        except Exception as e:
            print(e,"has occured")"""
    
            