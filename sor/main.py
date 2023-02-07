
from mapblock import*

def sorOpenFile(filename:str):
    with open(filename,'rb') as f:
        sbytes=f.read()        
        return sbytes
def sorReadBytes(nBytes,nType):
    match nType:
        case
    pass



def main():
    filename="t.sor"
    sbytes=sorOpenFile(filename)
    sorReadMap(sbytes)



main()