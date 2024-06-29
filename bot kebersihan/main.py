import random
def get_fact(loop):
    list_sampah = []
    sampah = "**Trash Fact :**\n"
    fakta_sampah = [
    "Setiap tahunnya, dunia menghasilkan sekitar 2 miliar ton sampah.",
    "Lebih dari 8 juta ton plastik berakhir di lautan setiap tahun.",
    "Hanya sekitar 9% dari semua plastik yang pernah diproduksi telah didaur ulang.",
    "Sekitar 1 juta botol plastik dibeli setiap menit di seluruh dunia.",
    "Butuh hingga 1.000 tahun bagi plastik untuk terurai di lingkungan.",
    "Sampah makanan menyumbang sekitar 1/3 dari semua makanan yang diproduksi di dunia.",
    "Rata-rata orang Amerika menghasilkan sekitar 2 kilogram sampah per hari.",
    "Tiongkok adalah negara penghasil sampah terbesar di dunia, diikuti oleh Amerika Serikat.",
    "Setiap tahun, lebih dari 2 juta kantong plastik digunakan per menit di seluruh dunia.",
    "Rata-rata, orang Eropa menghasilkan sekitar 480 kilogram sampah per tahun.",
    "Sampah elektronik adalah jenis limbah yang paling cepat berkembang di dunia.",
    "Lebih dari 50 juta ton sampah elektronik dihasilkan setiap tahun di dunia.",
    "Kurang dari 20% dari sampah elektronik didaur ulang secara resmi.",
    "Kertas bisa didaur ulang hingga tujuh kali sebelum seratnya terlalu pendek untuk digunakan lagi.",
    "Pembuangan sampah yang tidak tepat dapat menyebabkan pencemaran tanah dan air.",
    "Setiap tahun, lebih dari 1 juta burung laut mati karena menelan plastik.",
    "Produksi plastik global mencapai lebih dari 300 juta ton per tahun.",
    "Bahan organik seperti daun dan rumput menghasilkan gas metana saat membusuk di tempat pembuangan sampah, yang merupakan gas rumah kaca yang kuat.",
    "Setiap tahun, orang Amerika membuang cukup kaleng aluminium untuk membangun kembali seluruh armada komersial udara Amerika.",
    "Pada tahun 2050, diperkirakan akan ada lebih banyak plastik daripada ikan di lautan (berdasarkan berat).",
    "Satu botol kaca dapat didaur ulang dan digunakan kembali tanpa batas tanpa kehilangan kualitas.",
    "Kompos bisa mengurangi sampah rumah tangga hingga 30%.",
    "Tumbuhan yang tumbuh di tanah yang terkontaminasi oleh sampah bisa menjadi beracun.",
    "Botol plastik bisa membutuhkan waktu hingga 450 tahun untuk terurai di lingkungan laut.",
    "Membuang sampah sembarangan adalah salah satu penyebab utama banjir di banyak kota.",
    "Industri fashion cepat adalah salah satu penghasil limbah terbesar, menghasilkan jutaan ton sampah tekstil setiap tahun.",
    "Limbah medis sering kali mengandung bahan kimia berbahaya yang dapat mencemari lingkungan.",
    "Di beberapa negara, tempat pembuangan sampah sudah kelebihan kapasitas dan mengancam kesehatan masyarakat.",
    "Daur ulang satu ton kertas bisa menghemat 17 pohon, 26.500 liter air, dan 4.100 kWh listrik.",
    "Satu ban mobil membutuhkan waktu sekitar 50-80 tahun untuk terurai sepenuhnya.",
    "Setiap tahun, orang Amerika membuang makanan senilai sekitar 165 miliar dolar AS.",
    "Limbah makanan menghasilkan gas metana, yang 25 kali lebih kuat dari karbon dioksida sebagai gas rumah kaca.",
    "Membuang baterai sembarangan bisa menyebabkan pencemaran logam berat seperti timbal dan merkuri.",
    "Lebih dari 60% dari semua sampah di tempat pembuangan sampah dapat didaur ulang.",
    "Komunitas yang berada dekat dengan tempat pembuangan sampah sering kali mengalami tingkat penyakit pernapasan yang lebih tinggi.",
    "Kantong plastik hanya digunakan rata-rata selama 12 menit sebelum dibuang.",
    "Produksi plastik membutuhkan sekitar 8% dari total produksi minyak global setiap tahun.",
    "Sebanyak 40% dari makanan yang diproduksi di Amerika Serikat berakhir di tempat sampah.",
    "Pembuangan sampah ke laut ilegal di banyak negara, tetapi tetap saja terjadi secara luas.",
    "Pengelolaan sampah yang buruk dapat meningkatkan risiko bencana alam seperti tanah longsor dan banjir.",
    "Satu kaleng aluminium yang didaur ulang bisa menghemat energi yang cukup untuk menyalakan televisi selama tiga jam.",
    "Lebih dari 80% dari semua sampah plastik di lautan berasal dari daratan.",
    "Proses daur ulang bisa menghemat energi dan sumber daya alam yang signifikan.",
    "Limbah elektronik mengandung logam berharga seperti emas, perak, dan tembaga yang bisa didaur ulang.",
    "Tempat pembuangan sampah adalah sumber utama emisi gas metana, salah satu gas rumah kaca paling berbahaya.",
    "Penggunaan kompos dari sampah organik bisa meningkatkan kesuburan tanah.",
    "Hanya sekitar 14% dari semua kemasan plastik yang digunakan di seluruh dunia didaur ulang.",
    "Setiap tahun, lebih dari 100.000 mamalia laut mati akibat polusi plastik di lautan.",
    "Setiap ton kertas yang didaur ulang dapat menghemat energi yang cukup untuk menjalankan rumah rata-rata selama enam bulan.",
    "Sampah yang tidak terkelola dengan baik dapat menyebarkan penyakit melalui tikus dan serangga yang berkeliaran di tempat pembuangan sampah."
]
    if loop <= 20:
        while len(list_sampah) < loop:
            a = random.choice(fakta_sampah)
            if a not in list_sampah:
                list_sampah.append(a)
            elif a in list_sampah:
                a = random.choice(fakta_sampah)
    else:
        return "Maksimal fakta yang dapat diberikan adalah 20"
             
    for i in range(len(list_sampah)):
        sampah += f"{i+1}. {list_sampah[i]}\n"
    return sampah
    

