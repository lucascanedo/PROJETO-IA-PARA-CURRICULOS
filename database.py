from tinydb import TinyDB

class AnalyseDatabase(TinyDB):
    def __init__(self, db_path='db.json')