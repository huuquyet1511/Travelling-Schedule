import  json
from app import  app

def load_choose():
    with open('%s/data/choose.json' % app.root_path, encoding='utf-8') as f:
        return json.load(f)