from app.app import db, app
from app.models.injury_classes import InjuryClass

def seed_injuries():
    injuries_data = [
        {
            'name': 'Abrasions',
            'handling': '''
                Luka lecet adalah luka ringan yang terjadi ketika lapisan atas kulit tergores atau terkelupas. Biasanya terjadi akibat gesekan atau kecelakaan kecil.
                1. Pastikan tangan sudah bersih sebelum merawat luka
                2. Bersihkan area luka dengan air yang mengalir atau air saline (hindari menggunakan alkohol atau iodine langsung di luka)
                3. Jika ada oleskan salep luka/petroleum jelly pada luka
                4. Tutuplah luka dengan kasa steril atau plester
                5. Pastikan untuk mengganti kasa steril minimal sehari sekali

                Sumber:
                - https://www.alodokter.com/pertolongan-pertama-merawat-luka-lecet 
                - https://www.ncbi.nlm.nih.gov/books/NBK554465/ 
            '''
        },
        {
            'name': 'Bruises',
            'handling': '''
                Memar terjadi ketika pembuluh darah kecil di bawah kulit pecah akibat benturan atau pukulan, menyebabkan perubahan warna pada kulit.
                1. Istirahatkan bagian tubuh yang mengalami luka memar
                2. Kompres area luka dengan beberapa es batu yang dibungkus kain selama 15-20 menit
                3. Tinggikan bagian tubuh yang terluka hingga berada di atas jantung 
                4. Jika area memar membengkak balut dengan elastic bandage
                5. Apabila luka memar belum hilang, setelah dua hari Anda dapat menggunakan kompres hangat
                6. Gunakan handuk hangat untuk emngompres area luka selama 10 menit

                Sumber:
                - https://www.alodokter.com/alami-luka-memar-ini-pertolongannya 
                - https://www.webmd.com/skin-problems-and-treatments/bruises-article 
                - https://medlineplus.gov/ency/article/007213.htm
            '''
        },
        {
            'name': 'Burns',
            'handling': '''
                Luka bakar adalah kerusakan pada kulit yang disebabkan oleh panas, api, uap, atau bahan kimia. Luka bakar dapat dibagi menjadi tingkat ringan (derajat satu), sedang (derajat dua), dan berat (derajat tiga).
                1. Aliri luka dengan air mengalir selama 15 menit (jangan menggunakan air es)
                2. Oleskan salep bioplacenton atau petroleum jelly pada permukaan luka (hindari penggunaan pasta gigi pada luka)
                3. Balut permukaan luka menggunakan kasa steril dengan balutan longgar untuk melindungi luka

                Sumber:
                - https://www.halodoc.com/artikel/ini-cara-menangani-luka-bakar-berdasarkan-tingkat-keparahannya?srsltid=AfmBOopuuDTCTyrFi0kbGsnGjCDJHB1WWTbyXz6Zd5lPBOnnbAbHQt6B 
                - https://www.siloamhospitals.com/en/informasi-siloam/artikel/pertolongan-pertama-pada-luka-bakar 
            '''
        },
        {
            'name': 'First Degree Burns',
            'handling': '''
                Luka bakar adalah kerusakan pada kulit yang disebabkan oleh panas, api, uap, atau bahan kimia. Luka bakar dapat dibagi menjadi tingkat ringan (derajat satu), sedang (derajat dua), dan berat (derajat tiga).
                1. Aliri luka dengan air mengalir selama 15 menit (jangan menggunakan air es)
                2. Oleskan salep bioplacenton atau petroleum jelly pada permukaan luka (hindari penggunaan pasta gigi pada luka)
                3. Balut permukaan luka menggunakan kasa steril dengan balutan longgar untuk melindungi luka

                Sumber:
                - https://www.halodoc.com/artikel/ini-cara-menangani-luka-bakar-berdasarkan-tingkat-keparahannya?srsltid=AfmBOopuuDTCTyrFi0kbGsnGjCDJHB1WWTbyXz6Zd5lPBOnnbAbHQt6B 
                - https://www.siloamhospitals.com/en/informasi-siloam/artikel/pertolongan-pertama-pada-luka-bakar 
            '''
        },
        {
            'name': 'Second Degree Burns',
            'handling': '''
                Luka bakar adalah kerusakan pada kulit yang disebabkan oleh panas, api, uap, atau bahan kimia. Luka bakar dapat dibagi menjadi tingkat ringan (derajat satu), sedang (derajat dua), dan berat (derajat tiga).
                1. Lepaskan aksesoris di bagian tubuh yang mengalami luka bakar, tetapi jangan lepas apapun yang sudah menempel pada kulit yang terbakar
                2. Aliri luka bakar dengan air mengalir selama 15 menit (jangan gunakan air es)
                3. Jika ada bagian yang melepuh, hindari memecahkan lepuhan karena beresiko terkena infeksi
                4. Apabila luka bakar cukup luas atau muncul tanda-tanda infeksi (bengkak dan timbul nanah) segera periksakan diri ke rumah sakit.

                Sumber:
                - https://www.nhs.uk/conditions/burns-and-scalds/#:~:text=Treating%20burns%20and%20scalds&text=cool%20the%20burn%20with%20cool,it%20against%20the%20burnt%20area 
                - https://www.alodokter.com/wajib-tahu-pertolongan-pertama-pada-luka-bakar-untuk-selamatkan-nyawa
            '''
        },
        {
            'name': 'Third Degree Burns',
            'handling': '''
                Luka bakar adalah kerusakan pada kulit yang disebabkan oleh panas, api, uap, atau bahan kimia. Luka bakar dapat dibagi menjadi tingkat ringan (derajat satu), sedang (derajat dua), dan berat (derajat tiga).
                1. Lepaskan aksesoris di bagian tubuh yang mengalami luka bakar, tetapi jangan lepas apapun yang sudah menempel pada kulit yang terbakar
                2. Hindari mengoleskan luka dengan salep ataupun mengaliri luka bakar dengan air
                3. Balut area luka bakar dengan kasa steril secara longgar
                4. Bawa segera ke rumah sakit untuk mendapatkan perawatan lebih lanjut

                Sumber:
                - https://www.halodoc.com/artikel/ini-cara-menangani-luka-bakar-berdasarkan-tingkat-keparahannya?srsltid=AfmBOopuuDTCTyrFi0kbGsnGjCDJHB1WWTbyXz6Zd5lPBOnnbAbHQt6B 
                - https://www.siloamhospitals.com/en/informasi-siloam/artikel/pertolongan-pertama-pada-luka-bakar 
            '''
        },
        {
            'name': 'Cut',
            'handling': '''
                Luka sayat terjadi ketika kulit terpotong oleh benda tajam. Luka ini bisa dangkal atau dalam, tergantung pada kedalaman potongan.
                1. Pastikan tangan sudah bersih sebelum merawat luka
                2. Bersihkan area luka dengan air yang mengalir atau air saline (hindari menggunakan alkohol atau iodine langsung di luka)
                3. Tekan luka dengan kain bersih atau kasa steril, dan posisikan bagian tubuh yang terluka lebih tinggi daripada dada untuk mengontrol perdarahan dan pembengkakan.
                4. Jika luka cukup besar, tutup dengan kasa steril dan perban. Sedangkan untuk luka yang kecil, biarkan saja terbuka hingga sembuh dengan sendirinya.

                Sumber:
                - https://www.alodokter.com/luka-sayatan-ditangani-sendiri-atau-harus-oleh-dokter 
                - https://www.mayoclinic.org/first-aid/first-aid-cuts/basics/art-20056711 
            '''
        },
        {
            'name': 'Ingrown_nails',
            'handling': '''
                Kuku tumbuh ke dalam terjadi ketika ujung kuku menembus kulit di sekitar kuku, menyebabkan rasa sakit, peradangan, dan infeksi.
                1. Rendam kaki yang mengalami cantengan dengan air hangat selama 15-20 menit sebanyak 3-4 kali sehari
                2. Pastikan untuk menjaga kaki selalu kering
                3. Gunakan alas kaki yang nyaman dan memiliki cukup ruang untuk jari kaki
                4. Oleskan salep antibiotik seperti gentamicin pada jari yang mengalami cantengan untuk mencegah infeksi
                5. Perhatikan tanda-tanda infeksi. Jika ada demam, pembengkakan atau keluar nanah dari luka tersebut harap segera ke rumah sakit

                Sumber:
                - https://www.alodokter.com/inilah-cara-mengobati-kuku-cantenga
                - https://www.ncbi.nlm.nih.gov/books/NBK546697
            '''
        },
        {
            'name': 'Laceration',
            'handling': '''
                Luka robek terjadi ketika kulit robek atau sobek akibat benda tajam atau kecelakaan. Luka ini biasanya lebih dalam dibandingkan dengan luka sayat.
                1. Pastikan tangan sudah bersih sebelum merawat luka
                2. Kontrol perdarahan dengan beri tekanan langsung pada luka dengan menggunakan kasa steril/kain bersih sambil mengangkat area yang terluka hingga posisinya di atas jantung
                3. Balut dan tutup luka menggunakan kasa steril
                4. Bawa ke rumah sakit untuk mendapatkan perawatan lebih lanjut

                Sumber:
                - https://www.verywellhealth.com/how-to-treat-a-laceration-1298916 
                - https://hellosehat.com/hidup-sehat/pertolongan-pertama/vulnus-laceratum/ 
            '''
        },
        {
            'name': 'Stab_wound',
            'handling': '''
                Luka tusuk terjadi ketika benda tajam menembus kulit dan jaringan tubuh lainnya, sering kali lebih dalam dan dapat merusak organ dalam.
                1. Pastikan tangan sudah bersih sebelum merawat luka
                2. Kontrol perdarahan dengan beri tekanan langsung pada luka dengan menggunakan kasa steril/kain bersih sambil mengangkat area yang terluka hingga posisinya di atas jantung
                3. Saat perdarahan sudah berhenti bersihkan luka dengan air mengalir
                4. Balut dan tutup luka menggunakan kasa steril dan plester
                5. Pastikan untuk mengganti kasa steril minimal sehari sekali
                6. Minum obat pereda nyeri jika dibutuhkan
                7. Perhatikan tanda-tanda infeksi. Jika ada demam, pembengkakan atau keluar nanah dari luka tersebut harap segera ke rumah sakit

                Sumber:
                - https://www.alodokter.com/bahaya-luka-tusuk-dan-pertolongan-yang-perlu-dilakukan 
                - https://www.verywellhealth.com/puncture-wounds-8383991
            '''
        }
    ]

    with app.app_context():
        db.session.query(InjuryClass).delete()
        for injury_data in injuries_data:
            injury = InjuryClass.query.filter_by(class_name=injury_data['name']).first()
            if not injury:
                injury = InjuryClass(class_name=injury_data['name'], treatment=injury_data['handling'])
                db.session.add(injury)

        db.session.commit()
        print("Injuries and handling steps have been seeded.")
