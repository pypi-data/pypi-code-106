import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    """
    Tanggal: 26 Desember 2021 
    Waktu : 09:22:53 WIB
    Magnitudo: 5.2
    Kedalaman: 10 km
    Lokasi: 2.21 LU - 126.79 BT
    Pusat gempa: 130 km BaratLaut HALMAHERABARAT-MALUT
    Potensi: tidak berpotensi TSUNAMI
    """
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        title = soup.find('title')
        print(title.string)

        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        waktu = result[1]
        tanggal = result[0]

        result = soup.find(
            'div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        ls = None
        bt = None
        pusat = None
        kedalaman = None
        potensi = None
        dirasakan = None
        tsunami = None
        for res in result:
           
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            # elif i == 5:
            #     tsunami = res.text
            elif i == 5:
                dirasakan = res.text

            # print(i, res)

            i = i+1

        hasil = dict()
        hasil['tanggal'] = tanggal  # '26 Desember 2021'
        hasil['waktu'] = waktu  # '09:22:53 WIB'
        hasil['magnitudo'] = magnitudo  # 5.2
        hasil['kedalaman'] = kedalaman  # '10 km'
        hasil['koordinat'] = {'ls': ls, 'bt': bt}
        hasil['lokasi'] = lokasi
        # '130 km BaratLaut HALMAHERABARAT-MALUT'
        hasil['dirasakan'] = dirasakan
        # hasil['pusat'] = '130 km BaratLaut HALMAHERABARAT-MALUT'
        hasil['tsunami'] = tsunami  # 'Tidak berpotensi TSUNAMI'
        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print('Tidak bisa menemukan data gempa bumi terkini')
        return

    print('\nGempa Terakhir berdasarkan BMKG')
    print('Tanggal :', result['tanggal'])
    print('Waktu :', result['waktu'])
    print('Magnitudo :', result['magnitudo'])
    print('Kedalaman :', result['kedalaman'])
    print('Koordinat : LS=', (result['koordinat']
          ['ls']), 'BT=', (result['koordinat']['bt']))
    print('Lokasi :', result['lokasi'])
    print('Dirasakan :', result['dirasakan'])
    # print('Pusat :',result['pusat'])
    # print('Potensi :', result['tsunami'])


if __name__ == '__main__' :
    result = ekstraksi_data()
    tampilkan_data(result)