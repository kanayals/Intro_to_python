#Int
# (pagar) untuk komentar
x = 1 # integer
print("ini contoh integer : {0} ".format(x))
f = 10.5 #float
print("ini contoh nilai desimal : {0} ".format(f))
z = 2 + 3j #complex
print("ini contoh tipe data kompleks : {0} ".format(z))

#Sqyence Type
a = [1,2,3] #list : nilainya harus sama dan boleh diubah
print(a)
b = (4,5,6) #truple : nilainya tidak bisa diubah
print(b)
c = range(0,5) #range
print(c)

#Type Text
d = "hello , world!" #string (str)

#Mapping Type
e = {"nama" : "Kanaya Lintang Salsabila" , "age" : 22} #dictionary (dic)

#Set Type
f = {1,2,3} #set
g = frozenset({4,5,6}) #frozen set, it could be g = frozenset(f)

#Boolean type (kondisi)
h = True; #bool (True(1), False(0));
#binary Type 
i = b"Hello" #bytes
print(i)
j = bytearray(5) #bytearray, it also could be j = bytearray(f) or f could be change by 3,4,5,etc.
print(j)
k = memoryview(bytes(5)) #memoryview
print(k)

