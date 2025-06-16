from fastapi import FastAPI
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from db import (
    setup_database,
    init_session_factory
)
import logging.config, yaml, logging, os

logger = logging.getLogger(__name__)



@asynccontextmanager
async def lifespan(app: FastAPI):
    env = os.getenv("ENV", "local")
    file_path = f"./env/.env.{env}"
    load_dotenv(dotenv_path=file_path)

    # Load logging config
    with open("logger.yaml", "r") as f:
        config = yaml.safe_load(f)
        logging.config.dictConfig(config)

    logger.info(f"🔒 App startup using env:{env}, file: {file_path}")
    try:
        engine = await setup_database()
        init_session_factory(engine)
    except Exception as e:
        logger.warning(f"failed to initilize database , error: {e}")
    yield

    logger.info("🔒 App shutdown.")
