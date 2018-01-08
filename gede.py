=#!/usr/bin/python

import shapefile

class Gede(object):
	def __init__(self,namafile):
		self.sf = shapefile.Reader(namafile)

	def itungBaris(self):
		rec = self.sf.shapes()
		return len(rec)
	def selectNegara(self,NEGARA):
		i = 0
		for a in self.sf.records():
			if a[8] == NEGARA:
				return i
			i=i+1
		
	def __init__(self,bandung):
		self.sf = shapefile.Reader(bandung)
		
	def selectJalan(self,Jalan Tubagus Ismail Raya):
		i = 0
		for a in self.sf.records():
			if a[1] == Jalan Tubagus Ismail Raya:
				return i 
			i = i + 1
				
	def selectJalan(self,Jalan Sarijadi Raya):
		i = 0
		for a in self.sf.records():
			if a[1] == Jalan Sarijadi Raya:
				return i 
			i = i + 1
			
	def selectJalan(self,Jalan Geger Kalong Girang):
		i = 0
		for a in self.sf.records():
			if a[1] == Jalan Geger Kalong Girang:
				return i 
			i = i + 1
			
	def selectJalan(self,Jalan Cendana):
		i = 0
		for a in self.sf.records():
			if a[1] == Jalan Cendana:
				return i 
			i = i + 1
				
	def selectJalan(self,Jalan Cipaganti):
		i = 0
		for a in self.sf.records():
			if a[1] == Jalan Cipaganti:
				return i 
			i = i + 1			
	
	def selectJalan(self,Jalan Sukaraja):
		i = 0
		for a in self.sf.records():
			if a[1] == Jalan Sukaraja:
				return i 
			i = i + 1
	
	def selectJalan(self,Jalan Bengawan):
		i = 0
		for a in self.sf.records():
			if a[1] == Jalan Bengawan:
				return i 
			i = i + 1
		

	def selectJalan(self,Jalan Dago):
		i = 0
		for a in self.sf.records():
			if a[1] == Jalan Dago:
				return i 
			i = i + 1
	
	def selectJalan(self,Jalan Layang Pasupati):
		i = 0
		for a in self.sf.records():
			if a[1] == Jalan Layang Pasupati:
				return i 
			i = i + 1
	
	def selectJalan(self,Jalan Surapati):
		i = 0
		for a in self.sf.records():
			if a[1] == Jalan Surapati:
				return i 
			i = i + 1
			
	def selectJalan(self,Jalan Diponegoro):
		i = 0
		for a in self.sf.records():
			if a[1] == Jalan Diponegoro:
				return i 
			i = i + 1
			
	def selectJalan(self,Jalan Citarum):
		i = 0
		for a in self.sf.records():
			if a[1] == Jalan Citarum:
				return i 
			i = i + 1
			
	
	def selectJalan(self,Jalan Cikutra):
		i = 0
		for a in self.sf.records():
			if a[1] == Jalan Cikutra:
				return i 
			i = i + 1

			
	def selectJalan(self,Jalan Laswi):
		i = 0
		for a in self.sf.records():
			if a[1] == Jalan Laswi:
				return i 
			i = i + 1	
			
 	def selectJalan(self,Jalan Soekarno Hatta):
		i = 0
		for a in self.sf.records():
			if a[1] == Jalan Soekarno Hatta:
				return i 
			i = i + 1
		
	def selectJalan(self,Jalan Turangga):
		i = 0
		for a in self.sf.records():
			if a[1] == Jalan Turangga:
				return i 
			i = i + 1
			
	def selectJalan(self,Jalan Buah Batu):
		i = 0
		for a in self.sf.records():
			if a[1] == Jalan Buah Batu:
				return i 
			i = i + 1
		
	def selectJalan(self,Jalan Raya Lembang):
		i = 0
		for a in self.sf.records():
			if a[1] == Jalan Raya Lembang:
				return i 
			i = i + 1	
		
