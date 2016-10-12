# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# streamondemand.- XBMC Plugin
# Canale steinsgate
# http://blog.tvalacarta.info/plugin-xbmc/streamondemand.
# ------------------------------------------------------------
import re

from core import config
from core import logger
from core import scrapertools
from core.item import Item

__channel__ = "personale"
__category__ = "A"
__type__ = "generic"
__title__ = "Personale"
__language__ = "IT"

DEBUG = config.get_setting("debug")


def isGeneric():
    return True


def mainlist(item):
    logger.info("[steinsgate.py] mainlist")

    itemlist = [Item(channel=__channel__,
                     title="[COLOR azure]" + Titolo + "[/COLOR]",
                     action="episodi",
                     thumbnail="http://vignette4.wikia.nocookie.net/voiceacting/images/6/6e/Steins%3BGate_Anime_Poster.jpg",
                     fanart="http://assistiranime.com.br/wp-content/uploads/2016/08/steins-gate-wallpaper-38-1920_1200.jpg"),
                Item(channel=__channel__,
                     title="[COLOR azure]" + Titolo2 + "[/COLOR]",
                     action="oav",
                     thumbnail="https://openthesteinsgate.files.wordpress.com/2016/07/cover-2-0-02-fuka-ryouiki-no-deja-vu.png",
                     fanart="http://vignette1.wikia.nocookie.net/steins-gate/images/d/df/Steins_Gate_-_06_-_Large_16.jpg"),
                Item(channel=__channel__,
                     title="[COLOR azure]" + Titolo3 + "[/COLOR]",
                     action="speciali",
                     thumbnail="https://openthesteinsgate.files.wordpress.com/2016/07/cover-2-0-03-soumei-eichi-no-cognitive-computing.png",
                     fanart="https://leviatanimenews.files.wordpress.com/2014/10/steins-ibm1.jpg"),
                Item(channel=__channel__,
                     title="[COLOR azure]" + Titolo4 + "[/COLOR]",
                     action="cd",
                     thumbnail="http://vignette2.wikia.nocookie.net/steins-gate/images/3/30/61NSYs7ElaL._SL500_SS500_.jpg",
                     fanart="https://i.ytimg.com/vi/PM3XdXA0zRE/maxresdefault.jpg"),
                Item(channel=__channel__,
                     title="[COLOR azure]" + Titolo5 + "[/COLOR]",
                     action="cduno",
                     thumbnail="https://images-fe.ssl-images-amazon.com/images/I/61v1h%2BJsCLL._SS500.jpg",
                     fanart="https://i.ytimg.com/vi/ZCFpE5WOpIo/maxresdefault.jpg"),
                Item(channel=__channel__,
                     title="[COLOR azure]" + Titolo6 + "[/COLOR]",
                     action="cddue",
                     thumbnail="https://openthesteinsgate.files.wordpress.com/2016/07/cover-2-0-06-reimei-no-lyra.png",
                     fanart="https://i.ytimg.com/vi/S11NYLwsGOg/maxresdefault.jpg")]

    return itemlist


def episodi(item):
    logger.info("steinsgate.py episodi")

    itemlist = []
    for scrapedtitle, scrapedurl in elenco_episodi:
        scrapedtitle = scrapertools.decodeHtmlentities(scrapedtitle)
        itemlist.append(
            Item(channel=__channel__,
                 action="findvideos",
                 title=scrapedtitle,
                 thumbnail=item.thumbnail,
                 url=scrapedurl,
                 fanart="http://assistiranime.com.br/wp-content/uploads/2016/08/steins-gate-wallpaper-38-1920_1200.jpg"))

    return itemlist


def oav(item):
    logger.info("steinsgate.py episodi")

    itemlist = []
    for scrapedtitle, scrapedurl in elenco_oav:
        scrapedtitle = scrapertools.decodeHtmlentities(scrapedtitle)
        itemlist.append(
            Item(channel=__channel__,
                 action="findvideos",
                 title=scrapedtitle,
                 thumbnail=item.thumbnail,
                 url=scrapedurl,
                 fanart="http://vignette1.wikia.nocookie.net/steins-gate/images/d/df/Steins_Gate_-_06_-_Large_16.jpg"))

    return itemlist


