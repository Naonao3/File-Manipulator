import sys

command = sys.argv[1]

if command == "reverse":
    inputpath = sys.argv[2]
    outpath = sys.argv[3]
    text = ""
    with open(inputpath,"r") as f:
        text = f.read()
    with open(outpath,"w") as f:
        f.write(text[::-1])

elif command == "copy":
    inputpath = sys.argv[2]
    outpath = sys.argv[3]
    text = ""
    with open(inputpath,"r") as f:
        text = f.read()
    with open(outpath,"w") as f:
        f.write(text)

elif command == "duplicate-contents":
    inputpath = sys.argv[2]
    n = int(sys.argv[3])
    with open(inputpath,"r") as f:
        text = f.read()
        f.write(text * int(n))
elif command == "replace-string":
    inputpath = sys.argv[2]
    needle = sys.argv[3]
    newstring = sys.argv[4]
    with open(inputpath,"r") as f:
        text = f.read()
    with open(inputpath,"w"):
        f.write(text.replace(needle,newstring))