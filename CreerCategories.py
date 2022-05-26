#! /usr/bin/python3

# -*- coding: utf-8 -*-

import csv
import pywikibot

import CleDeTri

test = False # to test the script (without saving the result)

def createCategoryCalquesEn(page,cle):
  #Calques en anglais
  language = guessLanguage(page,"en","",cle)
  if not language:
    return

  wikitext = "[[Catégorie:Calques par langue|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Origines étymologiques des mots en " + language + "| Calque]]"
  return wikitext

def createCategoryCalquesIssus(page,cle):
  #Calques issus du français
  #Calques issus de l’éwé‏‎
  beg=page.find(" issus ")+7
  end=page.find("du ", beg)+3
  if end==2: #-1 + 3 = 2
    end=page.find("de l’", beg)+5
  language=page[end:]
  if language not in cle:
    return

  wikitext = "[[Catégorie:Calques issus d’une langue|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Mots issus d’un mot en " + language + "| Calque]]"
  return wikitext

def createCategoryCalquesEnIssusDunMot(page,cle):
  #Calques en français issus d’un mot en anglais
  beg=page.find(" en ")
  end=page.find(" issus")
  language1=page[beg+4:end]
  beg=page.find(" en ", end)
  language2=page[beg+4:]
  if ((language1 not in cle) or
      (language2 not in cle)):
    return
  
  listConsonnes = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
  particle = " de l’"
  if language2[0:1] in listConsonnes:
    particle = " du "

  wikitext = "[[Catégorie:Calques en " + language1 + "|" + cle[language2] + "]]\n"
  wikitext += "[[Catégorie:Calques issus" + particle + language2 + "|" + cle[language1] + "]]\n"
  wikitext += "[[Catégorie:Mots en " + language1 + " issus d’un mot en " + language2 + "]]"
  return wikitext

def createCategoryEmpruntsEn(page,cle):
  #Catégorie:Emprunts en biélorusse
  beg = page.find(" en ")+4
  language = page[beg:]
  if language not in cle:
    return
  
  wikitext = "[[Catégorie:Emprunts par langue|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Origines étymologiques des mots en " + language + "| Emprunts]]"
  return wikitext

def createCategoryEmpruntsVers(page,cle):
  #Catégorie:Emprunts vers le biélorusse
  beg = page.find(" le ")+4
  if (beg == 3):
    beg = page.find("l’")+2
  language = page[beg:]
  if language not in cle:
    return
  
  wikitext = "[[Catégorie:Emprunts vers une langue|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Emprunts en " + language + "|vers]]"
  return wikitext

def createCategoryCaractereEn(page,cle):
  #Catégorie:Caractère 吹 en japonais
  language = guessLanguage(page,"en","",cle)
  if not language:
    return
  
  wikitext = "{{tableau han/cat}}"
  return wikitext

def createCategoryCompositionsEn(page,cle):
  #Catégorie:Compositions en suédois
  language = guessLanguage(page,"en","",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Compositions|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Origines étymologiques des mots en " + language + "| Compositions]]"
  return wikitext

def createCategoryConjugaisonsManquantes(page,cle):
  #Catégorie:Wiktionnaire:Conjugaisons manquantes en breton
  language = guessLanguage(page,"en","",cle)
  if not language:
    return

  wikitext = "__HIDDENCAT__\n"
  wikitext += "[[Catégorie:Wiktionnaire:Conjugaisons manquantes|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Conjugaison en " + language + "|!]]"
  return wikitext

def createCategoryDerivationsEn(page,cle):
  #Catégorie:Dérivations en tchèque
  language = guessLanguage(page,"en","",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Dérivations|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Origines étymologiques des mots en " + language + "| Derivations]]"
  return wikitext

def createCategoryEbauches(page,cle):
  #Wiktionnaire:Ébauches en italien
  language = guessLanguage(page,"en","",cle)
  if not language:
    return
  
  wikitext = "Cette catégorie liste les [[ébauche]]s en [[" + language + "]].\n\n"
  wikitext += "__HIDDENCAT__\n"
  wikitext += "[[Catégorie:Wiktionnaire:Ébauches à compléter|" + cle[language] + "]]"
  return wikitext

def createCategoryEtymologiesEnIncluantReconstruction(page,cle):
  #Catégorie:Étymologies en français incluant une reconstruction
  language = guessLanguage(page,"en","incluant",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Reconstructions|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Origines étymologiques des mots en " + language + "| Reconstructions]]"
  return wikitext

def createCategoryExemplesManquants(page,cle):
  #Wiktionnaire:Exemples manquants en italien
  language = guessLanguage(page,"en","",cle)
  if not language:
    return
  
  wikitext = "__HIDDENCAT__\n"
  wikitext += "[[Catégorie:Wiktionnaire:Exemples manquants|" + cle[language] + "]]"
  return wikitext

def createCategoryEtymologiesManquantes(page,cle):
  #Wiktionnaire:Étymologies manquantes en italien
  language = guessLanguage(page,"en","",cle)
  if not language:
    return
  
  wikitext = "L’étymologie de ces mots en [[" + language + "]] n’a pas été précisée, merci d’y remédier si vous la connaissez.\n\n"
  wikitext += "__HIDDENCAT__\n"
  wikitext += "[[Catégorie:Wiktionnaire:Étymologies manquantes|" + cle[language] + "]]"
  return wikitext

def createCategoryGrammaire(page,cle):
  #Grammaire en abu’‏‎
  language = guessLanguage(page,"en","",cle)
  if not language:
    return
  
  wikitext = "Cette catégorie a pour but de réunir les sous-catégories traitant de la grammaire en " + language + ", notamment :\n"
  wikitext += "* Les natures de mots (nom, verbe…)\n"
  wikitext += "* Les formes (locutions, sigles…)\n"
  wikitext += "* les formes infléchies, déclinées, conjuguées…\n\n"
  wikitext += "[[Catégorie:" + language + "|Grammaire]]\n"
  wikitext += "[[Catégorie:Grammaire par langue|" + cle[language] +"]]"
  return wikitext

def createCategoryDatesManquantes(page,cle):
  #Dates manquantes en français
  language = guessLanguage(page,"en","",cle)
  if not language:
    return

  wikitext = "__HIDDENCAT__\n"
  wikitext += "[[Catégorie:Dates manquantes|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:{{MediaWiki:Hidden-category-category}}|" + cle[language]+ "  Dates manquantes]]"
  return wikitext

def createCategoryLangageEnfantin(page,cle):
  #Catégorie:Langage enfantin en 
  language = guessLanguage(page,"en","",cle)
  if not language:
    return

  wikitext = "[[Catégorie:Langage enfantin|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Registres de langue en " + language + "|enfantin]]"
  return wikitext

def createCategoryRegistresLangueEn(page,cle):
  #Catégorie:Registres de langue en lituanien
  language = guessLanguage(page,"en","",cle)
  if not language:
    return

  wikitext = "[[Catégorie:Registres de langue|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:" + language + "]]"
  return wikitext

def createCategoryLexique(page, cle, code, listeLexique):
  #On verifie que le titre de la page contient au moins un des éléments
  #contenus dans la liste des lexiques
  #si ce n'est pas le cas, c'est que le lexique n'est pas encore géré
  #donc on ne crée pas la catégorie

  #TODO: problème avec Catégorie:Lexique en gotique de l’économie
  # car le lexique "go" est reconnu
  trouve=False
  for mot in listeLexique[::-1]:
    #print(">>" + mot + "<<")
    beg = page.find(" de ")
    pos = page.find(mot,beg+4)
    if(pos != -1):
      #print(page + " contient le mot : " + mot)
      trouve=True
      break

  if(not trouve):
    print("Lexique non reconnu dans " + page)
    return


  #on récupère le nom de la langue pour vérifier qu'il ne contient pas de "de" ou de "du"
  #si c'est le cas, il faut indiquer le code de langue en paramètre du modèle
  beg = page.find(" en ")
  # On cherche dans le titre de la page qui précède le lexique que l'on vient d'identifier.
  # Ca permet de gérer correctement les cas comme
  # Catégorie:Lexique en quechua de Cuzco du chemin de fer‏‎
  end = page[:pos].rfind(" d");
  language = page[beg+4:end]
  if (language not in cle):
    return

  beg = page.find(language)
  domain = page[beg+len(language):]
  domain = domain[domain[1:].find(" ")+1:]
  #print(f"domain:{domain}")
  
  wikitext = "{{catégorisation lexique"
  if (language.find(" d") != -1 or
      domain.find(" d") != -1):
    wikitext += "|" + code[language]
  wikitext += "}}"
  return wikitext

def createCategoryAdjectifs(page,cle):
  #Catégorie:Adjectifs en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Adjectifs|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Grammaire en " + language + "|adverbes]]"
  return wikitext

def createCategoryAdverbes(page,cle):
  #Catégorie:Adverbes en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Adverbes|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Grammaire en " + language + "|adverbes]]"
  return wikitext

def createCategoryAcaryotes(page,cle):
  #Catégorie:Acaryotes en anglais
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Super-règnes en " + language + "]]\n"
  wikitext += "[[Catégorie:Acaryotes|" + cle[language] + "]]"
  return wikitext

def createCategoryAliments(page,cle):
  #Catégorie:Aliments en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Aliments|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|aliments]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la cuisine|aliments]]"
  return wikitext

def createCategoryAnimaux(page,cle):
  #Catégorie:Animaux en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Animaux|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|animaux]]"
  return wikitext

def createCategoryAnimauxMulticellulaires(page,cle):
  #Catégorie:Animaux multicellulaires en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Animaux multicellulaires|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Animaux en " + language + "|multicellulaires]]"
  return wikitext

def createCategoryArbres(page,cle):
  #Catégorie:Arbres en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Arbres|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Plantes en " + language + "|arbres]]"
  return wikitext

def createCategoryArmes(page,cle):
  #Catégorie:Armes en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Armes|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|armes]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de l’armement|armes]]"
  return wikitext

def createCategoryBateaux(page,cle):
  #Catégorie:Bateaux en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Bateaux|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|bateaux]]"
  wikitext += "[[Catégorie:Lexique en " + language + " de la navigation|bateaux]]"
  return wikitext

def createCategoryBoissons(page,cle):
  #Catégorie:Boissons en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Boissons|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|boissons]]"
  wikitext += "[[Catégorie:Lexique en " + language + " de la cuisine|boissons]]"
  return wikitext

def createCategoryCardinaux(page,cle):
  #Catégorie:Cardinaux en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Cardinaux|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Adjectifs numéraux en " + language + "|cardinaux]]"
  wikitext += "[[Catégorie:Lexique en " + language + " des mathématiques|cardinaux]]"
  return wikitext

def createCategoryCereales(page,cle):
  #Catégorie:Céréales en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Céréales|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Plantes en " + language + "|cereales]]"
  return wikitext

def createCategoryCirconfixes(page,cle,code):
  #Catégorie:Circonfixes en anglais
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  wikitext = "{{catégorie d’affixe|" + code[language] + "}}\n\n"
  wikitext += "[[Catégorie:Circonfixes|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Grammaire en " + language + "]]"
  return wikitext

def createCategoryCocktails(page,cle):
  #Catégorie:Cocktails en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Cocktails|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Boissons alcoolisées en " + language + "|cocktails]]"
  return wikitext

def createCategoryConjonctions(page,cle):
  #Catégorie:Conjonctions en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Conjonctions|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Grammaire en " + language + "|conjonctions]]"
  return wikitext

def createCategoryConjugaison(page,cle):
  #Catégorie:Conjugaison en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  wikitext = "Cette catégorie a pour but de réunir les annexes décrivant la [[conjugaison]] des verbes en " + language + ".\n\n"
  wikitext += "[[Catégorie:Conjugaison|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:" + language + "|conjugaison]]"
  return wikitext

def createCategoryCouleurs(page,cle):
  #Catégorie:Couleurs en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Couleurs|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|couleurs]]"
  return wikitext

def createCategoryCuriositesLinguistiques(page,cle):
  #Catégorie:Curiosités linguistiques en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Curiosités linguistiques par langue|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:" + language + "]]"
  return wikitext

def createCategoryDateManquante(page,cle):
  #Catégorie:Date manquante en breton
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "__HIDDENCAT__\n"
  wikitext = "[[Catégorie:Date manquante|" + cle[language] + "]]"
  return wikitext

