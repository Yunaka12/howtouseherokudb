from flask import Flask, render_template, request, jsonify
import psycopg2

app = Flask(__name__)


def manipulate_database():

    conn = psycopg2.connect("host= user= dbname=  port= password=")
    cur = conn.cursor()
    #データベースと接続

    cur.execute("CREATE TABLE test(content text);")
    #TESTという名前テーブルを作成を作成　content というtext型の項目を持つ。

    cur.execute("insert into test values('テスト投稿');")
    #データを挿入

    conn.commit()
    #コミットする

    cur.close()
    conn.close()
    #接続終了

@app.route("/")
 #appに対して / というURLに対応するアクションを登録
def render_html():
    manipulate_database()
    conn = psycopg2.connect("host= user= dbname=  port= password=")
    cur = conn.cursor()
    #データベースと接続

    cur.execute("SELECT * FROM test;")
    #TESTテーブルを選択

    data = cur.fetchall()
    #TESTテーブルのデータを全部取得

    cur.close()
    conn.close()
    #接続終了

    return render_template("index.html",database_data = data)



# デバッグ用
if __name__ == '__main__':
    app.debug = True
    app.run(port=8100)
