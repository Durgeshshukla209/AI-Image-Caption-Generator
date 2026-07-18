from flask import Flask, render_template, request
import os
from predict import generate_caption

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def home():

    caption = None
    image_path = None

    if request.method == "POST":

        image = request.files["image"]

        if image:

            path = os.path.join(app.config["UPLOAD_FOLDER"], image.filename)

            image.save(path)

            caption = generate_caption(path)

            image_path = "/" + path.replace("\\", "/")

    return render_template(
        "index.html",
        caption=caption,
        image=image_path
    )


if __name__ == "__main__":
    app.run(debug=True)