def createCategoryDivinitesEn(page,cle):
  #Catégorie:Divinités en français
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  wikitext = "[[Catégorie:Divinités|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la mythologie| Divinites]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la religion| Divinites]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "]]"
  return wikitext

def createCategoryDivinitesXXXEn(page,cle):
  #Catégorie:Divinités grecques en français
  #Catégorie:Divinités slaves en français
  beg=page.find("Divinités ")
  end=page.find(" en ")
  typeDivinite=page[beg+10:end]
  #on enlève le "s"
  typeDivinite=typeDivinite[:-1]
  language=page[end+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Divinités " + typeDivinite + "s|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Divinités en " + language + "|" + CleDeTri.CleDeTri(typeDivinite) + "]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la mythologie " + typeDivinite + "| divinites]]"
  return wikitext

def createCategoryDesserts(page,cle):
  #Catégorie:Desserts en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Desserts|" + cle[language] + "]]\n"
  wikitext = "[[Catégorie:Préparations culinaires en " + language + "|desserts]]"
  return wikitext

def createCategoryEucaryotes(page,cle):
  #Catégorie:Eucaryotes en minnan
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Eucaryotes|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Super-règnes en " + language + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "]]"

  return wikitext

def createCategorySuperRegnes(page,cle):
  #Catégorie:Super-règnes en tchétchène
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Super-règnes|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|Super regnes]]"

  return wikitext

def createCategoryExemples(page,cle):
  #Catégorie:Exemples en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Exemples|" + cle[language] + "]]"
  return wikitext

def createCategoryExemplesTraduire(page,cle):
  #Catégorie:Exemples en italien
  beg=page.find(" en ")
  fin=page.find(" à traduire")
  language=page[beg+4:fin]
  if (language not in cle):
    return
  
  wikitext = "__HIDDENCAT__\n"
  wikitext += "Cette catégorie énumère les mots en " + language + " pour lesquels une demande de traduction de l’exemple d’usage a été placée. Pour la satisfaire, voir [[Aide:Exemples#Mots_non-français]].\n"
  wikitext += "{{DEFAULTSORT:" + cle[language] + " traductions en francais demandee}}\n"
  wikitext += "[[Catégorie:Exemples à traduire]]\n"
  wikitext += "[[Catégorie:Traductions en " + language +"|francais]]"
  return wikitext

def createCategoryExpressions(page,cle):
  #Catégorie:Expressions en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Expressions|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:" + language + "]]"
  return wikitext

def createCategoryCaprins(page,cle):
  #Catégorie:Caprins en suédois
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Caprins|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Ruminants en " + language + "]]"
  return wikitext

def createCategoryCrustaces(page,cle):
  #Catégorie:Crustacés en français
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Crustacés|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Arthropodes en " + language + "]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la zoologie| ]]"
  return wikitext

def createCategoryEquins(page,cle):
  #Catégorie:Équins en suédois
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Équins|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Ongulés en " + language + "]]"
  return wikitext

def createCategoryArthropodes(page,cle):
  #Catégorie:Arthropodes en français
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Arthropodes|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Ecdysozoaires en " + language + "]]"
  return wikitext

def createCategoryEcdysozoaires(page,cle):
  #Catégorie:Ecdysozoaires en français
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Ecdysozoaires|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Animaux en " + language + "]]"
  return wikitext

def createCategoryChevaux(page,cle):
  #Catégorie:Chevaux en bas-sorabe
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Chevaux|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Équins en " + language + "]]"
  return wikitext

def createCategoryCrapauds(page,cle):
  #Catégorie:Crapauds en français
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Crapauds|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Amphibiens en " + language + "]]"
  return wikitext

def createCategoryFelins(page,cle):
  #Catégorie:Félins en algonquin
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Félins|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Mammifères en " + language + "]]"
  return wikitext

def createCategoryOngules(page,cle):
  #Catégorie:Ongulés en français
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Ongulés|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Mammifères en " + language + "]]"
  return wikitext

def createCategoryOvins(page,cle):
  #Catégorie:Ovins en dioula
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Ovins|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Ruminants en " + language + "]]"
  return wikitext

def createCategoryPapillons(page,cle):
  #Catégorie:Papillons en allemand
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Papillons|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Insectes en " + language + "]]"
  return wikitext

def createCategoryReptiles(page,cle):
  #Catégorie:Reptiles en français
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Reptiles|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Tétrapodes en " + language + "]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de l’herpétologie]]"
  return wikitext

def createCategoryRuminants(page,cle):
  #Catégorie:Ruminants en français
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Ruminants|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Ongulés en " + language + "]]"
  return wikitext

def createCategoryTetrapodes(page,cle):
  #Catégorie:Tétrapodes en français
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Tétrapodes|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Vertébrés en " + language + "]]"
  return wikitext

def createCategoryTortues(page,cle):
  #Catégorie:Tortues en bambara
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Tortues|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Reptiles en " + language + "]]"
  return wikitext

def createCategoryFruits(page,cle):
  #Catégorie:Fruits en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Fruits|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Aliments en " + language + "|fruits]]\n"
  wikitext += "[[Catégorie:Plantes en " + language + "|fruits]]"
  return wikitext

def createCategoryFruitsMer(page,cle):
  #Catégorie:Fruits de mer en vietnamien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext ="[[Catégorie:Fruits de mer|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Aliments en " + language + "|Fruits de mer]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la pêche| Fruits de mer]]"
  return wikitext

def createCategoryFromages(page,cle):
  #Catégorie:Fromages en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Fromages|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Aliments en " + language + "]]"
  return wikitext

def createCategoryGateaux(page,cle):
  #Catégorie:Gâteaux en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Gâteaux|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Pâtisseries en " + language + "| Gateaux]]\n"
  wikitext += "[[Catégorie:Desserts en " + language + "|gateaux]]"
  return wikitext

def createCategoryCoursDeauDePaysEn(page,cle,continent):
  #Catégorie:Cours d’eau de France en latin
  #Catégorie:Cours d’eau d’Europe en latin

  isPays = False
  isContinent = False

  beg=page.find("Cours d’eau d")+11
  beg2=page.find("’",beg)
  # s'il n'y a pas d'apostropes,
  # on récupère ce qui suit après une espace
  if(beg2 == -1 or # il n'y a pas d'apostrophes
     (beg2!=beg+2 and
     beg2!=beg+5)): # Cours d’eau de l’Inde
    beg2=page.find(" ",beg+1)
  end=page.find(" en ")
  paysContinent=page[beg2+1:end]
  if (paysContinent in continent):
    isPays = True
  if (not isPays and paysContinent in continent.values()):
    isContinent = True  
  if(not isPays and not isContinent):
    return
  
  language=page[end+4:]
  if (language not in cle):
    return

  particle = ""
  if(page.find("Cours d’eau d’") != -1):
    particle="d’"
  elif(page.find("Cours d’eau des") != -1):
    particle="des "
  elif(page.find("Cours d’eau de") != -1):
    particle="de "
  if(page.find("Cours d’eau de l’") != -1):
    particle="de l’"
  elif(page.find("Cours d’eau du") != -1):
    particle="du "
      
  if isPays:
    de="d’"
    if(continent[paysContinent] == "Caraïbes"):
      de="des "
    if(continent[paysContinent] == "Canada" or
       continent[paysContinent] == "Royaume-Uni"):
      de="du "
    wikitext = "[[Catégorie:Cours d’eau " + de + continent[paysContinent] + " en " + language + "|" + CleDeTri.CleDeTri(paysContinent) + "]]\n"
    wikitext += "[[Catégorie:Cours d’eau " + particle + paysContinent + "|" + cle[language] + "]]\n"
    wikitext += "[[Catégorie:" + paysContinent + " en " + language + "]]"

  if isContinent:
    wikitext = "[[Catégorie:Cours d’eau " + particle + paysContinent + "|" + cle[language] + "]]\n"
    wikitext += "[[Catégorie:" + paysContinent + " en " + language + "]]"    
    
  return wikitext

def createCategoryCoursDeauDePays(page,cle,continent):
  #Catégorie:Cours d’eau de France
  #Catégorie:Cours d’eau d’Europe

  isPays = False
  isContinent = False

  beg=page.find("Cours d’eau d")+11
  beg2=page.find("’",beg)
  # s'il n'y a pas d'apostropes,
  # on récupère ce qui suit après une espace
  if(beg2 == -1 or # il n'y a pas d'apostrophes
     (beg2!=beg+2 and
     beg2!=beg+5)): # Cours d’eau de l’Inde
    beg2=page.find(" ",beg+1)
 
  paysContinent=page[beg2+1:]
  if (paysContinent in continent):
    isPays = True
  if (not isPays and paysContinent in continent.values()):
    isContinent = True  
  if(not isPays and not isContinent):
    return

  particle = ""
  if(page.find("Cours d’eau d’") != -1):
    particle="d’"
  elif(page.find("Cours d’eau des") != -1):
    particle="des "
  elif(page.find("Cours d’eau de") != -1):
    particle="de "
  if(page.find("Cours d’eau de l’") != -1):
    particle="de l’"
  elif(page.find("Cours d’eau du") != -1):
    particle="du "
    
  if isPays:
    de="d’"
    if(continent[paysContinent] == "Caraïbes"):
      de="des "
    if(continent[paysContinent] == "Canada" or
       continent[paysContinent] == "Royaume-Uni"):
      de="du "
    wikitext = "[[Catégorie:Cours d’eau " + de + continent[paysContinent] + "|" + CleDeTri.CleDeTri(paysContinent) + "]]\n"
    wikitext += "[[Catégorie:Cours d’eau par pays|" + CleDeTri.CleDeTri(paysContinent) + "]]\n"
    wikitext += "[[Catégorie:" + paysContinent + "| Cours deau]]"

  if isContinent:
    wikitext = "[[Catégorie:Cours d’eau|" + CleDeTri.CleDeTri(paysContinent) + "]]\n"
    wikitext += "[[Catégorie:" + paysContinent + "| Cours deau]]"    
    
  return wikitext

def createCategoryCoursDeauEn(page,cle):
  #Catégorie:Cours d’eau en italien

  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  wikitext = "[[Catégorie:Cours d’eau par langue|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Hydronymes en " + language + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "]]"

  return wikitext

def createCategoryGentilesDePaysEn(page,cle,continent):
  #Catégorie:Gentilés de Chine en français
  #Catégorie:Gentilés d’Europe en anglais

  isPays = False
  isContinent = False

  beg=page.find(" d")
  beg2=page.find("’",beg)
  if(beg2 == -1 or
     (beg2!=beg+2 and
     beg2!=beg+5)): # Gentilés de l’Inde
    beg2=page.find(" ",beg+1)
  end=page.find(" en ")
  paysContinent=page[beg2+1:end]
  if (paysContinent in continent):
    isPays = True
  if (not isPays and paysContinent in continent.values()):
    isContinent = True
  if(not isPays and not isContinent):
    return
  
  language=page[end+4:]
  if (language not in cle):
    return

  particle = ""
  if(page.find("Gentilés d’") != -1):
    particle="d’"
  elif(page.find("Gentilés des") != -1):
    particle="des "
  elif(page.find("Gentilés de") != -1):
    particle="de "
  if(page.find("Gentilés de l’") != -1):
    particle="de l’"
  elif(page.find("Gentilés du") != -1):
    particle="du "
      
  if isPays:
    de="d’"
    if(continent[paysContinent] == "Caraïbes"):
      de="des "
    if(continent[paysContinent] == "Canada" or
       continent[paysContinent] == "Royaume-Uni"):
      de="du "
    wikitext = "[[Catégorie:Gentilés " + de + continent[paysContinent] + " en " + language + "|" + CleDeTri.CleDeTri(paysContinent) + "]]\n"
    wikitext += "[[Catégorie:Gentilés " + particle + paysContinent + "|" + cle[language] + "]]\n"
    wikitext += "[[Catégorie:" + paysContinent + " en " + language + "|Gentiles]]"

  if isContinent:
    wikitext = "[[Catégorie:Gentilés " + particle + paysContinent + "|" + cle[language] + "]]\n"
    wikitext += "[[Catégorie:Gentilés en " + language + "|" + CleDeTri.CleDeTri(paysContinent) + "]]\n"
    wikitext += "[[Catégorie:" + paysContinent + " en " + language + "| Gentiles]]"    
    
  return wikitext