def speciali(item):
    logger.info("steinsgate.py episodi")

    itemlist = []
    for scrapedtitle, scrapedurl in elenco_speciali:
        scrapedtitle = scrapertools.decodeHtmlentities(scrapedtitle)
        itemlist.append(
            Item(channel=__channel__,
                 action="findvideos",
                 title=scrapedtitle,
                 thumbnail=item.thumbnail,
                 url=scrapedurl,
                 fanart="https://leviatanimenews.files.wordpress.com/2014/10/steins-ibm1.jpg"))

    return itemlist


def cd(item):
    logger.info("steinsgate.py episodi")

    itemlist = []
    for scrapedtitle, scrapedurl in elenco_cd:
        scrapedtitle = scrapertools.decodeHtmlentities(scrapedtitle)
        itemlist.append(
            Item(channel=__channel__,
                 action="findvideos",
                 title=scrapedtitle,
                 thumbnail=item.thumbnail,
                 url=scrapedurl,
                 fanart="https://i.ytimg.com/vi/PM3XdXA0zRE/maxresdefault.jpg"))

    return itemlist


def cduno(item):
    logger.info("steinsgate.py episodi")

    itemlist = []
    for scrapedtitle, scrapedurl in elenco_cduno:
        scrapedtitle = scrapertools.decodeHtmlentities(scrapedtitle)
        itemlist.append(
            Item(channel=__channel__,
                 action="findvideos",
                 title=scrapedtitle,
                 thumbnail=item.thumbnail,
                 url=scrapedurl,
                 fanart="https://i.ytimg.com/vi/ZCFpE5WOpIo/maxresdefault.jpg"))

    return itemlist


def cddue(item):
    logger.info("steinsgate.py episodi")

    itemlist = []
    for scrapedtitle, scrapedurl in elenco_cddue:
        scrapedtitle = scrapertools.decodeHtmlentities(scrapedtitle)
        itemlist.append(
            Item(channel=__channel__,
                 action="findvideos",
                 title=scrapedtitle,
                 thumbnail=item.thumbnail,
                 url=scrapedurl,
                 fanart="https://i.ytimg.com/vi/S11NYLwsGOg/maxresdefault.jpg"))

    return itemlist


# =========================================================
# Configurazione
# =========================================================
Titolo = "Steins;Gate Serie"

elenco_episodi = [
    ["1x01 - Prologo dell'inizio e della fine", "https://www.youtube.com/watch?v=Vl1BSZ2CTU0"],
    ["1x02 - Paranoia da spostamenti temporali", "https://www.youtube.com/watch?v=Uk4ahc7g_R4"],
    ["1x03 - Paranoia da realtà parallele", "https://www.youtube.com/watch?v=yFL4WC0doAo"],
    ["1x04 - Rendez-vous di collisioni di impossibili teorie erranti ", "https://www.youtube.com/watch?v=aiNrM2t_rxo"],
    ["1x05 - Rendez-vous di collisioni tra cariche elettriche", "https://www.youtube.com/watch?v=P2HmYQdOFiY"],
    ["1x06 - Divergenza dell'effetto farfalla", "https://www.youtube.com/watch?v=qz2Hr6Nm5LQ"],
    ["1x07 - Divergenza della frattura", "https://www.youtube.com/watch?v=s6vpac4HBiw"],
    ["1x08 - Omeostasi di una fantasia", "https://www.youtube.com/watch?v=mNvHdP9uq-A"],
    ["1x09 - Omeostasi di un'illusione", "https://www.youtube.com/watch?v=P76pLEc14xU"],
    ["1x10 - Omeostasi di una vita insieme", "https://www.youtube.com/watch?v=SeWmsqhYLI8"],
    ["1x11 - Dogma della frontiera spazio-tempo", "https://www.youtube.com/watch?v=z12yxP07A1A"],
    ["1x12 - Dogma del limite statico ", "https://www.youtube.com/watch?v=dWpgvWSOYT4"],
    ["1x13 - Necrosi metafisica", "https://openload.co/f/J9g9-UsSzz4/SG13.mkv.mp4"],
    ["1x14 - Necrosi fisica", "https://www.youtube.com/watch?v=5xCLrBzp3r8"],
    ["1x15 - Necrosi di un anello morente", "https://www.youtube.com/watch?v=xJXJkLoqBvA"],
    ["1x16 - Necrosi dell'irreversibilità", "https://www.youtube.com/watch?v=3RweH6TX640"],
    ["1x17 - Complesso di un'immagine virtuale distorta", "https://www.youtube.com/watch?v=6S4cWGTXWM0"],
    ["1x18 - Androginia auto-similare", "https://www.youtube.com/watch?v=kmZM7nEGj6c"],
    ["1x19 - Apoptosi di una catena infinita", "https://www.youtube.com/watch?v=pdHWy6JqKzY"],
    ["1x20 - Apoptosi del grido di rancore", "https://www.youtube.com/watch?v=YDctfQsyFnI"],
    ["1x21 - Meltdown del principio di casualità", "https://www.youtube.com/watch?v=AHQSZZgt8Xw"],
    ["1x22 - Meltdown dell'esistenza", "https://www.youtube.com/watch?v=q_JadtjyV0k"],
    ["1x23 - Lo Steins Gate di frontiera", "https://www.youtube.com/watch?v=FVz5WgJ3BVM"],
    ["1x24 - Prologo della fine e dell'inizio", "https://www.youtube.com/watch?v=o7fiqFuZXyI"],
    ["1x25 - Poriomania egoistica", "https://www.youtube.com/watch?v=pGSb_8Mwqz0"],
    ["Episodio 23b Alternativo - Dividi per Zero", "https://www.youtube.com/watch?v=GQDTE4QnH2E"]
]

