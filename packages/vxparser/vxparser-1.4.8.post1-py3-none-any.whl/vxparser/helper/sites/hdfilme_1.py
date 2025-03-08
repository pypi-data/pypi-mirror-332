# -*- coding: utf-8 -*-
# Python 3
# Always pay attention to the translations in the menu!
# HTML LangzeitCache hinzugef\xc3\x83\xc2\xbcgt
# showValue: 48 Stunden
# showEntries: 6 Stunden
# showEpisodes: 4 Stunden
 
from helper.requestHandler import cRequestHandler
from helper.tools import cParser

SITE_IDENTIFIER = 'hdfilme_1'
SITE_NAME = 'HD Filme'
SITE_ICON = 'hdfilme_1.png'

URL_MAIN = 'https://hdfilme.my'

URL_NEW = URL_MAIN + '/filme1/'
URL_KINO = URL_MAIN + '/kinofilme/'
URL_MOVIES = URL_MAIN
URL_SERIES = URL_MAIN + '/serien/'
URL_SEARCH = URL_MAIN + '/?story=%s&do=search&subaction=search'


def load(): # Menu structure of the site plugin
    logger.info('Load %s' % SITE_NAME)
    params = ParameterHandler()
    params.setParam('sUrl', URL_NEW)
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30500), SITE_IDENTIFIER, 'showEntries'), params) # New
    params.setParam('sUrl', URL_KINO)
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30501), SITE_IDENTIFIER, 'showEntries'), params) # Current films in the cinema
    params.setParam('sUrl', URL_MOVIES)
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30502), SITE_IDENTIFIER, 'showEntries'), params) # Movies
    params.setParam('sUrl', URL_SERIES)
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30511), SITE_IDENTIFIER, 'showEntries'), params) # Series
    params.setParam('Value', 'Jahres')
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30508), SITE_IDENTIFIER, 'showValue'), params) # Release Year
    params.setParam('Value', 'Genre')
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30506), SITE_IDENTIFIER, 'showValue'), params) # Genre
    params.setParam('Value', 'Land')
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30538), SITE_IDENTIFIER, 'showValue'), params) # Country
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30520), SITE_IDENTIFIER, 'showSearch')) # Search
    cGui().setEndOfDirectory()


def showValue():
    params = ParameterHandler()
    oRequest = cRequestHandler(URL_MAIN)
    if cConfig().getSetting('global_search_' + SITE_IDENTIFIER) == 'true':
        oRequest.cacheTime = 60 * 60 * 48 # HTML Cache Zeit 48 Stunden
    sHtmlContent = oRequest.request()
    pattern = '>{0}</a>(.*?)</ul>'.format(params.getValue('Value'))
    isMatch, sHtmlContainer = cParser.parseSingleResult(sHtmlContent, pattern)
    if not isMatch:
        pattern = '>{0}</(.*?)</ul>'.format(params.getValue('Value'))
        isMatch, sHtmlContainer = cParser.parseSingleResult(sHtmlContent, pattern)
    if isMatch:
        isMatch, aResult = cParser.parse(sHtmlContainer, 'href="([^"]+).*?>([^<]+)')
        if not isMatch:
            cGui().showInfo()
            return

    for sUrl, sName in aResult:
        if sUrl.startswith('/'):
            sUrl = URL_MAIN + sUrl
        params.setParam('sUrl', sUrl)
        cGui().addFolder(cGuiElement(sName, SITE_IDENTIFIER, 'showEntries'), params)
        cGui().setEndOfDirectory()


