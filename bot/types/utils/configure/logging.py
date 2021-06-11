from dataclasses import dataclass, field
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Logging:
    level: str = field(hash=False, repr=True, compare=False, default=None)
