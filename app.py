from flask import Flask, Response

app = Flask(__name__)

@app.route("/voice", methods=["GET", "POST"])
def voice():
    twiml = f"""
    <?xml version="1.0" encoding="UTF-8"?>
    <Response>
        <Play>https://github.com/priyanshu-dudi/OrderBuddy/releases/download/hiii/test1.mp3</Play>
    </Response>
    """
    return Response(twiml, mimetype='text/xml')

if __name__ == "__main__":
    app.run(debug=True)
