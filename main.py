#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python


import shapefile
sf = shapefile.Reader("shp/bts_negara.shp")
boljug = sf.shapes()
print len(boljug)

