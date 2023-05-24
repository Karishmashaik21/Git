def isAnagram(str1,str2):
    str1=input()
    str2=input()
    count=0
    if len(str1)==len(str2):
        for i in str1:
                if i in str2:
                    count+=1
        if count==len(str1):
            return "true"
        else:
            return "false"
    else:
        return "false"
str1=input()
str2=input()
print(isAnagram(str1,str2))