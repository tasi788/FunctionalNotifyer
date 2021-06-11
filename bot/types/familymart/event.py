from dataclasses_json import dataclass_json
from dataclasses import dataclass
from typing import Optional, List


@dataclass_json
@dataclass
class FamilyMartEvent:
    img: str
    date: Optional[str]
    title: str
    description: str
    link: str


@dataclass_json
@dataclass
class Event:
    hito: List[FamilyMartEvent]
    hot: List[FamilyMartEvent]
    service: List[FamilyMartEvent]
    lottery: List[FamilyMartEvent]
