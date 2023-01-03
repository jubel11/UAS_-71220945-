print("----Kredit keaktifan Mahasiswa----")
print("student activities credit")
print("-------------")

# a = (input("masukkan nilai prestasi"))
# b = (input("masukkan nilai organisasi"))
# c = (input("masukkan nilai kepanitiaan"))
# d = (input("masukkan nilai rekognisi"))


# if : (a + b + c + d ==  ) 

# masukkan_kegiatan : ("")
# print (input("1.prestasi: "))
# print(input("2.organisasi: "))
# print(input("3.kepanititaan: "))
# print(input("4.rekognisi: "))
# print(input("masukkan Kategori kegiatan"))



name = input("masukkan nama anda")
pilih_kegiatan=(input("tentukan kegiatan"))
print (input("1. prestasi"))       
print (input("2. organisasi"))
print (input("3. kepantiaan"))  
print (input("4. rekognisi"))
# if (prestasi , organisasi , kepanitiaan , rekognisi ) :
#     pilih_prestasi == 1 
if  pilih_prestasi == 1 :
    prestasi = int(input("masukkan nilai prestasi"))
    # print ("jumlah nilai adalah",prestasi)
elif pilih_organisasi == 2 :
    organisasi = int(input("masukkan nilai organisasi"))
elif pilih_kepanitiaan == 3 :
    kepanitiaan = int(input("masukkan nilai kepanitiaan"))
elif pilih_rekognisi == 4 :
    rekognisi = int(input("masukkan nilai rekognisi"))
else :    
    print(input("masukkan nama mahasiswa : "))
