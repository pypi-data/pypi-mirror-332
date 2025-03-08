# -*- coding: utf-8 -*-
from typing import Optional

from mantis_scenario_model.scenario_model import ScenarioExecutionStatus
from mantis_scenario_model.scenario_run_config_model import ContentType
from pydantic import BaseModel


class Lab(BaseModel):
    runner_id: str
    """Lab UUID."""

    status: ScenarioExecutionStatus
    """Lab status."""

    lab_creation_timestamp: float
    """Timestamp of lab creation step."""

    lab_start_timestamp: Optional[float]
    """Timestamp of lab starting step."""

    lab_content_end_timestamp: Optional[float]
    """Timestamp of end of content execution within the lab."""

    lab_end_timestamp: Optional[float]
    """Timestamp of end of lab execution."""

    content_type: ContentType
    """Content executed inside the lab (basebox, topology, attack or killchain)."""

    name: str
    """Name of the lab."""

    created_by: str
    """UUID of the user that created the lab."""

    group_name: str
    """Name of the group in which the lab is executed."""

    group_id: str
    """UUID of the group in which the lab is executed."""

    worker_id: str
    """UUID of the worker that executes the lab."""
