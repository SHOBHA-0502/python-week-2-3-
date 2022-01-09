def count_substring(string, sub_string):
    
    
    def count_substring(string, sub_string):
        fat = 0
        for i in range(len(string)):
            if string[i:].startswith(sub_string):
                print(string[i])
                fat += 1
    
        

            
    
    


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)