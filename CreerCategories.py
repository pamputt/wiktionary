#! /usr/bin/python3

# -*- coding: utf-8 -*-

import csv
import pywikibot

import CleDeTri

test = False # to test the script (without saving the result)

def createCategoryEtymologiesManquantes(page,cle):
  #Wiktionnaire:Étymologies manquantes en italien
  beg=page.find(" en ")
  language = page[beg+4:]
  if (not language in cle):
    return
  
  wikitext = "L’étymologie de ces mots en [[" + language + "]] n’a pas été précisée, merci d’y remédier si vous la connaissez.\n\n"
  wikitext += "__HIDDENCAT__\n"
  wikitext += "[[Catégorie:Wiktionnaire:Étymologies manquantes|" + cle[language] + "]]"
  return wikitext

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

def createCategoryLexiqueAcoustique(page,cle):
  #Catégorie:Lexique en français de l’acoustique
  beg=page.find(" en ")
  end=page.find(" de l’")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la musique|acoustique]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la physique|acoustique]]\n"
  wikitext += "[[Catégorie:Acoustique|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueAlchimie(page,cle):
  #Catégorie:Lexique en français de l’alchimie
  beg=page.find(" en ")
  end=page.find(" de l’")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "Cette catégorie recense les mots en " + language + " ayant trait à l’[[alchimie]].\n\n"
  wikitext += "[[Catégorie:Lexiques en " + language + "|alchimie]]\n"
  wikitext += "[[Catégorie:Alchimie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueAnthropologie(page,cle):
  #Catégorie:Lexique en anglais de l’anthropologie
  beg=page.find(" en ")
  end=page.find(" de l’")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|anthropologie]]\n"
  wikitext += "[[Catégorie:Anthropologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueAntiquite(page,cle):
  #Catégorie:Lexique en anglais de l’Antiquité
  beg=page.find(" en ")
  end=page.find(" de l’")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de l’histoire|antiquite]]\n"
  wikitext += "[[Catégorie:Antiquité|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueArgent(page,cle):
  #Catégorie:Lexique en italien de l’argent
  beg=page.find(" en ")
  end=page.find(" de l’")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|argent]]\n"
  wikitext += "[[Catégorie:Argent|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueAviation(page,cle):
  #Catégorie:Lexique en italien de l’aviation
  beg=page.find(" en ")
  end=page.find(" de l’")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|aviation]]\n"
  wikitext += "[[Catégorie:Aviation|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueBasesDonnees(page,cle,code):
  #Catégorie:Lexique en anglais des bases de données
  beg=page.find(" en ")
  end=page.find(" des ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  if (language not in code):
    return

  wikitext = "Le vocabulaire peut être ajouté à cette catégorie avec le modèle {{modl|base de données|" + code[language] + "}}.\n\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de l’informatique|base de donnees]]\n"
  wikitext += "[[Catégorie:Bases de données|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueBasketBall(page,cle):
  #Catégorie:Lexique en italien du basket-ball
  beg=page.find(" en ")
  end=page.find(" du ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " du sport|basket ball]]\n"
  wikitext += "[[Catégorie:Basket-ball|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueBiologie(page,cle):
  #Catégorie:Lexique en italien de la biologie
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|biologie]]\n"
  wikitext += "[[Catégorie:Biologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueBotanique(page,cle):
  #Catégorie:Lexique en italien de la botanique
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "Cette catégorie recense les mots en " + language + " ayant trait à la [[botanique]].\n\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la biologie|botanique]]\n"
  wikitext += "[[Catégorie:Botanique|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueCanoeKayak(page,cle):
  #Catégorie:Lexique en français du canoë-kayak
  beg=page.find(" en ")
  end=page.find(" du ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " du sport|canoe kayak]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la navigation|canoe kayak]]\n"
  wikitext += "[[Catégorie:Canoë-kayak|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueCeramique(page,cle,code):
  #Catégorie:Lexique en italien de la céramique
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  if (language not in code):
    return
  
  wikitext = "Vocabulaire concernant la [[céramique]] (art de la terre cuite).\n\n"
  wikitext += "{{modl|céramique|" + code[language] + "}} catégorise ici.\n\n"

  wikitext = "[[Catégorie:Lexiques en " + language + "|ceramique]]\n"
  wikitext += "[[Catégorie:Céramique|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueCharpenterie(page,cle):
  #Catégorie:Lexique en italien de la charpenterie
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la construction|charpenterie]]\n"
  wikitext += "[[Catégorie:Charpenterie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueCheminFer(page,cle):
  #Catégorie:Lexique en italien du chemin de fer
  beg=page.find(" en ")
  end=page.find(" du ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " du transport|chemin de fer]]\n"
  wikitext += "[[Catégorie:Chemin de fer|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueClimatologie(page,cle):
  #Catégorie:Lexique en français de la climatologie
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|climatologie]]\n"
  wikitext += "[[Catégorie:Climatologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueCommerce(page,cle):
  #Catégorie:Lexique en italien du commerce
  beg=page.find(" en ")
  end=page.find(" du ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|commerce]]\n"
  wikitext += "[[Catégorie:Commerce|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueCordonnerie(page,cle):
  #Catégorie:Lexique en français de la cordonnerie
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|cordonnerie]]\n"
  wikitext += "[[Catégorie:Cordonnerie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueCrisAnimaux(page,cle):
  #Catégorie:Lexique en anglais des cris d’animaux
  beg=page.find(" en ")
  end=page.find(" des ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la zoologie|Cris danimaux]]\n"
  wikitext += "[[Catégorie:Cris d’animaux|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueDermatologie(page,cle):
  #Catégorie:Lexique en français de la dermatologie
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return

  wikitext = "[[Catégorie:Lexique en " + language + " de la médecine|dermatologie]]\n"
  wikitext += "[[Catégorie:Dermatologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueEcologie(page,cle):
  #Catégorie:Lexique en italien de l’écologie
  beg=page.find(" en ")
  end=page.find(" de l’")
  language=page[beg+4:end]
  if (language not in cle):
    return

  wikitext = "[[Catégorie:Lexiques en " + language + "|ecologie]]\n"
  wikitext += "[[Catégorie:Écologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueEconomie(page,cle):
  #Catégorie:Lexique en italien de l’économie
  beg=page.find(" en ")
  end=page.find(" de l’")
  language=page[beg+4:end]
  if (language not in cle):
    return

  wikitext = "[[Catégorie:Lexiques en " + language + "|economie]]\n"
  wikitext += "[[Catégorie:Économie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueEscrime(page,cle):
  #Catégorie:Lexique en italien de l’escrime
  beg=page.find(" en ")
  end=page.find(" de l’")
  language=page[beg+4:end]
  if (language not in cle):
    return

  wikitext = "[[Catégorie:Lexique en " + language + " des sports de combat|escrime]]\n"
  wikitext += "[[Catégorie:Escrime|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueFauconnerie(page,cle):
  #Catégorie:Lexique en italien de la fauconnerie
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return

  wikitext = "[[Catégorie:Lexique en " + language + " de l’élevage|fauconnerie]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la chasse|fauconnerie]]\n"
  wikitext += "[[Catégorie:Fauconnerie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueGenealogie(page,cle):
  #Catégorie:Lexique en français de la généalogie
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "Cette catégorie recense les mots en [[" + language + "]] ayant trait à la [[généalogie]].\n\n"
  wikitext += "[[Catégorie:Lexiques en " + language + "|genealogie]]\n"
  wikitext += "[[Catégorie:Généalogie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueGrammaire(page,cle):
  #Catégorie:Lexique en italien de la grammaire
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|grammaire]]\n"
  wikitext += "[[Catégorie:Grammaire|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueGravure(page,cle):
  #Catégorie:Lexique en français de la gravure
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " du livre|gravure]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de l’art|gravure]]\n"
  wikitext += "[[Catégorie:Gravure|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueFamille(page,cle):
  #Catégorie:Lexique en italien de la famille
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|famille]]\n"
  wikitext += "[[Catégorie:Famille|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueGeologie(page,cle):
  #Catégorie:Lexique en italien de la géologie
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|geologie]]\n"
  wikitext += "[[Catégorie:Géologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueGolf(page,cle):
  #Catégorie:Lexique en italien du golf
  beg=page.find(" en ")
  end=page.find(" du ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " du sport|golf]]\n"
  wikitext += "[[Catégorie:Golf|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueHippologie(page,cle):
  #Catégorie:Lexique en anglais de l’hippologie
  beg=page.find(" en ")
  end=page.find(" de l’")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la zoologie|hippologie]]\n"
  wikitext += "[[Catégorie:Hippologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueHistoire(page,cle):
  #Catégorie:Lexique en anglais de l’histoire
  beg=page.find(" en ")
  end=page.find(" de l’")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|histoire]]\n"
  wikitext += "[[Catégorie:Histoire|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueHockey(page,cle):
  #Catégorie:Lexique en italien du hockey
  beg=page.find(" en ")
  end=page.find(" du ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " des sports de glisse|hockey]]\n"
  wikitext += "[[Catégorie:Hockey|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueIchtyologie(page,cle):
  #Catégorie:Lexique en anglais de l’ichtyologie
  beg=page.find(" en ")
  end=page.find(" de l’")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la zoologie|ichtyologie]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de l’élevage|ichtyologie]]\n"
  wikitext += "[[Catégorie:Ichtyologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueImprimerie(page,cle):
  #Catégorie:Lexique en italien de l’imprimerie
  beg=page.find(" en ")
  end=page.find(" de l’")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|imprimerie]]\n"
  wikitext += "[[Catégorie:Imprimerie|" + cle[language] + "]]"

