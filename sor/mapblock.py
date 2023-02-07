from collections import namedtuple
rType=namedtuple("readType",["bytes","type","name"])
mapStru=[False for x in range(4) ]

mapStru[0]=rType(4,"str","map")
mapStru[1]=rType(2,"int","version")
mapStru[2]=rType(2,"int",'nBytes')
mapStru[2]=rType(2,"int",'nBlocks')

def sorReadMap(sbytes:bytes,mapStru=map):
    name=sbytes[0:mapStru.bytes]
    version=sbytes[4:5]

    mapBlock=sbytes[0:4]
    print(mapBlock)