# graph_state.py
from typing import TypedDict, List

class BlogState(TypedDict):
    topic: str
    research: str
    outline: List[str]
    sections: List[str]
    blog: str