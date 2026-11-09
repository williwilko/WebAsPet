import argparse
from pathlib import Path

from models.pets import Pet
from models.users import User

# TODO: IMPLEMENT LOGGING

if __name__ == '__main__':
    print('Program starting...')
    parser = argparse.ArgumentParser(description='abc')
    parser.add_argument('-i', '--init', help='(Re-)Initialise the database', action='store_true')
    parser.add_argument('--db-path', help='Set path for SQLite database', type=str)
    args = parser.parse_args()

    if args.db_path:
        db_path = (Path(__file__).parent / args.db_path).resolve()
    else:
        print('please specify the database path')
        exit()


    if args.init and args.db_path:
        print('Initialising the database...')
        import db.__init__ as db_init

        print(f'Initialising database at {db_path}')
        db = db_init.Init(db_path=db_path)
        db.initialise()
        print('Initialisation complete!')
        print('Please rerun the program now')
        exit()
    else:
        print('Starting the program...')
        import db.controller as db_controller
        import service.petService as pet_service
        import service.userService as user_service

        db = db_controller.Database(db_path=db_path)
        petService = pet_service.PetService(db)
        userService = user_service.UserService(db)
        api = "" # TODO

        user = User(name='Wilko', password='abc')
        userService.addUser(user)