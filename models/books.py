from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import DBConnector


class Book(DBConnector.Base):
    """
    Database table *books* instance model. Initializes the table columns and creates relationships.
    """

    __tablename__ = "books"

    id_book = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(45), nullable=False)
    id_user = Column(Integer, ForeignKey("users.id_user"), nullable=False)
    description = Column(String(300), nullable=True)

    owner = relationship("User", back_populates="books")

    def __repr__(self):
        return f"Book({self.id_book}, {self.title}, {self.id_user}, {self.description})"

    def stringify(self):
        return self.__class__.__name__
