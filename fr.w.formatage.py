﻿#!/usr/bin/env python
# Ce script :
# 	Vérifie tous les hyperliens, les marque comme {{lien brisé}} le cas échéant, et traduit leurs modèles en français
# 	Retire les espaces dans {{FORMATNUM:}} qui empêche de les trier dans les tableaux
# 	Ajoute des liens vers les projets frères dans les pages d'homonymie, multilatéralement
# A terme peut-être :
# 	Mettra à jour les liens vers les projets frères existants (fusions avec Sisterlinks...), et remplacement des liens bleu fr.wikipedia.org/wiki par [[ ]], des liens rouges par {{lien|lang=xx}}
# 	Mettra à jour les évaluations à partir du bandeau ébauche
# 	Corrigera les fautes d'orthographes courantes, signalées dans http://fr.wikipedia.org/wiki/Wikip%C3%A9dia:AutoWikiBrowser/Typos (semi-auto) ou : python cosmetic_changes.py -lang:"fr" -recentchanges

# Importation des modules
import os, catlib, pagegenerators, re
import hyperlynx, HTMLUnicode		# Faits maison
from wikipedia import *

# Déclaration
language = "fr"
family = "wikipedia"
mynick = "JackBot"
site = getSite(language,family)
debogage = False
debogageLent = False
output = u'articles_WPout.txt'