def createCategoryGentilesDePays(page,cle,continent):
  #Catégorie:Gentilés de France
  #Catégorie:Gentilés d’Europe

  isPays = False
  isContinent = False

  beg=page.find(" d")
  beg2=page.find("’",beg)
  if(beg2 == -1 or
     (beg2!=beg+2 and
     beg2!=beg+5)): # Gentilés de l’Inde
    beg2=page.find(" ",beg+1)
  paysContinent=page[beg2+1:]
  if (paysContinent in continent):
    isPays = True
  if (not isPays and paysContinent in continent.values()):
    isContinent = True
  if(not isPays and not isContinent):
    return

  particle = ""
  if(page.find("Gentilés d’") != -1):
    particle="d’"
  elif(page.find("Gentilés des") != -1):
    particle="des "
  elif(page.find("Gentilés de") != -1):
    particle="de "
  if(page.find("Gentilés de l’") != -1):
    particle="de l’"
  elif(page.find("Gentilés du") != -1):
    particle="du "
      
  if isPays:
    de="d’"
    if(continent[paysContinent] == "Caraïbes"):
      de="des "
    if(continent[paysContinent] == "Canada" or
       continent[paysContinent] == "Royaume-Uni"):
      de="du "
    wikitext = "[[Catégorie:Gentilés par pays|" + CleDeTri.CleDeTri(paysContinent) + "]]\n"
    wikitext += "[[Catégorie:Gentilés " + de + continent[paysContinent] + "| " + CleDeTri.CleDeTri(paysContinent) + "]]\n"
    wikitext += "[[Catégorie:" + paysContinent + "| Gentiles]]"

  if isContinent:
    wikitext = "[[Catégorie:Gentilés par continent|" + CleDeTri.CleDeTri(paysContinent) + "]]\n"
    wikitext += "[[Catégorie:" + paysContinent + "| Gentiles]]"    
    
  return wikitext

def createCategoryGentilesEn(page,cle):
  #Catégorie:Gentilés en italien

  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  wikitext = "[[Catégorie:Noms communs en " + language + "|Gentiles]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|Gentiles]]\n"
  wikitext += "[[Catégorie:Gentilés|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la géographie|Gentiles]]"

  return wikitext

def createCategoryInfixes(page,cle,code):
  #Catégorie:Infixes en anglais
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  wikitext = "{{catégorie d’affixe|" + code[language] + "}}\n\n"
  wikitext += "[[Catégorie:Infixes|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Grammaire en " + language + "]]"
  return wikitext

def createCategoryInterfixes(page,cle,code):
  #Catégorie:Interfixes en anglais
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  wikitext = "{{catégorie d’affixe|" + code[language] + "}}\n\n"
  wikitext += "[[Catégorie:Interfixes|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Grammaire en " + language + "]]"
  return wikitext

def createCategoryInsectes(page,cle):
  #Catégorie:Insectes en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Insectes|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Animaux en " + language + "|insectes]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|insectes]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de l’entomologie|insectes]]"
  return wikitext

def createCategoryInstrumentsDeMusique(page,cle):
  #Catégorie:Instruments de musique en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Instruments de musique|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|instruments de musique]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la musique|instruments de musique]]"
  return wikitext

def createCategoryInterrogatifs(page,cle):
  #Catégorie:Interrogatifs en anglais
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Interrogatifs|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Grammaire en " + language + "|interrogatifs]]"
  return wikitext

def createCategoryJoursSemaine(page,cle):
  #Catégorie:Jours de la semaine en mirandais
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Jours de la semaine|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Calendrier en " + language + "]]"
  return wikitext

def createCategoryLangues(page,cle):
  #Catégorie:Langues en anglais
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Noms de langues|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|langues]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la linguistique|langues]]"
  return wikitext

def createCategoryLegumes(page,cle):
  #Catégorie:Légumes en indonésien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext ="[[Catégorie:Légumes|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Aliments en " + language + "|Legumes]]\n"
  wikitext += "[[Catégorie:Plantes en " + language + "|Legumes]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|Legumes]]"
  return wikitext

def createCategoryMetaux(page,cle):
  #Catégorie:Métaux en indonésien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext ="[[Catégorie:Métaux|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Substances chimiques en " + language + "|Metaux]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la chimie| Metaux]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la métallurgie| Metaux]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|Metaux]]"
  return wikitext

def createCategoryLexiques(page,cle):
  #Catégorie:Lexiques en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:" + language + "]]\n"
  wikitext += "[[Catégorie:Lexiques par langue|" + cle[language] + "]]"
  return wikitext

def createCategoryLocalitesDe(page,cle,continentByCountryDict):
  #Catégorie:Localités d’Italie

  particle = ""
  if(page.find("Localités d’") != -1):
    particle="d’"
  elif(page.find("Localités des") != -1):
    particle="des "
  elif(page.find("Localités de") != -1):
    particle="de "
  elif(page.find("Localités du") != -1):
    particle="du "

  
  country = ""
  if(particle=="de "):
    beg=page.find(" de ")
    country = page[beg+3:]
  elif(particle=="du "):
    beg=page.find(" du ")
    country = page[beg+4:]
  elif(particle=="des "):
    beg=page.find(" des ")
    country = page[beg+5:]

    
  # If the country in not in the list, then one does not process it
  isPays = False
  isContinent = False
  
  if (country in continentByCountryDict):
    isPays = True
  if (not isPays and country in continentByCountryDict.values()):
    isContinent = True
  if (not isPays and not isContinent):
    print(country + " :/")
    return

  if isPays:
    wikitext = "[[Catégorie:Localités par pays|" + CleDeTri.CleDeTri(country) + "]]\n"
    wikitext += "[[Catégorie:" + country + "| Localites]]"
    
  if isContinent:
    wikitext = "[[Catégorie:" + country + "| Localites]]\n"
    wikitext += "[[Catégorie:Localités|" + CleDeTri.CleDeTri(country) + "]]"

  return wikitext

def createCategoryLocalitesEn(page,cle):
  #Catégorie:Localités en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Localités par langue|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "]]\n"
  wikitext += "[[Catégorie:Toponymes en " + language + "|localites]]"
  return wikitext

def createCategoryLocalitesDeEn(page,cle,continentByCountryDict):
  #Catégorie:Localités d’Italie en français
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  particle = ""
  if(page.find("Localités d’") != -1):
    particle="d’"
  elif(page.find("Localités des") != -1):
    particle="des "
  elif(page.find("Localités de") != -1):
    particle="de "
  elif(page.find("Localités du") != -1):
    particle="du "

  
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
  isPays = False
  isContinent = False
  
  if (country in continentByCountryDict):
    isPays = True
  if (not isPays and country in continentByCountryDict.values()):
    isContinent = True
  if (not isPays and not isContinent):
    print(country + " :/")
    return

  if isPays:
    wikitext = "[[Catégorie:Localités " + particle + country + "|" + cle[language] + "]]\n"
    wikitext += "[[Catégorie:Localités en " + language + "|" + CleDeTri.CleDeTri(country) + "]]\n"
    wikitext += "[[Catégorie:" + country + " en " + language + "]]"
    
  if isContinent:
    wikitext = "[[Catégorie:Localités " + particle + country + " par langue|" + cle[language] + "]]\n"
    wikitext += "[[Catégorie:Localités en " + language + "|" + CleDeTri.CleDeTri(country) + "]]\n"
    wikitext += "[[Catégorie:" + country + " en " + language + "]]"

  return wikitext

def createCategoryMotsEnEsperantComportantRacine(page):
  #Catégorie:Mots en espéranto comportant la racine mejoz
  wikitext = "{{Catégorisation racine espéranto}}"

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
    print(f"La langue {language1} ou {language2} est inconnue")
    return
  
  wikitext = "Cette catégorie liste les termes en [[" + language1 + "]] ayant pour origine [[étymologique]] un mot en " + language2 + ". Lire aussi [[Aide:Étymologies]].\n\n"
  wikitext += "[[Catégorie:Origines étymologiques des mots en " + language1 + "|" + cle[language2] + "]]\n"
  wikitext += "[[Catégorie:Mots issus d’un mot en " + language2 + "|" + cle[language1] + "]]"
  return wikitext

def createCategoryMotsEnIssusDuneOnomatopee(page,cle):
  #Mots en espagnol issus d’une onomatopée
  beg=page.find(" en ")
  end=page.find(" issus")
  language=page[beg+4:end]
  if language not in cle:
    return
  
  wikitext = "[[Catégorie:Origines étymologiques des mots en " + language + "|*Onom]]\n"
  wikitext += "[[Catégorie:Mots issus d’une onomatopée|"+ cle[language] + "]]\n"
  wikitext += "[[Catégorie:Onomatopées en " + language + "]]"
  return wikitext

def createCategoryMotsEnInfixeAvec(page,cle):
  #Mots en azéri infixés avec
  beg=page.find(" en ")
  end=page.find(" infixés avec")
  language1=page[beg+4:end]
  if language1 not in cle:
    return

  wikitext = "{{cat mots affixés}}\n"
  wikitext += "{{CatégorieTDM}}"
  return wikitext

def createCategoryMotsEnPrefixeAvec(page,cle):
  #Mots en français préfixés avec
  beg=page.find(" en ")
  end=page.find(" préfixés avec")
  language1=page[beg+4:end]
  if language1 not in cle:
    return

  wikitext = "{{cat mots affixés}}\n"
  wikitext += "{{CatégorieTDM}}"
  return wikitext

def createCategoryMotsEnSuffixeAvec(page,cle):
  #Mots en français suffixés avec -isme
  beg=page.find(" en ")
  end=page.find(" suffixés avec")
  language1=page[beg+4:end]
  if language1 not in cle:
    return

  wikitext = "{{cat mots affixés}}\n"
  wikitext += "{{CatégorieTDM}}"
  return wikitext

def createCategoryMotsIssusDunMot(page,cle):
  #Mots issus d’un mot en abouré‏‎
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  wikitext = ""
  if (language.find("latin")!=-1 and
      language != "latin"):
    wikitext += "[[Catégorie:Mots issus d’un mot en latin| " + cle[language] + "]]"
  else:
    wikitext += "[[Catégorie:Origines étymologiques des mots|" + cle[language] + "]]\n"
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

def createCategoryLocutions(page,cle):
  #Catégorie:Locutions en italien
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "[[Catégorie:Locutions|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Grammaire en " + language + "|locutions]]"
  return wikitext

def createCategoryMammiferes(page,cle):
  #Catégorie:Mammifères en italien
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "[[Catégorie:Mammifères|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Vertébrés en " + language + "|mammiferes]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|mammiferes]]"
  return wikitext

def createCategoryMarsupiaux(page,cle):
  #Catégorie:Marsupiaux en italien
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "[[Catégorie:Marsupiaux|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Mammifères en " + language + "|mammiferes]]"
  return wikitext

def createCategoryMetiersEn(page,cle):
  #Catégorie:Métiers en italien
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "[[Catégorie:Métiers|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "]]"
  return wikitext

def createCategoryMetiersDroit(page,cle):
  #Catégorie:Métiers du droit en français
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "[[Catégorie:Métiers du droit|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " du droit| Metiers droit]]"
  wikitext += "[[Catégorie:Métiers du secteur tertiaire en " + language + "|Droit]]\n"
  return wikitext

def createCategoryMetiersRestauration(page,cle):
  #Catégorie:Métiers de la restauration en italien
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "[[Catégorie:Métiers de la restauration|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la cuisine| Metiers restauration]]"
  wikitext += "[[Catégorie:Lexique en " + language + " du commerce| Metiers restauration]]"
  wikitext += "[[Catégorie:Métiers du secteur tertiaire en " + language + "|Restauration]]\n"
  return wikitext

def createCategoryMetiersSante(page,cle):
  #Catégorie:Métiers de la santé en italien
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "[[Catégorie:Métiers de la santé|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Métiers du secteur tertiaire en " + language + "|Sante]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la médecine| Metiers sante]]"
  return wikitext

def createCategoryMetiersScience(page,cle):
  #Catégorie:Métiers de la science en italien
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "[[Catégorie:Métiers de la science|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Métiers du secteur tertiaire en " + language + "|Science]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " des sciences| Metiers science]]"
  return wikitext

