#! /usr/bin/python3

# -*- coding: utf-8 -*-

import csv
import pywikibot

import CleDeTri

test = False # to test the script (without saving the result)

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

def createCategoryLexiqueAcoustique(page,cle):
  #Catégorie:Lexique en français de l’acoustique
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la musique|acoustique]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la physique|acoustique]]\n"
  wikitext += "[[Catégorie:Acoustique|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueAeronautique(page,cle):
  #Catégorie:Lexique en italien de l’aéronautique
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " du transport|aeronautique]]\n"
  wikitext += "[[Catégorie:Aéronautique|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueAgriculture(page,cle):
  #Catégorie:Lexique en italien de l’agriculture
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|agriculture]]\n"
  wikitext += "[[Catégorie:Agriculture|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueAlchimie(page,cle):
  #Catégorie:Lexique en français de l’alchimie
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "Cette catégorie recense les mots en " + language + " ayant trait à l’[[alchimie]].\n\n"
  wikitext += "[[Catégorie:Lexiques en " + language + "|alchimie]]\n"
  wikitext += "[[Catégorie:Alchimie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueAlpinisme(page,cle):
  #Catégorie:Lexique en italien de l’alpinisme
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " du sport|alpinisme]]\n"
  wikitext += "[[Catégorie:Alpinisme|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueAnatomie(page,cle):
  #Catégorie:Lexique en anglais de l’anatomie
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la biologie|anatomie]]\n"
  wikitext += "[[Catégorie:Anatomie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueAnthropologie(page,cle):
  #Catégorie:Lexique en anglais de l’anthropologie
  beg=page.find(" en ")
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|anthropologie]]\n"
  wikitext += "[[Catégorie:Anthropologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueAntiquite(page,cle):
  #Catégorie:Lexique en anglais de l’Antiquité
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de l’histoire|antiquite]]\n"
  wikitext += "[[Catégorie:Antiquité|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueApiculture(page,cle):
  #Catégorie:Lexique en italien de l’apiculture
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de l’entomologie|apiculture]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de l’élevage|apiculture]]\n"
  wikitext += "[[Catégorie:Apiculture|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueArcheologie(page,cle):
  #Catégorie:Lexique en italien de l’archéologie
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|archeologie]]\n"
  wikitext += "[[Catégorie:Archéologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueArgent(page,cle):
  #Catégorie:Lexique en italien de l’argent
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|argent]]\n"
  wikitext += "[[Catégorie:Argent|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueArt(page,cle):
  #Catégorie:Lexique en italien de l’art
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|art]]\n"
  wikitext += "[[Catégorie:Art|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueArtsMartiaux(page,cle):
  #Catégorie:Lexique en français des arts martiaux
  language = guessLanguage(page,"en","des",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " des sports de combats|arts martiaux]]\n"
  wikitext += "[[Catégorie:Art martial|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueAstronautique(page,cle):
  #Catégorie:Lexique en italien de l’astronautique
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|astronautique]]\n"
  wikitext += "[[Catégorie:Astronautique|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueAstrophysique(page,cle):
  #Catégorie:Lexique en italien de l’astrophysique
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de l’astronomie|astrophysique]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la physique|astrophysique]]\n"
  wikitext += "[[Catégorie:Astrophysique|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueAthletisme(page,cle):
  #Catégorie:Lexique en italien de l’athlétisme
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " du sport|athletisme]]\n"
  wikitext += "[[Catégorie:Athlétisme|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueAudiovisuel(page,cle):
  #Catégorie:Lexique en italien de l’audiovisuel
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|audiovisuel]]\n"
  wikitext += "[[Catégorie:Audiovisuel|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueAutomobile(page,cle):
  #Catégorie:Lexique en italien de l’automobile
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|automobile]]\n"
  wikitext += "[[Catégorie:Automobile|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueAviation(page,cle):
  #Catégorie:Lexique en italien de l’aviation
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|aviation]]\n"
  wikitext += "[[Catégorie:Aviation|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueBandeDessinee(page,cle):
  #Catégorie:Lexique en italien de la bande dessinée
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la littérature|bande dessinee]]\n"
  wikitext += "[[Catégorie:Bande dessinée|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueBaseball(page,cle):
  #Catégorie:Lexique en italien du baseball
  language = guessLanguage(page,"en","du",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " du sport|baseball]]\n"
  wikitext += "[[Catégorie:Baseball|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueBasesDonnees(page,cle,code):
  #Catégorie:Lexique en anglais des bases de données
  language = guessLanguage(page,"en","des",cle)
  if not language:
    return
  if (language not in code):
    return

  wikitext = "Le vocabulaire peut être ajouté à cette catégorie avec le modèle {{modl|base de données|" + code[language] + "}}.\n\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de l’informatique|base de donnees]]\n"
  wikitext += "[[Catégorie:Bases de données|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueBasketBall(page,cle):
  #Catégorie:Lexique en italien du basket-ball
  language = guessLanguage(page,"en","du",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " du sport|basket ball]]\n"
  wikitext += "[[Catégorie:Basket-ball|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueBiochimie(page,cle):
  #Catégorie:Lexique en italien de la biochimie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la biologie|biochimie]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la chimie|biochimie]]\n"
  wikitext += "[[Catégorie:Biochimie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueBiologie(page,cle):
  #Catégorie:Lexique en italien de la biologie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|biologie]]\n"
  wikitext += "[[Catégorie:Biologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueBotanique(page,cle):
  #Catégorie:Lexique en italien de la botanique
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "Cette catégorie recense les mots en " + language + " ayant trait à la [[botanique]].\n\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la biologie|botanique]]\n"
  wikitext += "[[Catégorie:Botanique|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueBoxe(page,cle):
  #Catégorie:Lexique en italien de la boxe
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " des sports de combat|boxe]]\n"
  wikitext += "[[Catégorie:Boxe|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueCanoeKayak(page,cle):
  #Catégorie:Lexique en français du canoë-kayak
  language = guessLanguage(page,"en","du",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " du sport|canoe kayak]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la navigation|canoe kayak]]\n"
  wikitext += "[[Catégorie:Canoë-kayak|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueCartesAJouer(page,cle):
  #Catégorie:Lexique en français des cartes à jouer
  language = guessLanguage(page,"en","des",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " des jeux|cartes a jouer]]\n"
  wikitext += "[[Catégorie:Cartes à jouer|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueCartophilie(page,cle):
  #Catégorie:Lexique en français de la cartophilie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|cartophilie]]\n"
  wikitext += "[[Catégorie:Cartophilie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueCeramique(page,cle,code):
  #Catégorie:Lexique en italien de la céramique
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "Vocabulaire concernant la [[céramique]] (art de la terre cuite).\n\n"
  wikitext += "{{modl|céramique|" + code[language] + "}} catégorise ici.\n\n"

  wikitext = "[[Catégorie:Lexiques en " + language + "|ceramique]]\n"
  wikitext += "[[Catégorie:Céramique|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueCharpenterie(page,cle):
  #Catégorie:Lexique en italien de la charpenterie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la construction|charpenterie]]\n"
  wikitext += "[[Catégorie:Charpenterie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueChasse(page,cle):
  #Catégorie:Lexique en italien de la chasse
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|chasse]]\n"
  wikitext += "[[Catégorie:Chasse|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueCheminFer(page,cle):
  #Catégorie:Lexique en italien du chemin de fer
  language = guessLanguage(page,"en","du",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " du transport|chemin de fer]]\n"
  wikitext += "[[Catégorie:Chemin de fer|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueChirurgie(page,cle):
  #Catégorie:Lexique en italien de la chirurgie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la médecine|chirurgie]]\n"
  wikitext += "[[Catégorie:Chirurgie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueChristianisme(page,cle):
  #Catégorie:Lexique en italien du christianisme
  language = guessLanguage(page,"en","du",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la religion|christianisme]]\n"
  wikitext += "[[Catégorie:Christianisme|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueClimatologie(page,cle):
  #Catégorie:Lexique en français de la climatologie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|climatologie]]\n"
  wikitext += "[[Catégorie:Climatologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueColorimetrie(page,cle):
  #Catégorie:Lexique en italien de la colorimétrie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " des sciences|colorimetrie]]\n"
  wikitext = "[[Catégorie:Lexique en " + language + " de la photographie|colorimetrie]]\n"
  wikitext += "[[Catégorie:Colorimétrie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueCommerce(page,cle):
  #Catégorie:Lexique en italien du commerce
  language = guessLanguage(page,"en","du",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|commerce]]\n"
  wikitext += "[[Catégorie:Commerce|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueConstruction(page,cle):
  #Catégorie:Lexique en français de la construction
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de l’architecture|construction]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de l’urbanisme|construction]]\n"
  wikitext += "[[Catégorie:Construction|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueCordonnerie(page,cle):
  #Catégorie:Lexique en français de la cordonnerie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|cordonnerie]]\n"
  wikitext += "[[Catégorie:Cordonnerie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueCrisAnimaux(page,cle):
  #Catégorie:Lexique en anglais des cris d’animaux
  language = guessLanguage(page,"en","des",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la zoologie|Cris danimaux]]\n"
  wikitext += "[[Catégorie:Cris d’animaux|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueCuisine(page,cle):
  #Catégorie:Lexique en italien de la cuisine
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|cuisine]]\n"
  wikitext += "[[Catégorie:Vie domestique en " + language + "|cuisine]]"
  wikitext += "[[Catégorie:Cuisine|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueCyclisme(page,cle):
  #Catégorie:Lexique en italien du cyclisme
  language = guessLanguage(page,"en","du",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " du sport|cyclisme]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " du transport|cyclisme]]\n"
  wikitext += "[[Catégorie:Cyclisme|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueDermatologie(page,cle):
  #Catégorie:Lexique en français de la dermatologie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return

  wikitext = "[[Catégorie:Lexique en " + language + " de la médecine|dermatologie]]\n"
  wikitext += "[[Catégorie:Dermatologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueEchecs(page,cle):
  #Catégorie:Lexique en italien des échecs
  language = guessLanguage(page,"en","des",cle)
  if not language:
    return

  wikitext = "[[Catégorie:Lexique en " + language + " des jeux|echecs]]\n"
  wikitext += "[[Catégorie:Échecs|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueEcologie(page,cle):
  #Catégorie:Lexique en italien de l’écologie
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return

  wikitext = "[[Catégorie:Lexiques en " + language + "|ecologie]]\n"
  wikitext += "[[Catégorie:Écologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueEconomie(page,cle):
  #Catégorie:Lexique en italien de l’économie
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return

  wikitext = "[[Catégorie:Lexiques en " + language + "|economie]]\n"
  wikitext += "[[Catégorie:Économie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueEdition(page,cle):
  #Catégorie:Lexique en italien de l’édition
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return

  wikitext = "[[Catégorie:Lexique en " + language + " de la littérature|edition]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " des médias|edition]]\n"
  wikitext += "[[Catégorie:Édition|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueElectronique(page,cle):
  #Catégorie:Lexique en français de l’électronique
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return

  wikitext = "[[Catégorie:Lexique en " + language + "|electronique]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la physique|electronique]]\n"
  wikitext += "[[Catégorie:Électronique|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueElevage(page,cle):
  #Catégorie:Lexique en italien de l’élevage
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return

  wikitext = "[[Catégorie:Lexiques en " + language + "|elevage]]\n"
  wikitext += "[[Catégorie:Élevage|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueEmbryologie(page,cle):
  #Catégorie:Lexique en italien de l’embryologie
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return

  wikitext = "[[Catégorie:Lexique en " + language + " de la biologie|embryologie]]\n"
  wikitext += "[[Catégorie:Embryologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueEntomologie(page,cle):
  #Catégorie:Lexique en italien de l’entomologie
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return

  wikitext = "[[Catégorie:Lexique en " + language + " de la zoologie|entomologie]]\n"
  wikitext += "[[Catégorie:Entomologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueEquitation(page,cle):
  #Catégorie:Lexique en italien de l’équitation
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return

  wikitext = "[[Catégorie:Lexique en " + language + " du sport|equitation]]\n"
  wikitext += "[[Catégorie:Équitation|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueEscrime(page,cle):
  #Catégorie:Lexique en italien de l’escrime
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return

  wikitext = "[[Catégorie:Lexique en " + language + " des sports de combat|escrime]]\n"
  wikitext += "[[Catégorie:Escrime|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueEthnologie(page,cle):
  #Catégorie:Lexique en italien de l’ethnologie
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return

  wikitext = "[[Catégorie:Lexique en " + language + " de l’anthropologie|ethnologie]]\n"
  wikitext += "[[Catégorie:Ethnologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueFamille(page,cle):
  #Catégorie:Lexique en italien de la famille
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|famille]]\n"
  wikitext += "[[Catégorie:Famille|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueFauconnerie(page,cle):
  #Catégorie:Lexique en italien de la fauconnerie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return

  wikitext = "[[Catégorie:Lexique en " + language + " de l’élevage|fauconnerie]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la chasse|fauconnerie]]\n"
  wikitext += "[[Catégorie:Fauconnerie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueFiscalite(page,cle):
  #Catégorie:Lexique en italien de la fiscalité
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de l’économie|fiscalite]]\n"
  wikitext += "[[Catégorie:Fiscalité|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueGenealogie(page,cle):
  #Catégorie:Lexique en français de la généalogie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "Cette catégorie recense les mots en [[" + language + "]] ayant trait à la [[généalogie]].\n\n"
  wikitext += "[[Catégorie:Lexiques en " + language + "|genealogie]]\n"
  wikitext += "[[Catégorie:Généalogie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueGrammaire(page,cle):
  #Catégorie:Lexique en italien de la grammaire
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|grammaire]]\n"
  wikitext += "[[Catégorie:Grammaire|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueGravure(page,cle):
  #Catégorie:Lexique en français de la gravure
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " du livre|gravure]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de l’art|gravure]]\n"
  wikitext += "[[Catégorie:Gravure|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueGeographie(page,cle):
  #Catégorie:Lexique en italien de la géographie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|geographie]]\n"
  wikitext += "[[Catégorie:Géographie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueGeologie(page,cle):
  #Catégorie:Lexique en italien de la géologie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|geologie]]\n"
  wikitext += "[[Catégorie:Géologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueGeometrie(page,cle):
  #Catégorie:Lexique en kazakh de la géométrie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " des mathémtiques|geometrie]]\n"
  wikitext += "[[Catégorie:Géométrie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueGeophysique(page,cle):
  #Catégorie:Lexique en italien de la géophysique
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la géologie|geophysique]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la physique|geophysique]]\n"
  wikitext += "[[Catégorie:Géophysique|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueGolf(page,cle):
  #Catégorie:Lexique en italien du golf
  language = guessLanguage(page,"en","du",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " du sport|golf]]\n"
  wikitext += "[[Catégorie:Golf|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueHindouisme(page,cle):
  #Catégorie:Lexique en anglais de l’hindouisme
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la religion|hindouisme]]\n"
  wikitext += "[[Catégorie:Hindouisme|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueHippologie(page,cle):
  #Catégorie:Lexique en anglais de l’hippologie
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la zoologie|hippologie]]\n"
  wikitext += "[[Catégorie:Hippologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueHistoire(page,cle):
  #Catégorie:Lexique en anglais de l’histoire
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|histoire]]\n"
  wikitext += "[[Catégorie:Histoire|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueHockey(page,cle):
  #Catégorie:Lexique en italien du hockey
  language = guessLanguage(page,"en","du",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " des sports de glisse|hockey]]\n"
  wikitext += "[[Catégorie:Hockey|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueHorlogerie(page,cle):
  #Catégorie:Lexique en français de l’horlogerie
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|horlogerie]]\n"
  wikitext += "[[Catégorie:Horlogerie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueHorticulture(page,cle):
  #Catégorie:Lexique en français de l’horticulture
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de l’agriculture|horticulture]]\n"
  wikitext += "[[Catégorie:Horticulture|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueHydrologie(page,cle):
  #Catégorie:Lexique en italien de l’hydrologie
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|hydrologie]]\n"
  wikitext += "[[Catégorie:Hydrologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueIchtyologie(page,cle):
  #Catégorie:Lexique en anglais de l’ichtyologie
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la zoologie|ichtyologie]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de l’élevage|ichtyologie]]\n"
  wikitext += "[[Catégorie:Ichtyologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueImprimerie(page,cle):
  #Catégorie:Lexique en italien de l’imprimerie
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|imprimerie]]\n"
  wikitext += "[[Catégorie:Imprimerie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueInformatique(page,cle):
  #Catégorie:Lexique en italien de l’informatique
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|informatique]]\n"
  wikitext += "[[Catégorie:Informatique|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueInternet(page,cle):
  #Catégorie:Lexique en italien de l’Internet
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de l’informatique|internet]]\n"
  wikitext += "[[Catégorie:Internet|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueIslam(page,cle):
  #Catégorie:Lexique en italien de l’islam
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la religion|islam]]\n"
  wikitext += "[[Catégorie:Islam|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueJardinage(page,cle):
  #Catégorie:Lexique en italien du jardinage
  language = guessLanguage(page,"en","du",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " des loisirs|jardinage]]\n"
  wikitext += "[[Catégorie:Jardinage|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueJeux(page,cle):
  #Catégorie:Lexique en italien des jeux
  language = guessLanguage(page,"en","des",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " des loisirs|jeux]]\n"
  wikitext += "[[Catégorie:Jeux|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueJeuxVideo(page,cle):
  #Catégorie:Lexique en italien des jeux vidéo
  language = guessLanguage(page,"en","des",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " des jeux|video]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de l’informatique|video]]\n"
  wikitext += "[[Catégorie:Jeux video|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueJudo(page,cle):
  #Catégorie:Lexique en italien du judo
  language = guessLanguage(page,"en","du",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " des arts martiaux|judo]]\n"
  wikitext += "[[Catégorie:Judo|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueJustice(page,cle):
  #Catégorie:Lexique en français de la justice
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " du droit|justice]]\n"
  wikitext += "[[Catégorie:Justice|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueLegislation(page,cle):
  #Catégorie:Lexique en français de la législation
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " du droit|legislation]]\n"
  wikitext += "[[Catégorie:Législation|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueLinguistique(page,cle):
  #Catégorie:Lexique en italien de la linguistique
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|linguistique]]\n"
  wikitext += "[[Catégorie:Linguistique|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueLitterature(page,cle):
  #Catégorie:Lexique en italien de la littérature
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de l’art|litterature]]\n"
  wikitext += "[[Catégorie:Littérature|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueLivre(page,cle):
  #Catégorie:Lexique en italien du livre
  language = guessLanguage(page,"en","du",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de l’édition|livre]]\n"
  wikitext += "[[Catégorie:Livre|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueLogique(page,cle):
  #Catégorie:Lexique en italien de la logique
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " des mathématiques|logique]]\n"
  wikitext += "[[Catégorie:Logique|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueLoisirs(page,cle):
  #Catégorie:Lexique en italien des loisirs
  language = guessLanguage(page,"en","des",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|loisirs]]\n"
  wikitext += "[[Catégorie:Loisirs|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueLutherie(page,cle):
  #Catégorie:Lexique en italien de la lutherie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "Catégorie regroupant les termes concernant la [[lutherie]] en " + language +".\n\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la musique|lutherie]]\n"
  wikitext += "[[Catégorie:Lutherie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueMarine(page,cle):
  #Catégorie:Lexique en italien de la marine
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|marine]]\n"
  wikitext += "[[Catégorie:Marine|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueMathematiques(page,cle):
  #Catégorie:Lexique en italien des mathématiques
  language = guessLanguage(page,"en","des",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|mathematiques]]\n"
  wikitext += "[[Catégorie:Mathématiques|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueMecanique(page,cle):
  #Catégorie:Lexique en italien de la mécanique
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|mecanique]]\n"
  wikitext += "[[Catégorie:Mécanique|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueMedecine(page,cle):
  #Catégorie:Lexique en italien de la médecine
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|medecine]]\n"
  wikitext += "[[Catégorie:Médecine|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueMedias(page,cle):
  #Catégorie:Lexique en italien des médias
  language = guessLanguage(page,"en","des",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|medias]]\n"
  wikitext += "[[Catégorie:Médias|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueMetallurgie(page,cle):
  #Catégorie:Lexique en italien de la métallurgie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|metallurgie]]\n"
  wikitext += "[[Catégorie:Métallurgie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueMercatique(page,cle):
  #Catégorie:Lexique en anglais de la mercatique
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|mercatique]]\n"
  wikitext += "[[Catégorie:Mercatique|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueMeteorologie(page,cle,code):
  #Catégorie:Lexique en italien de la météorologie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
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
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|metrologie]]\n"
  wikitext += "[[Catégorie:Métrologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueMicrobiologie(page,cle):
  #Catégorie:Lexique en italien de la microbiologie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return

  wikitext = "Cette catégorie réunit les mots qui ont trait à la [[microbiologie]] en usage en [[" + language + "]].\n\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la biologie|microbiologie]]\n"
  wikitext += "[[Catégorie:microbiologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueMilitaire(page,cle):
  #Catégorie:Lexique en italien du militaire
  language = guessLanguage(page,"en","du",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|militaire]]\n"
  wikitext += "[[Catégorie:Militaire|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueMineralogie(page,cle):
  #Catégorie:Lexique en italien de la minéralogie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|mineralogie]]\n"
  wikitext += "[[Catégorie:Minéralogie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueMonarchie(page,cle):
  #Catégorie:Lexique en anglais de la monarchie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la politique|monarchie]]\n"
  wikitext += "[[Catégorie:Monarchie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueMotocyclisme(page,cle):
  #Catégorie:Lexique en italien du motocyclisme
  language = guessLanguage(page,"en","du",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|motocyclisme]]\n"
  wikitext += "[[Catégorie:Motocyclisme|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueMusique(page,cle):
  #Catégorie:Lexique en italien de la musique
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + "de l’art|musique]]\n"
  wikitext += "[[Catégorie:Musique|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueMycologie(page,cle):
  #Catégorie:Lexique en italien de la mycologie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la biologie|mycologie]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la cuisine|mycologie]]\n"
  wikitext += "[[Catégorie:Mycologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueMythologie(page,cle):
  #Catégorie:Lexique en italien de la mythologie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|mythologie]]\n"
  wikitext += "[[Catégorie:Mythologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueNavigation(page,cle):
  #Catégorie:Lexique en italien de la navigation
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "Cette page liste les mots en " + language + " en rapport avec la [[navigation]].\n\n"
  wikitext += "[[Catégorie:Lexique en " + language + " du transport|navigation]]\n"
  wikitext += "[[Catégorie:Navigation|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueNeurologie(page,cle):
  #Catégorie:Lexique en italien de la neurologie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la médecine|neurologie]]\n"
  wikitext += "[[Catégorie:Neurologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueNoblesse(page,cle):
  #Catégorie:Lexique en italien de la noblesse
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la monarchie|noblesse]]\n"
  wikitext += "[[Catégorie:Noblesse|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueNosologie(page,cle,code):
  #Catégorie:Lexique en italien de la nosologie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  if (language not in code):
    return
  
  wikitext = "* Pour ajouter des termes dans cette catégorie, merci d’utiliser le modèle {{modl|nosologie|" + code[language] + "}} dans les articles à catégoriser.\n\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la médecine|nosologie]]\n"
  wikitext += "[[Catégorie:Nosologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueNutrition(page,cle):
  #Catégorie:Lexique en italien de la nutrition
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la cuisine|nutrition]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la physiologie|nutrition]]\n"
  wikitext += "[[Catégorie:Nutrition|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueOenologie(page,cle,code):
  #Catégorie:Lexique en italien de l’œnologie
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  if (language not in code):
    return
  
  wikitext = "Pour alimenter cette page, merci d’ajouter aux articles le modèle {{modl|oenologie|" + code[language] + "}}.\n"
  wikitext += "[[Catégorie:Lexiques en " + language + "|oenologie]]\n"
  wikitext += "[[Catégorie:Œnologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueOrnithologie(page,cle):
  #Catégorie:Lexique en italien de l’ornithologie
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la zoologie|ornithologie]]\n"
  wikitext += "[[Catégorie:Ornithologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiquePapeterie(page,cle):
  #Catégorie:Lexique en italien de la papeterie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " du livre|papeterie]]\n"
  wikitext += "[[Catégorie:Papeterie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiquePatinage(page,cle):
  #Catégorie:Lexique en français du patinage
  language = guessLanguage(page,"en","du",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " des sports d’hiver|patinage]]\n"
  wikitext += "[[Catégorie:Patinage|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiquePatisserie(page,cle):
  #Catégorie:Lexique en italien de la pâtisserie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la cuisine|patisserie]]\n"
  wikitext += "[[Catégorie:Pâtisserie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiquePeche(page,cle):
  #Catégorie:Lexique en italien de la pêche
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|peche]]\n"
  wikitext += "[[Catégorie:Pêche|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiquePedologie(page,cle):
  #Catégorie:Lexique en anglais de la pédologie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|pedologie]]\n"
  wikitext += "[[Catégorie:Pédologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiquePeloteBasque(page,cle,code):
  #Catégorie:Lexique en français de la pelote basque
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  if (language not in code):
    return
  
  wikitext = "Pour référencer automatiquement un mot dans cette catégorie, il est possible d’ajouter dans la définition le modèle : {{modl|pelote|" + code[language] + "}}.\n\n"
  wikitext += "[[Catégorie:Lexique en " + language + " du sport|pelote basque]]\n"
  wikitext += "[[Catégorie:Pelote basque|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiquePhilosophie(page,cle):
  #Catégorie:Lexique en italien de la philosophie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|philosophie]]\n"
  wikitext += "[[Catégorie:Philosophie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiquePhonologie(page,cle):
  #Catégorie:Lexique en anglais de la phonologie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la linguistique|phonologie]]\n"
  wikitext += "[[Catégorie:Phonologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiquePhotographie(page,cle):
  #Catégorie:Lexique en anglais de la photographie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de l’art|photographie]]\n"
  wikitext += "[[Catégorie:Photographie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiquePlomberie(page,cle):
  #Catégorie:Lexique en italien de la plomberie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la construction|plomberie]]\n"
  wikitext += "[[Catégorie:Plomberie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiquePhilatelie(page,cle):
  #Catégorie:Lexique en italien de la philatélie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|philatelie]]\n"
  wikitext += "[[Catégorie:Philatélie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiquePhysique(page,cle):
  #Catégorie:Lexique en italien de la physique
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|physique]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " des sciences|physique]]\n"
  wikitext += "[[Catégorie:Physique|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiquePhytosociologie(page,cle):
  #Catégorie:Lexique en français de la phytosociologie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|phytosociologie]]\n"
  wikitext += "[[Catégorie:Phytosociologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiquePhysiologie(page,cle):
  #Catégorie:Lexique en italien de la physiologie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|physiologie]]\n"
  wikitext += "[[Catégorie:Physiologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiquePrehistoire(page,cle):
  #Catégorie:Lexique en same du Nord de la préhistoire
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de l’histoire|prehistoire]]\n"
  wikitext += "[[Catégorie:Lexiques en " + language + "|prehistoire]]\n"
  wikitext += "[[Catégorie:Préhistoire|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiquePhysiologie(page,cle):
  #Catégorie:Lexique en italien de la physiologie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|physiologie]]\n"
  wikitext += "[[Catégorie:Physiologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiquePolitique(page,cle):
  #Catégorie:Lexique en italien de la politique
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|politique]]\n"
  wikitext += "[[Catégorie:Politique|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueReproduction(page,cle):
  #Catégorie:Lexique en italien de la reproduction
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la biologie|reproduction]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la sexualité|reproduction]]\n"
  wikitext += "[[Catégorie:Reproduction|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueReseauxInformatiques(page,cle):
  #Catégorie:Lexique en italien des réseaux informatiques
  language = guessLanguage(page,"en","des",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de l’informatique|reseau]]\n"
  wikitext += "[[Catégorie:Réseaux informatiques|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueRhetorique(page,cle):
  #Catégorie:Lexique en italien de la rhétorique
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de l’art|rhetorique]]\n"
  wikitext += "[[Catégorie:Rhétorique|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueRobotique(page,cle):
  #Catégorie:Lexique en italien de la robotique
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|robotique]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la technique|robotique]]\n"
  wikitext += "[[Catégorie:Robotique|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueSciences(page,cle):
  #Catégorie:Lexique en italien des sciences
  language = guessLanguage(page,"en","des",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|sciences]]\n"
  wikitext += "[[Catégorie:Sciences|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueSerrurerie(page,cle):
  #Catégorie:Lexique en anglais de la serrurerie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|serrurerie]]\n"
  wikitext += "[[Catégorie:Serrurerie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueSexualite(page,cle):
  #Catégorie:Lexique en anglais de la sexualité
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|sexualite]]\n"
  wikitext += "[[Catégorie:Sexualité|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueScienceFiction(page,cle,code):
  #Catégorie:Lexique en italien de la science-fiction
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  if (language not in code):
    return
  
  wikitext = "Les termes peuvent être ajoutés à cette liste avec {{modl|sci-fi|" + code[language] + "}}.\n\n"
  wikitext += "=== Voir aussi ===\n"
  wikitext += "* [[:Catégorie:Lexique en " + language + " du fantastique]]\n\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la littérature|science fiction]]\n"
  wikitext += "[[Catégorie:Science-fiction|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueSentiments(page,cle):
  #Catégorie:Lexique en français des sentiments
  language = guessLanguage(page,"en","des",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|sentiments]]\n"
  wikitext += "[[Catégorie:Sentiments|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueSociologie(page,cle):
  #Catégorie:Lexique en français de la sociologie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|sociologie]]\n"
  wikitext += "[[Catégorie:Sociologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueSport(page,cle):
  #Catégorie:Lexique en italien du sport
  language = guessLanguage(page,"en","du",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|sport]]\n"
  wikitext += "[[Catégorie:Sport|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueSquelette(page,cle):
  #Catégorie:Lexique en italien du squelette
  language = guessLanguage(page,"en","du",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de l’anatomie|squelette]]\n"
  wikitext += "[[Catégorie:Squelette|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueStatistiques(page,cle):
  #Catégorie:Lexique en italien des statistiques
  language = guessLanguage(page,"en","des",cle)
  if not language:
    return
  
  wikitext = "Cette catégorie recense les mots en " + language + " utilisés en [[statistiques]].\n\n"
  wikitext += "[[Catégorie:Lexiques en " + language + "|statistiques]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " des mathématiques|statistiques]]\n"
  wikitext += "[[Catégorie:Statistiques|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueSylviculture(page,cle):
  #Catégorie:Lexique en français de la sylviculture
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la foresterie|sylviculture]]\n"
  wikitext += "[[Catégorie:Sylviculture|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueSyntaxe(page,cle,code):
  #Catégorie:Lexique en français de la syntaxe
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  if (language not in code):
    return
  
  wikitext = "Cette catégorie recense le vocabulaire lié à la [[syntaxe]] en " + language + " ; le mot peut être listé ici avec le modèle {{modl|syntaxe|" + code[language] + "}}.\n\n"
  wikitext += "[[Catégorie:Lexiques en " + language + "|syntaxe]]\n"
  wikitext += "[[Catégorie:Syntaxe|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueSystemesElectoraux(page,cle):
  #Catégorie:Lexique en français des systèmes électoraux
  language = guessLanguage(page,"en","des",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la politique|systeme electoraux]]\n"
  wikitext += "[[Catégorie:Systèmes électoraux|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueTechnique(page,cle):
  #Catégorie:Lexique en italien de la technique
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|technique]]\n"
  wikitext += "[[Catégorie:Technique|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueTechnologie(page,cle):
  #Catégorie:Lexique en italien de la technologie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|technologie]]\n"
  wikitext += "[[Catégorie:Technologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueTelecommunications(page,cle):
  #Catégorie:Lexique en italien des télécommunications
  language = guessLanguage(page,"en","des",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|telecommunications]]\n"
  wikitext += "[[Catégorie:Télécommunications|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueTelephonie(page,cle):
  #Catégorie:Lexique en italien de la téléphonie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " des télécommunications|telephonie]]\n"
  wikitext += "[[Catégorie:Téléphonie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueTemps(page,cle):
  #Catégorie:Lexique en same du Nord du temps
  language = guessLanguage(page,"en","du",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|temps]]\n"
  wikitext += "[[Catégorie:Temps|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueTennis(page,cle):
  #Catégorie:Lexique en italien du tennis
  language = guessLanguage(page,"en","du",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " du sport|tennis]]\n"
  wikitext += "[[Catégorie:Tennis|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueTextile(page,cle):
  #Catégorie:Lexique en italien du textile
  language = guessLanguage(page,"en","du",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|textile]]\n"
  wikitext += "[[Catégorie:Textile|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueTheologie(page,cle):
  #Catégorie:Lexique en italien de la théologie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|theologie]]\n"
  wikitext += "[[Catégorie:Théologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueToponymie(page,cle):
  #Catégorie:Lexique en italien de la toponymie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la géographie|toponymie]]\n"
  wikitext += "[[Catégorie:Toponymie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueTransport(page,cle):
  #Catégorie:Lexique en italien du transport
  language = guessLanguage(page,"en","du",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|transport]]\n"
  wikitext += "[[Catégorie:Transport|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueTravail(page,cle):
  #Catégorie:Lexique en italien du travail
  language = guessLanguage(page,"en","du",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|travail]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de l’argent|travail]]\n"
  wikitext += "[[Catégorie:Travail|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueUrbanisme(page,cle):
  #Catégorie:Lexique en italien de l’urbanisme
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|urbanisme]]\n"
  wikitext += "[[Catégorie:Urbanisme|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueWikis(page,cle,code):
  #Catégorie:Lexique en italien des wikis
  language = guessLanguage(page,"en","des",cle)
  if not language:
    return
  if (language not in code):
    return

  wikitext = "Cette catégorie liste les termes du [[jargon]] des [[wiki]]s en " + language + ", c’est-à-dire ceux qui sont spécifiquement utilisés par les utilisateurs des wikis pour parler entre eux. Ils doivent être ajoutés avec {{modl|wiki|" + code[language] +"}}.\n\n"

  wikitext += "[[Catégorie:Lexique en " + language + " de l’Internet|wiki]]\n"
  wikitext += "[[Catégorie:Wiki|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueZoologie(page,cle):
  #Catégorie:Lexique en bukawa de la zoologie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de la biologie|zoologie]]\n"
  wikitext += "[[Catégorie:Zoologie|" + cle[language] + "]]"
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

