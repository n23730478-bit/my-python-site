from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
  # Здесь данные, которые передаются на сайт
  title = "Мой первый сайт"
  items = [
      "Работает на Python и Flask",
      "Легко редактируется и настраивается",
      "Бесплатно опубликован в интернете",
  ]
  return render_template("index.html", title=title, items=items)


@app.route("/about")
def about():
  return "<h1>О проекте</h1><p>Это страница создана мной самостоятельно!</p>"


if __name__ == "__main__":
  app.run(debug=True)
