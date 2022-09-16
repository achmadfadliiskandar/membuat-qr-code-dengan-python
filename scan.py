import qrcode
# ok saya jelasin dah sebenarnya ini kerjaan gabut saya
# dan saya ingin menambah pengalaman dan ilmu juga
# input dulu apa yang mau dimasukin dan dijadiin qr-generator
link = input("Masukan Link Nya ya : ")
nama = input("Masukin Nama ya: ")
# kondisi supaya tidak ada yang mengosongkan isinya
if link == "" or nama == "":
    print('kosong')
else:
    # fungsi make untuk membuat dari hasil inputan yang kita taro dari 
    link = qrcode.make(link)
    # hasilnya jadi qr generator dengan nama
    link.save(nama+'.'+'png')
    # kalau mau aman kasih waktu aja biar nggak bentrok