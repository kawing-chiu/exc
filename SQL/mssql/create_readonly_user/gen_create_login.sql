SET NOCOUNT ON;

DECLARE @user_name      SYSNAME,
        @login_name     SYSNAME,
        @password       VARCHAR(20);

SELECT @user_name = 'username',
       @login_name = 'username',
       @password = ''

-- 注意需要有view any definition才能列出databases
-- 要在master里面创建相应user才能让sqlalchemy获得正确的default schema
SELECT '
USE [master];

CREATE LOGIN ' + QUOTENAME(@login_name)
   + ' WITH PASSWORD=''' + @password + ''','
   + ' CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF;

CREATE USER ' + QUOTENAME(@user_name)
   + ' FOR LOGIN ' + QUOTENAME(@login_name) + '

GRANT VIEW ANY DEFINITION TO ' + QUOTENAME(@login_name) + '

GO
'

SELECT '
USE [model];

CREATE USER ' + QUOTENAME(@user_name)
   + ' FOR LOGIN ' + QUOTENAME(@login_name) + '

EXEC sp_addrolemember
  ''db_datareader'',
  ''' + @user_name + ''';
   
GO
'

SELECT '
USE ' + QUOTENAME(NAME) + ';

CREATE USER ' + QUOTENAME(@user_name)
   + ' FOR LOGIN ' + QUOTENAME(@login_name) + '

EXEC sp_addrolemember
  ''db_datareader'',
  ''' + @user_name + ''';

GO
'
FROM   sys.databases
-- 4为系统数据库个数
WHERE  database_id > 4
       AND state_desc = 'ONLINE' 

