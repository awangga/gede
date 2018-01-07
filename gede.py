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
		
			
		self.label = Label(self.frame, text = "Image Dir:")
        	self.label.grid(row = 1, column = 0, sticky = E)
        	self.entry = Entry(self.frame)
        	self.entry.grid(row = 1, column = 1, sticky = W+E)
        	self.ldBtn = Button(self.frame, text = "Load", command = self.loadDir)
        	self.ldBtn.grid(row = 1, column = 2, sticky = W+E)
		
		self.lb1 = Label(self.frame, text = 'Bounding boxes:')
       		self.lb1.grid(row = 1, column = 2,  sticky = W+N)
        	self.listbox = Listbox(self.frame, width = 22, height = 12)
        	self.listbox.grid(row = 2, column = 2, sticky = N)
        	self.btnDel = Button(self.frame, text = 'Delete', command = self.delBBox)
        	self.btnDel.grid(row = 3, column = 2, sticky = W+E+N)
        	self.btnClear = Button(self.frame, text = 'ClearAll', command = self.clearBBox)
        	self.btnClear.grid(row = 4, column = 2, sticky = W+E+N)
		
		self.ctrPanel = Frame(self.frame)
        	self.ctrPanel.grid(row = 5, column = 1, columnspan = 2, sticky = W+E)
        	self.prevBtn = Button(self.ctrPanel, text='<< Prev', width = 10, command = self.prevImage)
		self.prevBtn.pack(side = LEFT, padx = 5, pady = 3)
        	self.nextBtn = Button(self.ctrPanel, text='Next >>', width = 10, command = self.nextImage)
        	self.nextBtn.pack(side = LEFT, padx = 5, pady = 3)
        	self.progLabel = Label(self.ctrPanel, text = "Progress:     /    ")
        	self.progLabel.pack(side = LEFT, padx = 5)
        	self.tmpLabel = Label(self.ctrPanel, text = "Go to Image No.")
        	self.tmpLabel.pack(side = LEFT, padx = 5)
        	self.idxEntry = Entry(self.ctrPanel, width = 5)
        	self.idxEntry.pack(side = LEFT)
        	self.goBtn = Button(self.ctrPanel, text = 'Go', command = self.gotoImage)
        	self.goBtn.pack(side = LEFT)
		
		self.egPanel = Frame(self.frame, border = 10)
        	self.egPanel.grid(row = 1, column = 0, rowspan = 5, sticky = N)
        	self.tmpLabel2 = Label(self.egPanel, text = "Examples:")
        	self.tmpLabel2.pack(side = TOP, pady = 5)
        	self.egLabels = []
		
        	for i in range(3):
            		self.egLabels.append(Label(self.egPanel))
            		self.egLabels[-1].pack(side = TOP)
			
        		self.disp = Label(self.ctrPanel, text='')
        		self.disp.pack(side = RIGHT)

        		self.frame.columnconfigure(1, weight = 1)
        		self.frame.rowconfigure(4, weight = 1)
		
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



