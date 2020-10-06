import hashlib

fin = open("input.txt")
sin = fin.read()
fin.close()

hash = hashlib.sha1()
hash.update(sin.encode())

fout = open("output.txt", "w")
fout.write(hash.hexdigest())
fout.close()
