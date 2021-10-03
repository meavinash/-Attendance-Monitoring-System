from flask import Flask, render_template, Response, request, redirect, url_for
import sys
import Attendance

# app = Flask(__name__)

# @app.route('/', methods=['POST', 'GET'])
# def home():
#     print("heer", file=sys.stderr)
#     if request.method == "POST":
#         print("heer", file=sys.stderr)
#         return Attendance.main()

#     return render_template('model.html')

# if __name__ == '__main__':
#    app.run()



# from flask import Flask, render_template, Response, request, redirect, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('model.html')

@app.route("/forward/", methods=['POST'])
def move_forward():
    print("heer", file=sys.stderr)
    Attendance.main()
    return render_template('model.html')
    

if __name__ == '__main__':
   app.run()

    