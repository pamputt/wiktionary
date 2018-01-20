#! /usr/bin/python3

# -*- coding: utf-8 -*-

import csv
import pywikibot

import CleDeTri

test = False # to test the script (without saving the result)

def createCategoryGrammaire(page,cle):
  #Grammaire en abu’‏‎
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "Cette catégorie a pour but de réunir les sous-catégories traitant de la grammaire en " + language + ", notamment :\n"
  wikitext += "* Les natures de mots (nom, verbe…)\n"
  wikitext += "* Les formes (locutions, sigles…)\n"
  wikitext += "* les formes infléchies, déclinées, conjuguées…\n\n"
  wikitext += "[[Catégorie:" + language + "|Grammaire]]\n"
  wikitext += "[[Catégorie:Grammaire par langue|" + cle[language] +"]]"
  return wikitext

def createCategoryLexiqueBotanique(page,cle):
  #Catégorie:Lexique en italien de la botanique
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "Cette catégorie recense les mots en " + language + " ayant trait à la [[botanique]].\n\n"
  wikitext += "[[Catégorie:Lexiques en " + language + " de la biologie|botanique]]\n"
  wikitext += "[[Catégorie:Botanique|" + cle[language] + "]]"
  return wikitext;

def createCategoryLexiqueClimatologie(page,cle):
  #Catégorie:Lexique en français de la climatologie
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|climatologie]]\n"
  wikitext += "[[Catégorie:Climatologie|" + cle[language] + "]]"
  return wikitext;

def createCategoryLexiqueGrammaire(page,cle):
  #Catégorie:Lexique en italien de la grammaire
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|grammaire]]\n"
  wikitext += "[[Catégorie:Grammaire|" + cle[language] + "]]"
  return wikitext;

def createCategoryLexiqueMathematiques(page,cle):
  #Catégorie:Lexique en italien des mathématiques
  beg=page.find(" en ")
  end=page.find(" des ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|mathematiques]]\n"
  wikitext += "[[Catégorie:Mathématiques|" + cle[language] + "]]"
  return wikitext;

def createCategoryLocalitesDeEn(page,cle,countryList):
  #Catégorie:Localités d’Italie en français
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  particle = ""
  if(page.find("Localités d’") != -1):
    particle="d’"
  elif(page.find("Localités de") != -1):
    particle="de "
  elif(page.find("Localités du") != -1):
    particle="du "
  elif(page.find("Localités des") != -1):
    particle="des "

  
  country = ""
  if(particle=="de "):
    beg=page.find(" de ")
    end=page.find(" en ")
    country = page[beg+4:end]
  elif(particle=="d’"):
    beg=page.find(" d’")
    end=page.find(" en ")
    country = page[beg+3:end]
  elif(particle=="du "):
    beg=page.find(" du ")
    end=page.find(" en ")
    country = page[beg+4:end]
  elif(particle=="des "):
    beg=page.find(" des ")
    end=page.find(" en ")
    country = page[beg+5:end]

  # If the country in not in the list, then one does not process it
  if (country not in countryList):
    print(country + " :/")
    return

  wikitext = "[[Catégorie:Localités " + particle + country + "|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Localités en " + language + "|" + CleDeTri.CleDeTri(country) + "]]\n"
  wikitext += "[[Catégorie:" + country + " en " + language + "]]"

  return wikitext

def createCategoryMotsEnIssusDunMot(page,cle):
  #Mots en français issus d’un mot en catalan
  beg=page.find(" en ")
  end=page.find(" issus")
  language1=page[beg+4:end]
  beg=page.find(" en ", end)
  language2=page[beg+4:]
  if ((language1 not in cle) or
      (language2 not in cle)):
    return

  wikitext = "[[Catégorie:Origines étymologiques des mots en " + language1 + "|" + cle[language2] + "]]\n"
  wikitext += "[[Catégorie:Mots issus d’un mot en " + language2 + "|" + cle[language1] + "]]"
  return wikitext

def createCategoryMotsIssusDunMot(page,cle):
  #Mots issus d’un mot en abouré‏‎
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  wikitext = "[[Catégorie:Origines étymologiques des mots|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:" + language + "]]"
  return wikitext

def createCategoryNombres(page,cle):
  #Catégorie:Nombres en anglais
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  wikitext = "[[Catégorie:Nombres|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " des mathématiques]]"

  return wikitext


def createCategoryNomsCommuns(page,cle):
  #Catégorie:Noms communs en saho‏‎
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "[[Catégorie:Noms communs|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Grammaire en " + language + "]]"
  return wikitext

def createCategoryNomsPropresIssus(page,cle):
  #Catégorie:Noms propres en français issus d’un mot en catalan
  beg=page.find(" en ")
  end=page.find(" issus")
  language1=page[beg+4:end]
  beg=page.find(" en ", end)
  language2=page[beg+4:]
  if ((language1 not in cle) or
      (language2 not in cle)):
    return
  
  wikitext = "[[Catégorie:Mots en " + language1 + " issus d’un mot en " + language2 + "|" + cle[language1] + "]]\n"
  wikitext += "[[Catégorie:Origines étymologiques des noms propres en " + language1 + "|" + cle[language2] + "]]"

  return wikitext

def createCategoryOriginesEtmylogiquesMots(page,cle):
  #Origines étymologiques des mots en néerlandais
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return


  wikitext = "{{CatégorieTDM}}\n\n"
  wikitext = "Cette catégorie liste les catégories relatives aux différentes origines [[étymologique]]s des mots (et locutions) en " + language + ".\n\n"
  wikitext += "==== Note ====\n"
  wikitext += ": L’[[étymologie]] n’étant pas une [[w:Sciences exactes|science exacte]], il se pourrait que ce référencement retranscrive plusieurs hypothèses étymologiques. Merci de bien vérifier dans la section ''Étymologie'' des articles concernés.\n\n"
  wikitext += "[[Catégorie:Origines étymologiques des mots|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:" + language + "]]"
  
  return wikitext