def get_contoh(jenis):

    jenis = jenis.lower()
    jenis = jenis.capitalize()

    sampah = f"**Berikut ini merupakan contoh sampah dari jenis sampah {jenis}:**\n"
    jenis_sampah = {
        "Organik": ["Kulit buah", "Sisa sayuran", "Daun gugur", "Rumput", "Kopi bekas", "Kulit telur", "Sisa makanan", "Batang sayuran", "Serbuk kayu", "Bunga layu"],
        "Anorganik": ["Botol plastik", "Kantong plastik", "Sedotan plastik", "Gelas plastik", "Kaleng soda", "Botol kaca", "Kertas koran", "CD/DVD bekas", "Ban bekas", "Styrofoam"],
        "B3": ["Pestisida", "Obat nyamuk", "Baterai bekas", "Cat tembok", "Pelumas mesin", "Cairan pembersih", "Produk kimia rumah tangga", "Thermometer merkuri", "Bahan bakar minyak", "Asam sulfat"]
    }

    if jenis in jenis_sampah:
        for i in range(len(jenis_sampah[jenis])):
            sampah += f"{i+1}. {jenis_sampah[jenis][i]}\n"
        return sampah
    else:
        return "Tidak ada jenis sampah tersebut"

def get_info(jenis):

    jenis = jenis.lower()
    jenis = jenis.capitalize()

    jenis_sampah = {
    "Organik": f"Sampah yang berasal dari bahan-bahan alami yang mudah terurai oleh mikroorganisme.\nContohnya adalah sisa makanan, daun, dan kulit buah.\n\n**Contoh lebih lengkap ada di $contoh {jenis}.**",
    "Anorganik": f"Sampah yang berasal dari bahan-bahan non-alami dan sulit terurai.\nContohnya adalah plastik, kaleng, kaca, dan kertas.\n\n**Contoh lebih lengkap ada di $contoh {jenis}.**",
    "B3": f"Sampah yang mengandung bahan berbahaya dan beracun yang dapat membahayakan kesehatan manusia dan lingkungan.\nContohnya adalah pestisida, baterai bekas, dan cat tembok.\n\n**Contoh lebih lengkap ada di $contoh {jenis}.**"
}
    if jenis in jenis_sampah:
        return f"**{jenis} :** {jenis_sampah[jenis]}"
    else:
        return "Tidak ada jenis sampah tersebut"

def get_tips(loop):
    list_sampah = []
    sampah = "**Green Tips :**\n"
    lingkungan = [
    "Kurangi penggunaan plastik sekali pakai",
    "Gunakan tas kain atau tas belanja yang dapat digunakan kembali",
    "Pisahkan sampah organik dan non-organik",
    "Daur ulang kertas, plastik, kaca, dan logam",
    "Matikan lampu dan alat elektronik saat tidak digunakan",
    "Gunakan lampu LED yang lebih hemat energi",
    "Jangan biarkan keran air mengalir saat menggosok gigi atau mencuci piring",
    "Periksa kebocoran di pipa atau keran",
    "Bersepeda, berjalan kaki, atau menggunakan transportasi umum",
    "Carpool dengan teman atau rekan kerja",
    "Tanam pohon dan tanaman di sekitar rumah",
    "Pilih produk yang memiliki label ramah lingkungan",
    "Gunakan produk yang menggunakan bahan daur ulang",
    "Hindari produk yang mengandung bahan kimia berbahaya",
    "Kurangi penggunaan kertas dengan beralih ke format digital",
    "Gunakan kedua sisi kertas jika harus mencetak",
    "Beli produk lokal untuk mengurangi jejak karbon",
    "Sebarkan kesadaran tentang pentingnya menjaga lingkungan",
    "Ajak teman, keluarga, dan komunitas untuk melakukan hal yang sama",
    "Hemat listrik dengan menggunakan alat yang efisien energi",
    "Kurangi pemakaian air dengan mandi singkat",
    "Gunakan shower hemat air",
    "Gunakan transportasi ramah lingkungan seperti mobil listrik",
    "Hindari pembakaran sampah yang bisa mencemari udara",
    "Daur ulang pakaian dan barang-barang bekas",
    "Gunakan produk pembersih ramah lingkungan",
    "Kumpulkan air hujan untuk menyiram tanaman",
    "Hemat penggunaan kertas dengan membaca buku atau koran digital",
    "Dukung organisasi yang bergerak dalam pelestarian lingkungan",
    "Ikuti kegiatan gotong royong membersihkan lingkungan"
]
    if loop <= 20 :
        while len(list_sampah) < loop:
            a = random.choice(lingkungan)
            if a not in list_sampah:
                list_sampah.append(a)
            elif a in list_sampah:
                a = random.choice(lingkungan)
    else:
        return "Maksimal tips yang dapat diberikan adalah 20"
             
    for i in range(len(list_sampah)):
        sampah += f"{i+1}. {list_sampah[i]}\n"
    return sampah
    
    
    
   

