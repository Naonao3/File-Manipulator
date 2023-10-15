def reverse(inputpath,outpath):
    text = ""
    with open(inputpath,"r") as f:
        text = f.read()
    with open(outpath,"w") as f:
        f.write(text[::-1])

def copy(inputpath,outpath):
    text = ""
    with open(inputpath,"r") as f:
        text = f.read()
    with open(outpath,"w") as f:
        f.write(text)

def duplicateContents(inputpath,n):
    with open(inputpath,"r") as f:
        text = f.read()
        f.write(text * int(n))

def replaceString(inputpath,needle,newstring):
    with open(inputpath,"r") as f:
        text = f.read()
    with open(inputpath,"w"):
        f.write(text.replace(needle,newstring))