Titolo2 = "Steins;Gate il Film"

elenco_oav = [
    ["Steins;Gate: Fuka Ryouiki no Déjà vu [Sub ITA]", "https://www.youtube.com/watch?v=zKjzzLiMInY"]
]

Titolo3 = "Steins;Gate Speciali: Soumei Eichi no Cognitive Computing"

elenco_speciali = [
    ["1x01 - Diario di Cucina [Sub ITA]", "https://www.youtube.com/watch?v=QP4OHEiJ8OY"],
    ["1x02 - Diario di Navigazione [Sub ITA]", "https://www.youtube.com/watch?v=L8-2IUwAzOo"],
    ["1x03 - Note sulla Moda [Sub ITA]", "https://www.youtube.com/watch?v=Rt7yjQ-8y1s"],
    ["1x04 - Verbale della riunione [Sub ITA]", "https://www.youtube.com/watch?v=Rt7yjQ-8y1s"]
]

Titolo4 = "Steins;Gate Drama CD y: Hyde of the Dark Dimension"

elenco_cd = [
    ["1x01 - Giorno 1 (Ore 17:04) [Sub ITA]", "https://www.youtube.com/watch?v=AVeZ1coBoKU"],
    ["1x02 - Giorno 1 (Ore 17.26) [Sub ITA]", "https://www.youtube.com/watch?v=wY3BxLQglds"],
    ["1x03 - Giorno 1 (Ore 18.13) [Sub ITA]", "https://www.youtube.com/watch?v=jm0eH1_gMz4"],
    ["1x04 - Giorno 1 (Ore 18.48) [Sub ITA]", "https://www.youtube.com/watch?v=DjlYhLAEIQs"],
    ["1x05 - Giorno 2 (Ore 12.02) [Sub ITA]", "https://www.youtube.com/watch?v=2KBrIurr4fQ"],
    ["1x06 - Giorno 2 (Ore 13.51) [Sub ITA]", "https://www.youtube.com/watch?v=xGDTehOYsu8"],
    ["1x07 - Giorno 2 (Ore 16.32) [Sub ITA]", "https://www.youtube.com/watch?v=PM3XdXA0zRE"],
    ["1x08 - Giorno 2 (Ore 17.05) [Sub ITA]", "https://www.youtube.com/watch?v=jfsj-5VFvJc"]
]

Titolo5 = "Steins;Gate Drama CD: Aion Hichou no Amadeus"

elenco_cduno = [
    ["Il silenzioso Requiem di Amadeus [Sub ITA]", "www.youtube.com/embed/XKCKNZOVmPQ"]
]

Titolo6 = "Steins;Gate Drama CD: Reimei no Lyra"

elenco_cddue = [
    ["Lyra dell'Alba [Sub ITA]", "https://www.youtube.com/embed/kcKG4ytaNRU"]
]