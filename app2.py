from flask import Flask,render_template
app = Flask("app")

@app.route("/top")
def mypage():
    return render_template(
        "index.html",
        title = "dear ANGERME",
        message="PayPay,Welcome tp BIGLOVE"
    )

app.run()