def createCategoryMetiersVente(page,cle):
  #Catégorie:Métiers de la vente en français
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "[[Catégorie:Métiers de la vente|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Métiers du secteur tertiaire en " + language + "|Vente]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " du commerce| Metiers vente]]"
  return wikitext

def createCategoryMetiersSecteur(page,cle):
  #Catégorie:Métiers du secteur primaire en italien
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  beg=page.find("secteur ")
  end=page.find(" en ")
  secteur = page [beg+8:end]
  
  wikitext = "[[Catégorie:Métiers du secteur " + secteur + "|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Métiers en " + language + "|" + CleDeTri.CleDeTri(secteur) + "]]"
  return wikitext

def createCategoryNomsAnimes(page,cle):
  #Catégorie:Noms animés en atikamekw
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "[[Catégorie:Noms animés|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Noms communs en " + language + "]]"
  return wikitext

def createCategoryNomsDenombrables(page,cle):
  #Catégorie:Noms dénombrables en néerlandais
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "[[Catégorie:Noms dénombrables|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Noms communs en " + language + "]]"
  return wikitext

def createCategoryNomsInanimes(page,cle):
  #Catégorie:Noms inanimés en micmac
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "[[Catégorie:Noms inanimés|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Noms communs en " + language + "]]"
  return wikitext

def createCategoryNomsIndenombrables(page,cle):
  #Catégorie:Noms indénombrables en occitan
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "[[Catégorie:Noms indénombrables|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Noms communs en " + language + "]]"
  return wikitext

def createCategoryNomsMultigenresEn(page,cle):
  #Catégorie:Noms multigenres en breton
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "[[Catégorie:Noms multigenres|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Noms communs en " + language + "|multigenres]]"
  return wikitext

def createCategoryMotsParfoisFemininsMasculins(page,cle):
  #Catégorie:Mots parfois féminins ou masculins en breton
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "__HIDDENCAT__\n\n"
  wikitext += "== Voir aussi ==\n"
  wikitext += "* {{Catégorie|Mots parfois masculins ou féminins en " + language + "}}\n\n"
  wikitext += "[[Catégorie:Mots parfois féminins ou masculins|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Grammaire en " + language + "]]\n"
  wikitext += "[[Catégorie:Curiosités linguistiques en " + language + "]]\n"
  wikitext += "[[Catégorie:{{MediaWiki:Hidden-category-category}}|" + cle[language] + "  parfois feminins masculins]]"  
  return wikitext

def createCategoryMotsParfoisMasculinsFeminins(page,cle):
  #Catégorie:Mots parfois masculins ou féminins en breton
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "__HIDDENCAT__\n\n"
  wikitext += "== Voir aussi ==\n"
  wikitext += "* {{Catégorie|Mots parfois féminins ou masculins en " + language + "}}\n\n"
  wikitext += "[[Catégorie:Mots parfois masculins ou féminins|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Grammaire en " + language + "]]\n"
  wikitext += "[[Catégorie:Curiosités linguistiques en " + language + "]]\n"
  wikitext += "[[Catégorie:{{MediaWiki:Hidden-category-category}}|" + cle[language] + "  parfois masculins feminins]]"
  return wikitext

def createCategoryNomsCommuns(page,cle):
  #Catégorie:Noms communs en saho
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "[[Catégorie:Noms communs|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Grammaire en " + language + "]]"
  return wikitext

def createCategoryNomsPropres(page,cle):
  #Catégorie:Noms propres en italien
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "[[Catégorie:Noms propres|" + cle[language] + "]]\n"
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

def createCategoryNomsSciencesEn(page,cle):
  #Catégorie:Noms de sciences en bosniaque
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "[[Catégorie:Noms de sciences|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|Noms de sciences]]"
  return wikitext

def createCategoryNumeraux(page,cle):
  #Catégorie:Numéraux en mahorais
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "[[Catégorie:Numéraux|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:" + language + "|numeraux]]"
  return wikitext

def createCategoryOiseaux(page,cle):
  #Catégorie:Oiseaux en italien
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "[[Catégorie:Oiseaux|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Vertébrés en " + language + "|oiseaux]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|oiseaux]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de l’ornithologie]]"
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

def createCategoryOrdinaux(page,cle):
  #Catégorie:Ordinaux en italien
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "[[Catégorie:Ordinaux|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Adjectifs numéraux en " + language + "|ordinaux]]"
  return wikitext

def createCategoryOutils(page,cle):
  #Catégorie:Outils en italien
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "[[Catégorie:Outils|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|outils]]"
  return wikitext

def createCategoryPagesLieesEn(page,cle):
  #Catégorie:Pages liées en grec
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "{{Stats pages liées|" + language + "}}\n\n"
  wikitext += "[[Catégorie:Pages liées par langue|" + cle[language] + "]]"
  return wikitext

def createCategoryPagesLieesAEn(page,cle):
  #Catégorie:Pages liées à Wikiquote en italien
  beg=page.find(" à ")
  end=page.rfind(" en ", beg+1)
  site=page[beg+3:end]
  listSite = ["Wikilivres","Wikipédia","Wikiquote","Wikisource","Wikispecies","Wikiversité","Wikivoyage"]
  print(site)
  if (not site in listSite):
    return
  
  language = page[end+4:]
  if (not language in cle):
    return

  wikitext = "__HIDDENCAT__\n"
  wikitext += "[[Catégorie:Pages liées à " + site + "|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Pages liées en " + language + "|" + site + "]]"
  return wikitext

def createCategoryPalindromes(page,cle):
  #Catégorie:Palindromes en italien
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "Cette page recense les [[palindrome]]s en " + language + ".\n\n"
  wikitext += "[[Catégorie:Palindromes|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:" + language + "]]"
  return wikitext

def createCategoryPays(page,cle):
  #Catégorie:Pays en italien
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "[[Catégorie:Thématiques en " + language + "]]\n"
  wikitext += "[[Catégorie:Pays par langue|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Noms propres en " + language + "]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la géographie]]"
  return wikitext

def createCategoryPlantes(page,cle):
  #Catégorie:Plantes en swahili
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "[[Catégorie:Plantes|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|plantes]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la botanique]]"
  return wikitext

def createCategoryPoissons(page,cle):
  #Catégorie:Poissons en italien
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "[[Catégorie:Poissons|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Vertébrés en " + language + "|poissons]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de l’ichtyologie]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la pêche]]"
  return wikitext

def createCategoryPreparationsCulinaires(page,cle):
  #Catégorie:Préparations culinaires en italien
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "[[Catégorie:Préparations culinaires|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la cuisine]]"
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

def createCategoryPrononciationsAudioManquantes(page,cle):
  #catégorie:Wiktionnaire:Prononciations audio manquantes en italien
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return

  wikitext = "__HIDDENCAT__\n"
  wikitext +="[[Catégorie:Wiktionnaire:Prononciations audio manquantes|" + cle[language] + "]]"
  return wikitext

def createCategoryPrononciationsPhonetiquesManquantes(page,cle):
  #catégorie:Wiktionnaire:Prononciations phonétiques manquantes en italien
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "La prononciation de ces enregistrement en " + language + " n’a pas été précisée, merci d’y remédier :\n"
  wikitext += "* si vous connaissez l’API ou\n"
  wikitext += "* si la prononciation se trouve sur un autre Wiktionnaire.\n\n"

  wikitext += "__HIDDENCAT__\n"
  wikitext +="[[Catégorie:Wiktionnaire:Prononciations phonétiques manquantes|" + cle[language] + "]]"
  return wikitext

def createCategoryPrononciationsManquantes(page,cle):
  #Catégorie:Wiktionnaire:Prononciations manquantes en italien
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return

  wikitext = "La prononciation de ces mots en " + language + " n’a pas été précisée, merci d’y remédier :\n"
  wikitext += "* si vous connaissez l’API ou\n"
  wikitext += "* si vous avez un dictionnaire indiquant l’API ou\n"
  wikitext += "* si la prononciation se trouve sur un autre Wiktionnaire.\n\n"
  wikitext += "__HIDDENCAT__\n"
  wikitext += "[[Catégorie:Wiktionnaire:Prononciations manquantes|" + cle[language] + "]]"
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

def createCategoryPrefixes(page,cle,code):
  #Catégorie:Préfixes en anglais
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  wikitext = "{{catégorie d’affixe|" + code[language] + "}}\n\n"
  wikitext += "[[Catégorie:Préfixes|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Grammaire en " + language + "]]"
  return wikitext

def createCategoryPrenoms(page,cle):
  #Catégorie:Prénoms en anglais
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  wikitext = ""
  
  if (page.find("Prénoms en ") != -1):
    wikitext += "Voici quelques [[prénom]]s en [[" + language + "]], et n’oubliez pas que si vous voulez compléter la liste, vous êtes le bienvenu.\n\n"
    wikitext += "[[Catégorie:Prénoms par langue|" + cle[language] + "]]\n"
    wikitext += "[[Catégorie:Thématiques en " + language + "|Prenoms]]"
    
  elif (page.find("Prénoms masculins en ") != -1):
    wikitext += "* Voir aussi ''{{catégorie|Prénoms féminins en " + language + "}}''.\n"
    wikitext += "* Voir aussi ''{{catégorie|Prénoms mixtes en " + language + "}}''.\n\n"
    wikitext += "[[Catégorie:Prénoms masculins|" + cle[language] + "]]\n"
    wikitext += "[[Catégorie:Prénoms en " + language + "|Masculins]]"
    
  elif (page.find("Prénoms féminins en ") != -1):
    wikitext += "* Voir aussi ''{{catégorie|Prénoms masculins en " + language + "}}''.\n"
    wikitext += "* Voir aussi ''{{catégorie|Prénoms mixtes en " + language + "}}''.\n\n"
    wikitext += "[[Catégorie:Prénoms féminins|" + cle[language] + "]]\n"
    wikitext += "[[Catégorie:Prénoms en " + language + "|Feminins]]"
    
  elif (page.find("Prénoms mixtes en ") != -1):
    wikitext += "* Voir aussi ''{{catégorie|Prénoms masculins en " + language + "}}''.\n"
    wikitext += "* Voir aussi ''{{catégorie|Prénoms féminins en " + language + "}}''.\n\n"
    wikitext += "[[Catégorie:Prénoms mixtes|" + cle[language] + "]]\n"
    wikitext += "[[Catégorie:Prénoms en " + language + "|Mixtes]]"
  
  return wikitext

def createCategoryReferencesNecessaires(page,cle):
  #Catégorie:Références nécessaires en français
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  wikitext = "__HIDDENCAT__\n"
  wikitext += "[[Catégorie:Références nécessaires|" + cle[language] + "]]"

  return wikitext

def createCategoryReligieux(page,cle):
  #Catégorie:Religieux en tchèque
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  wikitext = "[[Catégorie:Lexique en " + language + " de la religion]]\n"
  wikitext += "[[Catégorie:Religieux|" + cle[language] + "]]"
  return wikitext

def createCategoryRoches(page,cle):
  #Catégorie:Roches en catalan
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  wikitext = "[[roche|Roches]] en [[" + language + "]].\n\n"
  wikitext += "=== Voir aussi ==="
  wikitext += "* {{Catégorie|Minéraux en " + language + "}}\n\n"
  wikitext = "[[Catégorie:Roches|" + cle[language] + "]]\n"
  wikitext = "[[Catégorie:Lexique en " + language + " de la géologie|Roches]]\n"
  wikitext = "[[Catégorie:Lexique en " + language + " de la pédologie|Roches]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|Roches]]"
  return wikitext

def createCategoryCalendrier(page,cle):
  #Catégorie:Calendrier en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "Voir aussi l’[[Annexe:Calendriers du monde|annexe contenant la traduction du calendrier dans de multiples langues]].\n\n"
  wikitext += "[[Catégorie:Calendrier|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " du temps]]"
  return wikitext

def createCategorySaisons(page,cle):
  #Catégorie:Saisons en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext ="[[Catégorie:Saisons|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|Saisons]]\n"
  wikitext += "[[Catégorie:Calendrier en " + language + "]]"
  return wikitext

def createCategorySoldats(page,cle):
  #Catégorie:Soldats en same du Nord
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext ="[[Catégorie:Soldats|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|Soldats]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " du militaire]]\n"
  wikitext += "[[Catégorie:Métiers du secteur tertiaire en " + language + "]]"
  return wikitext

