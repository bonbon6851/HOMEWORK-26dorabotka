from src.dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self, filters):
        page = filters.get('page')

        return self.dao.get_all(page)

    def create(self, director_d):
        return self.dao.create(director_d)

    def update(self, director_d):
        self.dao.update(director_d)
        return self.dao