def createCategoryLexiqueJeux(page,cle):
  #Catégorie:Lexique en italien des jeux
  beg=page.find(" en ")
  end=page.find(" des ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " des loisirs|jeux]]\n"
  wikitext += "[[Catégorie:Jeux|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueLivre(page,cle):
  #Catégorie:Lexique en italien du livre
  beg=page.find(" en ")
  end=page.find(" du ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de l’édition|livre]]\n"
  wikitext += "[[Catégorie:Livre|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueMathematiques(page,cle):
  #Catégorie:Lexique en italien des mathématiques
  beg=page.find(" en ")
  end=page.find(" des ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|mathematiques]]\n"
  wikitext += "[[Catégorie:Mathématiques|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueMedias(page,cle):
  #Catégorie:Lexique en italien des médias
  beg=page.find(" en ")
  end=page.find(" des ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|medias]]\n"
  wikitext += "[[Catégorie:Médias|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueMetallurgie(page,cle):
  #Catégorie:Lexique en italien de la métallurgie
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|metallurgie]]\n"
  wikitext += "[[Catégorie:Métallurgie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueMeteorologie(page,cle,code):
  #Catégorie:Lexique en italien de la météorologie
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  if (language not in code):
    return
  
  wikitext = "Cette page liste les mots en " + language + " en rapport avec la [[météorologie]].\n\n"
  wikitext += "Les pages contenant {{modl|météorologie|" + code[language] + "}} sont automatiquement catégorisées ici.\n\n"
  wikitext += "[[Catégorie:Lexiques en " + language + "|meteorologie]]\n"
  wikitext += "[[Catégorie:Météorologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueMetrologie(page,cle):
  #Catégorie:Lexique en italien de la métrologie
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|metrologie]]\n"
  wikitext += "[[Catégorie:Métrologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueMonarchie(page,cle):
  #Catégorie:Lexique en anglais de la monarchie
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la politique|monarchie]]\n"
  wikitext += "[[Catégorie:Monarchie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueMotocyclisme(page,cle):
  #Catégorie:Lexique en italien du motocyclisme
  beg=page.find(" en ")
  end=page.find(" du ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|motocyclisme]]\n"
  wikitext += "[[Catégorie:Motocyclisme|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueMycologie(page,cle):
  #Catégorie:Lexique en italien de la mycologie
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la biologie|mycologie]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la cuisine|mycologie]]\n"
  wikitext += "[[Catégorie:Mycologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueNavigation(page,cle):
  #Catégorie:Lexique en italien de la navigation
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "Cette page liste les mots en " + language + " en rapport avec la [[navigation]].\n\n"
  wikitext += "[[Catégorie:Lexique en " + language + " du transport|navigation]]\n"
  wikitext += "[[Catégorie:Navigation|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueNoblesse(page,cle):
  #Catégorie:Lexique en italien de la noblesse
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la monarchie|noblesse]]\n"
  wikitext += "[[Catégorie:Noblesse|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueOenologie(page,cle,code):
  #Catégorie:Lexique en italien de l’œnologie
  beg=page.find(" en ")
  end=page.find(" de l’")
  language=page[beg+4:end]
  if (language not in cle):
    return
  if (language not in code):
    return
  
  wikitext = "Pour alimenter cette page, merci d’ajouter aux articles le modèle {{modl|oenologie|" + code[language] + "}}.\n"
  wikitext += "[[Catégorie:Lexiques en " + language + "|oenologie]]\n"
  wikitext += "[[Catégorie:Œnologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueOrnithologie(page,cle):
  #Catégorie:Lexique en italien de l’ornithologie
  beg=page.find(" en ")
  end=page.find(" de l’")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la zoologie|ornithologie]]\n"
  wikitext += "[[Catégorie:Ornithologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiquePapeterie(page,cle):
  #Catégorie:Lexique en italien de la papeterie
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " du livre|papeterie]]\n"
  wikitext += "[[Catégorie:Papeterie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiquePatinage(page,cle):
  #Catégorie:Lexique en français du patinage
  beg=page.find(" en ")
  end=page.find(" du ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " des sports d’hiver|patinage]]\n"
  wikitext += "[[Catégorie:Patinage|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiquePeloteBasque(page,cle,code):
  #Catégorie:Lexique en français de la pelote basque
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  if (language not in code):
    return
  
  wikitext = "Pour référencer automatiquement un mot dans cette catégorie, il est possible d’ajouter dans la définition le modèle : {{modl|pelote|" + code[language] + "}}.\n\n"
  wikitext += "[[Catégorie:Lexique en " + language + " du sport|pelote basque]]\n"
  wikitext += "[[Catégorie:Pelote basque|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiquePhilosophie(page,cle):
  #Catégorie:Lexique en italien de la philosophie
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|philosophie]]\n"
  wikitext += "[[Catégorie:Philosophie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiquePhonologie(page,cle):
  #Catégorie:Lexique en anglais de la phonologie
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la linguistique|phonologie]]\n"
  wikitext += "[[Catégorie:Phonologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiquePlomberie(page,cle):
  #Catégorie:Lexique en italien de la plomberie
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la construction|plomberie]]\n"
  wikitext += "[[Catégorie:Plomberie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiquePhysique(page,cle):
  #Catégorie:Lexique en italien de la physique
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|physique]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " des sciences|physique]]\n"
  wikitext += "[[Catégorie:Physique|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiquePhytosociologie(page,cle):
  #Catégorie:Lexique en français de la phytosociologie
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|phytosociologie]]\n"
  wikitext += "[[Catégorie:Phytosociologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiquePhysiologie(page,cle):
  #Catégorie:Lexique en italien de la physiologie
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|physiologie]]\n"
  wikitext += "[[Catégorie:Physiologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiquePrehistoire(page,cle):
  #Catégorie:Lexique en same du Nord de la préhistoire
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de l’histoire|prehistoire]]\n"
  wikitext += "[[Catégorie:Lexiques en " + language + "|prehistoire]]\n"
  wikitext += "[[Catégorie:Préhistoire|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueSerrurerie(page,cle):
  #Catégorie:Lexique en anglais de la serrurerie
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|serrurerie]]\n"
  wikitext += "[[Catégorie:Serrurerie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueTemps(page,cle):
  #Catégorie:Lexique en same du Nord du temps
  beg=page.find(" en ")
  end=page.find(" du ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|temps]]\n"
  wikitext += "[[Catégorie:Temps|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueReseauxInformatiques(page,cle):
  #Catégorie:Lexique en italien des réseaux informatiques
  beg=page.find(" en ")
  end=page.find(" des ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de l’informatique|reseau]]\n"
  wikitext += "[[Catégorie:Réseaux informatiques|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueScienceFiction(page,cle,code):
  #Catégorie:Lexique en italien de la science-fiction
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  if (language not in code):
    return
  
  wikitext = "Les termes peuvent être ajoutés à cette liste avec {{modl|sci-fi|" + code[language] + "}}.\n\n"
  wikitext += "=== Voir aussi ===\n"
  wikitext += "* [[:Catégorie:Lexique en " + language + " du fantastique]]\n\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la littérature|science fiction]]\n"
  wikitext += "[[Catégorie:Science-fiction|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueTextile(page,cle):
  #Catégorie:Lexique en italien du textile
  beg=page.find(" en ")
  end=page.find(" du ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|textile]]\n"
  wikitext += "[[Catégorie:Textile|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueTheologie(page,cle):
  #Catégorie:Lexique en italien de la théologie
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|theologie]]\n"
  wikitext += "[[Catégorie:Théologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueToponymie(page,cle):
  #Catégorie:Lexique en italien de la toponymie
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la géographie|toponymie]]\n"
  wikitext += "[[Catégorie:Toponymie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueTransport(page,cle):
  #Catégorie:Lexique en italien du transport
  beg=page.find(" en ")
  end=page.find(" du ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|transport]]\n"
  wikitext += "[[Catégorie:Transport|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueZoologie(page,cle):
  #Catégorie:Lexique en bukawa de la zoologie
  beg=page.find(" en ")
  end=page.find(" de la ")
  language=page[beg+4:end]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la biologie|zoologie]]\n"
  wikitext += "[[Catégorie:Zoologie|" + cle[language] + "]]"
  return wikitext

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

