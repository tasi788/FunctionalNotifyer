from dataclasses import dataclass, field
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Log:
    namecheck: int = field(hash=False, repr=True, compare=False, default=None)
    spamname: int = field(hash=False, repr=True, compare=False, default=None)
    evidence: int = field(hash=False, repr=True, compare=False, default=None)
