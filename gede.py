#!/usr/bin/python

import shapefile
from Tkinter import *
import tkMessageBox
from PIL import Image, ImageTk
import os
import glob
import random

# colors for the bboxes
COLORS = ['red', 'blue', 'yellow', 'pink', 'cyan', 'green', 'black']
# image sizes for the examples
SIZE = 256, 256

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
		
			
		(self.label = Label(self.frame, text = "Image Dir:")
        	self.label.grid(row = 1, column = 0, sticky = E)
        	self.entry = Entry(self.frame)
        	self.entry.grid(row = 1, column = 1, sticky = W+E)
        	self.ldBtn = Button(self.frame, text = "Load", command = self.loadDir)
        	self.ldBtn.grid(row = 1, column = 2, sticky = W+E) )
		self.entry.grid(row = 1, column = 1, sticky = W+E)
        	self.ldBtn = Button(self.frame, text = "Load", command = self.loadDir)
        	self.ldBtn.grid(row = 1, column = 2, sticky = W+E) )
		
		(self.label = Label(self.frame, text = "Image Dir:")
        	self.label.grid(row = 1, column = 0, sticky = E)
        	self.entry = Entry(self.frame)
        	self.entry.grid(row = 2, column = 1, sticky = W+E)
		 (self.label = Label(self.frame, text = "Image Dir:")
        	self.label.grid(row = 1, column = 0, sticky = E)
        	self.entry = Entry(self.frame)
        	self.entry.grid(row = 2, column = 1, sticky = W+E)
		 self.entry = Entry(self.frame)
        	self.entry.grid(row = 2, column = 1, sticky = W+E)
        	
        	self.ldBtn = Button(self.frame, text = "Load", command = self.loadDir)
        	self.ldBtn.grid(row = 3, column = 2, sticky = W+E) )
		
		self.lb1 = Label(self.frame, text = 'Bounding boxes:')
       		self.lb1.grid(row = 1, column = 2,  sticky = W+N)
        	self.listbox = Listbox(self.frame, width = 22, height = 12)
        	self.listbox.grid(row = 2, column = 2, sticky = N)
        	self.btnDel = Button(self.frame, text = 'Delete', command = self.delBBox)
        	self.btnDel.grid(row = 3, column = 2, sticky = W+E+N)
        	self.btnClear = Button(self.frame, text = 'ClearAll', command = self.clearBBox)
        	self.btnClear.grid(row = 4, column = 2, sticky = W+E+N)
		 
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
	def loadDir(self, dbg = False):
        if not dbg:
            s = self.entry.get()
            self.parent.focus()
            self.category = int(s)
        else:
		s = r'D:\workspace\python\labelGUI'
		
	self.imageDir = os.path.join(r'./Images', '%03d' %(self.category))
        self.imageList = glob.glob(os.path.join(self.imageDir, '*.JPEG'))
        if len(self.imageList) == 0:
            print 'No .JPEG images found in the specified dir!'
            return

		self.cur = 1
        self.total = len(self.imageList)

         # set up output dir
        self.outDir = os.path.join(r'./Labels', '%03d' %(self.category))
        if not os.path.exists(self.outDir):
            os.mkdir(self.outDir)
	
	self.egDir = os.path.join(r'./Examples', '%03d' %(self.category))
        if not os.path.exists(self.egDir):
            return
        filelist = glob.glob(os.path.join(self.egDir, '*.JPEG'))
        self.tmp = []
        self.egList = []
        random.shuffle(filelist)
        for (i, f) in enumerate(filelist):
            if i == 3:
                break
            im = Image.open(f)
            r = min(SIZE[0] / im.size[0], SIZE[1] / im.size[1])
            new_size = int(r * im.size[0]), int(r * im.size[1])
            self.tmp.append(im.resize(new_size, Image.ANTIALIAS))
            self.egList.append(ImageTk.PhotoImage(self.tmp[-1]))
	    self.egLabels[i].config(image = self.egList[-1], width = SIZE[0], height = SIZE[1])

	    self.loadImage()
 	    print '%d images loaded from %s' %(self.total, s)
		
	def loadImage(self):
        # load image
        imagepath = self.imageList[self.cur - 1]
        self.img = Image.open(imagepath)
        self.tkimg = ImageTk.PhotoImage(self.img)
        self.mainPanel.config(width = max(self.tkimg.width(), 400), height = max(self.tkimg.height(), 400))
        self.mainPanel.create_image(0, 0, image = self.tkimg, anchor=NW)
        self.progLabel.config(text = "%04d/%04d" %(self.cur, self.total))

        # load labels
        self.clearBBox()
        self.imagename = os.path.split(imagepath)[-1].split('.')[0]
        labelname = self.imagename + '.txt'
        self.labelfilename = os.path.join(self.outDir, labelname)
	bbox_cnt = 0
        
	if os.path.exists(self.labelfilename):
            with open(self.labelfilename) as f:
                for (i, line) in enumerate(f):
                    if i == 0:
                        bbox_cnt = int(line.strip())
                        continue
                    tmp = [int(t.strip()) for t in line.split()]
##                    print tmp
                    self.bboxList.append(tuple(tmp))
                    tmpId = self.mainPanel.create_rectangle(tmp[0], tmp[1], \
                                                            tmp[2], tmp[3], \
                                                            width = 2, \
                                                            outline = COLORS[(len(self.bboxList)-1) % len(COLORS)])
                    self.bboxIdList.append(tmpId)
                    self.listbox.insert(END, '(%d, %d) -> (%d, %d)' %(tmp[0], tmp[1], tmp[2], tmp[3]))
                    self.listbox.itemconfig(len(self.bboxIdList) - 1, fg = COLORS[(len(self.bboxIdList) - 1) % len(COLORS)])

		 def saveImage(self):
        with open(self.labelfilename, 'w') as f:
            f.write('%d\n' %len(self.bboxList))
            for bbox in self.bboxList:
                f.write(' '.join(map(str, bbox)) + '\n')
	print 'Image No. %d saved' %(self.cur)
		 
	def mouseClick(self, event):
        if self.STATE['click'] == 0:
            self.STATE['x'], self.STATE['y'] = event.x, event.y
        else:
            x1, x2 = min(self.STATE['x'], event.x), max(self.STATE['x'], event.x)
            y1, y2 = min(self.STATE['y'], event.y), max(self.STATE['y'], event.y)
            self.bboxList.append((x1, y1, x2, y2))
            self.bboxIdList.append(self.bboxId)
            self.bboxId = None
            self.listbox.insert(END, '(%d, %d) -> (%d, %d)' %(x1, y1, x2, y2))
            self.listbox.itemconfig(len(self.bboxIdList) - 1, fg = COLORS[(len(self.bboxIdList) - 1) % len(COLORS)])
        self.STATE['click'] = 1 - self.STATE['click']

    def mouseMove(self, event):
        self.disp.config(text = 'x: %d, y: %d' %(event.x, event.y))
        if self.tkimg:
            if self.hl:
                self.mainPanel.delete(self.hl)
            self.hl = self.mainPanel.create_line(0, event.y, self.tkimg.width(), event.y, width = 2)
            if self.vl:
                self.mainPanel.delete(self.vl)
            self.vl = self.mainPanel.create_line(event.x, 0, event.x, self.tkimg.height(), width = 2)
        if 1 == self.STATE['click']:
            if self.bboxId:
                self.mainPanel.delete(self.bboxId)
            self.bboxId = self.mainPanel.create_rectangle(self.STATE['x'], self.STATE['y'], \
                                                            event.x, event.y, \
                                                            width = 2  , \
                                                            outline = COLORS[len(self.bboxList) % len(COLORS)])
                               

		def cancelBBox(self, event):
        if 1 == self.STATE['click']:
            if self.bboxId:
                self.mainPanel.delete(self.bboxId)
                self.bboxId = None
self.STATE['click'] = 0

def delBBox(self):
        sel = self.listbox.curselection()
        if len(sel) != 1 :
            return
        idx = int(sel[0])
        self.mainPanel.delete(self.bboxIdList[idx])
        self.bboxIdList.pop(idx)
        self.bboxList.pop(idx)
        self.listbox.delete(idx)

    def clearBBox(self):
        for idx in range(len(self.bboxIdList)):
            self.mainPanel.delete(self.bboxIdList[idx])
        self.listbox.delete(0, len(self.bboxList))
        self.bboxIdList = []
        self.bboxList = []

    def prevImage(self, event = None):
        self.saveImage()
        if self.cur > 1:
            self.cur -= 1
            self.loadImage()

def nextImage(self, event = None):
        self.saveImage()
        if self.cur < self.total:
            self.cur += 1
            self.loadImage()

    def gotoImage(self):
        idx = int(self.idxEntry.get())
        if 1 <= idx and idx <= self.total:
            self.saveImage()
            self.cur = idx
            self.loadImage()

if __name__ == '__main__':
    root = Tk()
    tool = LabelTool(root)
    root.resizable(width =  True, height = True)
    root.mainloop()
     
	def __init__(self,bandung):
		self.sf = shapefile.Reader(bandung)
		
	def selectTempat(self,Universitas_Nurtanio):
		i =0 
		for a in self.sf.records():
				if a[1] == Universitas Nurtanio:
						return i
				i=i+1
	def selectTempat(self,Kolam_Renang_Karang_Setra):
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
	def selectTempat(self,Kartika_Sari):
		i =0 
		for a in self.sf.records():
				if a[1] == Kartika Sari:
						return i
				i=i+1
	def selectTempat(self,Secapa_AD):
		i =0 
		for a in self.sf.records():
				if a[1] == Secapa_AD:
						return i
				i=i+1
	def selectTempat(self,Paris_Van_Java):
		i =0 
		for a in self.sf.records():
				if a[1] == Paris_Van_Java:
						return i
				i=i+1
	def selectTempat(self,Borma_Toserba_Setiabudi):
		i =0 
		for a in self.sf.records():
				if a[1] == Borma_Toserba_Setiabudi:
						return i
				i=i+1
				
	def selectTempat(self,Universitas Kristen Maranata):
	i =0 
	for a in self.sf.records():
				if a[1] == Universitas Kristen Maranata:
						return i
				i=i+1
	def selectTempat(self, The Lodge Maribaya Jawa Barat):
		i =0
		for a in self.sf.records():
				if a[1] == The Lodge Maribaya Jawa Barat:
						return i
				i=i+1
				
	def selectTempat(self, The Lodge Maribaya Bandung Jawa Barat):
		i =0
		for a in self.sf.records():
				if a[1] == The Lodge Maribaya Bandung Jawa Barat:
						return i
				i=i+1

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
		zbb = sby.shapes(0)
		zbb.shapetype
		
	def __init__(mdn,medan):
		mdn.sf = shapefile.Reader(medan)
	def melihattype(mdn):
		h = mdn.shapes(0)
		h.shapetype
		
	def __init__(mks,makasar):
		mks.sf = shapefile.Reader(makasar)
	def melihattype(mks):
		g = mks.shapes(0)
		g.shapetype

	def __init__(pnt,pontianak):
		pnt.sf = shapefile.Reader(pontianak)
	def melihattype(pnt):
		c = pnt.shapes(0)
		c.shapetype

	def __init__(ldn,london):
		ldn.sf = shapefile.Reader(london)
	def melihattype(ldn):
		d = ldn.shapes(0)
		d.shapetype
		
	def __init__(rma,roma):
		rma.sf = shapefile.Reader(roma)
	def melihattype(rma):
		e = rma.shapes(0)
		e.shapetype
		
	def __init__(dpk,depok):
		dpk.sf = shapefile.Reader(depok)
	def melihattype(dpk):
		zaz = dpk.shapes(0)
		zaz.shapetype
	def __init__(tsk,tasikmalaya):
		tsk.sf = shapefile.Reader(tasikmalaya)
	def melihattype(tsk):
		z = tsk.shapes(0) 
		z.shapetype
	def __init__(mdr,madrid):
		mdr.sf = shapefile.Reader(madrid)
	def melihattype(mdr):
		zz =mdr.shapes(0)
	zz.shapetype
	def __init__(nyc,newyork):
		nyc.sf = shapefile.Reader(newyork)
	def melihattype(nyc):
		o = nyc.shapes(0)
		o.shapetype

	def __init__(tky,tokyo):
		tky.sf = shapefile.Reader(tokyo)
	def melihattype(tky):
		t = tky.shapes(0)
		t.shapetype
		
	def __init__(sdy,sydney):
		sdy.sf = shapefile.Reader(sydney)
	def melihattype(sdy):
		s = sdy.shapes(0)
		s.shapetype
	def __init__(slt,salatiga):
		slt.sf = shapefile.Reader(salatiga)
	def melihattype(slt):
		x = slt.shapes(0)
		x.shapetype
		
	def selectTempat(self, Masjid Raya Bandung):
		i =0
		for a in self.sf.records():
				if a[1] == Masjid Raya Bandung:
						return i
				i=i+1
		
	def selectTempat(self, Alun Alun Bandung):
		i =0
		for a in self.sf.records():
				if a[1] == Alun Alun Bandung:
						return i
				i=i+1
				
	def selectTempat(self, Tugu Asia Afrika):
		i =0
		for a in self.sf.records():
				if a[1] == Tugu Asia Afrika:
						return i
				i=i+1
				
	def selectTempat(self, Gedung Merdeka):
		i =0
		for a in self.sf.records():
				if a[1] == Gedung Merdeka:
						return i
				i=i+1
	
	def selectTempat(self, Apotek Kimia Farma - Braga):
		i =0
		for a in self.sf.records():
				if a[1] == Apotek Kimia Farma - Braga:
						return i
				i=i+1
	
	def selectTempat(self, Stasiun Kereta Api Bandung):
		i =0
		for a in self.sf.records():
				if a[1] == Stasiun Kereta Api Bandung:
						return i
				i=i+1			
				
		
	def selectTempat(self, Museum Konferensi Asia Afrika):
		i =0
		for a in self.sf.records():
				if a[1] == Museum Konferensi Asia Afrika:
						return i
				i=i+1			
				
	def selectTempat(self, Dusun Bambu):
		i =0
		for a in self.sf.records():
				if a[1] == Dusun Bambu:
						return i
				i=i+1

	def selectTempat(self, NuArt Sculpture Park):
		i =0
		for a in self.sf.records():
				if a[1] == NuArt Sculpture Park:
						return i
				i=i+1			
		
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
				
	def selectTempat(self, Water Blaster):
		i =0
		for a in self.sf.records():
				if a[1] == Water Blaster:
						return i
				i=i+1	
	
	def selectTempat(self, Yayasan Buddhagaya ):
		i =0
		for a in self.sf.records():
				if a[1] == Yayasan Buddhagaya:
						return i
				i=i+1			
	
	def selectTempat(self, Pasar Johar):
		i =0
		for a in self.sf.records():
				if a[1] == Pasar Johar:
						return i
				i=i+1	
				
	def selectTempat(self, UNDIP):
		i =0
		for a in self.sf.records():
				if a[1] == UNDIP:
						return i
				i=i+1	
	

	def selectTempat(self, Paris Van Java):
		i =0
		for a in self.sf.records():
				if a[1] == Paris Van Java:
						return i
				i=i+1
				
	def selectTempat(self, Kawah Putih):
		i =0
		for a in self.sf.records():
				if a[1] == Kawah Putih:
						return i
				i=i+1
				
	def selectTempat(self, villa istana bunga):
		i =0
		for a in self.sf.records():
				if a[1] == villa istana bunga:
						return i
				i=i+1
				
	
	def selectTempat(self, Bandung Adventist Hospital):
		i =0
		for a in self.sf.records():
				if a[1] == Bandung Adventist Hospital:
						return i
				i=i+1
				
				
				
	def selectTempat(self, Donat Madu):
		i =0
		for a in self.sf.records():
				if a[1] == Donat Madu:
						return i
				i=i+1
				
	
	def selectTempat(self, Amazing Art World):
		i =0
		for a in self.sf.records():
				if a[1] == Amazing Art World:
						return i
				i=i+1
				
				
	def selectTempat(self, SMAN 15 Bandung):
		i =0
		for a in self.sf.records():
				if a[1] == SMAN 15 Bandung:
						return i
				i=i+1
				
				
	def selectTempat(self, Dago Dream Park):
		i =0
		for a in self.sf.records():
				if a[1] ==  Dago Dream Park:
						return i
				i=i+1
				

	def selectTempat(self, Bandung Station):
		i =0
		for a in self.sf.records():
				if a[1] == Bandung Station:
						return i
				i=i+1
