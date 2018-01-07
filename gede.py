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
		z = sby.shapes(0)
		z.shapetype
		
	def __init__(mdn,medan):
		mdn.sf = shapefile.Reader(medan)
	def melihattype(mdn):
		z = mdn.shapes(0)
		z.shapetype
