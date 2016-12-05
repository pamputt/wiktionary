#!/usr/bin/python
# -*- coding: utf-8  -*-
"""
 
This script counts the number of quotes.
 
# TODO :
#  - Check for different quotes with the same 'original' field
#  - Check not only for equal, but similar quotes (distance d'edition)
#  - Check for same quote with different refs
 
This script understands various command-line arguments:
 
    -cat           Work on all pages which are in a specific category.
                   Argument can also be given as "-cat:categoryname".
 
    -ref           Work on all pages that link to a certain page.
                   Argument can also be given as "-ref:referredpagetitle".
 
    -links         Work on all pages that are linked from a certain page.
                   Argument can also be given as "-links:linkingpagetitle".
 
    -new           Work on the most recent new pages on the wiki
 
    -subcat        When the pages to work on have been chosen by -cat, pages in
                   subcategories of the selected category are also included.
                   When -cat has not been selected, this has no effect.
 
 
    -file:         used as -file:filename, read a list of pages to treat
                   from the named file
 
 
    -start:        used as -start:title, specifies that the robot should
                   go alphabetically through all pages on the home wiki,
                   starting at the named page.
    -output:       used as -output:pagename, generate report to pagename.
    -outputprefix: used as -output:pagename, create NUMBEROFQUOTES and
                   NUMBEROFARTICLES as subpages of pagename
    -outputquotes: used as -outputquotes:pagename, put the number of quotes
                   on pagename
    -outputarticles: used as -outputarticles:pagename, put the number of
                   articles containing quotes on pagename
 
"""
 
import wikipedia, pagegenerators, catlib, config
import sys, re, string, time, locale, operator
 
msg = {
    'fr': (u'<h1 style="border-bottom:none;margin-top:0;margin-bottom:0.8em;text-align:center;"> %d citations dans %d articles ',
           u'<small>(Le nombre d\'articles n\'inclut que les articles qui possÃ¨dent au moins une citation. Les citations en plusieurs exemplaires ne sont comptÃ©es qu\'une fois.)',
           u'== RÃ©partion par article ==\n\n',
           u'{| class="wikitable"\n|+\'\'\'Nombre de citations par article\'\'\'\n! align="center" | Article\n! align="center" | Nombre de citations\n',
           u'|- align="center" \n| \'\'\'Moyenne\'\'\' || %0.2f\n',
           u'<small>La moyenne exclut les articles ne contenant aucune citation.</small>\n\n',
           u'== Citations en plusieurs exemplaires ==\n',
           u'<small>(Ce tableau recense le nombre de citations qui figurent dans plusieurs articles. Ainsi, si le premier champ vaut N et le second M, cela signifie que M citations figurent en N exemplaires (dans N articles))</small>\n\n',
           u'{| class="wikitable" style="width: 40%%"\n|+\'\'\'Nombre d\'exemplaires de la citation\'\'\'\n! align="center" | Article\n! align="center" | Nombre de citations\n',
           u'Mise Ã  jour des statistiques'),
    'is': (u'<h1 style="border-bottom:none;margin-top:0;margin-bottom:0.8em;text-align:center;"> %d tilvitnanir Ã­ %d greinum ',
           u'<small>(Ã fjÃ¶lda greina eru greinar meÃ° engum tilvitnunum ekki taldar meÃ°. TvÃ¶faldaÃ°ar tilvitnanir eru taldar sem ein.)',
           u'== Eftir greinum ==\n\n',
           u'{| class="wikitable"\n|+\'\'\'FjÃ¶ldi tilvitnana eftir greinum\'\'\'\n! align="center" | Grein\n! align="center" | FjÃ¶ldi tilvitna\n',
           u'|- align="center" \n| \'\'\'MeÃ°altal\'\'\' || %0.2f\n',
           u'<small>MeÃ°altaliÃ° telur ekki meÃ° greinar sem innihalda engar tilvitnanir.</small>\n\n',
           u'== TvÃ¶faldar tilvitnanir ==\n',
           u'<small>(Ãžessi tafla sÃ½nir fjÃ¶lda tilvitnana sem koma fram Ã­ fleirum en einni grein. If the first field is N and the second M, it means M quotes appear N times (in N articles))</small>\n\n',
           u'{| class="wikitable" style="width: 40%%"\n|+\'\'\'FjÃ¶ldi greina sem tilvitnunin kemur fyrir\'\'\n! align="center" | Greinar\n! align="center" | FjÃ¶ldi tilvitnana\n',
           u'Updated statistics'),
    'en': (u'<h1 style="border-bottom:none;margin-top:0;margin-bottom:0.8em;text-align:center;"> %d quotes in %d articles ',
           u'<small>(The number of articles does not include articles without quotes. Duplicated quotes are counted only once.)',
           '== By article ==\n\n',
           '{| class="wikitable"\n|+\'\'\'Number of quotes by article\'\'\'\n! align="center" | Article\n! align="center" | Number of quotes\n',
           '|- align="center" \n| \'\'\'Mean\'\'\' || %0.2f\n',
           '<small>Mean excludes articles without quotes.</small>\n\n',
           '== Duplicated quotes ==\n',
           '<small>(This table gives the number of quotes that appear in more than one article. If the first field is N and the second M, it means M quotes appear N times (in N articles))</small>\n\n',
           '{| class="wikitable" style="width: 40%%"\n|+\'\'\'Number of articles where the quote appears\'\'\n! align="center" | Articlse\n! align="center" | Number of quotes\n',
           'Updated statistics')
    }
 
