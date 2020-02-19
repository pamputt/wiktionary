#! /usr/bin/python3

# -*- coding: utf-8 -*-

import io
import pywikibot

def parseData(wikitext):
  lexique = []
  
  # Languages
  beg = wikitext.find("local t = {")
  end =	wikitext.find("return t")
  buf = io.StringIO(wikitext[beg:end])
  lines = buf.readlines()

  for line in lines:
    # Getting the lexique
    # One searches for line that starts with "['" and ends with "'] = {"
    # but we are not interested in lines that contain "super_categories"
    # (that also match this pattern)
    beg = line.find("super_categories")
    if(beg != -1):
      continue
    
    beg = line.find("  ['");
    if(beg == -1):
      continue
    
    end = line.find("'] = {", beg+1);
    if(end == -1):
      continue
       
    # Getting the lexique name
    beg = line.find("'")
    end = line.find("'", beg+1)
    lexique.append(line[beg+1:end])
        
    print(">> " + line + " : " + lexique[-1])
    
  return lexique

def main():
# l['dum'] = { nom = 'moyen néerlandais', tri = 'neerlandais moyen' }

  page = pywikibot.Page(pywikibot.Site(), "Module:categories/data/lexiques")
  wikitext = page.get()

  data = parseData(wikitext)
  
  outfile = open(u'liste_lexique.dat', "w")
  for mot in data:
    print("Writing %s" % (mot))
    outfile.write(mot + "\n")

  outfile.close()
  

if __name__ == '__main__':

  try:

    main()
    
  finally:

    pywikibot.stopme()
