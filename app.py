
## Flask App Routing

from flask import Flask,render_template,request,redirect,url_for,jsonify

## create a simple flask application
app=Flask(__name__)     ### entry point of program

@app.route("/",methods=["GET"])
def welcome():
  return "<h1>welcome The blessing moon</h1>"

@app.route("/index",methods=["GET"])
def index():
  return "<h2>welcome The indexing page</h2>"

## variable rule
@app.route('/success/<int:score>')
def success(score):
  return "person has passed and score is: "+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
  return "person has failed and score is: "+ str(score)

@app.route('/form',methods=["GET","POST"])
def form():
  if request.method=="GET":
    return render_template('form.html')
  else:
    maths=float(request.form['Maths'])
    science=float(request.form['Science'])  
    history=float(request.form['History'])
    
    average_marks= (maths+science+history)/3
    res=""
    if average_marks>=50:
      res="success"
    else:
      res="fail"
      
    return redirect(url_for(res,score=average_marks))
      
    #return render_template('form.html',score=average_marks)
    
@app.route('/api', methods=['POST'])
def calculate_sum():
  data=request.get_json()
  a_val=float(dict(data)['a'])
  b_val=float(dict(data)['a'])
  return jsonify(a_val+b_val)



if __name__ == '__main__':
  app.run(debug=True)
