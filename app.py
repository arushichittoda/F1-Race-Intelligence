from flask import Flask, render_template

app = Flask(__name__)

DASHBOARD_URL = "https://public.tableau.com/views/Book1_17930463521270/Dashboard1?:showVizHome=no"
STORY_URL = "https://public.tableau.com/views/Book1_17930463521270/Story1?:showVizHome=no"


@app.route("/")
def home():
    return render_template(
        "index.html",
        dashboard_url=DASHBOARD_URL,
        story_url=STORY_URL
    )


if __name__ == "__main__":
    app.run(debug=True)