def createCategorySports(page,cle):
  #Catégorie:Sports en anglais
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext ="[[Catégorie:Sports|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|Sports]]"
  return wikitext

def createCategorySuffixes(page,cle,code):
  #Catégorie:Suffixes en anglais
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  wikitext = "{{catégorie d’affixe|" + code[language] + "}}\n\n"
  wikitext += "[[Catégorie:Suffixes|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Grammaire en " + language + "]]"
  return wikitext

def createCategorySymboles(page,cle):
  #Catégorie:Symboles en français
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  wikitext = "[[Catégorie:Symboles|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:" + language + "]]"
  return wikitext

def createCategoryTermesEn(page,cle,code):
  #Catégorie:Termes archaïques en allemand
  #Catégorie:Termes argotiques en espagnol
  #Catégorie:Termes didactiques en grec
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  beg=page.find("Termes ")
  end=page.find(" en ")
  domaine = page[beg+7:end]

  wikitext = ""
  if (domaine=="archaïques"):
    wikitext += "[[Catégorie:" + language + "|Archaique]]\n"
    wikitext += "[[Catégorie:Archaïsmes|" + cle[language] + "]]"
    
  elif (domaine=="argotiques"):
    wikitext += "Termes catégorisés par le modèle {{modl|argot|" + code[language] + "}}.\n\n"
    wikitext += "[[Catégorie:" + language + "|Argot]]\n"
    wikitext += "[[Catégorie:Argot|" + cle[language] + "]]"
    
  elif (domaine=="didactiques"):
    wikitext += "[[Catégorie:Thématiques en " + language + "|didactique]]\n"
    wikitext += "[[Catégorie:Didactique|" + cle[language] + "]]"
    
  elif (domaine=="désuets"):
    wikitext += "[[Catégorie:" + language + "|Termes desuets]]\n"
    wikitext += "[[Catégorie:Langage désuet|" + cle[language] + "]]"
    
  elif (domaine=="familiers"):
    wikitext += "[[Catégorie:Registres de langue en " + language + "|Familier]]\n"
    wikitext += "[[Catégorie:Langage familier|" + cle[language] + "]]"
    
  elif (domaine=="généralement pluriels"):
    wikitext += "[[Catégorie:Grammaire en " + language + "]]\n"
    wikitext += "[[Catégorie:Termes généralement pluriels|" + cle[language] + "]]"
    
  elif (domaine=="généralement singuliers"):
    wikitext += "[[Catégorie:Grammaire en " + language + "]]\n"
    wikitext += "[[Catégorie:Termes généralement singuliers|" + cle[language] + "]]"
    
  elif (domaine=="informels"):
    wikitext += "[[Catégorie:Registres de langue en " + language + "|informels termes]]\n"
    wikitext += "[[Catégorie:Langage informel|" + cle[language] + "]]"
    
  elif (domaine=="littéraires"):
    wikitext += "[[Catégorie:Registres de langue en " + language + "|litteraires termes]]\n"
    wikitext += "[[Catégorie:Termes littéraires|" + cle[language] + "]]"
    
  elif (domaine=="par dérision"):
    wikitext += "[[Catégorie:" + language + "|derision]]\n"
    wikitext += "[[Catégorie:Dérisions|" + cle[language] + "]]"
    
  elif (domaine=="non standards"):
    wikitext += "[[Catégorie:Registres de langue en " + language + "|non standard]]\n"
    wikitext += "[[Catégorie:Langage non standard|" + cle[language] + "]]"
    
  elif (domaine=="péjoratifs"):
    wikitext += "[[Catégorie:Registres de langue en " + language + "|pejoratif]]\n"
    wikitext += "[[Catégorie:Langage péjoratif|" + cle[language] + "]]"
    
  elif (domaine=="poétiques"):
    wikitext += "[[Catégorie:Registres de langue en " + language + "|poetique]]\n"
    wikitext += "[[Catégorie:Langage poétique|" + cle[language] + "]]"
    
  elif (domaine=="populaires"):
    wikitext += "[[Catégorie:Registres de langue en " + language + "|populaire termes]]\n"
    wikitext += "[[Catégorie:Langage populaire|" + cle[language] + "]]"
    
  elif (domaine=="soutenus"):
    wikitext += "[[Catégorie:Registres de langue en " + language + "|soutenu]]\n"
    wikitext += "[[Catégorie:Langage soutenu|" + cle[language] + "]]"
    
  elif (domaine=="vieillis"):
    wikitext += "[[Catégorie:" + language + "|Vieilli]]\n"
    wikitext += "[[Catégorie:Langage vieilli|" + cle[language] + "]]"
    
  elif (domaine=="vulgaires"):
    wikitext += "[[Catégorie:Registres de langue en " + language + "|vulgaire]]\n"
    wikitext += "[[Catégorie:Langage vulgaire|" + cle[language] + "]]"
    
  return wikitext

def createCategoryTermesEnParCaractere(page,cle):
  #Catégorie:Termes en anglais par caractère
  language = guessLanguage(page,"en","par",cle)
  if (language not in cle):
    return

  wikitext = "[[Catégorie:Termes par caractère|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Curiosités linguistiques en " + language + "]]"
  return wikitext

def createCategoryTitresNoblesse(page,cle):
  #Catégorie:Titres de noblesse en suédois
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  wikitext = "[[Catégorie:Titres de noblesse|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la noblesse]]"
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
  #Catégorie:Traductions en anglais
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  wikitext = "{{CatégorieTDM}}\n"
  wikitext += "__HIDDENCAT__\n\n"

  wikitext += "[[Catégorie:Traductions|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:" + language + "]]"

  return wikitext

def createCategoryTraductionsManquantes(page, cle, code):
  #Catégorie:Wiktionnaire:Traductions manquantes en espéranto
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  wikitext = "La traduction en " + language + " de ces mots n’a pas été précisée, merci d’y remédier si vous le pouvez. Pour une liste beaucoup plus complète : [//fr.wiktionary.org/w/index.php?title=Sp%C3%A9cial:Recherche&limit=250&offset=0&profile=default&search=insource%3A%22%7B%7BS%7Ctraductions%7D%7D%22+-insource%3A%22%7B%7BT%7C" + code[language] + "%7D%7D%22]\n\n"

  wikitext += "__HIDDENCAT__\n"
  wikitext += "{{DEFAULTSORT:" + cle[language] + "  traductions manquantes}}\n"
  wikitext += "[[Catégorie:Wiktionnaire:Traductions manquantes]]"

  return wikitext

def createCategoryTraductionsTrier(page, cle, code):
  #Catégorie:Wiktionnaire:Traductions à trier en zoulou
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  wikitext = "{{Catégorie:Wiktionnaire:Traductions à trier (par langue)|" + code[language] + "}}"

  return wikitext

def createCategoryVehicules(page,cle):
  #Catégorie:Véhicules en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  wikitext = "[[Catégorie:Véhicules|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Machines en " + language + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "]]"
  return wikitext

def createCategoryVerbes(page,cle):
  #Catégorie:Verbes en anglais
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  wikitext = "[[Catégorie:Verbes par langue|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Conjugaison en " + language + "]]\n"
  wikitext += "[[Catégorie:Grammaire en " + language + "]]"
  return wikitext

def createCategoryVertebres(page,cle):
  #Catégorie:Vertébrés en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext ="[[Catégorie:Vertébrés|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|vertebres]]\n"
  wikitext += "[[Catégorie:Animaux multicellulaires en " + language + "|vertebres]]"
  return wikitext

def createCategoryVieDomestique(page,cle):
  #Catégorie:Vie domestique en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext ="[[Catégorie:Vie domestique|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|vie domestique]]"
  return wikitext

def createCategoryVirus(page,cle):
  #Catégorie:Virus en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Virus|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la virologie]]\n"
  wikitext += "[[Catégorie:Maladies en " + language + "]]\n"
  wikitext += "[[Catégorie:Acaryotes en " + language + "]]"
  return wikitext

def createCategoryVetements(page,cle):
  #Catégorie:Vêtements en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext ="[[Catégorie:Vêtements|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|vetements]]"
  return wikitext

def createCategoryEdifices(page,cle):
  #Catégorie:Édifices en vietnamien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext ="[[Catégorie:Édifices|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la construction| edifices]]"
  return wikitext

def createCategoryEpices(page,cle):
  #Catégorie:Épices en grec
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  wikitext ="[[Catégorie:Épices|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Aliments en " + language + "|Epices]]"
  return wikitext

def createCategoryElementsChimiques(page,cle):
  #Catégorie:Éléments chimiques en grec
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext ="[[Catégorie:Éléments chimiques|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|Elements chimiques]]\n"
  wikitext += "[[Catégorie:Substances chimiques en " + language + "|Elements chimiques]]"
  return wikitext

def createCategorySubstancesChimiques(page,cle):
  #Catégorie:Substances chimiques en français
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext ="[[Catégorie:Substances chimiques|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la chimie| Substances chimiques]]"
  return wikitext

def createCategoryFormesEn(page,cle):
  #Catégorie:Formes de noms propres en allemand
  notTreated = ["locutions", "pronoms", "noms scientifiques","articles"]
  
  beg=page.find(" d")
  end=page.find(" en ",beg+1)
  if(page[beg+2:beg+3] == "’"):
    beg=beg+3
  else:
    beg = page.find(" ",beg+1)+1
  # [beg:end] pour les cas comme Catégorie:Formes de noms communs en me’phaa de Malinaltepec
  word=page[beg:end]
  for aWord in notTreated:
    if(word.find(aWord) != -1):
      return
    
  language=page[end+4:]
  if (language not in cle):
    return
  
  particle = ""
  if(page[:beg].find(" d’") != -1):
    particle="d’"
  elif(page[:beg].find(" des") != -1):
    particle="des "
  elif(page[:beg].find(" de") != -1):
    particle="de "
  elif(page[:beg].find(" du") != -1):
    particle="du "
  
  wikitext = "[[Catégorie:Formes " + particle + word + "|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:" + word[:1].upper() + word[1:] + " en " + language + "]]"
  return wikitext

def createCategoryPaysEnLangue(page,cle,continent):
  #Catégorie:Kiribati en same du Nord
  #Catégorie:Asie en français
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  isPays = False
  isContinent = False
  
  end=beg
  beg=page.find(":")
  paysContinent=page[beg+1:end]
  if (paysContinent in continent):
    isPays = True
  if (not isPays and paysContinent in continent.values()):
    isContinent = True
  if (not isPays and not isContinent):
    return

  if isPays:
    wikitext = "[[Catégorie:" + paysContinent + "|" + cle[language] + "]]\n"
    if (paysContinent != "Antilles" and
        paysContinent != "Québec"):
      wikitext += "[[Catégorie:Pays en " + language + "]]\n"
    wikitext += "[[Catégorie:" + continent[paysContinent] + " en " + language + "|" + CleDeTri.CleDeTri(paysContinent) + "]]"
  if isContinent:
    wikitext = "[[Catégorie:" + paysContinent + " par langue|" + cle[language] + "]]\n"
    wikitext += "[[Catégorie:Continents en " + language + "|" + CleDeTri.CleDeTri(paysContinent) + "]]"
    
  return wikitext

