import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy import select
from sqlalchemy import and_, or_, not_
from sqlalchemy import text
from sqlalchemy import bindparam
from sqlalchemy import func, desc
from sqlalchemy import inspect



### 1. create engine (connecting)
print("\n### 1. create engine (connecting)")

# an engine can be viewed as a repository for database connections capable of 
# issuing SQL to the database
engine = create_engine('sqlite:///:memory:', echo=True)
# explicitly connecting
conn = engine.connect()

### 2. define and create table
print("\n### 2. define and create table")

metadata = MetaData()
users = Table('users', metadata,
    # for oracle, we need to add Sequence('user_id_seq') to auto-generate new 
    # primary key
    Column('id', Integer, primary_key=True),
    # for mysql, we need to specify a maximum length like String(20)
    Column('name', String),
    Column('fullname', String)
)
addresses = Table('addresses', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', None, ForeignKey('users.id')),
    Column('email_address', String, nullable=False)
)

# both are ok
#metadata.create_all(engine)
metadata.create_all(conn)


### 3. insert expr
print("\n### 3. insert expr")

ins = users.insert()
print("ins:", str(ins))
ins = users.insert().values(name='jack', fullname='Jack Jones')
print("ins with values:", str(ins))

# bound params will not show in str(ins)
print("params:", ins.compile().params)

### 4. executing
print("\n### 4. executing")

result = conn.execute(ins)

# pass params on execute
ins = users.insert()
conn.execute(ins, name='wendy', fullname='Wendy Williams')

# many inserts at once
i_result = conn.execute(addresses.insert(), [
    {'user_id': 1, 'email_address': 'jack@yahoo.com'},
    {'user_id': 1, 'email_address' : 'jack@msn.com'},
    {'user_id': 2, 'email_address' : 'wenddy@163.com'},
    {'user_id': 2, 'email_address' : 'wendy@aol.com'},
])

### 5. select
print("\n### 5. select")

s = select([users])
s_result = conn.execute(s)
for row in s_result:
    print(row)

# fetch one by one
s_result = conn.execute(s)
row = s_result.fetchone()
# different ways of indexing
print(row['id'], row['name'], row['fullname'])
print(row[0], row[1], row[2])
print(row[users.c.id], row[users.c.name], row[users.c.fullname])

# important: result sets which have pending rows should be explicitly closed
s_result.close()

# select column explicitly
s = select([users.c.name, users.c.fullname])

# select two tables without where clause
# equivalent to 'cartesian product' of the two table's columns
s = select([users, addresses])
s_result = conn.execute(s)

# with a proper where clause
s = select([users, addresses]).where(users.c.id == addresses.c.user_id)
s_result = conn.execute(s)
print(s_result.keys())
for row in s_result:
    print(row)

# the sql of the where clause
print("where clause:", str(users.c.id == addresses.c.user_id))

### 6. operator
print("\n### 6. operator")

print(users.c.id == addresses.c.user_id)
print(users.c.id == 10)
print(users.c.id == None)

# the result of the operator depends on the types of the operands
print(users.c.id + addresses.c.id)
print(users.c.name + users.c.fullname)
# and the dialect that is in use
print((users.c.name + users.c.fullname).
        compile(bind=create_engine('mysql+pymysql://')))

# new operatos can also be defined
print(users.c.name.op('shenmegui')('foo'))

### 7. conjunction
print("\n### 7. conjunction")

print(
    and_(
        # sql 'like'
        users.c.name.like('j%'),
        users.c.id == addresses.c.user_id,
        or_(
            addresses.c.email_address == 'jack@yahoo.com',
            addresses.c.email_address == 'wendy@aol.com',
        ),
        not_(users.c.id > 5)
    )
)

s = select([(users.c.fullname + ": " +
            # column alias using 'label()'
            addresses.c.email_address).label('title')]).\
        where(
            and_(
                users.c.id == addresses.c.user_id,
                # between()
                users.c.name.between('m', 'z'),
                or_(
                    addresses.c.email_address.like('%@aol.com'),
                    addresses.c.email_address.like('%@163.com'),
                )
            )
        )
s_result = conn.execute(s)
print("keys:", s_result.keys())
s_all = s_result.fetchall()
print("fetchall:", s_all)

# chaining multiple where() is equivalent to using and_()
# the following is equivalent to the above select
s = select([(users.c.fullname + ": " +
            # column alias using 'label()'
            addresses.c.email_address).label('title')]).\
        where(users.c.id == addresses.c.user_id).\
        where(users.c.name.between('m', 'z')).\
        where(
                or_(
                    addresses.c.email_address.like('%@aol.com'),
                    addresses.c.email_address.like('%@163.com'),
                )
        )
print(s)

### 8. textual sql
print("\n### 8. textual sql")

