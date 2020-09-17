from flask import Flask,render_template,request,redirect,url_for
from flask import request
from werkzeug.utils import secure_filename
import os
import test
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/name',methods=['GET','POST'])
def get_name():
    if request.method=='POST':
        return 'zxh POST'
    else:
        return 'zxh GET'


@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method=='POST':
        f=request.files['file']
        basepath = os.path.dirname(__file__)
        upload_path=os.path.join('/tmp',secure_filename(f.filename))
        f.save(upload_path)
        sudoPassword = 'zxh991103'
        command = 'mv /tmp/'+secure_filename(f.filename)+'  /var/www/html/upload'
        str = os.system('echo %s|sudo -S %s' % (sudoPassword, command)) 
        return redirect(url_for('upload'))
    return render_template('upload.html')


def html(list1):
    list1.sort()
    s=""
    for i in list1:
        
        s=s+i
        s=s+"</a>"
        
    
    return s
    

@app.route('/delete',methods=['GET','POST'])
def delete():
   
    delname=['delname']
    dellist=test.list_dir('/var/www/html/upload')
    
    
    str1=html(dellist)
    dellist=str1.split('</a>')
    if request.method=='POST':
        
        nm=request.form['nm']
        print(type(nm),nm)
        sudoPassword = 'zxh991103'
        command = 'rm '+'  /var/www/html/upload/'+nm
        os.system('echo %s|sudo -S %s' % (sudoPassword, command))
        
        return redirect(url_for('delete'))
    
    return render_template('delete.html',content=dellist,labels=delname)

@app.route('/hw',methods=['GET','POST'])
def hw():
   
   
    if request.method=='POST':
        
        sid=request.form['id']
        score=request.form['score']
        num=request.form['num']
        print(sid,score)
        from test import changescore
        res=changescore(io="/home/ubuntu/ds/19aihw.xlsx",sid=int(sid),score=int(score),num=int(num))
        if res=="No this sid":
          return res
        return redirect(url_for('hw'))
    
    return render_template('hw.html')
    
    
@app.route('/ex',methods=['GET','POST'])
def ex():
   
   
    if request.method=='POST':
        
        sid=request.form['id']
        score=request.form['score']
        num=request.form['num']
        print(sid,score)
        from test import changescore
        res=changescore(io="/home/ubuntu/ds/19aiex.xlsx",sid=int(sid),score=int(score),num=int(num))
        if res=="No this sid":
          return res
        return redirect(url_for('ex'))
    
    return render_template('ex.html')


@app.route('/repo',methods=['GET','POST'])
def repo():
   
   
    if request.method=='POST':
        
        sid=request.form['id']
        score=request.form['score']
        num=request.form['num']
        print(sid,score)
        from test import changescore
        res=changescore(io="/home/ubuntu/ds/19airepo.xlsx",sid=int(sid),score=int(score),num=int(num))
        if res=="No this sid":
          return res
        return redirect(url_for('repo'))
    
    return render_template('repo.html')
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=9999)
    
