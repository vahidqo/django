forfiles -p "C:\Program Files\PostgreSQL\13\autobc" /D -7 /C "cmd /c del @path"
for /f "tokens=1-4 delims=/ " %%i in ("%date%") do (
     set dow=%%i
     set month=%%j
     set day=%%k
     set year=%%l
)
set datestr=%month%_%day%_%year%
set PGPASSWORD=vahid
pg_dump -h "localhost" -U "postgres" -f "C:\\Program Files\\PostgreSQL\\13\\autobc\\hr_backup_%datestr%" "PMWorks_II"