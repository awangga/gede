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
			
	def __init__(qefl,bandung):
		qefl.sf = shapefile.Reader(bandung)
	def melihattype(qefl):
		a = qelf.shapes(0)
		a.shapetype

	def __init__(adcp,jakarta):
		adcp.sf = shapefile.Reader(jakarta)
	def melihattype(adcp):
		f = adcp.shapes(0)
		f.shapetype

	def __init__(smg,semarang):
		qefl.sf = shapefile.Reader(semarang)
	def melihattype(smg):
		b = qelf.shapes(0)
		b.shapetype