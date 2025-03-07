import os
import argparse
from contextlib import closing
from dataclasses import dataclass, field

def get_arguments() -> dict:
    """Parse command-line arguments and return as a dictionary."""
    parser = argparse.ArgumentParser(description="MariaDB Configuration")
    parser.add_argument("--host", help="MariaDB host")
    parser.add_argument("--port", type=int, help="MariaDB port")  # type=int 추가
    parser.add_argument("--user", help="MariaDB user")
    parser.add_argument("--password", help="MariaDB password")
    parser.add_argument("--database", help="MariaDB database")
    args = parser.parse_args()

    return {k: v for k, v in vars(args).items() if v is not None}

@dataclass
class DBconfig:
    """Database configuration"""
    host: str = field(default_factory=lambda: os.getenv("MARIADB_HOST", "localhost"))
    port: int = field(default_factory=lambda: int(os.getenv("MARIADB_PORT", "3306")))
    user: str = field(default_factory=lambda: os.getenv("MARIADB_USER", ""))
    password: str = field(default_factory=lambda: os.getenv("MARIADB_PASSWORD", ""))
    database: str = field(default_factory=lambda: os.getenv("MARIADB_DATABASE", ""))

    @classmethod
    def from_args(cls) -> 'DBconfig':
        """Create a DBconfig instance from command-line arguments and environment variables."""
        cli_args = get_arguments()
        return cls(**{**cls().__dict__, **cli_args})

# Usage
config = DBconfig.from_args()

print(config)

print(config.host)
print(config.port)
print(config.user)
print(config.password)
print(config.database)
