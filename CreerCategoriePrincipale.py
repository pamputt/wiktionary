#! /usr/bin/python3

# -*- coding: utf-8 -*-

import csv
import pywikibot

import CleDeTri

test = False # to test the script (without saving the result)

def getListOfCategories():
  page = pywikibot.Page(pywikibot.getSite(), "Wiktionnaire:Statistiquesb")
  wikitext = page.get()

  lines = wikitext.split(u'\n')

  languages = []
  for line in lines:
    #print(">>> " + line)
    # |align="left" bgcolor="#EEEEEE" |[[:Catégorie:movima|movima]]||bgcolor='#A9F5F2'|4|| bgcolor='#FFFFFF'|0 || bgcolor='#F1C5F9'|4|| 0|| bgcolor='#FAC865'|4||4||0||0||0|| 0 ||0||bgcolor='#F7BE81'|4 ||0 ||  0
    beg = line.find(u'[[:Catégorie:')
    if (beg == -1):
      continue
    end = line.find("|",beg+1)
    languages.append(line[beg+13:end])

  return languages

def isCategoryExist(language):

  page = pywikibot.Page(pywikibot.getSite(), u'Catégorie:'+language)

  try:
    text = page.get()
  except pywikibot.NoPage:
    return False
  except pywikibot.IsRedirectPage:
    return False

  return True

def createCategory(language,code):  
  if (language not in code):
    return
  
  wikitext = "Cette catégorie réunit les mots et locutions en [[" + language + "]] (code <code>" + code[language] + "</code>). "
  wikitext += "La [[:Catégorie:Grammaire en " + language + "|section grammaire]] contient tous les types de mots comme les [[:Catégorie:Noms communs en " + language + "|noms communs]] ou les [[:Catégorie:Acronymes en " + language + "|acronymes]]. Elle contient en outre des sous-catégories thématiques : [[:Catégorie:Animaux en " + language + "|noms d’animaux]] ou [[:Catégorie:Lexique en " + language + " de la musique|lexique de la musique]], ou encore des catégories d’[[:Catégorie:Expressions en " + language + "|expressions]], ou enfin des registres de langue.\n"
  wikitext += "* '''[[:Catégorie:Grammaire en " + language + "|Grammaire]]'''\n"
  wikitext += "* '''[[:Catégorie:Thématiques en " + language + "|Thématiques]]'''\n"
  wikitext += "* '''[[:Catégorie:Lexiques en " + language + "|Lexiques]]'''\n\n"
#  wikitext += "{{CatégorieTDM}}\n"
  wikitext += "<!--- Voir aussi les [[Special:Whatlinkshere/Modèle:" + language + "|mots traduits en " + language + "]]. --->Voir aussi les [[:catégorie:Traductions en " + language + "|mots traduits en " + language + "]].\n\n"
  wikitext += "[[Catégorie:Langues"
  if(CleDeTri.CleDeTri(language)!=language):
    wikitext += "|" + CleDeTri.CleDeTri(language)
  wikitext += "]]"


  page = pywikibot.Page(pywikibot.getSite(), "Catégorie:"+language)
  if not test:
    page.put(wikitext)
  else:
    pywikibot.output(page.title() + u' :\n' + wikitext)


def WantedPagesCategoryGenerator(total=100, site=None):
  """
  Wanted category generator.

  @param total: Maximum number of pages to retrieve in total
  @type total: int
  @param site: Site for generator results.
  @type site: L{pywikibot.site.BaseSite}
  """

  if site is None:
    site = pywikibot.Site()
  for page in site.wantedcategories(total=total):
    yield page

def getLanguageCodes():

  language = {}
  with open("liste_langue.dat") as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
      name, code, key = row
      language[name] = code

  return language

def main():
  CategoriesDemandees=True
  
  codes = getLanguageCodes()
  
  if (CategoriesDemandees):
    for page in WantedPagesCategoryGenerator(5000):
      #Convert Category into string object
      page = str(page)
      beg=page.find(":Catégorie:")
      end=page.find("]]")
      page = page[beg+11:end]
      print("Treating " + page)
      exist = isCategoryExist(page)
      if exist:
        continue
      createCategory(page,codes)
  else:
    languages = getListOfCategories()
#   createCategory("shall-zwall",codes)
    for language in languages:
      print("Treating " + language)
      exist = isCategoryExist(language)
      if exist:
        continue
      createCategory(language,codes)
    

if __name__ == '__main__':

  try:

    main()
    
  finally:

    pywikibot.stopme()
