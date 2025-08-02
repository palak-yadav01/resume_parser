from flask import Flask, request, render_template
from parser.extract import extract_text_from_pdf
from parser.nlp_parser import extract_name, extract_skills, extract_education
from models.db import insert_candidate

app = Flask(__name__)

SKILLS = ["Python", "Java", "SQL", "Flask", "Django", "C++", "Machine Learning"]

@app.route('/', methods=['GET', 'POST'])
def upload_resume():
    if request.method == 'POST':
        file = request.files['resume']
        text = extract_text_from_pdf(file)
        name = extract_name(text)
        skills = extract_skills(text, SKILLS)
        education = extract_education(text)

        insert_candidate(name, skills, education)
        return f"Resume parsed and stored for: {name}"

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
