from typing import (
    Optional,
    Dict,
    Any,
    Callable,
    Text,
    List,
)


class ConnexionRequest:
    url = ...  # type: str
    method = ...  # type: str
    path_params = ...  # type: Optional[Dict[str, str]]
    query = ...  # type: Optional[Dict[str, str]]
    headers = ...  # type: Optional[Dict[str, str]]
    form = ...  # type: Optional[Dict[str, str]]
    body = ...  # type: Optional[Any]
    json_getter = ...  # type: Callable[[], Text]
    files = ...  # type: Optional[List[Any]]
    context = ...  # type: Optional[Dict[str, str]]

    def __init__(self,
                 url: str,
                 method: str,
                 path_params: Optional[Dict[str, str]] = ...,
                 query: Optional[Dict[str, str]] = ...,
                 headers: Optional[Dict[str, str]] = ...,
                 form: Optional[Dict[str, str]] = ...,
                 body: Optional[Any] = ...,
                 json_getter: Optional[Callable[[], str]] = ...,
                 files: Optional[List[Any]] = ...,
                 context: Optional[Dict[str, str]] = ...) -> None: ...

    @property
    def json(self) -> str: ...