s = text(
        "SELECT users.fullname || ':: ' || addresses.email_address AS title "
        "FROM users, addresses "
        "WHERE users.id = addresses.user_id "
            "AND users.name BETWEEN :x AND :y "
            "AND (addresses.email_address LIKE :e1 "
                "OR addresses.email_address LIKE :e2)"
    )
s_result = conn.execute(s, x='m', y='z', e1='%@aol.com', e2='%163%')
print(s_result.fetchall())

# setting column types and binding params for text
s = text(
        "SELECT users.fullname || ':: ' || addresses.email_address AS title "
        "FROM users, addresses "
        "WHERE users.id = addresses.user_id "
            "AND users.name BETWEEN :x AND :y "
            "AND (addresses.email_address LIKE :e1 "
                "OR addresses.email_address LIKE :e2)"
    )
s1 = s.columns(title=String)
s2 = s1.bindparams(x='m', y='z', e1='%@aol.com', e2='%@msn.com')

# text and non-text can be mixed, this is NOT recommended
s = select([
        text("users.fullname || ', ' || addresses.email_address AS title")
     ]).\
         where(
             and_(
                 text("users.id = addresses.user_id"),
                 text("users.name BETWEEN 'm' AND 'z'"),
                 text(
                     "(addresses.email_address LIKE :x "
                     "OR addresses.email_address LIKE :y)")
             )
         ).select_from(text('users, addresses'))
print(conn.execute(s, x='%@aol.com', y='%@msn.com').fetchall())


### 9. alias
print("\n### 9. alias")

a1 = addresses.alias('alias_name')
# alias name can be omitted
a2 = addresses.alias()
s = select([users, a1, a2]).\
       where(and_(
           # use alias to join the same table two times
           users.c.id == a1.c.user_id,
           users.c.id == a2.c.user_id,
           a1.c.email_address == 'jack@msn.com',
           a2.c.email_address == 'jack@yahoo.com'
       ))
s_result = conn.execute(s)
print(s_result.keys())
print(s_result.fetchall())


### 10. join
print("\n### 10. join")

# with a foreign key, the common column can be automatically determined
print(users.join(addresses))

# general join using 'on' + 'condition'
print(users.join(addresses,
        addresses.c.email_address.like(users.c.name + '%')
    )
)

# use explicit FROM clause when joining tables
s = select([users.c.fullname]).select_from(
   users.join(addresses,
            addresses.c.email_address.like(users.c.name + '%'))
   )

### 11. bindparam, functions, order by, group by
print("\n### 11. bindparam, functions, order by, group by")

# literals can be specified dynamically, by using bindparam() explicitly when 
# constructing SQL
s = users.select(users.c.name == bindparam('username'))
print(s)
print(conn.execute(s, username='wendy').fetchall())

# types of the literals can also be specified when needed
# type_=String cannot be omitted here
s = users.select(users.c.name.like(bindparam('username', type_=String) + text("'%'")))
print(conn.execute(s, username='wendy').fetchall())


# funcs examples:
# use select_from to specify the table
print(select([func.count('*')]).select_from(users))

print(func.current_timestamp())
print(func.some_non_exist_function())


# order by, etc.
from sqlalchemy import func, desc
s = select([
        addresses.c.user_id,
        func.count(addresses.c.id).label('num_addresses')
    ]).\
    group_by(addresses.c.user_id).\
    order_by(desc("num_addresses"))
s_result = conn.execute(s)
print(s_result.keys())
print(s_result.fetchall())

s = select([users.c.name]).\
        where(addresses.c.email_address.
               contains(users.c.name)).\
        distinct()
s_result = conn.execute(s)
print(s_result.keys())
print(s_result.fetchall())

### 12. update and delete
print("\n### 12. update and delete")

s = users.update().\
        where(users.c.name == 'jack').\
        values(fullname='Jackson Li')
u_result = conn.execute(s)

# bound params can be used
s = users.update().\
            where(users.c.name == bindparam('oldname')).\
            values(name=bindparam('newname'))
u_result = conn.execute(s, [
    {'oldname':'jack', 'newname':'jim'},
    {'oldname':'wendy', 'newname':'mary'},
])

print(users.delete().where(users.c.name > 'm'))


### 13. inspector
print("\n### 13. inspector")

insp = inspect(engine)
print("tables:", insp.get_table_names())

meta = MetaData()
meta.reflect(engine)

for table in meta.tables.values():
    print("Table {}:".format(table))
    #print("\tforeign keys: {}".format(
    #    ' '.join([x.target_fullname for x in table.foreign_keys])
    #))
    print("\tcolumns:")
    for col in table.columns:
        line = "\t\t{}".format(col.name)
        if col.primary_key:
            line += "  (primary-key)"
        if col.foreign_keys:
            line += "  (foreign-key: {})".format(
                ' '.join([x.target_fullname for x in col.foreign_keys])
            )
        print(line)





