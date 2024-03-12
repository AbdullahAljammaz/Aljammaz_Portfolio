from sqlalchemy import create_engine, text

engine = create_engine(
    "mysql+pymysql://admin:1234admin@database-1.c3ig0msk6wy8.eu-north-1.rds.amazonaws.com/project?charset=utf8mb4"
)

with engine.connect() as conn:
  result = conn.execute(text("select * from trial"))
  print(result.all())
#interaction betweeen  mysql and python 
