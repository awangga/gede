#!/usr/bin/python

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



