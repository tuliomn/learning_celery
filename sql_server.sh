#!/bin/bash

docker run --name sqlserver -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=P@ssw0rd!" -p 1433:1433 -d mcr.microsoft.com/mssql/server

