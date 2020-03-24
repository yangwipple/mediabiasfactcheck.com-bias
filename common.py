from dataclasses import dataclass
from enum import Enum


class Factual(Enum):
    VERYHIGH = 1
    HIGH = 2
    MOSTLYHIGH = 3
    MIXED = 4
    QUESTIONABLE = 5


@dataclass
class Source(object):
    name: str
    domain_url: str
    page_url: str
    img_url: str
    factual: Factual
    bias_class: str
    bias: int


@dataclass
class BrokenSource(object):
    page_url: str
    error_message: str


@dataclass
class AdFontesMediaSource(object):
    name: str
    vertical_rank: int
    horizontal_rank: int
