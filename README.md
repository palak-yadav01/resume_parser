# 🧠 Automated Resume Parser

An intelligent web application that extracts and categorizes candidate information (like name, skills, and education) from resumes in PDF format using Python, spaCy, and PDFPlumber — and stores the data in a PostgreSQL database.

---

## 🔧 Technologies Used

- **Python 3**
- **Flask** – Web framework
- **spaCy** – NLP library for entity extraction
- **PDFPlumber** – PDF text extraction
- **PostgreSQL** – Relational database
- **HTML/Jinja2** – Template rendering

---

## 🚀 Features

- Upload resumes in **PDF format**
- Automatically extract:
  - Full Name
  - Email Address
  - Phone Number
  - Skills (using NLP)
  - Education Details
- Store candidate data into a **PostgreSQL database**
- Simple web interface with upload form
- Modular and extensible code structure

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/resume_parser.git
cd resume_parser
2. Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate         # Windows
# OR
source venv/bin/activate      # macOS/Linux
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
python -m spacy download en_core_web_sm
4. Configure Database
Ensure PostgreSQL is installed and running.

Create a new database (e.g., resumedb)

Update the config.py file with your DB credentials:

python
Copy
Edit
DATABASE = {
    'dbname': 'resumedb',
    'user': 'your_db_user',
    'password': 'your_db_password',
    'host': 'localhost',
    'port': 5432
}
5. Run the App
bash
Copy
Edit
python app.py
Visit http://127.0.0.1:5000 in your browser.

📁 Project Structure
bash
Copy
Edit
resume_parser/
│
├── app.py               # Main Flask app
├── config.py            # Database config
├── requirements.txt     # Python dependencies
├── parser/
│   └── resume_parser.py # Resume parsing logic (NLP)
├── models/
│   └── db.py            # PostgreSQL connection + insert logic
├── templates/
│   └── index.html       # Upload form (Jinja2 template)
🧠 Future Improvements
Support for DOCX file format

Admin dashboard to view stored candidates

Integration with job portals or HR systems

Resume quality scoring

🙋‍♀️ Author
Palak Yadav
Feel free to connect on GitHub or reach out for suggestions and collaborations!






git clone https://github.com/YOUR_USERNAME/resume_parser.git
cd resume_parser
