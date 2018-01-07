#! /usr/bin/python3

# -*- coding: utf-8 -*-

import io
import pywikibot

import CleDeTri

def parseData(wikitext):
  language = {}
  cledetri = {}
  
  # Languages
  beg = wikitext.find("-- Langues")
  end =	wikitext.find("-- Fin langues")
  buf = io.StringIO(wikitext[beg:end])
  lines = buf.readlines()

  for line in lines:
    # Getting the language code
    beg = line.find("l['");
    if(beg == -1):
      continue
    end = line.find("']", beg+1);
    code = line[beg+3:end]
       
    # Getting the language name
    beg = line.find("'", end+1)
    end = line.find("'", beg+1)
    name = line[beg+1:end]

    # Getting the sorting key
    beg = line.find("tri = '")
    end = line.find("'", beg+7)
    key = ""
    if(beg != -1):
      key = line[beg+7:end]
    
    if (len(key)==0):
      key = CleDeTri.CleDeTri(name)
        
    print(line + " : " + code + "->" + name + " (" + key + ")")
    language[name] = code
    cledetri[name] = key

  # Proto-languages
  beg = wikitext.find("-- Proto-langues")
  end =	wikitext.find("-- Fin protolangues")
  buf = io.StringIO(wikitext[beg:end])
  lines = buf.readlines()

  for line in lines:
    # Getting the language code
    beg = line.find("l['");
    if(beg == -1):
      continue
    end = line.find("']", beg+1);
    code = line[beg+3:end]
       
    # Getting the language name
    beg = line.find("'", end+1)
    end = line.find("'", beg+1)
    name = line[beg+1:end]

    # Getting the sorting key
    beg = line.find("tri = '")
    end = line.find("'", beg+7)
    key = ""
    if(beg != -1):
      key = line[beg+7:end]
    
    if (len(key)==0):
      key = CleDeTri.CleDeTri(name)
        
    print(line + " : " + code + "->" + name + " (" + key + ")")
    language[name] = code
    cledetri[name] = key
    
  return (language, cledetri)

def main():
# l['dum'] = { nom = 'moyen néerlandais', tri = 'neerlandais moyen' }

  page = pywikibot.Page(pywikibot.getSite(), "Module:langues/data")
  wikitext = page.get()

  data, cledetri = parseData(wikitext)
  
  outfile = open(u'liste_langue.dat', "w")
  for key,value in sorted(data.items(), key=lambda x:x[1]):
    print("Writing %s" % (key))
    outfile.write(key + ";" + value + ";" + cledetri[key] + "\n")

  outfile.close()
  

if __name__ == '__main__':

  try:

    main()
    
  finally:

    pywikibot.stopme()
