from flask import Flask, jsonify,request,redirect,url_for,render_template,flash
from flask_sqlalchemy import SQLAlchemy
import nltk
from nltk.tag import tnt
from nltk.corpus import indian
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
stop_words = set(stopwords.words('english')) 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

#Database to store the word (under username) and corresponding POS tag(under password)
class User(db.Model):
    id = db.Column('my_id',db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(8))
    
    def __repr__(self):
        return '<User %r>' % self.username

#Setting various flask routes.
@app.route('/')
def Introduction():
    return render_template('Introduction.html')

@app.route('/Objective')
def Objective():
    return render_template('Objective.html')

@app.route('/Feedback')
def Feedback():
    return render_template('Feedback.html')

@app.route('/Experiment')
def Experiment():
    return render_template('Experiment.html')

@app.route('/Experiment/pos-eng',methods= ['POST'])
def pos():
    #Takes an input text , tokenizes it using Python NLTK ---ie, breaks it into individual words, uses nltk tools to find out the POS tag of the word.
    text= request.form['sentence']
    tokenized = nltk.word_tokenize(text)
    output = nltk.pos_tag(tokenized)
    return jsonify({'output':output})


@app.route('/Experiment/pos-hin',methods= ['POST'])
def hindi_mode():
    #Takes input text in Hindi and tokenizes it using NLTK(Indian toolkit) and finds corresponding POS tag.
    train_data = indian.tagged_sents('hindi.pos')
    tnt_pos_tagger = tnt.TnT()
    tnt_pos_tagger.train(train_data)
    return tnt_pos_tagger
model = hindi_mode()
def hinpus():
    text= request.form['pankti']
    output = (model.tag(nltk.word_tokenize(text)))
    return jsonify({'output':output})

