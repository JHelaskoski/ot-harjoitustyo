import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)
        
    def test_luodun_kassan_rahamaara(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    
    def test_luodun_kassan_myydyt_lounaat_edulliset(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        
    def test_luodun_kassan_myydyt_lounaat_maukkaat(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
        
    def test_maksu_toimii_edullisesti_kateinen(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(vaihtoraha, 260)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.40)
        self.assertEqual(self.kassapaate.edulliset, 1)  
    
    def test_maksu_toimii_maukkaasti_kateinen(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.00)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        
    def test_maksu_ei_riita_edullisesti_kateinen(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_maksu_ei_riita_maukkaasti_kateinen(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortilla_riittavasti_rahaa_edullisesti(self):
        onnistui = self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(onnistui, True)
        self.assertEqual(self.kassapaate.edulliset, 1)
        
    def test_kortilla_riittavasti_rahaa_maukkaasti(self):
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(onnistui, True)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        
    def test_kortilla_ei_riittavasti_rahaa_edullisesti(self):
        kortti = Maksukortti(200)
        onnistui = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(onnistui, False)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)
        
    def test_kortilla_ei_riittavasti_rahaa_maukkaasti(self):
        kortti = Maksukortti(200)
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(onnistui, False)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)
        
    def test_rahan_lataaminen_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1005.00)
    
    def test_negatiivisen_summan_lataaminen_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -500)
        self.assertEqual(self.kortti.saldo, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)