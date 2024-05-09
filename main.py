import orcl
from flask import Flask, render_template
from flask import request

app = Flask(__name__)
cursor = orcl.get_cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/teams')
def teams():
    return render_template('teams.html')

@app.route('/members')
def members():
    return render_template('members.html')

@app.route('/mentorScoring')
def mentorScoring():
    return render_template('mentorScoring.html')

@app.route('/judgeScoring')
def judge_scores_page():
    return render_template('judgesScoring.html')

@app.route('/finalScores')
def final_scores_page():
    return render_template('finalScoresheet.html')

@app.route('/teamSubmission', methods=['GET', 'POST'])
def team_submissions_page():
    # if request.method == 'POST':
    #     team_id = request.form['team_id']
    #     presentation = request.form['presentation']
    #     github_link = request.form['github_link']
    #     mentor_scores = request.form['mentor_scores']
        # Add submission logic here
        # For demonstration purposes, let's assume the data is added to the submissions list
        # submissions.append({'Team_Id': team_id, 'Presentation': presentation, 'Github_Link': github_link, 'Mentor_Scores': mentor_scores})
    return render_template('submissions.html')

@app.route('/extensions')
def extensions_page():
    return render_template('extensions.html')



@app.route('/add_member', methods=['POST'])
def add_member():
    data = request.get_json()

    # name = data.get('name')
    # age = data.get('age')
    # cursor.execute("INSERT INTO members (name, age) VALUES (:name, :age)", {'name': name, 'age': age})

    # cursor.commit()

    # return 'Member added successfully'

@app.route('/add_team', methods=['POST'])
def add_team():
    data = request.get_json()

    # name = data.get('name')
    # cursor.execute("INSERT INTO teams (name) VALUES (:name)", {'name': name})

    # cursor.commit()

    # return 'Team added successfully'

if __name__ == "__main__":
    app.run(debug=True)