def createCategoryLangueDePays(page,cle,code,continent):
  #Catégorie:espagnol du Chili
  #Catégorie:français d’Inde
  #Catégorie:français d’Asie

  isPays = False
  isContinent = False
  
  beg=page.find(" d")
  language=page[10:beg] # 10 pour Catégorie:
  if (language not in cle):
    return
  if (language not in code):
    return
  
  beg2=page.find("’",beg)
  if(beg2 == -1 or beg2!=beg+2):
    beg2 = page.find(" ",beg+1)
  paysContinent=page[beg2+1:]
  if (paysContinent in continent):
    isPays = True
  if (not isPays and paysContinent in continent.values()):
    isContinent = True
  if (not isPays and not isContinent):
    return

  #Page de test : Catégorie:agni morofoué de Côte d’Ivoire
  posPays = page.find(paysContinent)
  particle = ""
  pageShort = page[len(language):posPays]
  if(pageShort.find(" d’") != -1):
    particle="d’"
  elif(pageShort.find(" des") != -1):
    particle="des "
  elif(pageShort.find(" de") != -1):
    particle="de "
  elif(pageShort.find(" du") != -1):
    particle="du "

  if isPays:
    de2=" d’"
    if(continent[paysContinent] == "Caraïbes"):
      de2=" des "
    if(continent[paysContinent] == "Canada" or
       continent[paysContinent] == "Royaume-Uni"):
      de2=" du "
    wikitext = "__NOTOC__\n"
    wikitext += "* Merci d’utiliser {{modl|" + paysContinent + "|" + code[language] + "}} pour ajouter des termes dans cette catégorie.\n\n"
    if paysContinent == "Antilles":
      wikitext += "[[Catégorie:" + language + " régional]]"
    else:
      wikitext += "[[Catégorie:Régionalisme " + particle + paysContinent + "|" + cle[language] + "]]\n"
      wikitext += "[[Catégorie:" + language + de2 + continent[paysContinent] + "|" + CleDeTri.CleDeTri(paysContinent) + "]]\n"
      wikitext += "[[Catégorie:Langues " + particle + paysContinent + "|" + cle[language] + "]]"

  if isContinent:
    wikitext = "__NOTOC__\n"
    wikitext += "* Merci d’utiliser {{modl|" + paysContinent + "|" + code[language] + "}} pour ajouter des termes dans cette catégorie.\n\n"
    wikitext += "=== Voir aussi ===\n"
    wikitext += "*{{WP|Projet:" + paysContinent + "}}\n\n"
    wikitext += "[[Catégorie:" + language + " régional|" + CleDeTri.CleDeTri(paysContinent) + "]]"
  
  return wikitext

def createCategoryLanguesDePays(page,cle,continent):
  #Catégorie:Langues de France
  #Catégorie:Langues d’Europe

  isPays = False
  isContinent = False
  
  beg=page.find(" d")  
  beg2=page.find("’",beg)
  if(beg2 == -1 or beg2!=beg+2):
    beg2 = page.find(" ",beg+1)
  paysContinent=page[beg2+1:]
  if (paysContinent in continent):
    isPays = True
  if (not isPays and paysContinent in continent.values()):
    isContinent = True
  if(not isPays and not isContinent):
    return
      
  if isPays:
    de=" d’"
    if(continent[paysContinent] == "Caraïbes"):
      de=" des "
    if(continent[paysContinent] == "Canada" or
       continent[paysContinent] == "Royaume-Uni"):
      de=" du "
    wikitext = "[[Catégorie:Langues par pays|" + CleDeTri.CleDeTri(paysContinent) + "]]\n"
    wikitext += "[[Catégorie:" + paysContinent + "| Langues]]"
  if isContinent:
    de=" d’"
    if(paysContinent == "Caraïbes"):
      de=" des "
    wikitext = "=== Voir aussi ===\n"
    wikitext += "* {{Catégorie|Régionalismes" + de + paysContinent + "}}\n"
    wikitext += "* {{Catégorie|Langues par pays}}\n\n"
    wikitext += "[[Catégorie:Langues par continent|" + CleDeTri.CleDeTri(paysContinent) + "]]\n"
    wikitext += "[[Catégorie:" + paysContinent + "| Langues]]"
    
  return wikitext

def createCategoryIlesDePaysEn(page,cle,continent):
  #Catégorie:Îles de Grèce en grec

  isPays = False
  isContinent = False

  beg=page.find(" d")
  beg2=page.find("’",beg)
  if(beg2 == -1 or beg2!=beg+2):
    beg2=page.find(" ",beg+1)
  end=page.find(" en ")
  paysContinent=page[beg2+1:end]
  if (paysContinent in continent):
    isPays = True
  if (not isPays and paysContinent in continent.values()):
    isContinent = True
  if(not isPays and not isContinent):
    return
  
  language=page[end+4:]
  if (language not in cle):
    return

  particle = ""
  if(page.find("Îles d’") != -1):
    particle="d’"
  elif(page.find("Îles des") != -1):
    particle="des "
  elif(page.find("Îles de") != -1):
    particle="de "
  elif(page.find("Îles du") != -1):
    particle="du "
      
  if isPays:
    wikitext = "[[Catégorie:Îles en " + language + "|" + CleDeTri.CleDeTri(paysContinent) + "]]\n"
    wikitext += "[[Catégorie:Îles " + particle + paysContinent + "|" + cle[language] + "]]\n"
    wikitext += "[[Catégorie:" + paysContinent + " en " + language + "|Iles]]"
    
  if isContinent:
    de="d’"
    if(paysContinent == "Caraïbes"):
      de="des "

    wikitext = "[[Catégorie:Îles en " + language + "|" + CleDeTri.CleDeTri(paysContinent) + "]]\n"
    wikitext += "[[Catégorie:Îles " + de + paysContinent + "|" + cle[language] + "]]\n"
    wikitext += "[[Catégorie:" + paysContinent + " en " + language +"| Iles]]"

  return wikitext

def createCategoryLanguesDePaysEn(page,cle,continent):
  #Catégorie:Langues de France en français
  #Catégorie:Langues d’Afrique en français
  #Catégorie:Langues de Côte d’Ivoire en bambara

  isPays = False
  isContinent = False

  beg=page.find(" d")
  beg2=page.find("’",beg)
  if(beg2 == -1 or beg2!=beg+2):
    beg2=page.find(" ",beg+1)
  end=page.find(" en ")
  paysContinent=page[beg2+1:end]
  if (paysContinent in continent):
    isPays = True
  if (not isPays and paysContinent in continent.values()):
    isContinent = True
  if(not isPays and not isContinent):
    return
  
  language=page[end+4:]
  if (language not in cle):
    return

  particle = ""
  if(page.find("Langues d’") != -1):
    particle="d’"
  elif(page.find("Langues des") != -1):
    particle="des "
  elif(page.find("Langues de") != -1):
    particle="de "
  elif(page.find("Langues du") != -1):
    particle="du "
      
  if isPays:
    de="d’"
    if(continent[paysContinent] == "Caraïbes"):
      de="des "
    if(continent[paysContinent] == "Canada" or
       continent[paysContinent] == "Royaume-Uni"):
      de="du "
    wikitext = "[[Catégorie:Langues par pays en " + language + "|" + CleDeTri.CleDeTri(paysContinent) + "]]\n"
    wikitext += "[[Catégorie:Langues " + de + continent[paysContinent] + " en " + language + "|" + CleDeTri.CleDeTri(paysContinent) + "]]\n"
    wikitext += "[[Catégorie:Langues " + particle + paysContinent + "|" + cle[language] + "]]\n"
    wikitext += "[[Catégorie:" + paysContinent + " en " + language + "]]"
    
  if isContinent:
    liste = []
    de="d’"
    le="l’"
    if(paysContinent == "Caraïbes"):
      le="les "
      de="des "
    wikitext = "Cette catégorie rassemble les catégories de langues par pays en " + language + " pour " + le + paysContinent + ".\n\n"
    wikitext += "=== Voir aussi ===\n"
    wikitext += "* {{Catégorie|Régionalismes " + de + paysContinent + "}}\n"
    for aContinent in continent.values():
      if aContinent not in liste:
        liste.append(aContinent)
      else:
        continue
      if (aContinent != paysContinent):
        if(aContinent=="Caraïbes"):
          wikitext += "* {{Catégorie|Langues des " + aContinent + " en " + language + "}}\n"
        else:
          wikitext += "* {{Catégorie|Langues d’" + aContinent + " en " + language + "}}\n"
    wikitext += "\n"
    wikitext += "[[Catégorie:Langues " + de + paysContinent + "|" + cle[language] + "]]"
    
  return wikitext

def createCategoryRegionsDePaysEn(page,cle,continent):
  #Catégorie:Régions de France en japonais
  #Catégorie:Régions d’Europe en coréen

  isPays = False
  isContinent = False

  beg=page.find(" d")
  beg2=page.find("’",beg)
  if(beg2 == -1 or
     (beg2!=beg+2 and
     beg2!=beg+5)): # Régions de l’Inde
    beg2=page.find(" ",beg+1)
  end=page.find(" en ")
  paysContinent=page[beg2+1:end]
  if (paysContinent in continent):
    isPays = True
  if (not isPays and paysContinent in continent.values()):
    isContinent = True
  if(not isPays and not isContinent):
    return
  
  language=page[end+4:]
  if (language not in cle):
    return

  particle = ""
  if(page.find("Régions d’") != -1):
    particle="d’"
  elif(page.find("Régions des") != -1):
    particle="des "
  elif(page.find("Régions de") != -1):
    particle="de "
  if(page.find("Régions de l’") != -1):
    particle="de l’"
  elif(page.find("Régions du") != -1):
    particle="du "
      
  if isPays:
    de="d’"
    if(continent[paysContinent] == "Caraïbes"):
      de="des "
    if(continent[paysContinent] == "Canada" or
       continent[paysContinent] == "Royaume-Uni"):
      de="du "
    wikitext = "[[Catégorie:Régions " + de + continent[paysContinent] + " en " + language + "|" + cle[language] + "]]\n"
    wikitext += "[[Catégorie:Régions en " + language + "|" + CleDeTri.CleDeTri(paysContinent) + "]]\n"
    wikitext += "[[Catégorie:" + paysContinent + " en " + language + "|regions]]"

  if isContinent:
    wikitext = "[[Catégorie:Régions " + particle + paysContinent + "|" + cle[language] + "]]\n"
    wikitext += "[[Catégorie:Régions en " + language + "|" + CleDeTri.CleDeTri(paysContinent) + "]]\n"
    wikitext += "[[Catégorie:" + paysContinent + " en " + language + "|Regions]]"    
    
  return wikitext

def createCategoryRegionsDe(page,cle,continent):
  #Catégorie:Régions de France
  #Catégorie:Régions d’Europe

  isPays = False
  isContinent = False

  beg=page.find(" d")
  beg2=page.find("’",beg)
  if(beg2 == -1 or
     (beg2!=beg+2 and
     beg2!=beg+5)): # Régions de l’Inde
    beg2=page.find(" ",beg+1)
  paysContinent=page[beg2+1:]
  if (paysContinent in continent):
    isPays = True
  if (not isPays and paysContinent in continent.values()):
    isContinent = True
  if(not isPays and not isContinent):
    return

  particle = ""
  if(page.find("Régions d’") != -1):
    particle="d’"
  elif(page.find("Régions des") != -1):
    particle="des "
  elif(page.find("Régions de") != -1):
    particle="de "
  if(page.find("Régions de l’") != -1):
    particle="de l’"
  elif(page.find("Régions du") != -1):
    particle="du "
      
  if isPays:
    de="d’"
    if(continent[paysContinent] == "Caraïbes"):
      de="des "
    if(continent[paysContinent] == "Canada" or
       continent[paysContinent] == "Royaume-Uni"):
      de="du "
    wikitext = "[[Catégorie:" + paysContinent + "| Regions]]\n"
    wikitext = "[[Catégorie:Régions " + de + continent[paysContinent] + "|" +  CleDeTri.CleDeTri(paysContinent) + "]]"

  if isContinent:
    wikitext = "[[Catégorie:Régions|" + CleDeTri.CleDeTri(paysContinent) + "]]\n"
    wikitext += "[[Catégorie:" + paysContinent + "|Regions]]"    
    
  return wikitext

def createCategoryRegionsEn(page,cle):
  #Catégorie:Régions en japonais
  
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return

  wikitext = "[[Catégorie:Régions par langue|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|Regions]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la géographie|Regions]]"    
    
  return wikitext

