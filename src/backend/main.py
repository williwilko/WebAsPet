import argparse
from pathlib import Path

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='abc')
    parser.add_argument('-i', '--init', help='(Re-)Initialise the database', action='store_true')
    parser.add_argument('--db-path', help='Set path for SQLite database', type=str)
    args = parser.parse_args()

    if args.init and args.db_path:
        import db.__init__ as db_init
        db_path = (Path(__file__).parent / args.db).resolve()
        db = db_init.Init(db_path=db_path)
        db.initialise()
