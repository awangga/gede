#!/usr/bin/python

import shapefile

class Gede(object):
	def __init__(self,namafile):
		self.sf = shapefile.Reader(namafile)
		self.parent = master
        	self.parent.title("LabelTool")
       	 	self.frame = Frame(self.parent)
        	self.frame.pack(fill=BOTH, expand=1)
		
		self.imageDir = ''
        	self.imageList= []
        	self.egDir = ''
        	self.egList = []
        	self.outDir = ''
        	self.cur = 0
        	self.total = 0
        	self.category = 0
        	self.imagename = ''
        	self.labelfilename = ''
		self.tkimg = None
		
		self.STATE = {}
        	self.STATE['click'] = 0
        	self.STATE['x'], self.STATE['y'] = 0, 0
		
		self.bboxIdList = []
        	self.bboxId = None
        	self.bboxList = []
        	self.hl = None
        	self.vl = None
		
		self.label = Label(self.frame, text = "Image Dir:")
        	self.label.grid(row = 0, column = 0, sticky = E)
        	self.entry = Entry(self.frame)
        	self.entry.grid(row = 0, column = 1, sticky = W+E)
        	self.ldBtn = Button(self.frame, text = "Load", command = self.loadDir)
        	self.ldBtn.grid(row = 0, column = 2, sticky = W+E)
		
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



