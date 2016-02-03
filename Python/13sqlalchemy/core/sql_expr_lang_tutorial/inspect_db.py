from collections import OrderedDict

from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column
from sqlalchemy import String, Integer, ForeignKey, ForeignKeyConstraint, Index

import numpy as np
import pandas as pd


engine = create_engine('sqlite:///test.db', echo=True)
conn = engine.connect()

metadata = MetaData()
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, unique=True),
    Column('fullname', String, index=True),
    Column('company_id', None),
    Column('company_id2', None),
    Index('idx_my_index', 'name', 'fullname'),
    ForeignKeyConstraint(['company_id', 'company_id2'], ['companies.id', 'companies.id2'])
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
    Column('title', String, nullable=False),
    Column('name', String),
    Index("idx_multi", "title", "name")
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

#for table in meta.tables.values():
#    print("Table {}:".format(table))
#    #print("\tforeign keys: {}".format(
#    #    ' '.join([x.target_fullname for x in table.foreign_keys])
#    #))
#    print(table.foreign_keys)
#    print(table.indexes)
#    print("\tcolumns:")
#    for col in table.columns:
#        indexes = []
#        line = "\t\t{}".format(col.name)
#        if col.primary_key:
#            line += "  (primary-key)"
#        if col.foreign_keys:
#            line += "  (foreign-key: {})".format(
#                ' '.join([x.target_fullname for x in col.foreign_keys])
#            )
#        for id_ in table.indexes:
#            if col.key in id_.columns:
#                indexes.append(id_.name)
#        if indexes:
#            line += "  (indexes: {})".format(
#                ', '.join(indexes)
#            )
#        print(line)

def inspect_table(table):
    cols = []
    for col in table.columns:
        info = OrderedDict()
        info['table'] = table.name
        info['column'] = col.name
        line = "\t\t{}".format(col.name)

        if col.primary_key:
            info['primary_key'] = 'True'
            line += "  (primary-key)"
        else:
            info['primary_key'] = ''

        if col.foreign_keys:
            assert len(col.foreign_keys) < 2
            #fkeys = ' '.join([x.target_fullname for x in col.foreign_keys])
            fkey = list(col.foreign_keys)[0].target_fullname
            info['foreign_key'] = fkey
            line += "  (foreign-key: {})".format(fkey)
        else:
            info['foreign_key'] = ''

        indexes = []
        for id_ in table.indexes:
            if col.key in id_.columns:
                indexes.append(id_.name)
        if indexes:
            ids = ','.join(indexes)
            info['index'] = ids
            line += "  (index: {})".format(ids)
        else:
            info['index'] = ''

        cols.append(info)
        print(line)

    return cols

def inspect_db(meta):
    tables = []
    for table in meta.tables.values():
        print("\nTable {}:".format(table.name))
        print("\tcolumns:")

        cols = inspect_table(table)
        cols_df = pd.DataFrame(cols, columns=cols[0].keys())
        tables.append(cols_df)

    res = pd.concat(tables)
    res = res.set_index(['table', 'column'])
    return res

def main():
    df = inspect_db(meta)
    #print(df)

if __name__ == '__main__':
    main()
