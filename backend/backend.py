from flask import Flask

app = Flask("nombre")

@app.route("/")
def blank():
	return "", 200

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=3000)