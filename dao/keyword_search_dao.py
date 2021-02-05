from repositories import repository
from models import keyword_search

class KeywordSearchDao():

    def __init__(self):
        self.__repository = repository.Repository()

    def select_keyword_search(self):
        # defino las sentencia sql
<<<<<<< HEAD
        sql_select = "SELECT id_keyword, descripcion FROM public.keyword_search where id_keyword BETWEEN 30 and 35"
=======
        sql_select = "SELECT id_keyword, descripcion FROM public.keyword_search"
>>>>>>> fa30c70650ebe2fb0444def33d8609392595f23a

        return self.__repository.select_keyword_search(sql_select)
