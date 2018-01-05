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



