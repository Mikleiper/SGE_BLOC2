# SGE_BLOC2
![alt text](<connect.py creat-1.jpg>)
S'ha creat l'arxiu connect.py per realitzar la connexió amb la base de dades
![alt text](<D:\Usuaris\Miguel\Documents\1\SEG\SGE_BLOC2\SGE_BLOC2\connect.py executat.jpg>)
S'està realitzant una connexió a una base de dades PostgreSQL a través d'una llibreria psycopg2. A dins del codi es pot veure com a través de la funció connection_db() s'estableix una connexió amb la base de dades the_bear utilitzant els paràmetres proporcionats. Es retorna l'objecte conn que representa la connexió a PostgreSQL. El print(conn) mostra com la connexió s'ha establert correctament (closed: 0) i com es tanca satisfàctoriament (closed: 1).

Per arribar fins aqui abans he tingut que posar en marxa PostgreSQL a traves de Docker, crear l'entorn virtual on funcioni Python 3.10, instal·lar les llibreries de  psycopg2 per connectar-se a PostgreSQL i poder carregar l'arxiu .csv amb el que treballarem i pandas per gestionar dades d'aquesta base de dades (com llegi, editar, etc.).