import argparse
from pathlib import Path
import logging

from models.pets import Pet
from models.users import User
from logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info('Program starting...')

    parser = argparse.ArgumentParser(description='abc')
    parser.add_argument('-i', '--init', help='(Re-)Initialise the database', action='store_true')
    parser.add_argument('--db-path', help='Set path for SQLite database', type=str)
    args = parser.parse_args()

    if args.db_path:
        db_path = (Path(__file__).parent / args.db_path).resolve()
    else:
        logger.critical('Exiting because no DB path was specified as start up parameter.')
        exit()


    if args.init and args.db_path:
        logger.info(f'Initialising new database at {args.db_path}...')
        import db.__init__ as db_init

        db = db_init.Init(db_path=db_path)
        db.initialise()
        logger.info('DB set up successfully, please rerun the program now.')
        exit()
    else:
        logger.info('Starting the program...')
        import db.controller as db_controller
        import service.petService as pet_service
        import service.userService as user_service

        db = db_controller.Database(db_path=db_path)
        petService = pet_service.PetService(db)
        userService = user_service.UserService(db)
        api = "" # TODO

        user = User(name='Wilko', password='abc')
        userService.addUser(user)

    logger.info('Exiting program.')