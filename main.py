from core.base.run import run
from core.base.parse_config import case, table, arg_dict
from core.base.db import DB

if __name__ == '__main__':
    DB.create_table(table=table, arg_dict=arg_dict)
    run(case)
    DB.commit()
