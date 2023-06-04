# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__, template_folder='')
app.debug = True
res_list = {}


@app.route('/', methods=['get', 'post'])
def results():
    client_msg = ''
    client_msg2 = ''
    server_msg = ''
    server_msg2 = ''
    if request.method == 'POST':
        client_msg = request.form.get('map')
        client_msg2 = request.form.get('time')

    if client_msg != '' and client_msg2 != '':
        res_list[client_msg] = client_msg2

    return render_template('results.html', map=server_msg, time=server_msg2, res=res_list)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5555)