def createCategory(page,cle,code,country,listeLexique):  
  #Convert Category into string object
  page = str(page)
  beg=page.find(":")
  end=page.find("]]")
  page = page[beg+1:end]

  wikitext = ""
  if (page.find("Catégorie:Prononciations audio en") != -1):
     wikitext = createCategoryPrononciationAudio(page,cle)
  elif (page.find("Catégorie:Caractère ") != -1):
     wikitext = createCategoryCaractereEn(page,cle)
  elif (page.find("Catégorie:Grammaire en") != -1):
     wikitext = createCategoryGrammaire(page,cle)
  elif (page.find("Catégorie:Wiktionnaire:Conjugaisons manquantes en ") != -1):
     wikitext = createCategoryConjugaisonsManquantes(page,cle)
  elif (page.find("Catégorie:Wiktionnaire:Ébauches en ") != -1):
     wikitext = createCategoryEbauches(page,cle)
  elif (page.find("Catégorie:Wiktionnaire:Étymologies manquantes en ") != -1):
     wikitext = createCategoryEtymologiesManquantes(page,cle)
  elif (page.find("Catégorie:Wiktionnaire:Exemples manquants en ") != -1):
     wikitext = createCategoryExemplesManquants(page,cle)
  elif (page.find("Catégorie:Wiktionnaire:Prononciations manquantes en ") != -1):
     wikitext = createCategoryPrononciationsManquantes(page,cle)
  elif (page.find("Catégorie:Wiktionnaire:Prononciations audio manquantes en ") != -1):
     wikitext = createCategoryPrononciationsAudioManquantes(page,cle)
  elif (page.find("Catégorie:Wiktionnaire:Prononciations phonétiques manquantes en ") != -1):
     wikitext = createCategoryPrononciationsPhonetiquesManquantes(page,cle)
  elif (page.find("Catégorie:Compositions en ") != -1):
     wikitext = createCategoryCompositionsEn(page,cle)
  elif (page.find("Catégorie:Dérivations en ") != -1):
     wikitext = createCategoryDerivationsEn(page,cle)
  elif (page.find("Catégorie:Étymologies en ") != -1 and
        page.find(" incluant une reconstruction") != -1):
     wikitext = createCategoryEtymologiesEnIncluantReconstruction(page,cle)
  elif (page.find("Catégorie:Adjectifs en") != -1):
     wikitext = createCategoryAdjectifs(page,cle)
  elif (page.find("Catégorie:Adverbes en") != -1):
     wikitext = createCategoryAdverbes(page,cle)
  elif (page.find("Catégorie:Acaryotes en") != -1):
     wikitext = createCategoryAcaryotes(page,cle)
  elif (page.find("Catégorie:Aliments en") != -1):
     wikitext = createCategoryAliments(page,cle)
  elif (page.find("Catégorie:Animaux en") != -1):
     wikitext = createCategoryAnimaux(page,cle)
  elif (page.find("Catégorie:Animaux multicellulaires en") != -1):
     wikitext = createCategoryAnimauxMulticellulaires(page,cle)
  elif (page.find("Catégorie:Arbres en") != -1):
     wikitext = createCategoryArbres(page,cle)
  elif (page.find("Catégorie:Armes en") != -1):
     wikitext = createCategoryArmes(page,cle)
  elif (page.find("Catégorie:Bateaux en") != -1):
     wikitext = createCategoryBateaux(page,cle)
  elif (page.find("Catégorie:Boissons en") != -1):
     wikitext = createCategoryBoissons(page,cle)
  elif (page.find("Catégorie:Calendrier en") != -1):
     wikitext = createCategoryCalendrier(page,cle)
  elif ((page.find("Catégorie:Calques en") != -1) and
        (page.find("issus d’un mot en") == -1)):
    wikitext = createCategoryCalquesEn(page,cle)
  elif (page.find("Catégorie:Calques issus d") != -1):
    wikitext = createCategoryCalquesIssus(page,cle)
  elif ((page.find("Catégorie:Calques en") != -1) and
        (page.find("issus d’un mot en") != -1)):
    wikitext = createCategoryCalquesEnIssusDunMot(page,cle)
  elif (page.find("Catégorie:Emprunts en") != -1):
    wikitext = createCategoryEmpruntsEn(page,cle)
  elif (page.find("Catégorie:Emprunts vers") != -1):
    wikitext = createCategoryEmpruntsVers(page,cle)
  elif (page.find("Catégorie:Cardinaux en") != -1):
     wikitext = createCategoryCardinaux(page,cle)
  elif (page.find("Catégorie:Céréales en") != -1):
     wikitext = createCategoryCereales(page,cle)
  elif (page.find("Catégorie:Circonfixes en") != -1):
     wikitext = createCategoryCirconfixes(page,cle,code)
  elif (page.find("Catégorie:Cocktails en") != -1):
     wikitext = createCategoryCocktails(page,cle)
  elif (page.find("Catégorie:Conjonctions en") != -1):
     wikitext = createCategoryConjonctions(page,cle)
  elif (page.find("Catégorie:Conjugaison en") != -1):
     wikitext = createCategoryConjugaison(page,cle)
  elif (page.find("Catégorie:Couleurs en") != -1):
     wikitext = createCategoryCouleurs(page,cle)
  elif (page.find("Catégorie:Cours d’eau d") != -1 and
        page.find(" en ") != -1):
     wikitext = createCategoryCoursDeauDePaysEn(page,cle,country)
  elif (page.find("Catégorie:Cours d’eau d") != -1):
     wikitext = createCategoryCoursDeauDePays(page,cle,country)
  elif (page.find("Catégorie:Cours d’eau en") != -1):
     wikitext = createCategoryCoursDeauEn(page,cle)
  elif (page.find("Catégorie:Curiosités linguistiques en") != -1):
     wikitext = createCategoryCuriositesLinguistiques(page,cle)
  elif (page.find("Catégorie:Date manquante en") != -1):
     wikitext = createCategoryDateManquante(page,cle)
  elif (page.find("Catégorie:Divinités en") != -1):
     wikitext = createCategoryDivinitesEn(page,cle)
  elif (page.find("Catégorie:Divinités") != -1 and
        page.find("Catégorie:Divinités en") == -1):
     wikitext = createCategoryDivinitesXXXEn(page,cle)
  elif (page.find("Catégorie:Eucaryotes en") != -1):
     wikitext = createCategoryEucaryotes(page,cle)
  elif (page.find("Catégorie:Super-règnes en") != -1):
     wikitext = createCategorySuperRegnes(page,cle)
  elif (page.find("Catégorie:Exemples en") != -1 and
        page.find("à traduire") != -1):
     wikitext = createCategoryExemplesTraduire(page,cle)
  elif (page.find("Catégorie:Exemples en") != -1):
     wikitext = createCategoryExemples(page,cle)
  elif (page.find("Catégorie:Expressions en") != -1):
     wikitext = createCategoryExpressions(page,cle)
  elif (page.find("Catégorie:Formes d") != -1 and
        page.find(" en ") != -1):
     wikitext = createCategoryFormesEn(page,cle)
  elif (page.find("Catégorie:Arthropodes en") != -1):
     wikitext = createCategoryArthropodes(page,cle)
  elif (page.find("Catégorie:Caprins en") != -1):
     wikitext = createCategoryCaprins(page,cle)
  elif (page.find("Catégorie:Crustacés en") != -1):
     wikitext = createCategoryCrustaces(page,cle)
  elif (page.find("Catégorie:Chevaux en") != -1):
     wikitext = createCategoryChevaux(page,cle)
  elif (page.find("Catégorie:Crapauds en") != -1):
     wikitext = createCategoryCrapauds(page,cle)
  elif (page.find("Catégorie:Équins en") != -1):
     wikitext = createCategoryEquins(page,cle)
  elif (page.find("Catégorie:Ecdysozoaires en") != -1):
     wikitext = createCategoryEcdysozoaires(page,cle)
  elif (page.find("Catégorie:Félins en") != -1):
     wikitext = createCategoryFelins(page,cle)
  elif (page.find("Catégorie:Ongulés en") != -1):
     wikitext = createCategoryOngules(page,cle)
  elif (page.find("Catégorie:Ovins en") != -1):
     wikitext = createCategoryOvins(page,cle)
  elif (page.find("Catégorie:Papillons en") != -1):
     wikitext = createCategoryPapillons(page,cle)
  elif (page.find("Catégorie:Reptiles en") != -1):
     wikitext = createCategoryReptiles(page,cle)
  elif (page.find("Catégorie:Ruminants en") != -1):
     wikitext = createCategoryRuminants(page,cle)
  elif (page.find("Catégorie:Tétrapodes en") != -1):
     wikitext = createCategoryTetrapodes(page,cle)
  elif (page.find("Catégorie:Tortues en") != -1):
     wikitext = createCategoryTortues(page,cle)
  elif (page.find("Catégorie:Fruits en") != -1):
     wikitext = createCategoryFruits(page,cle)
  elif (page.find("Catégorie:Fruits de mer en") != -1):
     wikitext = createCategoryFruitsMer(page,cle)
  elif (page.find("Catégorie:Fromages en") != -1):
     wikitext = createCategoryFromages(page,cle)
  elif (page.find("Catégorie:Gâteaux en") != -1):
     wikitext = createCategoryGateaux(page,cle)
  elif (page.find("Catégorie:Gentilés d") != -1 and
        page.find(" en ") != -1):
     wikitext = createCategoryGentilesDePaysEn(page,cle,country)
  elif (page.find("Catégorie:Gentilés d") != -1):
     wikitext = createCategoryGentilesDePays(page,cle,country)
  elif (page.find("Catégorie:Gentilés en") != -1):
     wikitext = createCategoryGentilesEn(page,cle)
  elif (page.find("Catégorie:Îles d") != -1 and
        page.find(" en ") != -1):
     wikitext = createCategoryIlesDePaysEn(page,cle,country)
  elif (page.find("Catégorie:Infixes en") != -1):
     wikitext = createCategoryInfixes(page,cle,code)
  elif (page.find("Catégorie:Interfixes en") != -1):
     wikitext = createCategoryInterfixes(page,cle,code)
  elif (page.find("Catégorie:Insectes en") != -1):
     wikitext = createCategoryInsectes(page,cle)
  elif (page.find("Catégorie:Instruments de musique en") != -1):
     wikitext = createCategoryInstrumentsDeMusique(page,cle)
  elif (page.find("Catégorie:Interrogatifs en") != -1):
     wikitext = createCategoryInterrogatifs(page,cle)
  elif (page.find("Catégorie:Jours de la semaine en") != -1):
     wikitext = createCategoryJoursSemaine(page,cle)
  elif (page.find("Catégorie:Langues en") != -1):
     wikitext = createCategoryLangues(page,cle)
  elif (page.find("Catégorie:Langues d") != -1 and
        page.find(" en ") == -1):
     wikitext = createCategoryLanguesDePays(page,cle,country)
  elif (page.find("Catégorie:Langues d") != -1 and
        page.find(" en ") != -1):
     wikitext = createCategoryLanguesDePaysEn(page,cle,country)
  elif (page.find("Catégorie:Régions d") != -1 and
        page.find(" en ") != -1):
     wikitext = createCategoryRegionsDePaysEn(page,cle,country)
  elif (page.find("Catégorie:Régions d") != -1):
     wikitext = createCategoryRegionsDe(page,cle,country)
  elif (page.find("Catégorie:Régions en") != -1):
     wikitext = createCategoryRegionsEn(page,cle)
  elif (page.find("Catégorie:Légumes en") != -1):
     wikitext = createCategoryLegumes(page,cle)
  elif (page.find("Catégorie:Métaux en") != -1):
     wikitext = createCategoryMetaux(page,cle)
  elif (page.find("Catégorie:Dates manquantes en") != -1):
     wikitext = createCategoryDatesManquantes(page,cle)
  elif (page.find("Catégorie:Langage enfantin en") != -1):
     wikitext = createCategoryLangageEnfantin(page, cle)
  elif (page.find("Catégorie:Lexique en") != -1):
     wikitext = createCategoryLexique(page, cle, code, listeLexique)
  elif (page.find("Catégorie:Lexiques en") != -1):
     wikitext = createCategoryLexiques(page,cle)
  elif (page.find("Catégorie:Localités d") != -1 and
        (page.find(" en ") != -1)):
      wikitext = createCategoryLocalitesDeEn(page,cle,country)
  elif (page.find("Catégorie:Localités d") != -1):
      wikitext = createCategoryLocalitesDe(page,cle,country)
  elif (page.find("Catégorie:Localités en") != -1):
      wikitext = createCategoryLocalitesEn(page,cle)
  elif (page.find("Catégorie:Locutions en") != -1):
     wikitext = createCategoryLocutions(page,cle)
  elif (page.find("Catégorie:Mammifères en") != -1):
     wikitext = createCategoryMammiferes(page,cle)
  elif (page.find("Catégorie:Marsupiaux en") != -1):
     wikitext = createCategoryMarsupiaux(page,cle)
  elif (page.find("Catégorie:Métiers en") != -1):
     wikitext = createCategoryMetiersEn(page,cle)
  elif (page.find("Catégorie:Métiers du secteur") != -1):
     wikitext = createCategoryMetiersSecteur(page,cle)
  elif (page.find("Catégorie:Métiers du droit en") != -1):
     wikitext = createCategoryMetiersDroit(page,cle)
  elif (page.find("Catégorie:Métiers de la restauration en") != -1):
     wikitext = createCategoryMetiersRestauration(page,cle)
  elif (page.find("Catégorie:Métiers de la santé en") != -1):
     wikitext = createCategoryMetiersSante(page,cle)
  elif (page.find("Catégorie:Métiers de la science en") != -1):
     wikitext = createCategoryMetiersScience(page,cle)
  elif (page.find("Catégorie:Métiers de la vente en") != -1):
     wikitext = createCategoryMetiersVente(page,cle)
  elif (page.find("Catégorie:Mots en espéranto comportant la racine ") != -1):
    wikitext = createCategoryMotsEnEsperantComportantRacine(page)
  elif ((page.find("Catégorie:Mots en") != -1) and
        (page.find("issus d’un mot en") != -1)):
    wikitext = createCategoryMotsEnIssusDunMot(page,cle)
  elif ((page.find("Catégorie:Mots en") != -1) and
        (page.find("issus d’une onomatopée") != -1)):
    wikitext = createCategoryMotsEnIssusDuneOnomatopee(page,cle)
  elif (page.find("Catégorie:Mots issus d’un mot en ") != -1):
    wikitext = createCategoryMotsIssusDunMot(page,cle)
  elif ((page.find("Catégorie:Mots en ") != -1) and
        (page.find("infixés avec") != -1)):
    wikitext = createCategoryMotsEnInfixeAvec(page,cle)
  elif ((page.find("Catégorie:Mots en ") != -1) and
        (page.find("préfixés avec") != -1)):
    wikitext = createCategoryMotsEnPrefixeAvec(page,cle)
  elif ((page.find("Catégorie:Mots en ") != -1) and
        (page.find("suffixés avec") != -1)):
    wikitext = createCategoryMotsEnSuffixeAvec(page,cle)
  elif (page.find("Catégorie:Nombres en ") != -1):
    wikitext = createCategoryNombres(page,cle)
  elif (page.find("Catégorie:Noms communs en ") != -1):
     wikitext = createCategoryNomsCommuns(page,cle)
  elif (page.find("Catégorie:Noms animés en ") != -1):
     wikitext = createCategoryNomsAnimes(page,cle)
  elif (page.find("Catégorie:Noms dénombrables en ") != -1):
     wikitext = createCategoryNomsDenombrables(page,cle)
  elif (page.find("Catégorie:Noms inanimés en ") != -1):
     wikitext = createCategoryNomsInanimes(page,cle)
  elif (page.find("Catégorie:Noms indénombrables en ") != -1):
     wikitext = createCategoryNomsIndenombrables(page,cle)
  elif (page.find("Catégorie:Noms multigenres en ") != -1):
     wikitext = createCategoryNomsMultigenresEn(page,cle)
  elif (page.find("Catégorie:Mots parfois masculins ou féminins en ") != -1):
     wikitext = createCategoryMotsParfoisMasculinsFeminins(page,cle)
  elif (page.find("Catégorie:Mots parfois féminins ou masculins en ") != -1):
     wikitext = createCategoryMotsParfoisFemininsMasculins(page,cle)
  elif ((page.find("Catégorie:Noms propres en ") != -1) and
        (page.find("issus d’un mot en") == -1)):
     wikitext = createCategoryNomsPropres(page,cle)
  elif ((page.find("Catégorie:Noms propres en ") != -1) and
        (page.find("issus d’un mot en") != -1)):
    wikitext = createCategoryNomsPropresIssus(page,cle)
  elif (page.find("Catégorie:Noms de sciences en ") != -1):
     wikitext = createCategoryNomsSciencesEn(page,cle)
  elif (page.find("Catégorie:Numéraux en") != -1):
     wikitext = createCategoryNumeraux(page,cle)
  elif (page.find("Catégorie:Oiseaux en") != -1):
     wikitext = createCategoryOiseaux(page,cle)
  elif (page.find("Catégorie:Ordinaux en") != -1):
     wikitext = createCategoryOrdinaux(page,cle)
  elif (page.find("Catégorie:Origines étymologiques des mots en ") != -1):
    wikitext = createCategoryOriginesEtmylogiquesMots(page,cle)
  elif (page.find("Catégorie:Origines étymologiques des noms propres en ") != -1):
    wikitext = createCategoryOriginesEtmylogiquesNomsPropres(page,cle)
  elif (page.find("Catégorie:Outils en") != -1):
     wikitext = createCategoryOutils(page,cle)
  elif (page.find("Catégorie:Pages liées en") != -1):
     wikitext = createCategoryPagesLieesEn(page,cle)
  elif (page.find("Catégorie:Pages liées à") != -1):
     wikitext = createCategoryPagesLieesAEn(page,cle)
  elif (page.find("Catégorie:Palindromes en") != -1):
     wikitext = createCategoryPalindromes(page,cle)
  elif (page.find("Catégorie:Pays en") != -1):
     wikitext = createCategoryPays(page,cle)
  elif (page.find("Catégorie:Plantes en") != -1):
     wikitext = createCategoryPlantes(page,cle)
  elif (page.find("Catégorie:Poissons en") != -1):
     wikitext = createCategoryPoissons(page,cle)
  elif (page.find("Catégorie:Préfixes en") != -1):
     wikitext = createCategoryPrefixes(page,cle,code)
  elif (page.find("Catégorie:Prénoms") != -1):
     wikitext = createCategoryPrenoms(page,cle)
  elif (page.find("Catégorie:Préparations culinaires en") != -1):
     wikitext = createCategoryPreparationsCulinaires(page,cle)
  elif (page.find("Catégorie:Registres de langue en") != -1):
     wikitext = createCategoryRegistresLangueEn(page,cle)
  elif (page.find("Catégorie:Saisons en") != -1):
     wikitext = createCategorySaisons(page,cle)
  elif (page.find("Catégorie:Soldats en") != -1):
     wikitext = createCategorySoldats(page,cle)
  elif (page.find("Catégorie:Sports en") != -1):
     wikitext = createCategorySports(page,cle)
  elif (page.find("Catégorie:Suffixes en") != -1):
     wikitext = createCategorySuffixes(page,cle,code)
  elif (page.find("Catégorie:Symboles en") != -1):
     wikitext = createCategorySymboles(page,cle)
  elif (page.find("Catégorie:Références nécessaires en") != -1):
     wikitext = createCategoryReferencesNecessaires(page,cle)
  elif (page.find("Catégorie:Religieux en") != -1):
     wikitext = createCategoryReligieux(page,cle)
  elif (page.find("Catégorie:Roches en") != -1):
     wikitext = createCategoryRoches(page,cle)
  elif ((page.find("Catégorie:Termes ") != -1) and
        page.find(" en ") != -1):
     wikitext = createCategoryTermesEn(page,cle,code)
  elif ((page.find("Catégorie:Termes en ") != -1) and
        (page.find("par caractère") != -1)):
    wikitext = createCategoryTermesEnParCaractere(page,cle)
  elif (page.find("Catégorie:Titres de noblesse en ") != -1):
    wikitext = createCategoryTitresNoblesse(page,cle)
  elif (page.find("Catégorie:Thématiques en ") != -1):
    wikitext = createCategoryThematiques(page,cle)
  elif (page.find("Catégorie:Traductions en ") != -1):
    wikitext = createCategoryTraductions(page,cle)
  elif (page.find("Catégorie:Wiktionnaire:Traductions manquantes en ") != -1):
    wikitext = createCategoryTraductionsManquantes(page,cle,code)
  elif (page.find("Catégorie:Wiktionnaire:Traductions à trier en ") != -1):
    wikitext = createCategoryTraductionsTrier(page, cle, code)
  elif (page.find("Catégorie:Véhicules en ") != -1):
    wikitext = createCategoryVehicules(page,cle)
  elif (page.find("Catégorie:Verbes en ") != -1):
    wikitext = createCategoryVerbes(page,cle)
  elif (page.find("Catégorie:Vertébrés en") != -1):
     wikitext = createCategoryVertebres(page,cle)
  elif (page.find("Catégorie:Vie domestique en") != -1):
     wikitext = createCategoryVieDomestique(page,cle)
  elif (page.find("Catégorie:Virus en") != -1):
     wikitext = createCategoryVirus(page,cle)
  elif (page.find("Catégorie:Vêtements en") != -1):
     wikitext = createCategoryVetements(page,cle)
  elif (page.find("Catégorie:Édifices en") != -1):
     wikitext = createCategoryEdifices(page,cle)
  elif (page.find("Catégorie:Épices en") != -1):
     wikitext = createCategoryEpices(page,cle)
  elif (page.find("Catégorie:Éléments chimiques en") != -1):
     wikitext = createCategoryElementsChimiques(page,cle)
  elif (page.find("Catégorie:Substances chimiques en") != -1):
     wikitext = createCategorySubstancesChimiques(page,cle)
  elif ((page.find("Catégorie:") != -1) and
        page.find(" en ") != -1):
    wikitext = createCategoryPaysEnLangue(page,cle,country)
  elif ((page.find("Catégorie:") != -1) and
        page.find(" d") != -1):
    wikitext = createCategoryLangueDePays(page,cle,code,country)

  else:
    return

  if not wikitext:
    return
  
  pwbpage = pywikibot.Page(pywikibot.Site(), page)
  if not test:
    pwbpage.put(wikitext)
  else:
    pywikibot.output(page + u' :\n' + wikitext)


