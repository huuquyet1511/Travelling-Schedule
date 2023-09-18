from flask import render_template
from app import app
from app import dao

@app.route('/')
def index():
    choose = dao.load_choose()
    return render_template('index.html', choose = choose)

if __name__ == '__main__':
    app.run(debug=True)
