from dataclasses import dataclass, asdict

@dataclass
class Account:
    username: str
    password: str