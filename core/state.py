from typing import Any, Dict, TypedDict

class State(TypedDict):
    userquestion: str
    Pii_Detectedcontext: Dict[str, Any]
    PIIcontext_node_output: str
    llm_guard_node_output: str
    finalanswer: Dict[str, Any]

