"""GDSFactory+ Pydantic models."""

from pathlib import Path
from typing import Annotated, Any, Literal

import sax
from gdsfactory.read.from_yaml import from_yaml
from pydantic import BaseModel, BeforeValidator, Field
from sax.netlist import RecursiveNetlist

from gdsfactoryplus.core.shared import get_active_pdk

from .settings import SETTINGS, Arange, Linspace

MimeType = Literal[
    "html", "json", "yaml", "plain", "base64", "png", "gds", "netlist", "dict", "error"
]


class ShowMessage(BaseModel):
    """A message to vscode to show an object."""

    what: Literal["show"] = "show"  # do not override
    mime: MimeType
    content: str


class ReloadSchematicMessage(BaseModel):
    """A message to vscode to trigger a schematic reload."""

    what: Literal["reloadSchematic"] = "reloadSchematic"
    path: str


class ErrorMessage(BaseModel):
    """A message to vscode to trigger an error popup."""

    what: Literal["error"] = "error"  # do not override
    category: str
    message: str
    path: str


class RefreshTreesMessage(BaseModel):
    """A message to vscode to trigger a pics tree reload."""

    what: Literal["refreshPicsTree"] = "refreshPicsTree"


class ReloadLayoutMessage(BaseModel):
    """A message to vscode to trigger a gds viewer reload."""

    what: Literal["reloadLayout"] = "reloadLayout"
    cell: str


Message = ShowMessage | ErrorMessage | RefreshTreesMessage | ReloadLayoutMessage


class SimulationConfig(BaseModel):
    """Data model for simulation configuration."""

    pdk: str = SETTINGS.pdk.name
    wls: Linspace | Arange = SETTINGS.sim.wls
    op: str = "none"
    port_in: str = ""
    settings: dict[str, Any] = Field(default_factory=dict)


def ensure_recursive_netlist(obj: Any) -> RecursiveNetlist:
    """Ensure that a given object is a recursive netlist."""
    if isinstance(obj, Path):
        obj = str(obj)

    if isinstance(obj, str):
        pdk = get_active_pdk()
        if "\n" in obj or obj.endswith(".pic.yml"):
            c = from_yaml(obj)
        else:
            c = pdk.get_component(obj)
        obj = c.get_netlist(recursive=True)

    if isinstance(obj, sax.Netlist):
        obj = {"top_level": obj.model_dump()}

    if isinstance(obj, sax.RecursiveNetlist):
        obj = obj.model_dump()

    if not isinstance(obj, dict):
        msg = f"Can't validate obj {obj} into RecursiveNetlist"
        raise TypeError(msg)

    return RecursiveNetlist.model_validate(obj)


class SimulationData(BaseModel):
    """Data model for simulation."""

    netlist: Annotated[RecursiveNetlist, BeforeValidator(ensure_recursive_netlist)]
    config: SimulationConfig = Field(default_factory=SimulationConfig)


class DoItForMe(BaseModel):
    """DoItForMe Data."""

    prompt: str = ""
    initial_circuit: str = ""
    url: str = "wss://doitforme.gdsfactory.com/ws"


class Result(BaseModel):
    """Result class containing logs and errors to be returned."""

    log: list[str] = Field(default_factory=list)
    errors: list[str] = Field(default_factory=list)
