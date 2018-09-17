from sys import argv

import bottle
from bottle import *

frettir = [["Hurricane florence","Mikil rigning fellibylsins Florence's og suðrænum stormþrýstihrúðum hófu að höggva ytri banka Norður-Karólínu fimmtudagsmorgunn og leiða leiðina til stormpakkninga 110 metra vinda. Flórens hefur veikst svolítið yfir 24 klukkustundir, en það hefur líka vaxið enn stærra - og það mun líklega dælna torrential rigning yfir Norður og Suður Karólína í gegnum mánudag.","florence_1.jpg","esr@frettir.is"],
           ["Hurricane florence orðinn að Category 2","WILMINGTON, NC - Ytri hljómsveitir vindur og rigningar frá veikburða en samt dauðans fellibylur Flórens byrjaði að losa Norður-Karólínu á fimmtudaginn þegar skrímsli stormurinn flutti inn í langan dvöl meðfram Suðausturströndinni og lofaði að drekka heimili eins manns og 10 milljónir manna með gríðarlegt magn af rigningu.","florence_1.gif","kys@frettir.is"],
           ["Af hverju er ég veikur?!?","stofu núm­er fjög­ur á ein­angr­un­ar­deild fyr­ir krabba­meins­sjúka á Karólínska sjúkra­hús­inu í Hudd­inge í Svíþjóð, í útjaðri Stokk­hólms, ligg­ur Hjört­ur Elías Ágústs­son, níu ára gam­all dreng­ur úr Árbæn­um. Síðan í fe­brú­ar hef­ur hann farið í marg­ar krefj­andi meðferðir við krabba­meini, bæði hér heima og er­lend­is, sem nú sér von­andi fyr­ir end­ann á.","reaper.jpg","smfh@frettir.is"]]

#bottle.debug(True)

@route('/')
def index():
       return """ 
        <a href="/a">Liður A</a>
        <a href="/b">Liður B</a>       
       """

@route('/a')
def index():
        return template("temp-A.tpl")

@route('/sida/<kt>')
def page(kt):
    return template("temp-kt.tpl", kt=kt)


@route('/b')
def about():
        return template("index.tpl")

@route('/frett/<id:int>')
def page(id):
    return template("frett.tpl", fyrirsogn = frettir[id][0], frett = frettir[id][1], mynd = frettir[id][2], hofundur = frettir[id][3])

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')


run(host='localhost', port=8800, debug = True, reloader=True)

#bottle.run(host='0.0.0.0', port=argv[1]) #Þetta þarf að vera í gangi til að heruko serverinn mun virka
