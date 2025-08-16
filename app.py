from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    courses = [
        {"title": "AWS Cloud & DevOps", "image": "aws.png", "desc": "Hands-on training on AWS services, CI/CD, and automation."},
        {"title": "Google Cloud & DevOps", "image": "gcp.png", "desc": "Learn GCP with Kubernetes, Terraform, and real projects."},
        {"title": "CI/CD & Containers", "image": "devops.png", "desc": "Master Jenkins, Docker, Kubernetes, and GitHub Actions."},
    ]
    return render_template("index.html", courses=courses)

if __name__ == "__main__":
    app.run(debug=True)

