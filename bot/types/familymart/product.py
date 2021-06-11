from dataclasses_json import dataclass_json
from dataclasses import dataclass, field
from typing import List, Optional, Union


@dataclass_json
@dataclass
class ProductDetails:
    id: Optional[str] = field(hash=False, repr=True, compare=False, default_factory=list)
    title: str = field(hash=False, repr=True, compare=False, default=None)
    img: str = field(hash=False, repr=True, compare=False, default=None)
    dates: Optional[str] = field(hash=False, repr=True, compare=False, default=None)
    eventstart: Optional[str] = field(hash=False, repr=True, compare=False, default=None)
    eventend: Optional[str] = field(hash=False, repr=True, compare=False, default=None)
    content: Optional[str] = field(hash=False, repr=True, compare=False, default=None)
    link: Optional[str] = field(hash=False, repr=True, compare=False, default=None)
    price: Optional[str] = field(hash=False, repr=True, compare=False, default=None)
    types: Optional[str] = field(hash=False, repr=True, compare=False, default=None)
    size: Optional[str] = field(hash=False, repr=True, compare=False, default=None)
    store: Optional[str] = field(hash=False, repr=True, compare=False, default=None)


@dataclass_json
@dataclass
class Product:
    eventneworder: List[str] = field(hash=False, repr=True, compare=False, default_factory=list)
    coffees: Optional[Union[str, ProductDetails]] = field(hash=False, repr=True, compare=False, default_factory=list)
    freshs: Optional[Union[str, ProductDetails]] = field(hash=False, repr=True, compare=False, default_factory=list)
    other: Optional[Union[str, ProductDetails]] = field(hash=False, repr=True, compare=False, default_factory=list)
    clothes: Optional[Union[str, ProductDetails]] = field(hash=False, repr=True, compare=False, default_factory=list)
    info: Optional[Union[str, ProductDetails]] = field(hash=False, repr=True, compare=False, default_factory=list)
    clothesother: Optional[Union[str, ProductDetails]] = field(hash=False, repr=True, compare=False, default_factory=list)