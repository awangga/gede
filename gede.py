#!/usr/bin/python

import shapefile

class Gede(object):
	def __init__(self,namafile):
		self.sf = shapefile.Reader(namafile)
		self.parent = master
        	self.parent.title("LabelTool")
       	 	self.frame = Frame(self.parent)
        	self.frame.pack(fill=BOTH, expand=1)
		
self.parent.resizable(width = FALSE, height = FALSE)

	def itungBaris(self):
		rec = self.sf.shapes()
		return len(rec)
	def selectNegara(self,NEGARA):
		i = 0
		for a in self.sf.records():
			if a[8] == NEGARA:
				return i
			i=i+1



