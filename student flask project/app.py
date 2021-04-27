from flask import *
from DBM import addstud,selectAllstud,deletestud,selectstudById,updatestud
f=Flask(__name__)

@f.route('/')
def home():
    return render_template('home.html')#templates 

@f.route('/reg')
def register():    
    return render_template('register.html')

@f.route('/addstud',methods=['POST'])
def add_stud():    
    roll_no=request.form['roll_no']
    name=request.form['name']
    college=request.form['clg']
    email=request.form['email']
    age=request.form['age']
    gender=request.form['gender']
    t=(roll_no,name,college,email,age,gender)
    addstud(t)
    return redirect('/')

@f.route('/studlist')
def stud_list():
    sl=selectAllstud()
    return render_template('studlist.html',slist=sl)

@f.route('/deletestud')
def delete_stud():
    roll_no=request.args.get('roll_no')
    deletestud(roll_no)
    return redirect('/studlist')

@f.route('/editstud')
def edit_stud():
    roll_no=request.args.get('roll_no')
    stud=selectstudById(roll_no)
    return render_template('updatestud.html',s=stud)

@f.route('/updatestud',methods=['POST'])
def update_stud():    
    roll_no=request.form['roll_no']
    name=request.form['name']
    college=request.form['clg']
    email=request.form['email']
    age=request.form['age']
    gender=request.form['gender']
    t=(name,college,email,age,gender,roll_no)
    updatestud(t)
    return redirect('/studlist')


if __name__=='__main__':
    f.run(debug=True)
