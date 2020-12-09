import sqlite3

"""
    try:
        con = sql.connect('database.db')
        cur = con.cursor()
        cur.execute("INSERT INTO profile (Name_id,name,email) \
             VALUES (1, 'Gabriel', 'gmail' )")
        con.commit()
        con.close()
    except:
        pass
"""

def checkSetup():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='profile'")
    result = cursor.fetchone()
    conn.close()
    if result is None:
        return False
    return True

def setup():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    create_perfil_table = """
        CREATE TABLE IF NOT EXISTS profile (
            "Name_id"  INT NOT NULL,
			"Name"	TEXT NOT NULL,
			"Email"	TEXT NOT NULL,
			PRIMARY KEY("Name_Id") 
        );
    """
    create_checklist_table = """
        CREATE TABLE IF NOT EXISTS checklist (
            "Id_checklist"	INTEGER PRIMARY KEY AUTOINCREMENT,
			"Name_checklist" TEXT NOT NULL,
			"Criado_por" TEXT NOT NULL,
            "Data_criada" TEXT NOT NULL,
			"Acao"	TEXT,
			"Responsavel_realizar"	TEXT,
            "Prazo"	TEXT,
            "Conformes" INT,
            "Nao_conformes" INT ,
            "Nao_aplicaveis" INT,
            "Total_resultado" FLOAT,
            "Descricao" TEXT,
			"Status" TEXT NOT NULL,
			FOREIGN KEY("ID_checklist") REFERENCES "profile"("Name_id")
        );
    """
    cursor.execute(create_perfil_table)
    cursor.execute(create_checklist_table)
    conn.commit()
    conn.close()

checkSetup()
setup()

def getConnection():
    return sqlite3.connect('database.db')
