import new
from flask import Flask, render_template,redirect, url_for
from flask import request

app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/teams')
def teams():
    teamsdata = new.get_teams()
    teamsdata.sort(key=lambda x: x[0])
    return render_template('teams.html', teams=teamsdata)

@app.route('/members')
def members():
    memberdata = new.get_members()
    return render_template('members.html', members = memberdata)

@app.route('/mentorScoring')
def mentorScoring():
    mentorScoringdata = new.get_mentor_scoring()
    return render_template('mentorScoring.html', mentor_scores = mentorScoringdata)

@app.route('/judgeScoring')
def judge_scores_page():
    judge_score_data = new.get_judge_scoring()
    return render_template('judgesScoring.html', judge_scores = judge_score_data)

@app.route('/finalScores')
def final_scores_page():
    final_scores = new.get_final_scores()
    return render_template('finalScoresheet.html', final_scores = final_scores)

@app.route('/teamSubmission', methods=['GET', 'POST'])
def team_submissions_page():
    submissiondata = new.get_team_submission()
    return render_template('submissions.html', submissions = submissiondata)

@app.route('/extensions')
def extensions_page():
    ext = new.get_extensions()
    tab = new.get_tables()
    print(ext, tab)
    return render_template('extensions.html', extension_data = ext, table_data = tab)



@app.route('/add_member', methods=['POST'])
def add_member():
    data = request.get_json()

@app.route('/add_team', methods=['POST'])
def add_team():
    team_name=request.form['team_name']
    new.put_team(team_name)
    return redirect(url_for('teams'))
if __name__ == "__main__":
    app.run(debug=True)
