# Postgres
Prevent DOS attacks by altering source code of postgreSQL

Modified entry points and print utilities to get time of execution of each query inside of postgre source code.
Added flag \maas or \m, to activate query rejection and de-activate it.
Creates a file in directory /pgdatabase/data to store all queries with their execution times.

## Files modified:

`postgres-master/src/backend/parser/parser.c` - this file is the entry point of a query in Postgre. This calls multiple lexer functions to tokensize the query and process it further. We write the ray query in the file along with entry timestamp(t1).

`postgres-master/src/fe_utils/print.c` - this file is the exit point of queries in postgreSQL. We modified it to write the timestamp when the query processing is completed by psql server. Timestamp(t2) is written in front of the query coming from `parser.c`.

`postgres-master/src/bin/psql/command.c` - modified to accommodate custom flag(\m or \maas) to swtich to modified version or not. If this flag is used then only queries are rejected based on time of execution and interval.

Finally, if an expensive query comes again within a fixed interval of time, then it is rejected by `parser.c` file. To find time of execution, we just subtract timestamps t1 and t2.

All these calculations are carried out in entry point of query - `parser.c`. 

## To run 
Issue all the commands present in bash script or copy-paste then on terminal. Make sure the databse directory has owner rights.

## Populating database
To populate database in psql, use `app.py`. Install different modules required and change username and password according to the postgre DB owner. 

## Contributor

1. Akhil Singhal
3. Swapnil Sharma