def trim(s):
    return s.strip(" \t\n\r\0\x0B")
 
def replace_citation(piece):
    for p in piece['parts']:
        if trim(p[0].lower()) == globalvar.quote_arg or trim(p[0]) == '1' or trim(p[0]) == '':
            return p[1]
 
def replace_lang(piece):
    # Return second argument.
    return piece['parts'][1][1]
 
def replace_template(piece):
    # Return title if no arg. 
    if len(piece['parts']) == 0:
        return piece['title']
 
    # Else : return first arg.
    return piece['parts'][0][1]
 
class Global(object):
    """Container class for global settings.
       Use of globals outside of this is to be avoided."""
    mainpagename = None
    quotes = {}
    # List of articles without quotes.
    noquotes = []
    quote_template = 'citation'
    quote_arg = 'citation'
    known_templates = {quote_template: replace_citation, 'lang': replace_lang}
    quiet = False
    debug = False
 
def outputq(s, newline = True):
    if not globalvar.quiet:
        wikipedia.output(u'%s' % s, newline = newline)
 
def debug(s):
    if globalvar.debug:
        wikipedia.output(u'%s' % s)
 
def error(s):
    # Output errors to ... stdout, because pywikipedia uses stderr for "normal"
    # output. *sigh*
    wikipedia.output(u'ERROR: %s' % s, toStdout = True)
 
def parse_templates(text):
    """Parse text (should be the beginning of a quote template) to get the
    content of the quote with all known templates substituted."""
    # Mostly adapted from <includes/Parser.php>
 
    # Returned text
    quote = ""
    # Built from this
    pieces = []
 
    stack = []
    # index in stack
    lastOpeningBrace = -1
 
    debug(u'Parsing templates')
    debug('Showing first 200 chars from text')
