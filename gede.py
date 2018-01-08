#!/usr/bin/python

import shapefile

class Gede(object):
	def __init__(self,bandung):
		self.sf = shapefile.Reader(bandung)
		
	def selectTempat(self,Universitas Nurtanio):
		i =0 
		for a in self.sf.records():
				if a[1] == Universitas Nurtanio:
						return i
				i=i+1
	def selectTempat(self,Kolam Renang Karang Setra):
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
	def selectTempat(self,Kartika Sari):
		i =0 
		for a in self.sf.records():
				if a[1] == Kartika Sari:
						return i
				i=i+1
				
	def selectTempat(self,Universitas Kristen Maranata):
	i =0 
	for a in self.sf.records():
				if a[1] == Universitas Kristen Maranata:
						return i
				i=i+1



	def __init__(self,Medan):
		self.sf = shapefile.Reader(Medan)
		
	def selectTempat(self, Masjid Raya):
		i =0
		for a in self.sf.records():
				if a[1] == Masjid Raya:
						return i
				i=i+1
		
	def selectTempat(self, Lapangan Benteng):
		i =0
		for a in self.sf.records():
				if a[1] == Lapangan Benteng:
						return i
				i=i+1
				
	def selectTempat(self, Merdeka Walk):
		i =0
		for a in self.sf.records():
				if a[1] == Merdeka Walk:
						return i
				i=i+1

		
	def selectTempat(self, Mall Kartini):
		i =0
		for a in self.sf.records():
				if a[1] == Mall Kartini:
						return i
				i=i+1

				
	def __init__(self,Jakarta):
		self.sf = shapefile.Reader(Jakarta)
		
	def selectTempat(self, Dufan):
		i =0
		for a in self.sf.records():
				if a[1] == Dufan:
						return i
				i=i+1

	def selectTempat(self, NuArt Sculpture Park):
		i =0
		for a in self.sf.records():
				if a[1] == NuArt Sculpture Park:
						return i
				i=i+1			

				
	def __init__(self,Semarang):
		self.sf = shapefile.Reader(Semarang)
		
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

	def selectTempat(self, Kebun Binatang Bandung Jawa Barat):
		i =0
		for a in self.sf.records():
				if a[1] == Kebun Binatang Bandung Jawa Barat:
						return i
				i=i+1
