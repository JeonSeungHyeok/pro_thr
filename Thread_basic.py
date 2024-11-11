N, M = map(int, input().split())
string = input()

i = 0
while True:
    if string=="":
        break
    print(f"string[{i}] : "+string)
    input()
    if string[i:i+M]==string[i]*M:
        tmp=string[i]
        while string[i:i+1]==tmp:
            string = string[:i]+string[i+1:]
            print(string)
            input()
        i=0
        continue
    elif i==len(string)-M:
        break
    i+=1

if string=="":
    print("CLEAR!")
else:
    print(string)