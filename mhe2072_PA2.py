#Mohammed Edhi
#1001372072
#April,3,2019
#Windows10


def main():
    sub = '{'
    end = '}'
    q = '"'
    c= '//'
    cnt = 0    
    p=False
    with open ("data.txt", "r") as myfile, open("data.txt", "a") as outfile:        
        for line in myfile:         
            linecopy=line
            if c in line:#If the line has a comment
                    com=line.partition(c)[2] #every thing after //            
                    line=line.replace(com,'') #deleting everything after//
                    line=line.replace('//','')#deleting //
            for letter in line:              
                if p:#boolean for being in quotes
                    if q in letter: #searchig for end  "
                        p^=True  #toggles the boolean
                    continue #skip if inside "  "
                if sub in letter and c not in line: #if there is a opening bracket not in a comment
                    cnt+= 1
                elif end in letter and c not in line:    #if there is a closing bracket not in a comment
                    cnt-= 1
                elif q in letter: # toggle quotes boolean
                    p^=True
            print(str(cnt)+linecopy) # print Nesting depth 
if __name__ == '__main__':
        main()





