from typing import List
from pydantic import BaseModel
from enum import Enum


class PythonVersion(str, Enum):
    PYTHON_314 = "3.14"
    PYTHON_313 = "3.13"
    PYTHON_312 = "3.12"
    PYTHON_311 = "3.11"
    PYTHON_310 = "3.10"

class Framework(str, Enum):
    DJANGO = "django"
    FASTAPI = "fastapi"
    FLASK = "flask"

class Database(str, Enum):
    NONE = "none"
    POSTGRES = "postgres"
    MYSQL = "mysql"

class DockerConfig(BaseModel):
    python_version: PythonVersion = PythonVersion.PYTHON_314
    framework: Framework = Framework.DJANGO
    database: Database = Database.NONE
    use_redis: bool = False
    use_celery: bool = False
    collect_static: bool = False
    app_name: str = "app"

    @property
    def requirements(self) -> List[str]:
        requirements = []

        if self.framework == Framework.DJANGO:
            requirements.extend(["Django>=4.2", "gunicorn"])
        elif self.framework == Framework.FASTAPI:
            requirements.extend(["fastapi", "gunicorn", "uvicorn[standard]"])
        elif self.framework == Framework.FLASK:
            requirements.extend(["Flask", "gunicorn"])

        if self.database == Database.POSTGRES:
            requirements.append("psycopg2-binary")
        elif self.database == Database.MYSQL:
            requirements.append("mysqlclient")

        if self.use_redis:
            requirements.append("redis")

        if self.use_celery:
            requirements.extend(["celery", "redis"] if "redis" not in requirements else ['celery'])

        return requirements