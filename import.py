import csv
import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session
from colorama import init, Fore, Back, Style
from dotenv import load_dotenv
load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    next(reader)
    
    for isbn, title, author, year in reader:
        try:
            query = text("INSERT INTO books (title, author, year, isbn) VALUES (:title, :author, :year, :isbn)")
            db.execute(query, {"title": title, "author": author, "year": year, "isbn": isbn})
            print(Fore.GREEN + "successful" + Style.RESET_ALL)
                 
        except Exception as e:
            print(Fore.RED + "Error" + Style.RESET_ALL)
    db.commit()
    
if __name__ == "__main__":
    main()