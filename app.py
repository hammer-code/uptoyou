from flask import Flask, render_template,url_for,request, redirect
import re,json
app = Flask(__name__)
app.config.from_object('config');

@app.route('/')
def index():
   w_dict ={
            'terserah' ,
            'aku ga apa-apa',
            'gue jelek banget',
            'ga usah ga perlu',
            'lo berubah banget',
            'cie selamat ya',
            'oke, aku yang salah',
            'aku belum mau pacaran'
   }
   return render_template('depan.html', kode = w_dict)

@app.route('/say', methods=['GET', 'POST'])
def say():

   diction = [{
   		"kode": "terserah",
   		"subject": [{
   			"kata": "pengertian"
   		}, {
   			"kata": "makan"
   		}, {
   			"kata": "tempat"
   		}, {
   			"kata": "peka"
   		}],
         "predikat": [{
   			"kata": "kok kamu ga pengertian"
   		}, {
   			"kata": "aku ga mau makan disini"
   		}, {
   			"kata": "gue ga suka tempat ini"
   		}, {
   			"kata": "ga peka"
   		}]
   	},
   	{
   		"kode": "aku ga apa-apa",
   		"subject": [{
   			"kata": "sakit"
   		}, {
   			"kata": "jahat"
   		}, {
   			"kata": "hibur"
   		}, {
   			"kata": "minta"
   		}],
         "predikat": [{
   			"kata": "sakit banget rasanya"
   		}, {
   			"kata": "jahat banget"
   		}, {
   			"kata": "hibur aku dong"
   		}, {
   			"kata": "minta maaf kek"
   		}]
   	},
   	{
   		"kode": "gue jelek banget",
   		"subject": [{
   			"kata": "cantik"
   		}],
         "predikat": [{
   			"kata": "bilang dong gue cantik"
   		}]
   	},
   	{
   		"kode": "ga usah ga perlu",
   		"subject": [{
   			"kata": "bantu"
   		}, {
   			"kata": "cuek"
   		}, {
   			"kata": "perlu"
   		}, {
   			"kata": "peduli"
   		}],
         "predikat": [{
   			"kata": "bantuin kek"
   		}, {
   			"kata": "cuek banget"
   		}, {
   			"kata": "iya perlu lah"
   		}, {
   			"kata": "kamu gak peduli sama aku"
   		}]
   	},
   	{
   		"kode": "berubah banget",
   		"subject": [{
   			"kata": "kangen"
   		}],
         "predikat": [{
   			"kata": "kangen lo yang dulu"
   		}]
   	},
   	{
   		"kode": "selamat ya",
   		"subject": [{
   			"kata": "enak banget"
   		}],
         "predikat": [{
   			"kata": "enak banget lo, coba gue aja"
   		}]
   	},
   	{
   		"kode": "aku yang salah",
   		"subject": [{
   				"kata": "egois"
   			}, {
   				"kata": "salah"
   			}],
         "predikat": [{
   				"kata": "dasar egois"
   			}, {
   				"kata": "ini semua salahmu"
   			}]
   	},
   	{
   		"kode": "belum mau pacaran",
   		"subject": [{
   			"kata": "pengen punya pacar"
   		}],
         "predikat": [{
   			"kata": "aku pengen punya pacar, tapi bukan (yang kayak) kamu"
   		}]
   	}]

   rule =''

   if request.method == 'POST':
      g_code = request.form['g_code']
      g_say = request.form['g_say']
      count = 0
      n_count = 0
      for w_dict in diction:
         if w_dict['kode'] == g_code:

            for k_dict in w_dict['subject']:
               rule = r''+k_dict['kata']
               found = re.search(rule,g_say)
               if found:
                  count += 1
               else:
                  n_count += 1
         else:
            pass
   else:
      pass
      # return redirect(url_for(''))

   print count
   print n_count
   return render_template('say.html')

if __name__ == '__main__':
   app.run(debug = True)
