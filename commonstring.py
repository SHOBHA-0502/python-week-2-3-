def count_substring(string, sub_string):
    count =0 
    for i in range(0,len(string)):
        for j in range(0,len(sub_string)):
            if(string[i]==sub_string[j]):
                string = string.replace(string[i], "9")
                
                count+=1
    print(count)
                # string[i] = "4"
            
    
    return

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)