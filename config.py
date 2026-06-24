from typing import Self
import shutil
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import HttpUrl, BaseModel, DirectoryPath, FilePath
from enum import Enum

class Browser(str, Enum):
    FIREFOX = 'firefox'
    CHROME = 'chrome'

class TestUser(BaseModel):
    username: str
    password: str



class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf8',
        env_nested_delimiter='.'
    )
    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    test_user: TestUser
    allure_results_dir: DirectoryPath

    @classmethod
    def _reset_dir(cls, path: Path):
        if path.exists():
            shutil.rmtree(path)
        path.mkdir(parents=True, exist_ok=True)

    @classmethod
    def _initialize(cls) -> Self:

        allure_results_dir = DirectoryPath('./allure-results')
        cls._reset_dir(allure_results_dir)
        allure_results_dir.mkdir(exist_ok=True)
        return Settings(allure_results_dir=allure_results_dir)




settings = Settings._initialize()