def createCategoryPrononciationAudio(page,cle):
  #Catégorie:Prononciations audio en biélorusse‏‎
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "__HIDDENCAT__\n"
  wikitext += "[[Catégorie:Prononciations audio|" + cle[language] + "]]"
  return wikitext

def createCategoryOriginesEtmylogiquesNomsPropres(page,cle):
  #Origines étymologiques des noms propres en néerlandais
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  wikitext = "[[Catégorie:Origines étymologiques des mots en " + language + "|noms propres]]\n"
  wikitext += "[[Catégorie:Noms propres en " + language + "]]\n"
  wikitext += "[[Catégorie:Origines étymologiques des noms propres|" + cle[language] + "]]"
  
  return wikitext

def createCategoryThematiques(page,cle):
  #Catégorie:Thématiques en anglais
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext ="Cette catégorie réunit les mots en " + language + " de même sujet : les [[:Catégorie:Animaux en " + language + "|noms d'animaux]], [[:Catégorie:Plantes en " + language + "|de plantes]], etc.\n"
  wikitext += "Consultez aussi la [[:Catégorie:Lexiques en " + language + "|catégorie des terminologies]] relatives à différents domaines comme la [[:Catégorie:Lexique en " + language + " de la médecine|médecine]] ou la [[:Catégorie:Lexique en " + language + " de la biologie|biologie]].\n\n"
  wikitext += "[[Catégorie:" + language + "|Thematiques]]\n"
  wikitext += "[[Catégorie:Thématiques par langue|" + cle[language] + "]]"

  return wikitext

def createCategoryTraductions(page,cle):
  #Catégorie:Thématiques en anglais
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  wikitext = "{{CatégorieTDM}}\n"
  wikitext += "__HIDDENCAT__\n\n"

  wikitext += "[[Catégorie:Traductions|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:" + language + "]]"


  return wikitext

def createCategory(page,cle,country):  
  #Convert Category into string object
  page = str(page)
  beg=page.find(":")
  end=page.find("]]")
  page = page[beg+1:end]

  wikitext = ""
  if (page.find("Catégorie:Prononciations audio en") != -1):
     wikitext = createCategoryPrononciationAudio(page,cle)
  elif (page.find("Catégorie:Grammaire en") != -1):
     wikitext = createCategoryGrammaire(page,cle)
  elif (page.find("Catégorie:Noms communs en") != -1):
     wikitext = createCategoryNomsCommuns(page,cle)
  elif ((page.find("Catégorie:Noms propres en") != -1) and
        (page.find("issus d’un mot en") != -1)):
    wikitext = createCategoryNomsPropresIssus(page,cle)
  elif ((page.find("Catégorie:Mots en") != -1) and
        (page.find("issus d’un mot en") != -1)):
    wikitext = createCategoryMotsEnIssusDunMot(page,cle)
  elif (page.find("Catégorie:Mots issus d’un mot en ") != -1):
    wikitext = createCategoryMotsIssusDunMot(page,cle)
  elif (page.find("Catégorie:Origines étymologiques des mots en ") != -1):
    wikitext = createCategoryOriginesEtmylogiquesMots(page,cle)
  elif (page.find("Catégorie:Origines étymologiques des noms propres en ") != -1):
    wikitext = createCategoryOriginesEtmylogiquesNomsPropres(page,cle)
  elif (page.find("Catégorie:Nombres en ") != -1):
    wikitext = createCategoryNombres(page,cle)
  elif (page.find("Catégorie:Localités d") != -1 and
        (page.find(" en ") != -1)):
    wikitext = createCategoryLocalitesDeEn(page,cle,country)
  elif (page.find("Catégorie:Thématiques en ") != -1):
    wikitext = createCategoryThematiques(page,cle)
  elif (page.find("Catégorie:Traductions en ") != -1):
    wikitext = createCategoryTraductions(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" des mathématiques") != -1)):
    wikitext = createCategoryLexiqueMathematiques(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la grammaire") != -1)):
    wikitext = createCategoryLexiqueGrammaire(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la climatologie") != -1)):
    wikitext = createCategoryLexiqueClimatologie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la botanique") != -1)):
    wikitext = createCategoryLexiqueBotanique(page,cle)
  else:
    return

  if not wikitext:
    return
  
  pwbpage = pywikibot.Page(pywikibot.getSite(), page)
  if not test:
    pwbpage.put(wikitext)
  else:
    pywikibot.output(page + u' :\n' + wikitext)


def getSortingKey():

  cledetri = {}
  with open("liste_langue.dat") as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
      name, code, key = row
      cledetri[name] = key

  return cledetri

def getCountryList():

  country = []
  f = open("country.csv",'r')
  lines  = f.readlines()
  f.close()

  for line in lines:
    country.append(line[:len(line)-1])

  return country

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

def main():
  cle = getSortingKey()
  countryList = getCountryList()

  if test:
    createCategory("[[:Catégorie:Thématiques en nahuatl de l’Isthme de Mecayapan]]",cle,countryList)
  #UserContributionsGenerator
  else:
    for page in WantedPagesCategoryGenerator(5000):
      createCategory(page,cle,countryList)
  

if __name__ == '__main__':

  try:

    main()
    
  finally:

    pywikibot.stopme()
