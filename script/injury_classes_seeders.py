from app.app import db, app
from app.models.injury_classes import InjuryClass

def seed_injuries():
    injuries_data = [
        {
            'name': 'Abrasions',
            'handling': '''
                Luka lecet adalah luka ringan yang terjadi ketika lapisan atas kulit tergores atau terkelupas. Biasanya terjadi akibat gesekan atau kecelakaan kecil.
                - Cuci luka dengan air bersih dan sabun ringan untuk menghilangkan kotoran.
                - Keringkan luka dengan lembut menggunakan kain bersih.
                - Oleskan salep antibiotik untuk mencegah infeksi.
                - Tutup luka dengan perban atau kasa steril untuk melindunginya dari kuman.
                - Gantilah perban setiap hari dan perhatikan tanda-tanda infeksi seperti kemerahan atau nanah.
            '''
        },
        {
            'name': 'Bruises',
            'handling': '''
                Memar terjadi ketika pembuluh darah kecil di bawah kulit pecah akibat benturan atau pukulan, menyebabkan perubahan warna pada kulit.
                - Segera kompres area yang memar dengan es batu yang dibungkus kain untuk mengurangi pembengkakan dan rasa sakit.
                - Tinggikan area yang memar untuk mengurangi aliran darah ke area tersebut.
                - Hindari tekanan langsung pada memar untuk mencegah pendarahan lebih lanjut.
                - Setelah beberapa hari, gunakan kompres hangat untuk mempercepat proses penyembuhan.
                - Jika memar disertai rasa sakit yang hebat atau pembengkakan, pertimbangkan untuk memeriksakan diri ke dokter.
            '''
        },
        {
            'name': 'Burns',
            'handling': '''
                Luka bakar adalah kerusakan pada kulit yang disebabkan oleh panas, api, uap, atau bahan kimia. Luka bakar dapat dibagi menjadi tingkat ringan (derajat satu), sedang (derajat dua), dan berat (derajat tiga).
                - Segera rendam luka bakar dengan air dingin selama 10-15 menit untuk mengurangi rasa sakit dan menghentikan kerusakan lebih lanjut.
                - Hindari menggunakan es langsung pada luka bakar, karena ini dapat merusak jaringan lebih dalam.
                - Untuk luka bakar ringan, oleskan salep luka bakar atau gel lidah buaya untuk meredakan peradangan.
                - Jika luka bakar cukup parah (misalnya, luka terbuka atau lepuh besar), segeralah pergi ke rumah sakit untuk perawatan medis lebih lanjut.
                - Jangan pecahkan lepuh atau tutupi luka dengan bahan yang tidak steril.
            '''
        },
        {
            'name': 'Cut',
            'handling': '''
                Luka sayat terjadi ketika kulit terpotong oleh benda tajam. Luka ini bisa dangkal atau dalam, tergantung pada kedalaman potongan.
                - Cuci luka dengan air bersih dan sabun untuk menghilangkan kotoran dan debu.
                - Gunakan kain bersih untuk menghentikan pendarahan dengan memberikan tekanan pada luka.
                - Setelah pendarahan berhenti, oleskan salep antibiotik untuk mencegah infeksi.
                - Tutup luka dengan perban steril dan perhatikan tanda-tanda infeksi seperti kemerahan atau nanah.
                - Jika luka cukup dalam atau tidak berhenti berdarah, pertimbangkan untuk mendapatkan jahitan dari profesional medis.
            '''
        },
        {
            'name': 'Ingrown_nails',
            'handling': '''
                Kuku tumbuh ke dalam terjadi ketika ujung kuku menembus kulit di sekitar kuku, menyebabkan rasa sakit, peradangan, dan infeksi.
                - Rendam kaki dalam air hangat untuk mengurangi peradangan dan rasa sakit.
                - Setelah merendam, keringkan kaki dan gunakan kapas atau kain lembut untuk perlahan-lahan mengangkat ujung kuku yang tumbuh ke dalam (gunakan alat steril jika diperlukan).
                - Oleskan salep antibiotik pada area yang terinfeksi.
                - Jika peradangan berlanjut atau infeksi berkembang, pertimbangkan untuk berkonsultasi dengan dokter atau ahli pedikur.
                - Pastikan untuk memotong kuku secara lurus dan tidak terlalu pendek di masa depan untuk mencegah masalah ini.
            '''
        },
        {
            'name': 'Laceration',
            'handling': '''
                Luka robek terjadi ketika kulit robek atau sobek akibat benda tajam atau kecelakaan. Luka ini biasanya lebih dalam dibandingkan dengan luka sayat.
                - Cuci luka dengan air bersih untuk menghilangkan kotoran.
                - Gunakan kain bersih untuk menghentikan pendarahan dengan memberikan tekanan pada luka.
                - Jika luka cukup besar atau dalam, segera bawa pasien ke rumah sakit untuk mendapatkan jahitan.
                - Setelah jahitan, pastikan luka tetap bersih dan kering.
                - Perhatikan tanda-tanda infeksi dan konsultasikan dengan dokter jika ada gejala seperti kemerahan atau nanah.
            '''
        },
        {
            'name': 'Stab_wound',
            'handling': '''
                Luka tusuk terjadi ketika benda tajam menembus kulit dan jaringan tubuh lainnya, sering kali lebih dalam dan dapat merusak organ dalam.
                - Jangan coba untuk mencabut benda tajam dari luka, karena ini bisa memperburuk cedera atau menyebabkan pendarahan lebih lanjut.
                - Tekan area luka dengan kain bersih untuk mengendalikan pendarahan.
                - Segera bawa pasien ke rumah sakit untuk mendapatkan perawatan medis lebih lanjut dan menilai tingkat keparahan cedera.
                - Jika benda tajam masih tertinggal dalam tubuh, segera bawa ke ruang gawat darurat.
            '''
        }
    ]

    with app.app_context():
        for injury_data in injuries_data:
            injury = InjuryClass.query.filter_by(class_name=injury_data['name']).first()
            if not injury:
                injury = InjuryClass(class_name=injury_data['name'], treatment=injury_data['handling'])
                db.session.add(injury)

        db.session.commit()
        print("Injuries and handling steps have been seeded.")