#    debug(u'%s' % text[:200])
 
    i = 0 
    # End when the first found template ends, i.e. when stack is empty and
    # we're not at the beginning 
    while (stack != [] or i == 0) and i < len(text):
        if lastOpeningBrace == -1:
            search = r'({{)'
        else:
            search = r'({{|}}|\|)'
 
        debug(u"searching for %s" % search)
 
        s = re.compile(search)
        m = s.search(text[i:])
        if not m:
            error(u'ERROR: pattern not found: %s' % search)
            return
 
        i += m.start()
        span = m.end() - m.start()
 
 
        debug(u'%s (%d, %d)' % (m.group(), m.start(), m.end()))
        debug(u'%s' % text[i:])
 
        if m.group() == "{{":
            debug(u"new template starting from %d" % i)
 
            stack.append({})
            lastOpeningBrace += 1
 
            stack[lastOpeningBrace]['start'] = i
            i += span
            stack[lastOpeningBrace]['lastPartStart'] = i
        else:
            # End of part.
            debug(u"part ending at %d" % i)
 
            part = text[stack[lastOpeningBrace]['lastPartStart']:i]
 
            # First part : template title.
            if not 'parts' in stack[lastOpeningBrace]:
                stack[lastOpeningBrace]['title'] = trim(part)
                stack[lastOpeningBrace]['parts'] = []
            else:
                # Argument.
                sep = part.find('=')
                if sep != -1:
                    argname = part[:sep]
                    arg = part[sep+1:]
                else:
                    argname = ''
                    arg = part
 
                debug(u"part : (%s, %s)" % (argname, arg))
 
                stack[lastOpeningBrace]['parts'].append([argname, arg])
            i += span
            stack[lastOpeningBrace]['lastPartStart'] = i
 
        if m.group() == "}}":
            # Replace template.
            title = stack[lastOpeningBrace]['title'].lower()
 
            debug(u"template: %s" % title)
 
            if title in globalvar.known_templates:
                debug(u"calling replace_citation on quote")
                piece = globalvar.known_templates[title](stack[lastOpeningBrace])
            else:
                # Default callback.
                debug(u"calling replace_template on other template")
                piece = replace_template(stack[lastOpeningBrace])
 
                debug("template %s replaced by %s" % (stack[lastOpeningBrace]['title'], piece))
 
            if piece == None:
                error("Found a null piece: probably unterminated %s template!" % title)
 
            start = stack[lastOpeningBrace]['start']
            text = text[:start] + piece + text[i:]
            i = start + len(piece)
 
            del stack[lastOpeningBrace]
            lastOpeningBrace -= 1
 
    if lastOpeningBrace != -1:
        error('quote template not finished at end of text!')
        return
 
    debug(u'Quote : %s' % text[:i])
    return [text, i]
 
 
def prepare_text(text):
    wikilinksR = re.compile(r"^([ %!\"$&'()*,\\\-.\\/0-9:;=?@A-Z\\\\^_`a-z~\\x80-\\xFF+#]+)(?:\|(.+?))?]](.*)", re.DOTALL)
    links = text.split('[[')
    # All texts before the first link.
    text = links.pop(0)
    for l in links:
        add = ""
        m = wikilinksR.match(l)
        if m:
            # [[0|1]]2 
            if m.group(2):
                add += m.group(2)
            else:
                add += m.group(1)
            if m.group(3):
                add += m.group(3)
        else:
            add += '[[' + l
        text += add
#        debug(u"Add: %s" % add) 
#    debug(u'After :')
#    debug(u'%s' % text)
 
    # Remove tags.
    tagsR = re.compile(r'<[^>]*>')
    text = tagsR.sub('', text)
    return text
 
def parse_quote(text):
    # Subst templates.
    return parse_templates(text)
 
def workon(page):
    if page.title() == globalvar.mainpagename:
        return
 
    outputq(u'handling : %s' % page.title())
 
    try:
        text = page.get()
    except wikipedia.IsRedirectPage:
        return
 
    text = prepare_text(text)
 
    if not wikipedia.getSite().nocapitalize:
        pattern = '[' + re.escape(globalvar.quote_template[0].upper()) + re.escape(globalvar.quote_template[0].lower()) + ']' + re.escape(globalvar.quote_template[1:])
    else:
        pattern = re.escape(globalvar.quote_template)
 
    r = re.compile(r'\{\{ *(?:[Tt]emplate:|[mM][sS][gG]:)?' + pattern)
 
    alnum = re.compile('\W')
 
    matches = r.finditer(text)
    offset = 0
    nquotes = 0
 
    for m in matches:
        debug(u'match (200) : %s' % text[m.start():m.start()+200])
        debug(u'offset: %d' % offset)
       # Real start of the match.
        nquotes += 1
        start = m.start() - offset
 
        [endtext, qlen] = parse_quote(text[start:])
 
        offset += (len(text[start:]) - len(endtext))
 
        quote = unicode(endtext[:qlen])
        text = text[:start] + endtext
 
        debug(u'Quote 2: %s' % (quote))
        debug(u'Text: %s' % text)
 
        # Strip all non-alphanumeric chars.
        squote = alnum.sub('', quote)
        h = hash(squote)
 
        if not h in globalvar.quotes:
            globalvar.quotes[h] = [squote, [[quote, page]]]
        else:
            if globalvar.quotes[h][0] != squote:
                error('hash collision! %s and %s have the same hash (%d).' % (globalvar.quotes[h][0], squote, h))
                sys.exit(-1)
 
            globalvar.quotes[h][1].append([quote, page])
 
 
    if nquotes == 0:
        outputq(u"no quotes in %s" % page.title())
        globalvar.noquotes.append(page)
 
 
