from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from src.api.di.providers.db import uow_provider, DataBaseProvider


def setup_di(app: FastAPI, pool: async_sessionmaker[AsyncSession]) -> None:
    provider = DataBaseProvider(pool)
    app.dependency_overrides[uow_provider] = provider.provide_db