def createCategory(page,cle,code,country):  
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
  elif (page.find("Catégorie:Wiktionnaire:Étymologies manquantes en ") != -1):
     wikitext = createCategoryEtymologiesManquantes(page,cle)
  elif (page.find("Catégorie:Wiktionnaire:Prononciations manquantes en ") != -1):
     wikitext = createCategoryPrononciationsManquantes(page,cle)
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
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’escrime") != -1)):
    wikitext = createCategoryLexiqueEscrime(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" du motocyclisme") != -1)):
    wikitext = createCategoryLexiqueMotocyclisme(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la charpenterie") != -1)):
    wikitext = createCategoryLexiqueCharpenterie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la philosophie") != -1)):
    wikitext = createCategoryLexiquePhilosophie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" des cris d’animaux") != -1)):
    wikitext = createCategoryLexiqueCrisAnimaux(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" du temps") != -1)):
    wikitext = createCategoryLexiqueTemps(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la généalogie") != -1)):
    wikitext = createCategoryLexiqueGenealogie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la préhistoire") != -1)):
    wikitext = createCategoryLexiquePrehistoire(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’alchimie") != -1)):
    wikitext = createCategoryLexiqueAlchimie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" du hockey") != -1) and
        (page.find(" sur glace") == -1)):
    wikitext = createCategoryLexiqueHockey(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" du patinage") != -1)):
    wikitext = createCategoryLexiquePatinage(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la zoologie") != -1)):
    wikitext = createCategoryLexiqueZoologie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la toponymie") != -1)):
    wikitext = createCategoryLexiqueToponymie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" du basket-ball") != -1)):
    wikitext = createCategoryLexiqueBasketBall(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la monarchie") != -1)):
    wikitext = createCategoryLexiqueMonarchie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la navigation") != -1)):
    wikitext = createCategoryLexiqueNavigation(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la pelote basque") != -1)):
    wikitext = createCategoryLexiquePeloteBasque(page,cle,code)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la phytosociologie") != -1)):
    wikitext = createCategoryLexiquePhytosociologie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’œnologie") != -1)):
    wikitext = createCategoryLexiqueOenologie(page,cle,code)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’ornithologie") != -1)):
    wikitext = createCategoryLexiqueOrnithologie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la physiologie") != -1)):
    wikitext = createCategoryLexiquePhysiologie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’aviation") != -1)):
    wikitext = createCategoryLexiqueAviation(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" des médias") != -1)):
    wikitext = createCategoryLexiqueMedias(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" des réseaux informatiques") != -1)):
    wikitext = createCategoryLexiqueReseauxInformatiques(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la métrologie") != -1)):
    wikitext = createCategoryLexiqueMetrologie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’argent") != -1)):
    wikitext = createCategoryLexiqueArgent(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’économie") != -1)):
    wikitext = createCategoryLexiqueEconomie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la papeterie") != -1)):
    wikitext = createCategoryLexiquePapeterie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" du transport") != -1)):
    wikitext = createCategoryLexiqueTransport(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la dermatologie") != -1)):
    wikitext = createCategoryLexiqueDermatologie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la phonologie") != -1)):
    wikitext = createCategoryLexiquePhonologie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’ichtyologie") != -1)):
    wikitext = createCategoryLexiqueIchtyologie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" du canoë-kayak") != -1)):
    wikitext = createCategoryLexiqueCanoeKayak(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la science-fiction") != -1)):
    wikitext = createCategoryLexiqueScienceFiction(page,cle,code)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’écologie") != -1)):
    wikitext = createCategoryLexiqueEcologie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" du textile") != -1)):
    wikitext = createCategoryLexiqueTextile(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la mycologie") != -1)):
    wikitext = createCategoryLexiqueMycologie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’hippologie") != -1)):
    wikitext = createCategoryLexiqueHippologie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" des bases de données") != -1)):
    wikitext = createCategoryLexiqueBasesDonnees(page,cle,code)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la serrurerie") != -1)):
    wikitext = createCategoryLexiqueSerrurerie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’Antiquité") != -1)):
    wikitext = createCategoryLexiqueAntiquite(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’anthropologie") != -1)):
    wikitext = createCategoryLexiqueAnthropologie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la cordonnerie") != -1)):
    wikitext = createCategoryLexiqueCordonnerie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’histoire") != -1)):
    wikitext = createCategoryLexiqueHistoire(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la météorologie") != -1)):
    wikitext = createCategoryLexiqueMeteorologie(page,cle,code)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la famille") != -1)):
    wikitext = createCategoryLexiqueFamille(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" du livre") != -1)):
    wikitext = createCategoryLexiqueLivre(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la biologie") != -1)):
    wikitext = createCategoryLexiqueBiologie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" des jeux") != -1) and
        (page.find(" vidéo") == -1)):
    wikitext = createCategoryLexiqueJeux(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la géologie") != -1)):
    wikitext = createCategoryLexiqueGeologie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la métallurgie") != -1)):
    wikitext = createCategoryLexiqueMetallurgie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" du chemin de fer") != -1)):
    wikitext = createCategoryLexiqueCheminFer(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" du commerce") != -1)):
    wikitext = createCategoryLexiqueCommerce(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la gravure") != -1)):
    wikitext = createCategoryLexiqueGravure(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la théologie") != -1)):
    wikitext = createCategoryLexiqueTheologie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’acoustique") != -1)):
    wikitext = createCategoryLexiqueAcoustique(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la fauconnerie") != -1)):
    wikitext = createCategoryLexiqueFauconnerie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la plomberie") != -1)):
    wikitext = createCategoryLexiquePlomberie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’imprimerie") != -1)):
    wikitext = createCategoryLexiqueImprimerie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la noblesse") != -1)):
    wikitext = createCategoryLexiqueNoblesse(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" du golf") != -1)):
    wikitext = createCategoryLexiqueGolf(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la physique") != -1)):
    wikitext = createCategoryLexiquePhysique(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la céramique") != -1)):
    wikitext = createCategoryLexiqueCeramique(page,cle,code)
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
  codeLangue = {}
  with open("liste_langue.dat") as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
      name, code, key = row
      cledetri[name] = key
      codeLangue[name] = code

  return cledetri, codeLangue

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
  cle, codeLangue = getSortingKey()
  countryList = getCountryList()

  if test:
    createCategory("[[:Catégorie:Thématiques en nahuatl de l’Isthme de Mecayapan]]",cle, codeLangue, countryList)
  #UserContributionsGenerator
  else:
    for page in WantedPagesCategoryGenerator(5000):
      createCategory(page,cle,codeLangue,countryList)
  

if __name__ == '__main__':

  try:

    main()
    
  finally:

    pywikibot.stopme()