@app.route('/Experiment/validate',methods= ['POST'])
def valo():
    #Obtaining the user input in the Experiment.html page to verify the input POS tag with the corresponding answer , which is queried from the database.
    wor0= request.form['word0']
    wor1= request.form['word1']
    wor2= request.form['word2']
    wor3= request.form['word3']
    wor4= request.form['word4']
    wor5= request.form['word5']
    wor6= request.form['word6']
    wor7= request.form['word7']
    wor8= request.form['word8']
    wor9= request.form['word9']
    wor10= request.form['word10']
    wor11= request.form['word11']
    wor12= request.form['word12']
    wor13= request.form['word13']
    wor14= request.form['word14']
    wor15= request.form['word15']
    wor16= request.form['word16']
    wor17= request.form['word17']
    wor18= request.form['word18']
    wor19= request.form['word19']
    wor20= request.form['word20']
    wor21= request.form['word21']
    wor22= request.form['word22']
    pos0 = request.form['pos0']
    pos1 = request.form['pos1']
    pos2 = request.form['pos2']
    pos3 = request.form['pos3']
    pos4 = request.form['pos4']
    pos5 = request.form['pos5']
    pos6 = request.form['pos6']
    pos7 = request.form['pos7']
    pos8 = request.form['pos8']
    pos9 = request.form['pos9']
    pos10 = request.form['pos10']
    pos11 = request.form['pos11']
    pos12 = request.form['pos12']
    pos13 = request.form['pos13']
    pos14 = request.form['pos14']
    pos15 = request.form['pos15']
    pos16 = request.form['pos16']
    pos17 = request.form['pos17']
    pos18 = request.form['pos18']
    pos19 = request.form['pos19']
    pos20 = request.form['pos20']
    pos21 = request.form['pos21']
    pos22 = request.form['pos22']
    #Validation of the chosen answers.
    x = User.query.filter_by(username=wor0).first()
    k0 = x.password
    if( k0 == pos0):
       ans0 = "Correct"
    else :
       ans0 = "Incorrect"
    x = User.query.filter_by(username=wor1).first()
    k1 = x.password
    if( k1 == pos1):
       ans1 = "Correct"
    else :
       ans1 = "Incorrect"
      
    x = User.query.filter_by(username=wor2).first()
    k2 = x.password
    if( k2 == pos2):
       ans2 = "Correct"
    else :
       ans2 = "Incorrect"
    x = User.query.filter_by(username=wor3).first()
    k3 = x.password
    if( k3 == pos3):
       ans3 = "Correct"
    else :
       ans3 = "Incorrect"
    x = User.query.filter_by(username=wor4).first()
    k4 = x.password
    if( k4 == pos4):
       ans4 = "Correct"
    else :
       ans4 = "Incorrect"
    x = User.query.filter_by(username=wor5).first()
    k5 = x.password
    if( k5 == pos5):
       ans5 = "Correct"
    else :
       ans5 = "Incorrect"
    x = User.query.filter_by(username=wor6).first()
    k6 = x.password
    if( k6 == pos6):
       ans6 = "Correct"
    else :
       ans6 = "Incorrect"
    x = User.query.filter_by(username=wor7).first()
    k7 = x.password
    if( k7 == pos7):
       ans7 = "Correct"
    else :
       ans7 = "Incorrect"
    x = User.query.filter_by(username=wor8).first()
    k8 = x.password
    if( k8 == pos8):
       ans8 = "Correct"
    else :
       ans8 = "Incorrect"
    x = User.query.filter_by(username=wor9).first()
    k9 = x.password
    if( k9 == pos9):
       ans9 = "Correct"
    else :
       ans9 = "Incorrect"
    x = User.query.filter_by(username=wor10).first()
    k10 = x.password
    if( k10 == pos10):
       ans10 = "Correct"
    else :
       ans10 = "Incorrect"  
    x = User.query.filter_by(username=wor11).first()
    k11 = x.password
    if( k11 == pos11):
       ans11 = "Correct"
    else :
       ans11 = "Incorrect"  
    x = User.query.filter_by(username=wor12).first()
    k12 = x.password
    if( k12 == pos12):
       ans12 = "Correct"
    else :
       ans12 = "Incorrect"  
    x = User.query.filter_by(username=wor13).first()
    k13 = x.password
    if( k13 == pos13):
       ans13 = "Correct"
    else :
       ans13 = "Incorrect"  
    x = User.query.filter_by(username=wor14).first()
    k14 = x.password
    if( k14 == pos14):
       ans14 = "Correct"
    else :
       ans14 = "Incorrect"  
    x = User.query.filter_by(username=wor15).first()
    k15 = x.password
    if( k15 == pos15):
       ans15 = "Correct"
    else :
       ans15 = "Incorrect"  
    x = User.query.filter_by(username=wor16).first()
    k16 = x.password
    if( k16 == pos16):
       ans16 = "Correct"
    else :
       ans16 = "Incorrect"  
    x = User.query.filter_by(username=wor17).first()
    k17 = x.password
    if( k17 == pos17):
       ans17 = "Correct"
    else :
       ans17 = "Incorrect"  
    x = User.query.filter_by(username=wor18).first()
    k18 = x.password
    if( k18 == pos18):
       ans18 = "Correct"
    else :
       ans18 = "Incorrect"  
    x = User.query.filter_by(username=wor19).first()
    k19 = x.password
    if( k19 == pos19):
       ans19 = "Correct"
    else :
       ans19 = "Incorrect" 
    x = User.query.filter_by(username=wor20).first()
    k20 = x.password
    if( k20 == pos20):
       ans20 = "Correct"
    else :
       ans20 = "Incorrect"  
    x = User.query.filter_by(username=wor21).first()
    k21 = x.password
    if( k21 == pos21):
       ans21 = "Correct"
    else :
       ans21 = "Incorrect"   
    x = User.query.filter_by(username=wor22).first()
    k22 = x.password
    if( k22 == pos22):
       ans22 = "Correct"
    else :
       ans22 = "Incorrect"   
    return jsonify({'k0':k0,'k1':k1,'k2':k2,'k3':k3,'k4':k4,'k5':k5,'k6':k6,'k7':k7,'k8':k8,'k9':k9,'k10':k10,'k11':k11,'k12':k12,'k13':k13,'k14':k14,'k15':k15,'k16':k16,'k17':k17,'k18':k18,'k19':k19,'k20':k20,'k21':k21,'k22':k22,'ans0':ans0,'ans1':ans1,'ans2':ans2,'ans3':ans3,'ans4':ans4,'ans5':ans5,'ans6':ans6,'ans7':ans7,'ans8':ans8,'ans9':ans9,'ans10':ans10,'ans11':ans11,'ans12':ans12,'ans13':ans13,'ans14':ans14,'ans15':ans15,'ans16':ans16,'ans17':ans17,'ans18':ans18,'ans19':ans19,'ans20':ans20,'ans21':ans21,'ans22':ans22})

@app.route('/Theory')
def Theory():
    return render_template('Theory.html')

@app.route('/Quizzes')
def Quizzes():
    return render_template('Quizzes.html')

@app.route('/Quizzes/pos',methods= ['POST'])
def quizo():
    #Creating an interactive quiz...user inputs are queried in the database and answer is validated.
    wor= request.form['word']
    posh = request.form['postag']
    x = User.query.filter_by(username=wor).first()
    k = x.password
    if( k == posh):
       output = "Correct"
    else :
       output = "Incorrect"
    return jsonify({'output':output})

@app.route('/Quizzes/possol',methods= ['POST'])
def quizup():
    wor= request.form['word']
    x = User.query.filter_by(username=wor).first()
    k = x.password
    return jsonify({'solution':k})
    
@app.route('/Procedure')
def Procedure():
    return render_template('Procedure.html')

@app.route('/FurtherReadings')
def FurtherReadings():
    return render_template('FurtherReadings.html')

@app.route('/Listofexperiments')
def LoE():
   return render_template('Listofexperiments.html')

#Run on the given address.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