def createCategoryArmes(page,cle):
  #Catégorie:Armes en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Armes|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|armes]]"
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

def createCategoryDesserts(page,cle):
  #Catégorie:Desserts en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:Desserts|" + cle[language] + "]]\n"
  wikitext = "[[Catégorie:Préparations culinaires en " + language + "|desserts]]"
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

def createCategoryLexiques(page,cle):
  #Catégorie:Lexiques en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext = "[[Catégorie:" + language + "]]\n"
  wikitext += "[[Catégorie:Lexiques par langue|" + cle[language] + "]]"
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
  if (country not in continentByCountryDict):
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

def createCategorySports(page,cle):
  #Catégorie:Sports en anglais
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext ="[[Catégorie:Sports|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|Saisons]]"
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

def createCategoryVetements(page,cle):
  #Catégorie:Vêtements en italien
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  wikitext ="[[Catégorie:Vêtements|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Thématiques en " + language + "|vetements]]\n"
  return wikitext

def createCategoryPaysEnLangue(page,cle,continent):
  #Catégorie:Kiribati en same du Nord
  beg=page.find(" en ")
  language=page[beg+4:]
  if (language not in cle):
    return
  
  end=beg
  beg=page.find(":")
  pays=page[beg+1:end]
  if (pays not in continent):
    return
  
  wikitext = "[[Catégorie:" + pays + "|" + cle[language] + "]]\n"
  wikitext += "[[Catégorie:Pays en " + language + "]]\n"
  wikitext += "[[Catégorie:" + continent[pays] + " en " + language + "|" + CleDeTri.CleDeTri(pays) + "]]"
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
  elif (page.find("Catégorie:Adjectifs en") != -1):
     wikitext = createCategoryAdjectifs(page,cle)
  elif (page.find("Catégorie:Adverbes en") != -1):
     wikitext = createCategoryAdverbes(page,cle)
  elif (page.find("Catégorie:Aliments en") != -1):
     wikitext = createCategoryAliments(page,cle)
  elif (page.find("Catégorie:Animaux en") != -1):
     wikitext = createCategoryAnimaux(page,cle)
  elif (page.find("Catégorie:Armes en") != -1):
     wikitext = createCategoryArmes(page,cle)
  elif (page.find("Catégorie:Bateaux en") != -1):
     wikitext = createCategoryBateaux(page,cle)
  elif (page.find("Catégorie:Boissons en") != -1):
     wikitext = createCategoryBoissons(page,cle)
  elif (page.find("Catégorie:Cardinaux en") != -1):
     wikitext = createCategoryCardinaux(page,cle)
  elif (page.find("Catégorie:Céréales en") != -1):
     wikitext = createCategoryCereales(page,cle)
  elif (page.find("Catégorie:Conjonctions en") != -1):
     wikitext = createCategoryConjonctions(page,cle)
  elif (page.find("Catégorie:Conjugaison en") != -1):
     wikitext = createCategoryConjugaison(page,cle)
  elif (page.find("Catégorie:Couleurs en") != -1):
     wikitext = createCategoryCouleurs(page,cle)
  elif (page.find("Catégorie:Curiosités linguistiques en") != -1):
     wikitext = createCategoryCuriositesLinguistiques(page,cle)
  elif (page.find("Catégorie:Expressions en") != -1):
     wikitext = createCategoryExpressions(page,cle)
  elif (page.find("Catégorie:Fruits en") != -1):
     wikitext = createCategoryFruits(page,cle)
  elif (page.find("Catégorie:Insectes en") != -1):
     wikitext = createCategoryInsectes(page,cle)
  elif (page.find("Catégorie:Instruments de musique en") != -1):
     wikitext = createCategoryInstrumentsDeMusique(page,cle)
  elif (page.find("Catégorie:Interrogatifs en") != -1):
     wikitext = createCategoryInterrogatifs(page,cle)
  elif (page.find("Catégorie:Langues en") != -1):
     wikitext = createCategoryLangues(page,cle)
  elif (page.find("Catégorie:Lexiques en") != -1):
     wikitext = createCategoryLexiques(page,cle)
  elif (page.find("Catégorie:Localités d") != -1 and
        (page.find(" en ") != -1)):
      wikitext = createCategoryLocalitesDeEn(page,cle,country)
  elif (page.find("Catégorie:Locutions en") != -1):
     wikitext = createCategoryLocutions(page,cle)
  elif (page.find("Catégorie:Mammifères en") != -1):
     wikitext = createCategoryMammiferes(page,cle)
  elif ((page.find("Catégorie:Mots en") != -1) and
        (page.find("issus d’un mot en") != -1)):
    wikitext = createCategoryMotsEnIssusDunMot(page,cle)
  elif (page.find("Catégorie:Mots issus d’un mot en ") != -1):
    wikitext = createCategoryMotsIssusDunMot(page,cle)
  elif (page.find("Catégorie:Nombres en ") != -1):
    wikitext = createCategoryNombres(page,cle)
  elif (page.find("Catégorie:Noms communs en") != -1):
     wikitext = createCategoryNomsCommuns(page,cle)
  elif (page.find("Catégorie:Noms propres en") != -1):
     wikitext = createCategoryNomsPropres(page,cle)
  elif ((page.find("Catégorie:Noms propres en") != -1) and
        (page.find("issus d’un mot en") != -1)):
    wikitext = createCategoryNomsPropresIssus(page,cle)
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
  elif (page.find("Catégorie:Palindromes en") != -1):
     wikitext = createCategoryPalindromes(page,cle)
  elif (page.find("Catégorie:Plantes en") != -1):
     wikitext = createCategoryPlantes(page,cle)
  elif (page.find("Catégorie:Poissons en") != -1):
     wikitext = createCategoryPoissons(page,cle)
  elif (page.find("Catégorie:Préparations culinaires en") != -1):
     wikitext = createCategoryPreparationsCulinaires(page,cle)
  elif (page.find("Catégorie:Sports en") != -1):
     wikitext = createCategorySports(page,cle)
  elif (page.find("Catégorie:Thématiques en ") != -1):
    wikitext = createCategoryThematiques(page,cle)
  elif (page.find("Catégorie:Traductions en ") != -1):
    wikitext = createCategoryTraductions(page,cle)
  elif (page.find("Catégorie:Verbes en ") != -1):
    wikitext = createCategoryVerbes(page,cle)
  elif (page.find("Catégorie:Vertébrés en") != -1):
     wikitext = createCategoryVertebres(page,cle)
  elif (page.find("Catégorie:Vie domestique en") != -1):
     wikitext = createCategoryVieDomestique(page,cle)
  elif (page.find("Catégorie:Vêtements en") != -1):
     wikitext = createCategoryVetements(page,cle)
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
        (page.find(" vidéo") == -1) and
        (page.find(" boules") == -1) and
        (page.find(" rôles") == -1)):
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
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’anatomie") != -1)):
    wikitext = createCategoryLexiqueAnatomie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" des sciences") != -1)):
    wikitext = createCategoryLexiqueSciences(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la religion") != -1)):
    wikitext = createCategoryLexiqueReligion(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la marine") != -1)):
    wikitext = createCategoryLexiqueMarine(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la philatélie") != -1)):
    wikitext = createCategoryLexiquePhilatelie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la linguistique") != -1)):
    wikitext = createCategoryLexiqueLinguistique(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la technologie") != -1)):
    wikitext = createCategoryLexiqueTechnologie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’équitation") != -1)):
    wikitext = createCategoryLexiqueEquitation(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la bande dessinée") != -1)):
    wikitext = createCategoryLexiqueBandeDessinee(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la géophysique") != -1)):
    wikitext = createCategoryLexiqueGeophysique(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la pédologie") != -1)):
    wikitext = createCategoryLexiquePedologie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la robotique") != -1)):
    wikitext = createCategoryLexiqueRobotique(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" des statistiques") != -1)):
    wikitext = createCategoryLexiqueStatistiques(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" du baseball") != -1)):
    wikitext = createCategoryLexiqueBaseball(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" du cyclisme") != -1)):
    wikitext = createCategoryLexiqueCyclisme(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" du squelette") != -1)):
    wikitext = createCategoryLexiqueSquelette(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la chasse") != -1)):
    wikitext = createCategoryLexiqueChasse(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" du militaire") != -1)):
    wikitext = createCategoryLexiqueMilitaire(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la nosologie") != -1)):
    wikitext = createCategoryLexiqueNosologie(page,cle,code)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la pâtisserie") != -1)):
    wikitext = createCategoryLexiquePatisserie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la géographie") != -1)):
    wikitext = createCategoryLexiqueGeographie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la littérature") != -1)):
    wikitext = createCategoryLexiqueLitterature(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la téléphonie") != -1)):
    wikitext = createCategoryLexiqueTelephonie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la technique") != -1)):
    wikitext = createCategoryLexiqueTechnique(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la mythologie") != -1)):
    wikitext = createCategoryLexiqueMythologie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" des loisirs") != -1)):
    wikitext = createCategoryLexiqueLoisirs(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" du travail") != -1) and
        (page.find(" du droit") == -1)):
    wikitext = createCategoryLexiqueTravail(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la cuisine") != -1)):
    wikitext = createCategoryLexiqueCuisine(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la médecine") != -1) and
        (page.find("vétérinaire") == -1)):
    wikitext = createCategoryLexiqueMedecine(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’aéronautique") != -1)):
    wikitext = createCategoryLexiqueAeronautique(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’art") != -1)):
    wikitext = createCategoryLexiqueArt(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la mécanique") != -1)):
    wikitext = createCategoryLexiqueMecanique(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’hydrologie") != -1)):
    wikitext = createCategoryLexiqueHydrologie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’informatique") != -1)):
    wikitext = createCategoryLexiqueInformatique(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’audiovisuel") != -1)):
    wikitext = createCategoryLexiqueAudiovisuel(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’astronautique") != -1)):
    wikitext = createCategoryLexiqueAstronautique(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’ethnologie") != -1)):
    wikitext = createCategoryLexiqueEthnologie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’entomologie") != -1)):
    wikitext = createCategoryLexiqueEntomologie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’urbanisme") != -1)):
    wikitext = createCategoryLexiqueUrbanisme(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’embryologie") != -1)):
    wikitext = createCategoryLexiqueEmbryologie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’édition") != -1)):
    wikitext = createCategoryLexiqueEdition(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’islam") != -1)):
    wikitext = createCategoryLexiqueIslam(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’horticulture") != -1)):
    wikitext = createCategoryLexiqueHorticulture(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’agriculture") != -1)):
    wikitext = createCategoryLexiqueAgriculture(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’automobile") != -1)):
    wikitext = createCategoryLexiqueAutomobile(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’athlétisme") != -1)):
    wikitext = createCategoryLexiqueAthletisme(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’archéologie") != -1)):
    wikitext = createCategoryLexiqueArcheologie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la boxe") != -1)):
    wikitext = createCategoryLexiqueBoxe(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la chirurgie") != -1)):
    wikitext = createCategoryLexiqueChirurgie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" des échecs") != -1)):
    wikitext = createCategoryLexiqueEchecs(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" du jardinage") != -1)):
    wikitext = createCategoryLexiqueJardinage(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la logique") != -1)):
    wikitext = createCategoryLexiqueLogique(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la mercatique") != -1)):
    wikitext = createCategoryLexiqueMercatique(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la microbiologie") != -1)):
    wikitext = createCategoryLexiqueMicrobiologie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la minéralogie") != -1)):
    wikitext = createCategoryLexiqueMineralogie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la reproduction") != -1)):
    wikitext = createCategoryLexiqueReproduction(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la sexualité") != -1)):
    wikitext = createCategoryLexiqueSexualite(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la rhétorique") != -1)):
    wikitext = createCategoryLexiqueRhetorique(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" du sport") != -1)):
    wikitext = createCategoryLexiqueSport(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" des sentiments") != -1)):
    wikitext = createCategoryLexiqueSentiments(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la sociologie") != -1)):
    wikitext = createCategoryLexiqueSociologie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" des télécommunications") != -1)):
    wikitext = createCategoryLexiqueTelecommunications(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" du tennis") != -1)):
    wikitext = createCategoryLexiqueTennis(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’apiculture") != -1)):
    wikitext = createCategoryLexiqueApiculture(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" des arts martiaux") != -1)):
    wikitext = createCategoryLexiqueArtsMartiaux(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’astrophysique") != -1)):
    wikitext = createCategoryLexiqueAstrophysique(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" du christianisme") != -1)):
    wikitext = createCategoryLexiqueChristianisme(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’électronique") != -1)):
    wikitext = createCategoryLexiqueElectronique(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’élevage") != -1)):
    wikitext = createCategoryLexiqueElevage(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la géométrie") != -1)):
    wikitext = createCategoryLexiqueGeometrie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’hindouisme") != -1)):
    wikitext = createCategoryLexiqueHindouisme(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’horlogerie") != -1)):
    wikitext = createCategoryLexiqueHorlogerie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" du judo") != -1)):
    wikitext = createCategoryLexiqueJudo(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la justice") != -1)):
    wikitext = createCategoryLexiqueJustice(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la législation") != -1)):
    wikitext = createCategoryLexiqueLegislation(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la musique") != -1)):
    wikitext = createCategoryLexiqueMusique(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" des wikis") != -1)):
    wikitext = createCategoryLexiqueWikis(page,cle,code)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la construction") != -1)):
    wikitext = createCategoryLexiqueConstruction(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’Internet") != -1)):
    wikitext = createCategoryLexiqueInternet(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la politique") != -1)):
    wikitext = createCategoryLexiquePolitique(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la sylviculture") != -1)):
    wikitext = createCategoryLexiqueSylviculture(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la syntaxe") != -1)):
    wikitext = createCategoryLexiqueSyntaxe(page,cle,code)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de l’alpinisme") != -1)):
    wikitext = createCategoryLexiqueAlpinisme(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la biochimie") != -1)):
    wikitext = createCategoryLexiqueBiochimie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" des cartes à jouer") != -1)):
    wikitext = createCategoryLexiqueCartesAJouer(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la cartophilie") != -1)):
    wikitext = createCategoryLexiqueCartophilie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la colorimétrie") != -1)):
    wikitext = createCategoryLexiqueColorimetrie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la fiscalité") != -1)):
    wikitext = createCategoryLexiqueFiscalite(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" des jeux vidéo") != -1)):
    wikitext = createCategoryLexiqueJeuxVideo(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la lutherie") != -1)):
    wikitext = createCategoryLexiqueLutherie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la neurologie") != -1)):
    wikitext = createCategoryLexiqueNeurologie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la nutrition") != -1)):
    wikitext = createCategoryLexiqueNutrition(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la pêche") != -1) and
        (page.find(" à la mouche") == -1)):
    wikitext = createCategoryLexiquePeche(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" de la photographie") != -1)):
    wikitext = createCategoryLexiquePhotographie(page,cle)
  elif ((page.find("Catégorie:Lexique en ") != -1) and
        (page.find(" des systèmes électoraux") != -1)):
    wikitext = createCategoryLexiqueSystemesElectoraux(page,cle)
  elif ((page.find("Catégorie:") != -1) and
        page.find(" en ") != -1):
    wikitext = createCategoryPaysEnLangue(page,cle,country)

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

def getContinentByCountryDict():

  output = {}
  with open("country.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
      myCountry, myContinent = row
      output[myCountry]=myContinent

  return output

def guessLanguage(page,myBegin,myEnd,cle):
  #TODO prevoir une fonction qui recupere le nom de la langue quel que soit le nom de la catégorie
  # cela permet de factoriser beaucoup de code provenant de chaque fonction individuelle
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

  if test:
    createCategory("[[:Catégorie:Kiribati en same du Nord]]", cle, codeLangue, continentByCountryDict)
    createCategory("[[:Catégorie:Localités d’Italie en français]]", cle, codeLangue, continentByCountryDict)

  #UserContributionsGenerator
  else:
    for page in WantedPagesCategoryGenerator(5000):
      createCategory(page,cle,codeLangue,continentByCountryDict)
  

if __name__ == '__main__':

  try:

    main()
    
  finally:

    pywikibot.stopme()
