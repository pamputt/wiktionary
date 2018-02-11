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

def createCategoryLexiqueAstronautique(page,cle):
  #Catégorie:Lexique en italien de l’astronautique
  language = guessLanguage(page,"en","de l’",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|astronautique]]\n"
  wikitext += "[[Catégorie:Astronautique|" + cle[language] + "]]"
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

def createCategoryLexiqueClimatologie(page,cle):
  #Catégorie:Lexique en français de la climatologie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|climatologie]]\n"
  wikitext += "[[Catégorie:Climatologie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueCommerce(page,cle):
  #Catégorie:Lexique en italien du commerce
  language = guessLanguage(page,"en","du",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|commerce]]\n"
  wikitext += "[[Catégorie:Commerce|" + cle[language] + "]]"
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

def createCategoryLexiqueFauconnerie(page,cle):
  #Catégorie:Lexique en italien de la fauconnerie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return

  wikitext = "[[Catégorie:Lexique en " + language + " de l’élevage|fauconnerie]]\n"
  wikitext += "[[Catégorie:Lexique en " + language + " de la chasse|fauconnerie]]\n"
  wikitext += "[[Catégorie:Fauconnerie|" + cle[language] + "]]"
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

def createCategoryLexiqueFamille(page,cle):
  #Catégorie:Lexique en italien de la famille
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|famille]]\n"
  wikitext += "[[Catégorie:Famille|" + cle[language] + "]]"
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

def createCategoryLexiqueReligion(page,cle):
  #Catégorie:Lexique en italien de la religion
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "Cette page liste les mots en [[" + language + "]] en rapport avec la [[religion]].\n\n"
  wikitext += "[[Catégorie:Lexiques en " + language + "|religion]]\n"
  wikitext += "[[Catégorie:Religion|" + cle[language] + "]]"
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

def createCategoryLexiqueSexualite(page,cle):
  #Catégorie:Lexique en anglais de la sexualité
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|sexualite]]\n"
  wikitext += "[[Catégorie:Sexualité|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueSerrurerie(page,cle):
  #Catégorie:Lexique en anglais de la serrurerie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|serrurerie]]\n"
  wikitext += "[[Catégorie:Serrurerie|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueSquelette(page,cle):
  #Catégorie:Lexique en italien du squelette
  language = guessLanguage(page,"en","du",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexique en " + language + " de l’anatomie|squelette]]\n"
  wikitext += "[[Catégorie:Squelette|" + cle[language] + "]]"
  return wikitext

def createCategoryLexiqueTemps(page,cle):
  #Catégorie:Lexique en same du Nord du temps
  language = guessLanguage(page,"en","du",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|temps]]\n"
  wikitext += "[[Catégorie:Temps|" + cle[language] + "]]"
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

def createCategoryLexiqueSport(page,cle):
  #Catégorie:Lexique en italien du sport
  language = guessLanguage(page,"en","du",cle)
  if not language:
    return
  
  wikitext = "[[Catégorie:Lexiques en " + language + "|sport]]\n"
  wikitext += "[[Catégorie:Sport|" + cle[language] + "]]"
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

def createCategoryLexiqueTelecommunication(page,cle):
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

def createCategoryLexiqueZoologie(page,cle):
  #Catégorie:Lexique en bukawa de la zoologie
  language = guessLanguage(page,"en","de la",cle)
  if not language:
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
        (page.find(" de la mineralogie") != -1)):
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

def guessLanguage(page,myBegin,myEnd,cle):
  #TODO prevoir une fonction qui recupere le nom de la langue quel que soit le nom de la catégorie
  # cela permet de factoriser beaucoup de code provenant de chaque fonction individuelle
  beg=page.find(" " + myBegin + " ")

  tmp = beg
  est = page.find(" de l’Est ",beg)
  if(est != -1):
    tmp = est
    
  ouest = page.find(" de l’Ouest ",beg)
  if(ouest != -1):
    tmp = ouest
    
  sud=page.find(" du Sud ",beg)
  if(sud != -1):
    tmp = sud
    
  nord=page.find(" du Nord ",beg)
  if(nord != -1):
    tmp = nord
    
  end=page.find(" " + myEnd,tmp+1)
  
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
  countryList = getCountryList()

  if test:
    createCategory("[[:Catégorie:Lexique en italien de la bande dessinée]]", cle, codeLangue, countryList)
  #UserContributionsGenerator
  else:
    for page in WantedPagesCategoryGenerator(5000):
      createCategory(page,cle,codeLangue,countryList)
  

if __name__ == '__main__':

  try:

    main()
    
  finally:

    pywikibot.stopme()