def generate_output(quotes):
    # We want to compute :
    #  - The total number of (unique) quotes.
    #  - The number of (unique) quotes per article.
    #  - The number of duplicates. 
    tcount = 0
    acount = {}
    dupcount = {}
    # We also want :
    #  - to print similar-but-not-equal quotes.
    #  - to print when the same quote appears twice in an article.
 
    outputq(u'quotes : %d' % len(quotes))
    for h in quotes:
        # Unique quotes.
        uquotes = {}
        [operator.setitem(uquotes, i[0], []) for i in quotes[h][1] if not uquotes.has_key(i[0])]
        outputq(u'uquotes : %s' % uquotes)
 
        # Get associated pages.
        for q in quotes[h][1]:
            if q[0] in uquotes:
                uquotes[q[0]].append(q[1])
 
        debug(u'increasing count by one')
        # Only increment by one, because all quotes with the same hash
        # should be similar enough to be considered identical.
        tcount += 1
 
        pr = False
        # Are all quotes the same?
        if len(uquotes) > 1:
            pr = True
            outputq(u'Similar quotes found :')
 
        articles = 0
        for q in uquotes:
            if pr:
                outputq(u'\t%s (on:' % q, newline = False)
            for a in uquotes[q]:
                if pr:
                    outputq(u' %s' % trim(a.title()), newline = False)
                if a in acount:
                    acount[a] += 1
                else:
                    acount[a] = 1;
                articles += 1
            if pr:
               outputq(u')')
 
        if articles in dupcount:
            dupcount[articles] += 1
        else:
            dupcount[articles] = 1
 
    outputq(u'TOTAL NUMBER OF QUOTES : %d' % tcount)
    output = msg[globalvar.lang][0] % (tcount, len(acount))
    output += '<small style="font-size: 70%%">(%s)</small></h1>\n' 
    output += msg[globalvar.lang][1]
    output += '\n\n'
 
#    locale.setlocale(locale.LC_ALL, "fr_FR@euro")
#    for l in sorted(acount.items(), lambda x,y: locale.strcoll(x[0].title().lower(), y[0].title().lower())):
#        wikipedia.output(u'%s' % l[0].title())
 
    # Sort by number of quotes (return list of tuples, not dict)
    acount = sorted(acount.items(), lambda x,y: cmp(y[1], x[1]) or locale.strcoll(x[0].title().lower(), y[0].title().lower()))
 
    output += msg[globalvar.lang][2] 
    output += msg[globalvar.lang][3]
 
    # Make it Unicode because the titles will be Unicode.
 
    for a in acount:
        outputq(u'adding to table: %s' % a[0].title())
        output += '|-\n| [[%s]] || %d\n' % (a[0].title(), a[1])
    for p in globalvar.noquotes:
        output += '|-\n| [[%s]] || 0\n' % p.title()
 
    mean = 0
    if len(acount) != 0:
        mean = tcount / float(len(acount))
 
    output2 = ""
    output2 += msg[globalvar.lang][4] % mean
    output2 += '|}\n\n'
    output2 += msg[globalvar.lang][5]
 
    output2 += msg[globalvar.lang][6]
    output2 += msg[globalvar.lang][7]
    output2 += msg[globalvar.lang][8]
 
    output += output2
 
    for a in dupcount:
        output += '|-\n|%d || %d\n' % (a, dupcount[a])
    output += '|}\n\n'
 
    return [output, tcount, len(acount)]
 
