class SosyalMedya:
    """Sosyal Medya hesaplarındaki takip durumunu kontrol eden sınıf"""
    hesap_adi:str = ""
    gercek_adi:str = ""
    takipci_sayisi:int = 0
    takibi_birakan_sayisi:int = 0

    def __init__ (self,hesap_adi,gercek_adi,takipci_sayisi,takibi_birakan_sayisi):
        self.hesap_adi = hesap_adi
        self.gercek_adi = gercek_adi
        self.takipci_sayisi = takipci_sayisi
        self.takibi_birakan_sayisi = takibi_birakan_sayisi

    
    def takip_et(self):
        """hesabın takipçi sayısını 1 artıran method"""
        if self.takipci_sayisi > self.takibi_birakan_sayisi :
            self.takipci_sayisi = self.takipci_sayisi +1
            


    def takibi_birak(self):
        """hesabın takipçi sayısını 1 azaltan method (takipci sayısı negatif olamaz)"""
        self.takipci_sayisi >= 0 
        if self.takipci_sayisi < self.takibi_birakan_sayisi :
           self.takipci_sayisi = self.takipci_sayisi+ 1
           


    def takipci_durumu(self):
        """hesap adı,gerçek adı,takipçi sayısı ve takibi bırakan sayısını ekrana basan method"""
        print (format (self.hesap_adi , self.gercek_adi , self.takipci_sayisi , self.takibi_birak))
