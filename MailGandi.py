#!/usr/bin/python
import sys, xmlrpclib, os

def cls():
    os.system(['clear','cls'][os.name == 'nt'])


##################################
##        SCRIPT BY REDIX       ##
##  CREATE MAILBOX MASS GANDI   ##
##     froment.a@gmail.com      ##
##################################
########     V.0.1    ############
##################################

clear = lambda: os.system('cls')

# Veuillez referencez votre CLE XML API GANDI
APIKEY = 'AZERTYUIOP0123456QSDF587'
api = xmlrpclib.ServerProxy("https://rpc.gandi.net/xmlrpc/");

# INFORMATION SUR LE DOMAINE
cls()
domain = raw_input("Nom de domaine : ")
cls()
print "....................................................................."
print "Information sur le domaine", domain
info_domain = api.domain.info(APIKEY, domain)
info_mailbox = api.domain.mailbox.count(APIKEY, domain)
print "Proprietaire du domaine", info_domain['contacts']['owner']['handle']
print "Nombre de boite mail : ", info_mailbox
print "....................................................................."

# CREATION OU ECRASSEMENT DU FICHIER RAPPORT.TXT
rapport = open("rapport.txt", "w")

# DEMANDE NOMBRE BOITE MAIL A CREEE
nbmail = int(raw_input("Nombre de boite mail a creer : "))

# BOUCLE JUSQUA FIN NBMAIL
for i in range(nbmail):
	nom = raw_input("Nom : ")
	password = raw_input("Password : ")
	quota = int(raw_input("Quota (mo) : "))
	quota = quota*1024
	params = {'password':password, 'quota':quota}
	try:
		# ON CREER LES BOITE MAIL
		createmail = api.domain.mailbox.create(APIKEY,domain,nom,params)
		print nom, "a ete cree avec succes."
	except:
		print "[ERREUR] Impossible de creer la boite !"
	try:
		#ON ENREGISTRE LES DONNEES
		rapport.write(nom)
		rapport.write(" - ")
		rapport.write(password)
		rapport.write(" - ")
		rapport.write(str(quota))
		rapport.write("\n")
	except:
		print "[ERREUR] Impossible d'ecrire le fichier rapport.txt"

# NOUS SOMMES PROPRES, ON FERME LE FICHIER
rapport.close()
