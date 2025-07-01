from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/player-info")
def player_info():
    uid = request.args.get("uid")
    server = request.args.get("server", "ind")
    
    if not uid:
        return jsonify({"error": "❌ UID is required"}), 400

    try:
        url = f"https://grizlyeditor-ebon.vercel.app/player-info?uid={uid}&region={server}"
        r = requests.get(url, timeout=10)
        data = r.json()

        if 'nickname' in data:
            return jsonify({
                "uid": uid,
                "server": server,
                "key": "grizly",
                "name": data['nickname'],
                "level": data['account_level']
            })
        else:
            return jsonify({
                "uid": uid,
                "server": server,
                "key": "grizly",
                "error": "UID not found or private"
            })

    except Exception as e:
        return jsonify({
            "uid": uid,
            "server": server,
            "key": "grizly",
            "error": "API fetch error",
            "details": str(e)
        }), 500