class Main(object):
    # Options
    __start = None
    __number = None
    ## Which page generator to use
    __workonnew = False
    __catname = None
    __catrecurse = False
    __linkpagetitle = None
    __refpagetitle = None
    __textfile = None
    __pagetitles = []
 
    __output = None
    __outputprefix = None
    __outputarticles = None
    __outputquotes = None
 
    def parse(self):
        # Parse options
 
        for arg in wikipedia.handleArgs():
            if arg.startswith('-ref'):
                if len(arg) == 4:
                    self.__refpagetitle = wikipedia.input(u'Links to which page should be processed?')
                else:
                    self.__refpagetitle = arg[5:]
            elif arg.startswith('-cat'):
                if len(arg) == 4:
                    self.__catname = wikipedia.input(u'Please enter the category name:');
                else:
                    self.__catname = arg[5:]
            elif arg.startswith('-subcat'):
                self.__catrecurse = True
            elif arg.startswith('-links'):
                if len(arg) == 6:
                    self.__linkpagetitle = wikipedia.input(u'Links from which page should be processed?')
                else:
                    self.__linkpagetitle = arg[7:]
            elif arg.startswith('-file:'):
                if len(arg) == 5:
                    self.__textfile = wikipedia.input(u'File to read pages from?')
                else:
                    self.__textfile = arg[6:]
            elif arg == '-new':
                self.__workonnew = True
            elif arg.startswith('-start:'):
                if len(arg) == 6:
                    self.__start = wikipedia.input(u'Which page to start from: ')
                else:
                    self.__start = arg[7:]
            elif arg.startswith('-number:'):
                if len(arg) == 7:
                    self.__number = int(wikipedia.input(u'Number of pages to parse: '))
                else:
                    self.__number = int(arg[8:])
            elif arg.startswith('-output:'):
                if len(arg) == 7:
                    self.__output = wikipedia.input(u'Which page to save report to: ')
                else:
                    self.__output = arg[8:]
            elif arg.startswith('-outputprefix:'):
                if len(arg) == 12:
                    self.__outputprefix = wikipedia.input(u'Which page to save templates to: ')
                else:
                    self.__outputprefix = arg[13:]
            elif arg.startswith('-outputquotes:'):
                if len(arg) == 12:
                    self.__outputquotes = wikipedia.input(u'Which page to save number of quotes to: ')
                else:
                    self.__outputquotes = arg[13:]
            elif arg.startswith('-outputarticles:'):
                if len(arg) == 14:
                    self.__outputarticles = wikipedia.input(u'Which page to save number of quotes to: ')
                else:
                    self.__outputarticles = arg[15:]
            elif arg.startswith('-template:'):
                if len(arg) == 9:
                    globalvar.quote_template = wikipedia.input(u'Which template is used for quotes?')
                else:
                    globalvar.quote_template = arg[10:]
            elif arg.startswith('-arg:'):
                if len(arg) == 4:
                    globalvar.quote_arg = wikipedia.input(u'Which template arg is used for quotes?')
                else:
                    globalvar.quote_arg = arg[5:]
            elif arg == '-quiet':
                globalvar.quiet = True
            elif arg == '-debug':
                globalvar.debug = True
            else:
                self.__pagetitles.append(arg)
 
    def generator(self):
        # Choose which generator to use according to options.
 
        pagegen = None
 
        if self.__workonnew:
            if not self.__number:
                self.__number = config.special_page_limit
            pagegen = pagegenerators.NewpagesPageGenerator(number = self.__number)
 
        elif self.__refpagetitle:
            refpage = wikipedia.Page(wikipedia.getSite(), self.__refpagetitle)
            pagegen = pagegenerators.ReferringPageGenerator(refpage)
 
        elif self.__linkpagetitle:
            linkpage = wikipedia.Page(wikipedia.getSite(), self.__linkpagetitle)
            pagegen = pagegenerators.LinkedPageGenerator(linkpage)
 
        elif self.__catname:
            cat = catlib.Category(wikipedia.getSite(), 'Category:%s' % self.__catname)
 
            if self.__start:
                pagegen = pagegenerators.CategorizedPageGenerator(cat, recurse = self.__catrecurse, start = self.__start)
            else:
                pagegen = pagegenerators.CategorizedPageGenerator(cat, recurse = self.__catrecurse)
 
        elif self.__textfile:
            pagegen = pagegenerators.TextfilePageGenerator(self.__textfile)
 
        else:
            if not self.__start:
                self.__start = '!'
            namespace = wikipedia.Page(wikipedia.getSite(), self.__start).namespace()
            start = wikipedia.Page(wikipedia.getSite(), self.__start).titleWithoutNamespace()
 
            pagegen = pagegenerators.AllpagesPageGenerator(start, namespace)
 
        return pagegen
 
 
    def main(self):
