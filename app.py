from flask import Flask, render_template,url_for
app = Flask(__name__)
app.config.from_object('config');

@app.route('/')
def index():
   return render_template('depan.html')

@app.route('/say')
def say():
   w_dict = {
           'terserah' : (
               'kok kamu ga pengertian sih?',
               'aku ga mau makan disini',
               'gue ga suka tempat ini, ga peka banget sih',
               'ga peka'
           ),
           'aku ga apa-apa' : (
               'sakit banget rasanya',
               'jahat banget',
               'hibur aku dong',
               'minta maaf kek'
           ),
           'gue jelek banget sih' : (
               'bilang dong gue cantik',
           ),
           'ga usah ga perlu' : (
               'bantuin kek',
               'cuek banget',
               'iya perlu lah',
               'kamu gak peduli sama aku'
           ),
           'lo berubah banget' : (
               'kangen lo yang dulu'
           ),
           'iya aku tau aku yang salah' :(
               'egois banget jadi cowok'
           ),
           'cie selamat ya' : (
               'enak banget sih lo, coba gue aja'
           ),
           'oke, aku yang salah' : (
               'dasar cowok egois',
               'ini semua salahmu'
           ),
           'aku belum mau pacaran' : (
               'aku pengen punya pacar, tapi bukan (yang kayak) kamu'
           ),
   }
   return render_template('say.html')

if __name__ == '__main__':
   app.run(debug = True)
