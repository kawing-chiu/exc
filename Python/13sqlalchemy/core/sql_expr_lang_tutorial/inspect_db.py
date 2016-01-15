from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column
from sqlalchemy import String, Integer, ForeignKey, Index


engine = create_engine('sqlite:///test.db', echo=True)
conn = engine.connect()

metadata = MetaData()
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, unique=True),
    Column('fullname', String, index=True),
    Index('idx_my_index', 'name', 'fullname')
)
addresses = Table('info', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', None, ForeignKey('users.id')),
    Column('company_id', None, ForeignKey('companies.id')),
    Column('email_address', String, nullable=False)
)
companies = Table('companies', metadata,
    Column('id', Integer, primary_key=True),
    Column('id2', Integer, primary_key=True),
    Column('title', String, nullable=False, index=True),
    Column('name', String, index=True),
)
metadata.create_all(conn)


conn.execute(addresses.insert(), [
    {'user_id': 1, 'company_id': 20, 'email_address': 'jack@yahoo.com'},
    {'user_id': 1, 'company_id': 30, 'email_address' : 'jack@msn.com'},
    {'user_id': 2, 'company_id': 30, 'email_address' : 'wenddy@163.com'},
    {'user_id': 2, 'company_id': 50, 'email_address' : 'wendy@aol.com'},
])


meta = MetaData()
meta.reflect(engine)

for table in meta.tables.values():
    print("Table {}:".format(table))
    #print("\tforeign keys: {}".format(
    #    ' '.join([x.target_fullname for x in table.foreign_keys])
    #))
    print(table.foreign_keys)
    print(table.indexes)
    print("\tcolumns:")
    for col in table.columns:
        indexes = []
        line = "\t\t{}".format(col.name)
        if col.primary_key:
            line += "  (primary-key)"
        if col.foreign_keys:
            line += "  (foreign-key: {})".format(
                ' '.join([x.target_fullname for x in col.foreign_keys])
            )
        for id_ in table.indexes:
            if col.key in id_.columns:
                indexes.append(id_.name)
        if indexes:
            line += "  (indexes: {})".format(
                ', '.join(indexes)
            )
        print(line)

