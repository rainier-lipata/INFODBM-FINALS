import pyodbc

try:
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=LAPTOP-8DAICJ5U\\MSSQLSERVER2025;"
        "DATABASE=INFODBM_MentorMatchSystem;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )

    print("Connected!")

except Exception as e:
    print(e)