def showEntries(entryUrl=False, sGui=False, sSearchText=False):
    oGui = sGui if sGui else cGui()
    params = ParameterHandler()
    isTvshow = False
    if not entryUrl: entryUrl = params.getValue('sUrl')
    oRequest = cRequestHandler(entryUrl, ignoreErrors=(sGui is not False))
    if cConfig().getSetting('global_search_' + SITE_IDENTIFIER) == 'true':
        oRequest.cacheTime = 60 * 60 * 6 # HTML Cache Zeit 6 Stunden
    sHtmlContent = oRequest.request()
    pattern = 'class="item relative mt-3">.*?href="([^"]+).*?title="([^"]+).*?data-src="([^"]+)(.*?)</div></div>'
    isMatch, aResult = cParser().parse(sHtmlContent, pattern)
    if not isMatch:
        if not sGui: oGui.showInfo()
        return

    total = len(aResult)
    for sUrl, sName, sThumbnail, sDummy in aResult:
        if sSearchText and not cParser.search(sSearchText, sName):
            continue
        isYear, sYear = cParser.parseSingleResult(sDummy, 'mt-1"><span>([\d]+)</span>') # Release Jahr
        isDuration, sDuration = cParser.parseSingleResult(sDummy, '</i><span>([\d]+).*?</span>') # Laufzeit
        if int(sDuration) <= int('70'): # Wenn Laufzeit kleiner oder gleich 70min, dann ist es eine Serie.
            isTvshow = True
        else:
            isTvshow = False
        if 'South Park: The End Of Obesity' in sName:
            isTvshow = False
        isQuality, sQuality = cParser.parseSingleResult(sDummy, '">([^<]+)</span>') # Qualit\xc3\x83\xc2\xa4t
        sThumbnail = URL_MAIN + sThumbnail
        oGuiElement = cGuiElement(sName, SITE_IDENTIFIER, 'showSeasons' if isTvshow else 'showHosters')
        if isYear:
            oGuiElement.setYear(sYear)
        if isDuration:
            oGuiElement.addItemValue('duration', sDuration)
        if isQuality:
            oGuiElement.setQuality(sQuality)
        oGuiElement.setMediaType('tvshow' if isTvshow else 'movie')
        oGuiElement.setThumbnail(sThumbnail)
        params.setParam('entryUrl', sUrl)
        params.setParam('sThumbnail', sThumbnail)
        oGui.addFolder(oGuiElement, params, isTvshow, total)
        if not sGui:
            isMatchNextPage, sNextUrl = cParser().parseSingleResult(sHtmlContent, 'nav_ext">.*?next">.*?href="([^"]+)')
            if isMatchNextPage:
                params.setParam('sUrl', sNextUrl)
            oGui.addNextPage(SITE_IDENTIFIER, 'showEntries', params)
            oGui.setView('tvshows' if isTvshow else 'movies')
            oGui.setEndOfDirectory()


def showSeasons():
    params = ParameterHandler()
    # Parameter laden
    sUrl = params.getValue('entryUrl')
    sThumbnail = params.getValue('sThumbnail')
    oRequest = cRequestHandler(sUrl)
    if cConfig().getSetting('global_search_' + SITE_IDENTIFIER) == 'true':
        oRequest.cacheTime = 60 * 60 * 6 # HTML Cache Zeit 6 Stunden
    sHtmlContent = oRequest.request()
    pattern = 'class="su-accordion collapse show"(.*?)<br>'
    isMatch, sHtmlContainer = cParser.parseSingleResult(sHtmlContent, pattern)
    if isMatch:
        isMatch, aResult = cParser.parse(sHtmlContainer, '#se-ac-(\d+)')
    if not isMatch:
        cGui().showInfo()
        return
    total = len(aResult)
    for sSeason in aResult:
        oGuiElement = cGuiElement('Staffel ' + str(sSeason), SITE_IDENTIFIER, 'showEpisodes')
        oGuiElement.setSeason(sSeason)
        oGuiElement.setMediaType('season')
        oGuiElement.setThumbnail(sThumbnail)
        cGui().addFolder(oGuiElement, params, True, total)
        cGui().setView('seasons')
        cGui().setEndOfDirectory()