# Modification du wiki
def modification(PageHS):
	summary = u'Formatage'
	page = Page(site,PageHS)
	print(PageHS.encode(config.console_encoding, 'replace'))
	if not page.exists(): return
	if page.namespace() != 0 and PageHS.find(u'Utilisateur:JackBot/test') == -1 and PageHS.find(u'Modèle:Cite pmid/') == -1: return
	try:
		PageBegin = page.get()
	except wikipedia.NoPage:
		print "NoPage"
		return
	except wikipedia.IsRedirectPage:
		print "Redirect page"
		return
	except wikipedia.LockedPage:
		print "Locked/protected page"
		return
	if PageBegin.find(u'{{en travaux') != -1 or PageBegin.find(u'{{En travaux') != -1:
		print "Page en travaux"
		return
	PageTemp = PageBegin
	
	# Traitements des URL et leurs modèles
	if debogage == True: print u'Test des URL'
	PageTemp = hyperlynx.hyperlynx(PageTemp, debogage)
	if debogage == True: print (u'--------------------------------------------------------------------------------------------')
	if PageTemp != PageBegin:
		summary = summary + u', [[Wikipédia:Bot/Requêtes/2012/11#Identifier les liens brisés (le retour ;-))|Vérification des liens externes]]'
		summary = summary + u', [[Wikipédia:Bot/Requêtes/2012/12#Remplacer_les_.7B.7BCite_web.7D.7D_par_.7B.7BLien_web.7D.7D|traduction de leurs modèles]]'
	regex = ur'({{[l|L]ien *\|[^}]*)traducteur( *=)'
	if re.search(regex, PageTemp):
		PageTemp = re.sub(regex, ur'\1trad\2', PageTemp)
	
	# Autres modèles (https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Page_utilisant_un_mod%C3%A8le_avec_un_param%C3%A8tre_obsol%C3%A8te)
	PageTemp = PageTemp.replace(u'{{Reflist|2}}', u'{{Références}}')
	PageTemp = PageTemp.replace(u'{{reflist|2}}', u'{{Références}}')
	PageTemp = PageTemp.replace(u'{{Reflist|3}}', u'{{Références}}')
	PageTemp = PageTemp.replace(u'{{reflist|3}}', u'{{Références}}')
	PageTemp = PageTemp.replace(u'{{Reflist|30em}}', u'{{Références}}')
	PageTemp = PageTemp.replace(u'{{reflist|30em}}', u'{{Références}}')
	PageTemp = PageTemp.replace(u'{{Reflist|colwidth = 30em}}', u'{{Références}}')
	PageTemp = PageTemp.replace(u'{{Reflist|colwidth=40em}}', u'{{Références}}')
	PageTemp = PageTemp.replace(u'{{Références|2}}', u'{{Références}}')
	PageTemp = PageTemp.replace(u'{{références|2}}', u'{{Références}}')
	PageTemp = PageTemp.replace(u'{{Références|30em}}', u'{{Références}}')
	PageTemp = PageTemp.replace(u'{{références|colonnes}}', u'{{Références}}')
	PageTemp = PageTemp.replace(u'{{Références|taille}}', u'{{Références}}')
	
	# Rustine temporaire pour https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Page_du_mod%C3%A8le_Article_comportant_une_erreur
	'''
	PageEnd = u''
	while PageTemp.find(u'{{article') != -1:
		PageEnd = PageEnd + PageTemp[:PageTemp.find(u'{{article')+len(u'{{article')]
		PageTemp = PageTemp[PageTemp.find(u'{{article')+len(u'{{article'):]
		if PageTemp.find(u'éditeur=') != -1 and PageTemp.find(u'éditeur=') < PageTemp.find(u'}}') and (PageTemp.find(u'périodique=') == -1 or PageTemp.find(u'périodique=') > PageTemp.find(u'}}')) and (PageTemp.find(u'revue=') == -1 or PageTemp.find(u'revue=') > PageTemp.find(u'}}')) and (PageTemp.find(u'journal=') == -1 or PageTemp.find(u'journal=') > PageTemp.find(u'}}')):
			PageEnd = PageEnd + PageTemp[:PageTemp.find(u'éditeur=')] + u'périodique='
			PageTemp = PageTemp[PageTemp.find(u'éditeur=')+len(u'éditeur='):]
	PageTemp = PageEnd + PageTemp
	PageEnd = u''
	while PageTemp.find(u'{{Article') != -1:
		PageEnd = PageEnd + PageTemp[:PageTemp.find(u'{{Article')+len(u'{{Article')]
		PageTemp = PageTemp[PageTemp.find(u'{{Article')+len(u'{{Article'):]
		if PageTemp.find(u'éditeur=') != -1 and PageTemp.find(u'éditeur=') < PageTemp.find(u'}}') and (PageTemp.find(u'périodique=') == -1 or PageTemp.find(u'périodique=') > PageTemp.find(u'}}')) and (PageTemp.find(u'revue=') == -1 or PageTemp.find(u'revue=') > PageTemp.find(u'}}')) and (PageTemp.find(u'journal=') == -1 or PageTemp.find(u'journal=') > PageTemp.find(u'}}')):
			PageEnd = PageEnd + PageTemp[:PageTemp.find(u'éditeur=')] + u'périodique='
			PageTemp = PageTemp[PageTemp.find(u'éditeur=')+len(u'éditeur='):]		
	PageTemp = PageEnd + PageTemp
	'''
	
	# Rustine pour https://fr.wikipedia.org/w/index.php?title=Achille_Varzi&diff=123170171&oldid=122929021
	PageTemp = PageTemp.replace(u'{{lien mortarchive|',u'{{lien mort archive|')
	
	# Nombres
	PageTemp = re.sub(ur'{{ *(formatnum|Formatnum|FORMATNUM)\:([0-9]*) *([0-9]*)}}', ur'{{\1:\2\3}}', PageTemp)

	# Protocoles
	PageTemp = PageTemp.replace(u'http://http://', u'http://')
	
	# Analyse des crochets et accolades (à faire : hors LaTex)
	if PageTemp.count('{') - PageTemp.count('}') != 0:
		if PageHS.find(u'Utilisateur:JackBot/') == -1: log(u'*[[' + PageHS + u']] : accolade cassée')
		#if debogageLent == True: raise Exception(u'Accolade cassée')
	if PageTemp.count('[') - PageTemp.count(']') != 0:
		if PageHS.find(u'Utilisateur:JackBot/') == -1: log(u'*[[' + PageHS + u']] : crochet cassé')
		#if debogageLent == True: raise Exception(u'Crochet cassé')
	if PageBegin.count('[[') - PageBegin.count(']]') != PageTemp.count('[[') - PageTemp.count(']]'):
		txtfile = codecs.open(output, 'a', 'utf-8')
		txtfile.write(PageTemp + u'\n\n------------------------------------------------------------------------------------------------------------\n\n')
		txtfile.close()	
		if debogage == True: print u'Crochets cassés'	#raise Exception(u'Crochets cassés')
		return
	if PageBegin.count('{{') - PageBegin.count('}}') != PageTemp.count('{{') - PageTemp.count('}}'):
		txtfile = codecs.open(output, 'a', 'utf-8')
		txtfile.write(PageTemp + u'\n\n------------------------------------------------------------------------------------------------------------\n\n')
		txtfile.close()	
		if debogage == True: print u'Accolades cassées'	#raise Exception(u'Accolades cassées')
		return

	# Catégories
	if PageHS.find(u'Modèle:Cite pmid/') != -1:
		PageTemp = PageTemp.replace(u'Catégorie:Modèle de source‎', u'Catégorie:Modèle pmid')
		PageTemp = PageTemp.replace(u'[[Catégorie:Modèle pmid]]', u'[[Catégorie:Modèle pmid‎|{{SUBPAGENAME}}]]')

	# Sauvegarde
	PageEnd = PageTemp
	if PageEnd != PageBegin and PageEnd != PageBegin.replace(u'{{chapitre |', u'{{chapitre|') and PageEnd != PageBegin.replace(u'{{Chapitre |', u'{{Chapitre|'):
		PageEnd = re.sub(ur'<br>', ur'<br/>', PageEnd)
		PageEnd = PageEnd.replace(ur'</ref><ref>', ur'</ref>{{,}}<ref>', )
		sauvegarde(page,PageEnd,summary)
		
