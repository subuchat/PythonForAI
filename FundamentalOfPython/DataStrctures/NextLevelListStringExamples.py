import re # using for regular expression function in palindrome

def main():
    #print("Basic String Compression Using count of repeated char")
    #make_string_compression_wth_rptd_counter()
    print("Check if a string is aplindrome = ignoring space/special characte/ case")
    check_palindrome()

def return_only_alpha_numeric_string(lstOfChar):
    outStr = ""
    for ch in lstOfChar:
        if ch.isalnum(): # Check if its ALPHANUMERIC
            outStr += ch
    return outStr

def check_palindrome():
    input_string = input("Provide a string : ")
    #remove any spaces
    format_str = input_string.strip();
    '''
    # Replace any character that is NOT alphanumeric (\w) or whitespace (\s)
    clean_text = re.sub(r"[^\w\s]", "", format_str)
    reverse_str = clean_text[::-1]
    if clean_text == reverse_str:
        print("Its a palindrome")
    else:
        print("Its not a palindrome")
    '''
    # Now make list of all characters
    list_of_char = list(format_str)
    print(list_of_char)
    # Make next list removing all characters which are not alphanumeric
    plain_input_str = return_only_alpha_numeric_string(list_of_char).lower()
    print(f"Plain lower case input string is {plain_input_str}")
    reversed_str = plain_input_str[::-1]    
    if plain_input_str == reversed_str:
        print("Palindrom")
    else:
        print("Not a Palindrome")
    

       

def make_string_compression_wth_rptd_counter():
    # Taking Input
    s = input()

    # Write your code here
    result = s[0]
    repeat_count = 1
    non_rpt_const = '1'
    all_same = True
    else_traversed = False

    if len(s) > 1 :
        for index in range(1,len(s)):
            if s[index] == s[index-1]:
                repeat_count += 1
                all_same = True
                else_traversed = False
            else:
                all_same = False
                if( repeat_count > 1 ):
                    result = result + f'{repeat_count}' 
                elif else_traversed == True: # Just adding this for non-consecutive pattern
                    result += non_rpt_const
                result = result + s[index] 
                repeat_count = 1
                else_traversed = True
    else:
        result = s
        
    if all_same == True and repeat_count > 1 : # When string ending in same charater repetation and coming out
        result = result + f'{repeat_count}' 

    if else_traversed == True: # if loop ending in  non-consecutive pattern
        result += non_rpt_const

    if len(result) > len(s):
        result = s
    # Print the Output
    print(result)


if __name__ == "__main__":
    main()