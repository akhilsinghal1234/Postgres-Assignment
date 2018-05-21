#!/bin/sh

rm -rf /opt/PostgreSQL-10/
rm -rf /pgdatabase/data

mkdir /opt/PostgreSQL-10/
./configure --prefix=/opt/PostgreSQL-10 --enable-debug

echo 'configured'
make clean
make -j 2
echo 'make complete'
make install -j 2
echo 'install complete'

mkdir /pgdatabase/data

chown -R postgres. /pgdatabase/data

echo 'export PATH=$PATH:/opt/PostgreSQL-10/bin' > /etc/profile.d/postgres.sh
su postgres
cd /opt/PostgreSQL-10/bin
./initdb -D /pgdatabase/data/ -U postgres -W
./pg_ctl -D /pgdatabase/data/ -l /pgdatabase/data/start.log start
./psql -p 5432

# \conninfo
# \dt
# \d
# run app.py to populate DB
# CREATE TABLE playground (    equip_id serial PRIMARY KEY,    type varchar (50) NOT NULL,    color varchar (25) NOT NULL,location varchar(25) check (location in ('north', 'south', 'west', 'east', 'northeast', 'southeast', 'southwest', 'northwest')),install_date date);
# INSERT INTO playground (type, color, location, install_date) VALUES ('slide', 'blue', 'south', '2014-04-28');
# INSERT INTO playground (type, color, location, install_date) VALUES ('swing', 'yellow', 'northwest', '2010-08-16');
