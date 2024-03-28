#!/usr/bin/python3
"""New engine DBStorage"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """Classe DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """init DBStorage"""
        from models.base_model import Base

        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")
        url = "mysql+mysqldb://{}:{}@{}/{}".format(user, passwd, host, db)
        self.__engine = create_engine(url, pool_pre_ping=True)
        if env is not None and env == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """method must return a dictionary"""
        from models.user import User
        from models.state import State
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.city import City

        table = {
            "user": User,
            "state": State,
            "city": City,
            "amenity": Amenity,
            "place": Place,
            "review": Review
        }
        objs = {}
        if cls is None:
            for base_class in table.values():
                for row in self.__session.query(base_class).all():
                    objs[
                        "{}.{}".format(base_class.__name__, row.id)] = row
        else:
            for row in self.__session.query(cls):
                objs[
                        "{}.{}".format(cls.__name__, row.id)] = row
        return objs

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        from models.user import User
        from models.state import State
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.city import City
        from models.base_model import Base

        Base.metadata.create_all(self.__engine)
        session_f = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_f)
        self.__session = Session()

    def close(self):
        """Close the session"""
        self.__session.close()
