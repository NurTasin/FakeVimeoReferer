from flask import Flask,request
from flask_cors import CORS,cross_origin
import requests as req

app=Flask(__name__)
cors=CORS(app)

@app.route('/video')
def VideoPlayback():
    referer=request.args.get('referer')
    vvid=request.args.get('vvid')
    res=req.get(f'https://player.vimeo.com/video/{vvid}',headers={
        'Referer': referer
    })
    return res.text


if __name__=="__main__":
    app.run('0.0.0.0','8080',True)