# Traitement d'une catégorie
def crawlerCat(category):
	cat = catlib.Category(site, category)
	pages = cat.articlesList(False)
	for Page in pagegenerators.PreloadingGenerator(pages,100):
		main = Page.title()
		main = main[11:len(main)]
		modification(main)
	subcat = cat.subcategories(recurse = True)
	for subcategory in subcat:
		pages = subcategory.articlesList(False)
		for Page in pagegenerators.PreloadingGenerator(pages,100):
			#if not crawlerFile(Page.title()):
			main = Page.title()
			main = main[11:len(main)]
			modification(main)

# Traitement des modèles PMID
def crawlerCatPMID(category):
	cat = catlib.Category(site, category)
	pages = cat.articlesList(False)
	for Page in pagegenerators.PreloadingGenerator(pages,100):
		main = Page.title()
		#main = main[11:len(main)]
		if main.find(u'pmid') != -1:
			modification(main)
			
# Traitement des pages liées			
def crawlerLink(pagename):
	#pagename = unicode(arg[len('-links:'):], 'utf-8')
	page = wikipedia.Page(site, pagename)
	gen = pagegenerators.ReferringPageGenerator(page)
	#gen =  pagegenerators.NamespaceFilterPageGenerator(gen, namespaces)
	for Page in pagegenerators.PreloadingGenerator(gen,100):
		if Page.namespace() == 1: modification(Page.title())
		elif Page.namespace() == 0: modification(u'Discussion:' + Page.title())

# Blacklist
def crawlerFile(PageCourante):
    PagesHS = open(u'BL.txt', 'r')
    while 1:
		PageHS = PagesHS.readline()
		fin = PageHS.find("\t")
		PageHS = PageHS[0:fin]
		if PageHS == '': 
			break
		elif PageHS == PageCourante: 
			return "False"
    PagesHS.close()
	
# Lecture du fichier articles_list.txt (au même format que pour replace.py)
def crawlerFile(source):
	if source:
		PagesHS = open(source, 'r')
		while 1:
			PageHS = PagesHS.readline()
			fin = PageHS.find("\t")
			PageHS = PageHS[0:fin]
			if PageHS == '': break
			if PageHS.find('[[') != -1:
				PageHS = PageHS[PageHS.find('[[')+2:len(PageHS)]
			if PageHS.find(']]') != -1:
				PageHS = PageHS[0:PageHS.find(']]')]
			modification(HTMLUnicode.HTMLUnicode(PageHS))
		PagesHS.close()

