import os
from typing import Dict, List, Optional
import streamlit.components.v1 as components

__version__ = "0.0.0"

# During development process, use the component served by `npm run start`.
# Otherwise, use the component build in `frontend/build`.
_DEVELOP = os.environ.get("CUSTOM_COMPONENT_DEVELOP", False)

if _DEVELOP:
    _component_func = components.declare_component(
        "editable_list",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend", "build")
    _component_func = components.declare_component("editable_list", path=build_dir)


def editable_list(
    initial_data: List[List],
    input_params: List[Dict],
    auto_save: bool = False,
    key: Optional[str] = None
) -> list[list]:
    """Create a new instance of "editable_list"."""

    new_data = _component_func(
        data=initial_data,
        input_params=input_params,
        auto_save=auto_save,
        key=key,
        default=initial_data,
    )

    return new_data
