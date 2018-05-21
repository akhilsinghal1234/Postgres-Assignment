# Postgres
Prevent DOS attacks by altering source code of postgreSQL

Modified entry points and print utilities to get time of execution of each query inside of postgre source code.
Added flag \maas or \m, to activate query rejection and de-activate it.
Creates a file in directory /pgdatabase/data to store all queries with their execution times.
