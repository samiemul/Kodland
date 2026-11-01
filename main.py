import random
from flask import Flask

app = Flask(__name__)

facts = ["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
         "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
         "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.","2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.",
         "Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır.",
         "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
         "Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor.",
         "Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız."]

word_list = {"CRINGE" : "garip yada utandirici olan bir sey icin bir sifat",
             "LOL" : "komik yada sacma bir seye verilen bir cevap",
             "AGGRO":"agresiflesmek/sinirlenmek"}

@app.route("/")
def main():
    return f'<h1>Merhaba bu sitede rastgele bir fact alabilirsin!</h1><a href="/random-fact">Rastgele bir gerçeği görüntüle!</a>'
    
@app.route("/random-fact")
def print_facts():
    return f'<p>{random.choice(facts)}</p>'

@app.route("/login")
def login():
    return '<h1>Login sayfasi</h1>giris yapmak icin kullanici adi ve sifre giriniz'#

@app.route("/dictionary")
def dictionary():
    return '<h1>Ben akilli bir kelime sözlügyüm,bana 3 farkli kelimenin anlamini sora bilirsin'
    return word_list
app.run(debug=True)