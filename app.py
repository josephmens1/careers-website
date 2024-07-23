from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {"id": 1, "category": "IT", "title": "DevOps Engineer", "location": "Austin, TX", "salary": "$100,000 - $120,000"},
    
    {"id": 2, "category": "Cybersecurity", "title": "Cybersecurity Analyst", "location": "Washington, D.C."},
    
    {"id": 3, "category": "Networking", "title": "Network Engineer", "location": "Dallas, TX", "salary": "$85,000 - $100,000"},
    
    {"id": 4, "category": "AI/Machine Learning", "title": "Machine Learning Engineer", "location": "Palo Alto, CA", "salary": "$130,000 - $160,000"}
]

@app.route('/')
def landing_page():
    return render_template('home.html', jobs=JOBS, company_name='GoyardCareers')
    
@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)