from SosyalMedya import SosyalMedya

hesap1 = SosyalMedya("ali123","Ali Kurtulan",8)
hesap2 = SosyalMedya("ayse2","Ayse Kaplan",5)
hesap3 = SosyalMedya("eren44","Eren Olgun",10)
hesap4 = SosyalMedya("fatma","Fatma Aslan",12)

hesaplar = [hesap1,hesap2,hesap3,hesap4]

def cikti_test(takipciler, birakanlar):
    for i in range(len(hesaplar)):
        for _ in range(1,takipciler[i]+1):
            hesaplar[i].takip_et()
        for _ in range(1,birakanlar[i]+1):
            hesaplar[i].takibi_birak()
        hesaplar[i].takipci_durumu()


#cikti_test(takipciler=[3,10,3,1],birakanlar=[15,3,11,16])
cikti_test(takipciler=[1,2,3,4],birakanlar=[12,11,10,9])

"""
Programın ekrana basması gereken çıktılar
hesap adi, gerçek adi, takipçi sayısı, takibi bırakan sayısı şeklinde olacak 

cikti_test(takipciler=[3,10,3,1],birakanlar=[15,3,11,16]) çağrısı için çıktı

ali123,Ali Kurtulan,0,11
ayse2,Ayse Kaplan,12,3
eren44,Eren Olgun,2,11
fatma,Fatma Aslan,0,13

cikti_test(takipciler=[1,2,3,4],birakanlar=[12,11,10,9]) çağrısı için 

ali123,Ali Kurtulan,0,9
ayse2,Ayse Kaplan,0,7
eren44,Eren Olgun,3,10
fatma,Fatma Aslan,7,9

"""