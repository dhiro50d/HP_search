from flask import Flask, render_template, request, jsonify
# from belongs import GROUP_MEMBER_DICTS
from eye_catch.links import MOVIE_LINK_DICT

MM_MEMBERS = [
    "石田亜佑美",
    "生田衣梨奈",
    "小田さくら",
    "野中美希",
    "牧野真莉愛",
    "横山玲奈",
    "羽賀朱音",
    "北川莉央",
    "岡村ほまれ",
    "山﨑愛生",
    "櫻井梨央",
    "井上春華",
    "弓桁朱琴",
]

AG_MEMBERS = [
    "川村文乃",
    "上國料萌衣",
    "佐々木莉佳子",
    "川名凜",
    "伊勢鈴蘭",
    "為永幸音",
    "橋迫鈴",
    "平山遊季",
    "下井谷幸穂",
    "松本わかな",
    "後藤花",
]

JJ_MEMBERS = [
    "植村あかり",
    "段原瑠々",
    "井上玲音",
    "有澤一華",
    "石山咲良",
    "工藤由愛",
    "松永里愛",
    "入江里咲",
    "江端妃咲",
    "川嶋美楓",
    "遠藤彩加里",
]

TF_MEMBERS = [
    "新沼希空",
    "谷本安美",
    "小野瑞歩",
    "小野田紗栞",
    "秋山眞緒",
    "河西結心",
    "八木栞",
    "福田真琳",
    "豫風瑠乃",
    "石井泉羽",
    "村田結生",
    "土居楓奏",
]

BY_MEMBERS = [
    "一岡伶奈",
    "島倉りか",
    "西田汐里",
    "江口紗耶",
    "高瀬くるみ",
    "前田こころ",
    "山﨑夢羽",
    "岡村美波",
    "清野桃姫",
    "平井美葉",
    "小林萌花",
    "里吉うたの"
]

OC_MEMBERS = {
    "斉藤円香",
    "広本瑠璃",
    "石栗奏美",
    "米村姫良々",
    "窪田七海",
    "田代すみれ",
    "中山夏月姫",
    "西﨑美空",
    "北原もも",
    "筒井澪心",
}


GROUP_MEMBER_DICTS = {
    "モーニング娘。": MM_MEMBERS,
    "アンジュルム": AG_MEMBERS,
    "Juice=Juice": JJ_MEMBERS,
    "つばきファクトリー": TF_MEMBERS,
    "BEYOOOOONDS": BY_MEMBERS,
    "OCHA NORMA": OC_MEMBERS,
}

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
