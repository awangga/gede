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
			
		def __init__(self,bandung):
		self.sf = shapefile.Reader(bandung)
		
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
				
	def selectJalan(self,Jalan Bengawan):
		i = 0
		for a in self.sf.records():
			if a[1] == Jalan Bengawan:
				return i 
			i = i + 1
		


