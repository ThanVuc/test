def dv_10(i):
    if i%3==1:
        ch=''
    elif i%3==2:
        ch='muoi'
    elif i%3==0:
        ch='tram'
    if i<4:
        return ch
    elif i<7:
        return ch+' nghin'
    elif i<10:
        return ch+' trieu'
def dv_khac(i):
    dv=i%10
    ti=int(i/10)
    s=''
    while ti!=0:
        ti-=1
        s=s+'ti'
    s=dv_10(dv)+s
    return s
def trans(ch):
    s=''
    if (ch=='1'):
        s='Mot'
    elif (ch=='2'):
        s='Hai'
    elif (ch=='3'):
        s='Ba'
    elif (ch=='4'):
        s='Bon'
    elif (ch=='5'):
        s='Nam'
    elif (ch=='6'):
        s='Sau'
    elif (ch=='7'):
        s='Bay'
    elif (ch=='8'):
        s='Tam'
    elif (ch=='9'):
        s='Chin'
    elif (ch=='0'):
        s='Khong'
    return s

n = int(input('Nhap n= '))
i=0; s=''
print(chr(48))
ok= False
while n!=0:
    i+=1
    tmp=n%10
    n=int(n/10)
    ch= chr(tmp+48)
    if i<10:
        s=trans(ch)+' '+dv_10(i)+' '+s
    else:
        s=trans(ch)+' '+dv_khac(i)+' '+s
print(s)
#update