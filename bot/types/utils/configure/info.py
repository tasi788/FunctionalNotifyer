from dataclasses import dataclass, field
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Info:
    version: int = field(hash=False, repr=True, compare=False, default=None)