# Traitement d'une catégorie
def crawlerCat(category,recursif,apres):
	modifier = u'False'
	cat = catlib.Category(site, category)
	pages = cat.articlesList(False)
	gen =  pagegenerators.NamespaceFilterPageGenerator(pages, [0])
	for Page in pagegenerators.PreloadingGenerator(gen,100):
		if not apres or apres == u'' or modifier == u'True':
			modification(Page.title()) #crawlerLink(Page.title())
		elif Page.title() == apres:
			modifier = u'True'
	if recursif == True:
		subcat = cat.subcategories(recurse = True)
		for subcategory in subcat:
			pages = subcategory.articlesList(False)
			for Page in pagegenerators.PreloadingGenerator(pages,100):
				modification(Page.title())

# Traitement des pages liées
def crawlerLink(pagename,apres):
	modifier = u'False'
	#pagename = unicode(arg[len('-links:'):], 'utf-8')
	page = wikipedia.Page(site, pagename)
	gen = pagegenerators.ReferringPageGenerator(page)				#,onlyTemplateInclusion=True
	gen =  pagegenerators.NamespaceFilterPageGenerator(gen, [0])	#Même désactivé, survient le bug du quota (de 500 + 300 transclusions ?). Cela fonctionne sur AWB
	for Page in pagegenerators.PreloadingGenerator(gen,100):
		#print(Page.title().encode(config.console_encoding, 'replace'))
		if not apres or apres == u'' or modifier == u'True':
			modification(Page.title()) #crawlerLink(Page.title())
		elif Page.title() == apres:
			modifier = u'True'
			
# Traitement des pages liées des entrées d'une catégorie
def crawlerCatLink(pagename,apres):
	modifier = u'False'
	cat = catlib.Category(site, pagename)
	pages = cat.articlesList(False)
	gen =  pagegenerators.NamespaceFilterPageGenerator(pages, [0])
	for Page in pagegenerators.PreloadingGenerator(gen,100):
		page = wikipedia.Page(site, Page.title())
		gen = pagegenerators.ReferringPageGenerator(page)
		#gen =  pagegenerators.NamespaceFilterPageGenerator(gen, namespaces)
		for PageLiee in pagegenerators.PreloadingGenerator(gen,100):
			#print(Page.title().encode(config.console_encoding, 'replace'))
			if not apres or apres == u'' or modifier == u'True':
				modification(PageLiee.title()) #crawlerLink(Page.title())
			elif PageLiee.title() == apres:
				modifier = u'True'
				
# Traitement d'une recherche
def crawlerSearch(pagename):
	gen = pagegenerators.SearchPageGenerator(pagename, site = site, namespaces = ns)
	for Page in pagegenerators.PreloadingGenerator(gen,100):
		modification(Page.title())

# Traitement des modifications récentes
def crawlerRC():
	gen = pagegenerators.RecentchangesPageGenerator()
	for Page in pagegenerators.PreloadingGenerator(gen,100):
		modification(Page.title())

# Traitement des modifications d'un compte
def crawlerUser(username):
	gen = pagegenerators.UserContributionsGenerator(username)
	for Page in pagegenerators.PreloadingGenerator(gen,100):
		modification(Page.title())

# Toutes les redirections
def crawlerRedirects():
	for Page in site.allpages(start=u'', namespace=ns, includeredirects='only'):
		modification(Page.title())	
										
# Traitement de toutes les pages du site
def crawlerAll(start):
	gen = pagegenerators.AllpagesPageGenerator(start,namespace=ns,includeredirects=False)
	for Page in pagegenerators.PreloadingGenerator(gen,100):
		#print (Page.title().encode(config.console_encoding, 'replace'))
		modification(Page.title())

def trim(s):
    return s.strip(" \t\n\r\0\x0B")