#        wikipedia.activateLog('count-quotes.log')
        wikipedia.setLogfileStatus(True, 'count_quotes.log')                    
 
        # Parse command line options
        self.parse()
 
        # ensure that we don't try to change main page
        try:
            site = wikipedia.getSite()
            globalvar.mainpagename = site.family.mainpages[site.language()]
        except:
            outputq(u'Missing main page name')
 
        if site.language() in msg:
            globalvar.lang = site.language()
        else:
            globalvar.lang = 'en'
 
        pagegen = self.generator()
 
        generator = None
        if self.__pagetitles:
            pages = []
            for p in self.__pagetitles:
                try:
                    pages.append(wikipedia.Page(wikipedia.getSite(), p))
                except wikipedia.NoPage: pass
            generator = pagegenerators.PreloadingGenerator(iter(pages))
        else:
            generator = pagegenerators.PreloadingGenerator(pagegen)
 
        for page in generator:
            workon(page)
 
        [output, nquotes, npages] = generate_output(globalvar.quotes)
        if self.__output:
            try:
                outputpage = wikipedia.Page(site, self.__output)
                if outputpage.exists():
                    oldtext = outputpage.get()
                else:
                     oldtext = u''
 
                if oldtext != output:
                    output = output % time.strftime('%d/%m/%y / %H:00')
                    outputpage.put(output, comment = msg[globalvar.lang][9])
            except:
                error(u'Getting/Modifying page %s failed, generated output was:\n%s' % (outputpage, output))
        else:
            wikipedia.output(output)
 
        nquotespage = None
        narticlespage = None
        if self.__outputprefix: 
                if self.__outputquotes:
                        pname = self.__outputquotes
                else:
                        pname = "NUMBEROFQUOTES"
                nquotespage = wikipedia.Page(site, u'%s%s' % (self.__outputprefix, pname))
 
                if self.__outputarticles:
                        pname = self.__outputarticles
                else:
                        pname = "NUMBEROFARTICLES"
                narticlespage = wikipedia.Page(site, u'%s%s' % (self.__outputprefix, pname))
        else:
                if self.__outputquotes:
                        nquotespage = wikipedia.Page(site, u'%s' % self.__outputquotes)
                if self.__outputarticles:
                        narticlespage = wikipedia.Page(site, u'%s' % self.__outputarticles)
 
        if nquotespage:
            # April fool (replace %d by %s too)
            #nquotes = hex(nquotes)
            nquotespage.put("%d" % nquotes, comment = msg[globalvar.lang][9])
 
        if narticlespage:
            # Same as above
            #npages = hex(npages)
            narticlespage.put("%d" % npages, comment = msg[globalvar.lang][9])
 
 
globalvar = Global()
try:
    if __name__ == "__main__":
        Main().main()
finally:
    wikipedia.stopme()
	
# python fr.q.count-quotes.py -lang:fr -family:wikiquote