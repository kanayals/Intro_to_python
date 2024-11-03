nilai_rapot = 10
#if
#if (kondisi yang dimau)
print("========  If  ========")
if nilai_rapot > 5:
    print("Wah nilai saya bagus nih!")

print("\n========  If Else  ========")
#ifelse
#petik satu itu artinya char karakter
#petik dua itu artinya string
#char nama [12] itu artinya panjang variable nama max 12 karakter
#char nama [12] berubah menjadi char nama [255] === string

#java (ex)
#if (nilai_rapot == "A" ){
#    print("Selamat kamu lulus ujian ini!");
#}
#else{
#    print("Kamu harus remedial lagi!!!");
#}

nilai_rapot = "F"
if nilai_rapot == "A" :
    print("Selamat kamu lulus ujian ini!")
else:
    print("Kamu harus remedial lagi!!!!")

#if elif else
#tipsnya pikirkan yang salah
print("\n========  if Elfi Else (If Nested / if Bersarang)  ========")
nilai_rapot = 'C'
if nilai_rapot == 'A' :
    print("Selamat kamu lulus ujian dengan nilai yang sempurna!")
elif nilai_rapot == 'B':
    print("Selamat kamu lulus ujian dengan nilai hampir sempurna, belajar sedikit lagi yaa!")
elif nilai_rapot == 'C':
    print("Selamat kamu lulus ujian dengan nilai yang pas, harus belajar lebih giat yaa!!") 
else:
    print("Sana kamu harus remedial ujian!!")  

#Ternary
print("\n========  Ternary  ========")
a = 10
b = 12
bandingkan = "Posisi A Menang" if a > b else "Posisi B Menang"
print(bandingkan)