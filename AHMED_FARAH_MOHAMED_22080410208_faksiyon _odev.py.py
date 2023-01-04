sinav_sonuc = {'isimler':['Ayse k' , 'ahmet m', 'nuri c', 'nawar t','suzan t', 'ala B' ],
'cinsiyet' : ['k', 'e', 'e','e','k','k'],
'matematik': [80, 60, 77, 25,36,75],
'türkçe': [90, 50, 53, 100, 98, 66],
}
c=[]
b=[]
count_k =0
count_e=0
k_math =0
e_math =0
k_tur=0
e_tur=0
for i in range(len(sinav_sonuc["cinsiyet"])):
    if sinav_sonuc['cinsiyet' ][i] == "k" :
        count_k+=1
        k_math = k_math + sinav_sonuc['matematik'][i]
        k_tur = k_tur + sinav_sonuc['türkçe'][i]
        c.append(sinav_sonuc['türkçe'][i])
    else:
        count_e += 1
        e_math = e_math + sinav_sonuc['matematik'][i]
        e_tur = e_tur + sinav_sonuc['türkçe'][i]
        b.append(sinav_sonuc['türkçe'][i])
x = ((k_tur + e_tur)/(count_k + count_e))
print(f"kadinlarin matematik ortalmasi:{k_math/count_k}\n\
erkeklerin matematik ortalamsi:{e_math/count_e}\n\
sinav_sonuc ortalamasi:{x}")
print("kadinlerin en yuksek türkçe notu:",max(c))
print("erkeklerin en yuksek türkçe notu:",max(b))
