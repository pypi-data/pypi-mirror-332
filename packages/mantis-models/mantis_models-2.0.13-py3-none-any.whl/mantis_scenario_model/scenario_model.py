# -*- coding: utf-8 -*-
from datetime import datetime
from enum import Enum
from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict

from .unit_attack_model import Timestamps
from .unit_attack_model import WorkerMitreData


class ScenarioExecutionStatus(str, Enum):
    created = "CREATED"  # The task has been created but is not yet
    # totally initialized (some metadata still
    # need to be created)
    pending = "PENDING"  # The runner (Cyber Range) has not been found yet
    runner_setup = (
        "RUNNER_SETUP"  # Runner initialization (Cyber Range APIs waiting to be up)
    )
    scenario_creation = "SCENARIO_CREATION"  # Simulation is starting
    scenario_setup = (
        "SCENARIO_SETUP"  # Scenario provisioning and setup (network capture, etc.)
    )
    scenario_execution = (
        "SCENARIO_EXECUTION"  # Proper scenario exection (life and attacks)
    )
    scenario_teardown = "SCENARIO_TEARDOWN"  # After scenario execution (forensic, etc.)
    scenario_finished = "SCENARIO_FINISHED"  # Scenario has been successfully finished
    runner_teardown = "RUNNER_TEARDOWN"  # Runner is terminating
    completed = "COMPLETED"  # Scenario has been successfully finished and runner is not available anymore
    cancelled = "CANCELLED"  # Scenario has been cancelled
    error = "ERROR"  # Scenario triggered an internal error
    pause = "PAUSE"  # Scenario pause


class ScenarioExecutionStopped(Exception):
    pass


class Steps(BaseModel):
    skip_deploy: bool = False
    skip_all_preparations: bool = False
    skip_provisioning_os_set_time: bool = False
    skip_provisioning_os_set_hostname: bool = False
    skip_provisioning_attack: bool = False
    skip_provisioning_os_monitoring: bool = False
    skip_user_activity: bool = False
    skip_compromise: bool = False
    skip_attack: bool = False
    skip_create_dataset: bool = False


class CompromissionOs(str, Enum):
    windows10 = "windows10"
    windows7 = "windows7"
    ubuntu_gnome = "ubuntu_gnome"


class CompromissionBeacon(str, Enum):
    exe_reverse_api = "exe_reverse_api"
    win_reverse_api = "win_reverse_api"
    powershell_reverse_api = "powershell_reverse_api"
    linux_python_reverse_api = "linux_python_reverse_api"


class CompromissionVector(str, Enum):
    simple = "simple"  # user_activity + provisioning
    webmail = "webmail"


class CompromissionInfras(str, Enum):
    legacy = "legacy"  # api_control + nginx


class CompromissionProtocol(str, Enum):
    http = "http"
    https = "https"


class CompromissionPrivilege(int, Enum):
    user = 0
    admin = 1
    system = 2


class CompromissionConfig(BaseModel):
    auto_compromission: bool
    target_name: str
    beacon: Optional[CompromissionBeacon] = (
        None  # mandatory if auto_compromission = true
    )
    vector: Optional[CompromissionVector] = (
        None  # mandatory if auto_compromission = true
    )
    infras: Optional[CompromissionInfras] = (
        None  # mandatory if auto_compromission = true
    )
    communication_protocol: Optional[CompromissionProtocol] = (
        None  # mandatory if auto_compromission = true
    )
    privilege_level: Optional[CompromissionPrivilege] = (
        None  # mandatory if auto_compromission = true
    )


class ScenarioConfig(BaseModel):
    name: str
    file: str
    compromission: CompromissionConfig
    production: bool


class Scenario(BaseModel):
    name: str = "default scenario name"
    keywords: List[str] = []
    description: str = ""
    description_fr: str = ""
    long_description: List[str] = []
    long_description_fr: List[str] = []
    unit_attacks: List[str] = []
    attacks: List[str] = []
    mitre_tags: Optional[List[WorkerMitreData]] = []
    steps: Optional[Steps] = Steps()
    timestamps: Optional[Timestamps] = None
    scenario_config: List[ScenarioConfig] = []
    creation_date: datetime
    last_update: datetime

    model_config = ConfigDict(extra="forbid", validate_assignment=True)
