nama = "Kanaya Lintang Salsabila"
umur = 22
tanggal = "20 October 2024"
resi = 1485289
metode = "JNT"

print("Hello , my name : {0}, umur saya : {1}".format(nama,umur)) #0 dan 1 adalah posisi

#\n for enter, \t for tab, ls for list, cd untuk masuk file, pwd untuk kesebelumnya

#real case (kalau kepanjangan ke view lalu wrap text)
print("\nKepada Yth.\n{nama_penerima},\n\tDengan ini kami memberitahukan bahwa barang Anda telah dikirimkan pada tanggal {tanggal_pengiriman}\nBerikut adalah rincian pengiriman: \nNomor Resi: {nomor_resi} \nMetode Pengiriman: {metode_pengiriman} \n".format(nama_penerima = nama, tanggal_pengiriman = tanggal, nomor_resi= resi, metode_pengiriman = metode))
