from sqlalchemy import create_engine, text
import os
engine =create_engine(os.environ ['DB_CONNECTION_STRING']) 



def load_projects_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from myprojects"))
    projects =[]
    for row in result.all():
      projects.append(dict(row._mapping))
  return projects


def load_project_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"select * from myprojects where id = {id}"))
    rows = result.all()  
    return dict(rows[0]._mapping)


def add_messsage_to_db(mdata):
  with engine.connect() as conn:
    sql = text(
        f"INSERT INTO mymessages (full_name, email, message) VALUES (\'{mdata['full_name']}\', \'{mdata['email']}\', \'{mdata['message']}\')"
    )
    print(sql)
    conn.execute(sql)
    conn.commit()
