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
    load_dotenv()
    with open("logger.yaml", "r") as f:
        config = yaml.safe_load(f)
        logging.config.dictConfig(config)
    logger.info(f"Database URL : {os.getenv("DATABASE_URL")}")
    try:
        engine = await setup_database()
        init_session_factory(engine)
    except Exception as e:
        logger.warning(f"failed to initilize database , error: {e}")
    yield

    logger.info("🔒 App shutdown.")