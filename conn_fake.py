def get_connection():
    import os
    from dotenv import load_dotenv
    pghost: str = os.getenv("PGHOST", "localhost")
    pgport: int = int(os.getenv("PGPORT", "5432"))
    pgdatabase: str = os.getenv("PGDATABASE", "EdvinDataTest")
    pguser: str = os.getenv("PGUSER", "postgres")
    pgpassword: str = os.getenv("PGPASSWORD", "*******")
    url = f"postgresql://{pguser}:{pgpassword}@{pghost}:{pgport}/{pgdatabase}"
    return url 

# postgresql://postgres:******@localhost:5432/EdvinDataTest