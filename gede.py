#!/usr/bin/python

import shapefile

class Gede(object):
	def __init__(self,bandung):
		self.sf = shapefile.Reader(bandung)
		
	def selectTempat(self,Universitas_Nurtanio):
		i =0 
		for a in self.sf.records():
				if a[1] == Universitas Nurtanio:
						return i
				i=i+1
	def selectTempat(self,Kolam_Renang_Karang_Setra):
		i =0 
		for a in self.sf.records():
				if a[1] == Kolam Renang Karang Setra:
						return i
				i=i+1
	def selectTempat(self,Politeknik Pos Indonesia):
		i =0 
		for a in self.sf.records():
				if a[1] == Politeknik Pos Indonesia:
						return i
				i=i+1
	def selectTempat(self,Kartika_Sari):
		i =0 
		for a in self.sf.records():
				if a[1] == Kartika Sari:
						return i
				i=i+1
	def selectTempat(self,Secapa_AD):
		i =0 
		for a in self.sf.records():
				if a[1] == Secapa_AD:
						return i
				i=i+1
	def selectTempat(self,Paris_Van_Java):
		i =0 
		for a in self.sf.records():
				if a[1] == Paris_Van_Java:
						return i
				i=i+1
	def selectTempat(self,Borma_Toserba_Setiabudi):
		i =0 
		for a in self.sf.records():
				if a[1] == Borma_Toserba_Setiabudi:
						return i
				i=i+1
				
	def selectTempat(self,Universitas Kristen Maranata):
	i =0 
	for a in self.sf.records():
				if a[1] == Universitas Kristen Maranata:
						return i
				i=i+1
	def selectTempat(self, The Lodge Maribaya Jawa Barat):
		i =0
		for a in self.sf.records():
				if a[1] == The Lodge Maribaya Jawa Barat:
						return i
				i=i+1
				
	def selectTempat(self, The Lodge Maribaya Bandung Jawa Barat):
		i =0
		for a in self.sf.records():
				if a[1] == The Lodge Maribaya Bandung Jawa Barat:
						return i
				i=i+1

	def itungBaris(self):
		rec = self.sf.shapes()
		return len(rec)
	def selectNegara(self,NEGARA):
		i = 0
		for a in self.sf.records():
			if a[8] == NEGARA:
				return i
			i=i+1
			
	def __init__(qefl,bandung):
		qefl.sf = shapefile.Reader(bandung)
	def melihattype(qefl):
		a = qelf.shapes(0)
		a.shapetype

	def __init__(jkt,jakarta):
		jkt.sf = shapefile.Reader(jakarta)
	def melihattype(jkt):
		f = jkt.shapes(0)
		f.shapetype

	def __init__(smg,semarang):
		smg.sf = shapefile.Reader(semarang)
	def melihattype(smg):
		b = smg.shapes(0)
		b.shapetype

	def __init__(sby,surabaya):
		sby.sf = shapefile.Reader(surabaya)
	def melihattype(sby):
		zbb = sby.shapes(0)
		zbb.shapetype
		
	def __init__(mdn,medan):
		mdn.sf = shapefile.Reader(medan)
	def melihattype(mdn):
		h = mdn.shapes(0)
		h.shapetype
		
	def __init__(mks,makasar):
		mks.sf = shapefile.Reader(makasar)
	def melihattype(mks):
		g = mks.shapes(0)
		g.shapetype

	def __init__(pnt,pontianak):
		pnt.sf = shapefile.Reader(pontianak)
	def melihattype(pnt):
		c = pnt.shapes(0)
		c.shapetype

	def __init__(ldn,london):
		ldn.sf = shapefile.Reader(london)
	def melihattype(ldn):
		d = ldn.shapes(0)
		d.shapetype
		
	def __init__(rma,roma):
		rma.sf = shapefile.Reader(roma)
	def melihattype(rma):
		e = rma.shapes(0)
		e.shapetype
		
	def __init__(dpk,depok):
		dpk.sf = shapefile.Reader(depok)
	def melihattype(dpk):
		zaz = dpk.shapes(0)
		zaz.shapetype
	def __init__(tsk,tasikmalaya):
		tsk.sf = shapefile.Reader(tasikmalaya)
	def melihattype(tsk):
		z = tsk.shapes(0) 
		z.shapetype
	def __init__(mdr,madrid):
		mdr.sf = shapefile.Reader(madrid)
	def melihattype(mdr):
		zz =mdr.shapes(0)
	zz.shapetype
	def __init__(nyc,newyork):
		nyc.sf = shapefile.Reader(newyork)
	def melihattype(nyc):
		o = nyc.shapes(0)
		o.shapetype

	def __init__(tky,tokyo):
		tky.sf = shapefile.Reader(tokyo)
	def melihattype(tky):
		t = tky.shapes(0)
		t.shapetype
		
	def __init__(sdy,sydney):
		sdy.sf = shapefile.Reader(sydney)
	def melihattype(sdy):
		s = sdy.shapes(0)
		s.shapetype
	def __init__(slt,salatiga):
		slt.sf = shapefile.Reader(salatiga)
	def melihattype(slt):
		x = slt.shapes(0)
		x.shapetype
		
	def selectTempat(self, Masjid Raya Bandung):
		i =0
		for a in self.sf.records():
				if a[1] == Masjid Raya Bandung:
						return i
				i=i+1
		
	def selectTempat(self, Alun Alun Bandung):
		i =0
		for a in self.sf.records():
				if a[1] == Alun Alun Bandung:
						return i
				i=i+1
				
	def selectTempat(self, Tugu Asia Afrika):
		i =0
		for a in self.sf.records():
				if a[1] == Tugu Asia Afrika:
						return i
				i=i+1
				
	def selectTempat(self, Gedung Merdeka):
		i =0
		for a in self.sf.records():
				if a[1] == Gedung Merdeka:
						return i
				i=i+1
	
	def selectTempat(self, Apotek Kimia Farma - Braga):
		i =0
		for a in self.sf.records():
				if a[1] == Apotek Kimia Farma - Braga:
						return i
				i=i+1
	
	def selectTempat(self, Stasiun Kereta Api Bandung):
		i =0
		for a in self.sf.records():
				if a[1] == Stasiun Kereta Api Bandung:
						return i
				i=i+1			
				
		
	def selectTempat(self, Museum Konferensi Asia Afrika):
		i =0
		for a in self.sf.records():
				if a[1] == Museum Konferensi Asia Afrika:
						return i
				i=i+1			
				
	def selectTempat(self, Dusun Bambu):
		i =0
		for a in self.sf.records():
				if a[1] == Dusun Bambu:
						return i
				i=i+1

	def selectTempat(self, NuArt Sculpture Park):
		i =0
		for a in self.sf.records():
				if a[1] == NuArt Sculpture Park:
						return i
				i=i+1			
		
	def selectTempat(self, Klenteng Sam Poo Kong):
		i =0
		for a in self.sf.records():
				if a[1] == Klenteng Sam Poo Kong:
						return i
				i=i+1		
				
	def selectTempat(self, Lawang Sewu):
		i =0
		for a in self.sf.records():
				if a[1] == Lawang Sewu:
						return i
				i=i+1	
				
	def selectTempat(self, Water Blaster):
		i =0
		for a in self.sf.records():
				if a[1] == Water Blaster:
						return i
				i=i+1	
	
	def selectTempat(self, Yayasan Buddhagaya ):
		i =0
		for a in self.sf.records():
				if a[1] == Yayasan Buddhagaya:
						return i
				i=i+1			
	
	def selectTempat(self, Pasar Johar):
		i =0
		for a in self.sf.records():
				if a[1] == Pasar Johar:
						return i
				i=i+1	
				
	def selectTempat(self, UNDIP):
		i =0
		for a in self.sf.records():
				if a[1] == UNDIP:
						return i
				i=i+1	
	

	def selectTempat(self, Paris Van Java):
		i =0
		for a in self.sf.records():
				if a[1] == Paris Van Java:
						return i
				i=i+1
				
	def selectTempat(self, Kawah Putih):
		i =0
		for a in self.sf.records():
				if a[1] == Kawah Putih:
						return i
				i=i+1
				
	def selectTempat(self, villa istana bunga):
		i =0
		for a in self.sf.records():
				if a[1] == villa istana bunga:
						return i
				i=i+1
				
	
	def selectTempat(self, Bandung Adventist Hospital):
		i =0
		for a in self.sf.records():
				if a[1] == Bandung Adventist Hospital:
						return i
				i=i+1
				
				
				
	def selectTempat(self, Donat Madu):
		i =0
		for a in self.sf.records():
				if a[1] == Donat Madu:
						return i
				i=i+1
				
	
	def selectTempat(self, Amazing Art World):
		i =0
		for a in self.sf.records():
				if a[1] == Amazing Art World:
						return i
				i=i+1
				
				
	def selectTempat(self, SMAN 15 Bandung):
		i =0
		for a in self.sf.records():
				if a[1] == SMAN 15 Bandung:
						return i
				i=i+1
				
				
	def selectTempat(self, Dago Dream Park):
		i =0
		for a in self.sf.records():
				if a[1] ==  Dago Dream Park:
						return i
				i=i+1
				

	def selectTempat(self, Bandung Station):
		i =0
		for a in self.sf.records():
				if a[1] == Bandung Station:
						return i
				i=i+1
