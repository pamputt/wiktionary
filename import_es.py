﻿#!/usr/bin/env python
# coding: utf-8
# Ce script identifie les palindrome depuis un dump TXT (List of page titles in main namespace)

# Importation des modules
import catlib, pagegenerators, os, langues
from wikipedia import *

# Déclaration
language = "fr"
family = "wiktionary"
mynick = "PamputtBot"
site = getSite(language,family)
debogage = False

# Modification du wiki
def modification(titre, PageHS):
	summary = u'Ajout de la forme conjuguée en espagnol'
	#if debogage == True: print u'------------------------------------'
	#print(PageHS.encode(config.console_encoding, 'replace'))

	print u'Traitement de ' + titre + u'!'
	
	# On retire les diacritiques et ignore la casse
	# le flag re.UNICODE est utilisé pour que \w matche toute lettre de tout alphabet
	titre_denude = unicodedata.normalize('NFKD', titre).lower()
	titre_denude = re.sub(ur'[^\w]', u'', titre_denude, flags=re.UNICODE)
	if len(titre_denude) > 1 and titre_denude == titre_denude[::-1]:
		try:
			print u'page = Page(site,titre)'
			page = Page(site,titre)
			print page
		except UnicodeDecodeError: 
			print "UnicodeDecodeError l 30"
			return
	
		if page.exists() and page.namespace() == 0:
			try:
				PageBegin = page.get()
			except wikipedia.NoPage:
				print "NoPage l 36"
				return
			except wikipedia.LockedPage: 
				print "Locked l 40"
				return
			except wikipedia.IsRedirectPage: 
				print "IsRedirect l 43"
				return
		else:
			print "NoPage l 46"
			return
		PageTemp = PageBegin
		print PageTemp
		PageEnd = u''

		# Si la page contient deja une section en espagnol, alors on la traitera manuellement
		if PageTemp.find('{{langue|es}}') != -1:
			fout.write(PageHS.encode('utf8'))
			return


		## # Pour chaque langue, recherche de la catégorie des palindromes
		## while PageTemp.find('{{langue|es}}') != -1:
		## 	PageEnd = PageEnd + PageTemp[:PageTemp.find('{{langue|')+len('{{langue|')]
		## 	PageTemp = PageTemp[PageTemp.find('{{langue|')+len('{{langue|'):]
		## 	codelangue = PageTemp[:PageTemp.find('}}')]
		## 	if len(codelangue) < 4:
		## 		NomLangue = langues.langues[codelangue].decode("utf8")
		## 		if NomLangue != u'':
		## 			#if debogage == True: print NomLangue.encode(config.console_encoding, 'replace')
		## 			if PageTemp.find(u'[[Catégorie:Palindromes en ' + NomLangue + ']]') == -1:
		## 				# Modification de la page
		## 				if PageTemp.find('{{langue|') != -1:
		## 					PageTemp2 = PageTemp[:PageTemp.find('{{langue|')]
		## 					PageTemp = PageTemp[:PageTemp2.rfind(u'\n')] + u'\n[[Catégorie:Palindromes en '+NomLangue+']]\n\n' + PageTemp[PageTemp2.rfind(u'\n'):]
		## 				else:
		## 					PageTemp = PageTemp + u'\n\n[[Catégorie:Palindromes en '+NomLangue+']]'
		## 				# On retire les lignes vides entre les catégories
		## 				PageTemp = re.sub(ur'(\[\[Catégorie:[^\]]*?\]\])\n{2,}\[\[Catégorie', ur'\1\n[[Catégorie', PageTemp)
		## 				PageTemp = PageTemp.replace('\n\n\n==', '\n\n==')

		## PageEnd = PageEnd + PageTemp		
		## #if debogage == True: print (u'--------------------------------------------------------------------------------------------')
		## if PageEnd != PageBegin:
		## 	sauvegarde(page,PageEnd, summary)
		## elif debogage == True:
			## 	print "Aucun changement"
		
		
def trim(s):
    return s.strip(" \t\n\r\0\x0B")

def crawlerXML(source):
	pages = [r for r in xmlreader.XmlDump(source, allrevisions=False).parse()]
	for Page in pages:
		modification(Page.title())
	
# Lecture du fichier es_conj.xml
def crawlerFile(source):
	if source:
		PagesHS = open(source, 'r')
		PageHS = u''
		titre = u''
		#PagesHS = codecs.open(source,"r","utf-8")
		while True:
			ligne = PagesHS.readline()
			ligne = ligne.decode('utf8')
			if ligne.find(u'xxxx') != -1:
				titre = PagesHS.readline()
				titre = titre[3:-4]
				## print titre
			
			if ligne.find(u'yyyy') == -1 and ligne.find(u'xxxx') == -1:	
				PageHS += ligne
			
			if  (ligne.find(u'yyyy') != -1 and titre):
				## print u'////////////////////'
				## print titre
				## print PageHS
				## print u'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'
				modification(titre, PageHS)
				titre  = u''
				PageHS = u''
				##break
				
			
		PagesHS.close()
		

# Permet à tout le monde de stopper le bot en lui écrivant
def ArretDUrgence():
		page = Page(site,u'User talk:' + mynick)
		if page.exists():
			PageTemp = u''
			try:
				PageTemp = page.get()
			except wikipedia.NoPage: return
			except wikipedia.IsRedirectPage: return
			except wikipedia.LockedPage: return
			except wikipedia.ServerError: return
			except wikipedia.BadTitle: return
			except pywikibot.EditConflict: return
			if PageTemp != u"{{/Stop}}":
				pywikibot.output (u"\n*** \03{lightyellow}Arrêt d'urgence demandé\03{default} ***")
				exit(0)

def sauvegarde(PageCourante, Contenu, summary):
	result = "ok"
	if debogage == True:
		if len(Contenu) < 6000:
			print(Contenu.encode(config.console_encoding, 'replace'))
		else:
			taille = 3000
			print(Contenu[:taille].encode(config.console_encoding, 'replace'))
			print u'\n[...]\n'
			print(Contenu[len(Contenu)-taille:].encode(config.console_encoding, 'replace'))
		result = raw_input("Sauvegarder ? (o/n) ")
	if result != "n" and result != "no" and result != "non":
		if PageCourante.title().find(u'Utilisateur:JackBot/') == -1: ArretDUrgence()
		if not summary: summary = u'[[Wiktionnaire:Structure des articles|Autoformatage]]'
		try:
			PageCourante.put(Contenu, summary)
		except wikipedia.NoPage: 
			print "NoPage en sauvegarde"
			return
		except wikipedia.IsRedirectPage: 
			print "IsRedirectPage en sauvegarde"
			return
		except wikipedia.LockedPage: 
			print "LockedPage en sauvegarde"
			return
		except pywikibot.EditConflict: 
			print "EditConflict en sauvegarde"
			return
		except wikipedia.ServerError: 
			print "ServerError en sauvegarde"
			return
		except wikipedia.BadTitle: 
			print "BadTitle en sauvegarde"
			return
		except AttributeError:
			print "AttributeError en sauvegarde"
			return
			
# Lancement
fout = open(u'aTraiterManuellement.txt', "a")
TraitementFichier = crawlerFile(u'es_conj.xml')
fout.close()

