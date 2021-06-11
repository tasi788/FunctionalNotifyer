from dataclasses import dataclass, field
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Bot:
    id: int = field(hash=False, repr=True, compare=False, default=None)
    token: str = field(hash=False, repr=True, compare=False, default=None)
    api_id: str = field(hash=False, repr=True, compare=False, default=None)
    api_hash: str = field(hash=False, repr=True, compare=False, default=None)
