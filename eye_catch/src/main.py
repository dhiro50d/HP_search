from flask import Flask, render_template, request, jsonify
from belongs import GROUP_MEMBER_DICTS
from links import MOVIE_LINK_DICT

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        group_name = request.form['group']
        member_names = GROUP_MEMBER_DICTS.get(group_name, [])
        return jsonify(member_names)
    return render_template('index.html', groups=GROUP_MEMBER_DICTS)


@app.route('/result', methods=['POST'])
def search():
    member = request.form['member']
    videos = MOVIE_LINK_DICT[member]
    return render_template('result.html', member=member, videos=videos)


if __name__ == '__main__':
    app.run(debug=True)
