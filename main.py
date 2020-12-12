from random import randint


letters=[chr(i) for i in range(97,123)]
arr=[(index,item) for index,item in enumerate(letters)]
key=randint(2,5)


def ceasor_Cipher(text):
    '''
    Adding key into the text which will decide the encrption of your text
    '''
    Cipher_text,text=[],text.lower().split(" ")
    for i in text:
        nums=[]
        for j in i:
            for pos,letter in arr:
                if letter==j:
                    nums.append(pos+key)
        Cipher_text.append(nums)
    return encrpyt(Cipher_text)




def encrpyt(num):
    '''
    Converting the numbers into encrypted text
    '''
    enc_text=[]
    new=[]
    for i in num:
        corr=[]
        for j in i:
            if j>=26:
                j=abs(25-j+1)
            corr.append(j)
        new.append(tuple(corr))
    for grp in new:
        text=""
        for n in grp:
            for index,item in arr:
                if n==index:
                    text+=item
        enc_text.append(text)
    return " ".join(enc_text)   




print(ceasor_Cipher("My name is vijay")) 