def getSortingKey():

  cledetri = {}
  codeLangue = {}
  with open("liste_langue.dat") as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
      name, code, key = row
      cledetri[name] = key
      codeLangue[name] = code

  return cledetri, codeLangue

def getContinentByCountryDict():

  output = {}
  with open("country.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
      myCountry, myContinent = row
      output[myCountry]=myContinent

  return output

def getLexique():
  lexique = []
  with open('liste_lexique.dat') as f:
    for line in f:
      lexique.append(line.rstrip())
      
  return lexique

def guessLanguage(page,myBegin,myEnd,cle):
  beg=page.find(" " + myBegin + " ")
  end=page.rfind(" " + myEnd, beg+1)
  
  language = ""
  if len(myEnd)>0:
    language=page[beg+len(myBegin)+2:end]
  else:
    language=page[beg+len(myBegin)+2:]
    
  if test:
    print(language)
  if (language not in cle):
    return
  return language

def guessCountryContinent(page,myBegin,myEnd,cle):
  beg=page.find(" " + myBegin + " ")
  end=page.rfind(" " + myEnd, beg+1)
  countryContinent=""
  
  

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
  cle, codeLangue = getSortingKey()
  continentByCountryDict = getContinentByCountryDict()
  listeLexique = getLexique()

  if test:
    createCategory("[[:Catégorie:Lexique en français des jeux de rôle]]", cle, codeLangue, continentByCountryDict, listeLexique)
    createCategory("[[:Catégorie:Étymologies en portugais incluant une reconstruction]]", cle, codeLangue, continentByCountryDict, listeLexique)
    createCategory("[[:Catégorie:Régions d’Europe en coréen]]", cle, codeLangue, continentByCountryDict, listeLexique)
    createCategory("[[:Catégorie:Lexique en quechua de Cuzco du chemin de fer‏‎]]", cle, codeLangue, continentByCountryDict, listeLexique)
    createCategory("[[:Catégorie:Emprunts vers l’asturien]]", cle, codeLangue, continentByCountryDict, listeLexique)
    createCategory("[[:Catégorie:Emprunts vers le basque]]", cle, codeLangue, continentByCountryDict, listeLexique)
    createCategory("[[:Catégorie:Lexique en ngiemboon de l’aménagement du territoire]]", cle, codeLangue, continentByCountryDict, listeLexique)
    createCategory("[[:Catégorie:agni morofoué de Côte d’Ivoire]]", cle, codeLangue, continentByCountryDict, listeLexique)

    #UserContributionsGenerator
  else:
    for page in WantedPagesCategoryGenerator(5000):
      createCategory(page,cle,codeLangue,continentByCountryDict, listeLexique)
  

if __name__ == '__main__':

  try:

    main()
    
  finally:

    pywikibot.stopme()
