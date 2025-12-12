

message = "creation reussite"
cree_fichier = open("test.txt","w")
cree_fichier.write(message)
cree_fichier.close()
cree_fichier = open("test.txt","a")
cree_fichier.write(message)
cree_fichier.close()