def showEpisodes():
    params = ParameterHandler()
    # Parameter laden
    entryUrl = params.getValue('entryUrl')
    sThumbnail = params.getValue('sThumbnail')
    sSeason = params.getValue('season')
    oRequest = cRequestHandler(entryUrl)
    if cConfig().getSetting('global_search_' + SITE_IDENTIFIER) == 'true':
        oRequest.cacheTime = 60 * 60 * 4 # HTML Cache Zeit 4 Stunden
    sHtmlContent = oRequest.request()
    pattern = '#se-ac-%s(.*?)<br/></div>' % sSeason
    isMatch, sHtmlContainer = cParser.parseSingleResult(sHtmlContent, pattern)
    if isMatch:
        isMatch, aResult = cParser.parse(sHtmlContainer, 'Episode\s(\d+)')
    if not isMatch:
        cGui().showInfo()
        return

    total = len(aResult)
    for sEpisode in aResult:
        oGuiElement = cGuiElement('Episode ' + str(sEpisode), SITE_IDENTIFIER, 'showEpisodeHosters')
        oGuiElement.setThumbnail(sThumbnail)
        oGuiElement.setMediaType('episode')
        params.setParam('entryUrl', entryUrl)
        params.setParam('season', sSeason)
        params.setParam('episode', sEpisode)
        cGui().addFolder(oGuiElement, params, False, total)
        cGui().setView('episodes')
        cGui().setEndOfDirectory()


def showEpisodeHosters():
    hosters = []
    params = ParameterHandler()
    # Parameter laden
    sUrl = params.getValue('entryUrl')
    sSeason = params.getValue('season')
    sEpisode = params.getValue('episode')
    sHtmlContent = cRequestHandler(sUrl).request()
    pattern = '#se-ac-%s(.*?)<br/></div>' % sSeason
    isMatch, sHtmlContainer = cParser.parseSingleResult(sHtmlContent, pattern)
    if isMatch:
        pattern = '>\Sx%s\sEpisode(.*?)<br/' % sEpisode
        isMatch, sHtmlLink = cParser.parseSingleResult(sHtmlContainer, pattern)
        if isMatch:
            isMatch, aResult = cParser().parse(sHtmlLink, 'href="([^"]+)')
            if isMatch:
            for sUrl in aResult:
                sName = cParser.urlparse(sUrl)
                if cConfig().isBlockedHoster(sName)[0]: continue # Hoster aus settings.xml oder deaktivierten Resolver ausschlie\xc3\x83\xc5\xb8en
                if 'youtube' in sUrl:
                    continue
                elif sUrl.startswith('//'):
                    sUrl = 'https:' + sUrl
                    hoster = {'link': sUrl, 'name': cParser.urlparse(sUrl)}
                    hosters.append(hoster)
    if hosters:
        hosters.append('getHosterUrl')
    return hosters


def showHosters():
    hosters = []
    params = ParameterHandler()
    sUrl = params.getValue('entryUrl')
    sHtmlContent = cRequestHandler(sUrl).request()
    pattern = '<iframe\sw.*?src="([^"]+)'
    isMatch, hUrl = cParser.parseSingleResult(sHtmlContent, pattern)
    if isMatch:
        sHtmlContainer = cRequestHandler(hUrl).request()
        isMatch, aResult = cParser().parse(sHtmlContainer, 'data-link="([^"]+)')
        if isMatch:
            for sUrl in aResult:
                sName = cParser.urlparse(sUrl)
                if cConfig().isBlockedHoster(sName)[0]: continue # Hoster aus settings.xml oder deaktivierten Resolver ausschlie\xc3\x83\xc5\xb8en
                if 'youtube' in sUrl:
                    continue
                elif sUrl.startswith('//'):
                    sUrl = 'https:' + sUrl
                    hoster = {'link': sUrl, 'name': cParser.urlparse(sUrl)}
                    hosters.append(hoster)
    if hosters:
        hosters.append('getHosterUrl')
    return hosters


def getHosterUrl(sUrl=False):
    return [{'streamUrl': sUrl, 'resolved': False}]


def showSearch():
    sSearchText = cGui().showKeyBoard()
    if not sSearchText: return
    _search(False, sSearchText)
    cGui().setEndOfDirectory()


def _search(oGui, sSearchText):
    showEntries(URL_SEARCH % cParser.quotePlus(sSearchText), oGui, sSearchText)

