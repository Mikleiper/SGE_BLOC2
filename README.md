# SGE_BLOC2

### **CONNEXIÓ A BASE DE DADES**

![connexió](connectpy executat.jpg)

S'està realitzant una connexió a una base de dades PostgreSQL a través d'una llibreria psycopg2. A dins del codi es pot veure com a través de la funció connection_db() s'estableix una connexió amb la base de dades the_bear utilitzant els paràmetres proporcionats. Es retorna l'objecte conn que representa la connexió a PostgreSQL. El print(conn) mostra com la connexió s'ha establert correctament (closed: 0) i com es tanca satisfàctoriament (closed: 1).

Per arribar fins aqui abans he tingut que posar en marxa PostgreSQL a traves de Docker, crear l'entorn virtual on funcioni Python 3.10, instal·lar les llibreries de  psycopg2 per connectar-se a PostgreSQL i poder carregar l'arxiu .csv amb el que treballarem i pandas per gestionar dades d'aquesta base de dades (com llegi, editar, etc.).

### **INSERCIÓ DEL REGISTRE A LA BASE DE DADES**

![create_table.jpg](create_table.jpg)

Després de descarregar les dades en format csv, passem a la part del procés per inserir aquestes dades 
a la nostra base de dades.

Com veiem a la imatge, al primer pas utilitzem l'arxiu create table per crear una taula 
sense cap registre encara i tot seguint el format de l'arxiu csv esmentat anteriorment. Més específicament, veiem com en aquest arxiu 
es defineix una funció amb nom _create_table_ que estableix una connexió amb la base de dades 
de PostgresSQL tot executant una consulta SQL per crear uan taula anomenada "clientes".

Després es guarden els canvis i es tanca la connexió i el cursor. aquest últim aclarir que és 
un objecte en psycopg2 que permet executar consultes SQL dins d'una connexió (conn), Així és la forma d'interactuar
amb la base de dades des de Python. En la imatge es pot veure com estableix la connexió (cursor = conn.cursor())
i executa la creació de la taula (cursor.execute(sql_clients)) 




