from apiflask import APIFlask, Schema, fields
from datetime import datetime

app = APIFlask(__name__, title="Logger API", version="1.0")

class LogInput(Schema):
    tag = fields.String(required=True)
    message = fields.String(required=True)


def get_item(data, key:str):
    return f'\'{data[key]}\'' if data is not None else f'\'{key}\''

@app.get('/health')
def health_check():
    return {'status': 'ok'}

@app.post('/log')
@app.input(LogInput)
def log(json_data):
    iso_now = datetime.now().isoformat()
    print(f'INSER INTO dm_logs (tag, time, message) values ({get_item(json_data, "tag")}, {get_item(None, str(iso_now))}, {get_item(json_data, "message")})')
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)