def log(source):		
	txtfile = codecs.open(output, 'a', 'utf-8')
	txtfile.write(source + u'\n')
	txtfile.close()
	
def filtre(projets,langue,PageHS):
	projets2 = projets[projets.find(langue + u'='):len(projets)]
	if projets2.find(u'\n') == -1:
		return projets[0:projets.find(langue + u'=')] + u'w=' + PageHS
	else:
		return projets[0:projets.find(langue + u'=')] + u'w=' + PageHS + projets[projets.find(langue + u'=')+projets2.find(u'\n'):len(projets)]			

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
			print(Contenu[max(len(Contenu)-taille,0):].encode(config.console_encoding, 'replace'))
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
debogage = False
if len(sys.argv) > 1:
	DebutScan = u''
	if len(sys.argv) > 2:
		if sys.argv[2] == u'debug':
			debogage = True
		else:
			DebutScan = sys.argv[2]
	if sys.argv[1] == u'test':
		TraitementPage = modification(u'Utilisateur:' + mynick + u'/test')
	elif sys.argv[1] == u'test2':
		TraitementPage = modification(u'Utilisateur:' + mynick + u'/test2')
	elif sys.argv[1] == u'txt':
		TraitementFichier = crawlerFile(u'articles_' + language + u'_' + family + u'.txt')
	elif sys.argv[1] == u'txt2':
		TraitementFichier = crawlerFile(u'articles_' + language + u'_' + family + u'2.txt')
	elif sys.argv[1] == u'u':
		TraitementUtilisateur = crawlerUser(u'Utilisateur:JackBot')
	elif sys.argv[1] == u'r':
		if len(sys.argv) > 2:
			TraitementRecherche = crawlerSearch(sys.argv[2])
		else:
			TraitementRecherche = crawlerSearch(u'chinois')
	elif sys.argv[1] == u'mod':
		modification(u'Modèle:Cladogramme Paraves')
	elif sys.argv[1] == u'm':
		TraitementLiens = crawlerLink(u'Modèle:périodique',u'')
	elif sys.argv[1] == u'cat':
		#TraitementCategory = crawlerCat(u'Catégorie:Page utilisant un modèle avec un paramètre obsolète',False,u'')
		TraitementCategory = crawlerCat(u'Page du modèle Article comportant une erreur',False,u'')
		#TraitementCategory = crawlerCat(u'Catégorie:Page utilisant un modèle avec une syntaxe erronée',True,u'')	# En test
	elif sys.argv[1] == u'page':
		TraitementPage = modification(u'Utilisateur:JackBot/test unitaire')
	else:
		TraitementPage = modification(sys.argv[1])	# Format http://tools.wmflabs.org/jackbot/xtools/public_html/unicode-HTML.php
else:
	# Quotidiennement :
	TraitementCatPMID = crawlerCatPMID(u'Catégorie:Modèle de source')
	TraitementLiens = crawlerLink(u'Modèle:Cite web',u'')
	TraitementLiens = crawlerLink(u'Modèle:Cite journal',u'')
	TraitementLiens = crawlerLink(u'Modèle:Cite news',u'')
	TraitementLiens = crawlerLink(u'Modèle:Cite press release',u'')
	TraitementLiens = crawlerLink(u'Modèle:Cite episode',u'')
	TraitementLiens = crawlerLink(u'Modèle:Cite video',u'')
	TraitementLiens = crawlerLink(u'Modèle:Cite conference',u'')
	TraitementLiens = crawlerLink(u'Modèle:Cite arXiv',u'')
	TraitementLiens = crawlerLink(u'Modèle:Lien news',u'')
	TraitementLiens = crawlerLink(u'Modèle:Lien mort',u'')
	TraitementLiens = crawlerLink(u'Modèle:Docu',u'')
	TraitementLiens = crawlerLink(u'Modèle:Cita web',u'')
	TraitementLiens = crawlerLink(u'Modèle:Cita noticia',u'')
	TraitementLiens = crawlerLink(u'Modèle:Cite book',u'')
'''
while 1:
	TraitementRC = crawlerRC()
'''

