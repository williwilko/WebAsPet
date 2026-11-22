import argparse
from pathlib import Path
import logging

import uvicorn
from fastapi import FastAPI

from api.router import router
from models.pets import Pet
from models.users import User
from logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(
    title="WebAsPet API",
    description="Backend API for WebAsPet",
    version="1.0.0"
)

app.include_router(router)


if __name__ == '__main__':
    logger.info('Program starting...')

    parser = argparse.ArgumentParser(description='abc')
    parser.add_argument(
        '-i', '--init',
        help='(Re-)Initialise the database',
        action='store_true'
    )
    parser.add_argument(
        '--db-path',
        help='Set path for SQLite database',
        type=str
    )

    args = parser.parse_args()

    if not args.db_path:
        logger.critical('No DB path specified.')
        exit(1)

    db_path = (Path(__file__).parent / args.db_path).resolve()

    if args.init:
        logger.info(f'Initialising new database at {db_path}...')

        import db as db_init

        db = db_init.Init(db_path=db_path)
        db.initialise()

        logger.info('DB set up successfully.')
        exit(0)

    logger.info('Starting the program...')

    import db.controller as db_controller
    import service.petService as pet_service
    import service.userService as user_service

    db = db_controller.Database(db_path=db_path)

    petService = pet_service.PetService(db)
    userService = user_service.UserService(db)

    user = User(name='Wilko', password='abc')
    userService.addUser(user)

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000
    )

    logger.info('Exiting program.')