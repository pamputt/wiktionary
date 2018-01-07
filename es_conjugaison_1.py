#!/usr/bin/env python
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
def modification(titre, PageEspagnol):
	summary = u'Ajout de la forme conjuguée en espagnol'
	#if debogage == True: print u'------------------------------------'
	#print(PageEspagnol.encode(config.console_encoding, 'replace'))

	print u'Traitement de ' + titre + u'!'
	
	# On retire les diacritiques et ignore la casse
	# le flag re.UNICODE est utilisé pour que \w matche toute lettre de tout alphabet
	titre_denude = unicodedata.normalize('NFKD', titre).lower()
	titre_denude = re.sub(ur'[^\w]', u'', titre_denude, flags=re.UNICODE)
	if len(titre_denude) > 0:
		try:
			## print u'page = Page(site,titre)'
			page = Page(site,titre)
			## print page
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
		## print PageTemp
		PageEnd = u''

		## Si la page contient deja une section en espagnol		
		if PageTemp.find('{{langue|es}}') != -1:
			fout.write(u'>>>' + titre + u'<<<\n')
			fout.write(PageEspagnol)
			return

		# on cherche où placer la section espagnole

		ligne = u''
		codelang = u''
		ajoute = False
		first = True
		## print PageTemp
		for ligne in PageTemp.splitlines():
			## print u'>>>>   ' + ligne
			pos1 = ligne.find(u'{{langue|')
			if ( pos1 != -1):
				pos2 = ligne.find(u'}}')
				codelang = ligne[pos1+9:pos2]

			## si ce n'est pas une section de langue ({{voir}} par exemple,
			## on passe à la ligne suivante
			if len(codelang)==0: continue
			
			result = ordreLang(codelang);
			## print u'code lang: ' + codelang + u', ' + str(result)

			## le code de langue n'a pas encore ete repertorie
			if result==0 and codelang!=u'es' and len(codelang)>0:
				print u'>> Code inconnu: ' + codelang + u'\n'
				fcodeout.write(codelang + u'\n')
				return
			

			## s'il n'y a qu'une seule langue qui se place avant l'espagnol
			## alors on vérifie s'il y a des catégories, des liens interwikis ou une clé de tri
			## si c'est le cas, on place l'espagnol avant
			##catégorie
			if ligne.find(u'[[Catégorie:')!=-1 and not ajoute:
				PageEnd = PageEnd + PageEspagnol + u'\n'
				ajoute = True
			## interwiki
			if re.search(u'\[\[(.)+:' + titre + u']]',ligne) and not ajoute:
				PageEnd = PageEnd + PageEspagnol + u'\n'
				ajoute = True
			## clé de tri
			if ligne.find(u'{{clé de tri')!=-1 and not ajoute:
				PageEnd = PageEnd + u'\n' + PageEspagnol + u'\n'
				ajoute = True


			## on ajoute « {{vérifier création automatique||es}} » en haut de l'article
			##if first:
			##	PageEnd = u'{{vérifier création automatique||es}}\n' + PageEnd
			##	first = False
				
			## si c'est un code langue avant l'espagnol (parmi ceux identifies)
			## alors on ajoute juste le texte de la page actuelle
			if result>0 or ajoute:
			        ## print u'---> ' + ligne + u', ' + codelang + u', ' + str(result) + u', ' + str(result<0) + u', ' + str(ajoute) + u' <---' 
				## print u'1//// ' + PageEnd + u'\\\\\\\\1'

				PageEnd = PageEnd + ligne + u'\n'

				## print u'2//// ' + PageEnd + u'\\\\\\\\2'
			## on ajoute le texte pour l'espagnol
			else:
				## print u'<1> ' + PageEnd + u'</1>'
				PageEnd = PageEnd + PageEspagnol + u'\n'
				PageEnd = PageEnd + ligne + u'\n'
				ajoute = True
				## print u'<2> ' + PageEnd + u'</2>'
		
	        if PageEnd != PageBegin:
			## print u'>>>>>>>>>>>>>>>>>>>>'
			## print PageEnd
			## print u'<<<<<<<<<<<<<<<<<<<<'
			sauvegarde(page, PageEnd, summary)

def createForm(titre):
	## a la fin on doit retourner une liste qui contient toutes les formes conjuguees
	return 0
		
def ordreLang(code):

	# si c'est de l'espagnol, on sort directement
	if(code == u'es'):
		return 0

	#cas particulier pour conv et fr qui sont toujours au début
	if(code == u'conv'):
		return 1
	if(code == u'fr'):
		return 1
	
	# on enlève les caractères spéciaux du nom de la langue
	## s1    = unicode(code,'utf-8')
	code2 = unicodedata.normalize('NFD', code).encode('ascii', 'ignore')
	
	for code_lang, nom_lang in langues.langues.items():
		if(code2 == code_lang):
			s1 = unicode(nom_lang,'utf-8')
			nom_lang2 = unicodedata.normalize('NFD', s1).encode('ascii', 'ignore')
			## print code2 + u' ' + nom_lang2 + '\n'
			if (nom_lang2 < u'espagnol'): return 1
			else: return -1
	return 0
	
# Lecture du fichier es_conj.xml
def crawlerFile(source, commenceA):
	if source:
		PagesHS = codecs.open(source,"r","utf-8")
		PageEspagnol = u''
		titre = u''
		ligne = u''
		ok = False
		while True:
			ligne = PagesHS.readline()
			if ligne.find(u'xxxx') != -1:
				titre = PagesHS.readline()
				titre = titre[3:-4]
				## print titre

			if len(commenceA)>0:
				if not ok:
					if titre != commenceA:
						continue
					else:
						ok = True
			
			if ligne.find(u'yyyy') == -1 and \
			       ligne.find(u'xxxx') == -1 and \
			       ligne.find(u'{{clé de tri|') == -1 and \
			       ligne.find(u'{{vérifier création automatique||es}}') == -1:	
				PageEspagnol += ligne
			
			if  (ligne.find(u'yyyy') != -1 and titre):
				## print u'////////////////////'
				## print titre
			        ## print PageEspagnol
				## print u'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'
				modification(titre, PageEspagnol)
				titre  = u''
				PageEspagnol = u''
				## break
				
		PagesHS.close()
		
		if len(commenceA)>0 and not ok:
			print commenceA + u' n\'a pas été trouvé'
		

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
		print PageCourante.title()
		if PageCourante.title().find(u'Utilisateur:PamputtBot/') != -1:
			print u'On arrête'
			ArretDUrgence()
		if not summary: summary = u'Ajout de la forme conjuguée en espagnol'
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

fout = codecs.open(u'aTraiterManuellement.txt',"a","utf-8")

fcodeout = codecs.open(u'codeLangue.txt',"w","utf-8")

TraitementFichier = crawlerFile(u'es_conj.xml', sys.argv[1].decode("utf-8"))
## modification(u'abandera', u'>>>  test  <<<')
## modification(u'abandonas', u'>>>  test  <<<')
fout.close()
