import random
def makeDist_generate(banyak_data):
    list_data = []
    for i in range(banyak_data):
        nilai_acak= (random.randint(1,100)) # bisa juga langsung ditulis singkat gini: list_data.append(random.randint(1,100)) tanpa tulis nilai_acak
        list_data.append(nilai_acak)
    return list_data

def bubble_short(data):
    n = len(data) # len itu function untuk mengukur banyak data dalam list atau karakter

    for i in range(n):
        for j in range(0,n-i-1):
            if data[j] > data [j+1]:
                # temporary or temp = data [j]
                # data [j] = data [j+1]
                # data [j+1] = temporary or temp
                data [j], data[j+1] = data[j+1],data[j]


value = int(input("Banyak data yang akan di looping : "))
list_data = makeDist_generate(value)
print("List data sebelum diurutkan: ")
print(list_data)
print("\nList data setelah diurutkan: ")
bubble_short(list_data)
print(list_data)