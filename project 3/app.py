from flask import Flask, request, redirect, url_for,render_template
app = Flask(__name__)

user_names = ['kajal-jadhav-3074321a2','tejabandekar','sahil-patil-a74204215','himeshkoli']

@app.route('/')
def home_page():
    return "Welcome to HOME PAGE"

@app.route('/search')
def fun_1():
    return render_template('search.html')

@app.route('/search',methods=['POST'])
def fun_2():
    return "Welcome to the search page using POST Req"

@app.route('/search',methods=['GET','POST'])
def search_fun():
    if request.method=='POST':
        return "Welcome to the search page using POST Req"
    else:
        return render_template('search.html')

@app.route('/about')
def about_page():
    return "Hello Everyone!!   My Name is Juilee Kuthe. I want to thanks to Innomatics Reasearch Labs to giving such a good opportunity. "

@app.route('/add', methods=['GET','POST'])
def add_fun():
    a = request.form.get('var_1')
    b = request.form.get('var_2')
    return str(int(a) + int(b))

@app.route('/upper')
def Upper_case():
    a = request.args.get('a')
    return a.upper()

@app.route('/in/<user>')
def profile_page(user):
    if user in user_names:
        return f"Welcome {user}"
    else:
        return "Username Not Found"

#https://www.linkedin.com/in/kajal-jadhav-3074321a2/
#https://www.linkedin.com/in/tejabandekar/
#https://www.linkedin.com/in/sahil-patil-a74204215/
#https://www.linkedin.com/in/himeshkoli/



if __name__ == '__main__':
    app.run (debug=True)
