from colav_protobuf import ControllerFeedback
from enum import Enum

class CtrlMode(Enum):
    UNKNOWN = 0
    CRUISE = 1
    T2LOS = 2
    T2Theta = 3
    FB = 4
    WAYPOINT_REACHED = 5

class CtrlStatus(Enum):
    UNKOWN_STATUS = 0
    ACTIVE = 1
    INACTIVE = 2
    ERROR = 3

def gen_controller_feedback(
        mission_tag: str,
        agent_tag: str,
        mode: CtrlMode,
        status: CtrlStatus,
        velocity: float,
        yaw_rate: float,
        timestamp: str
):
    feedback = ControllerFeedback()
    feedback.mission_tag = mission_tag
    feedback.agent_tag = agent_tag
    feedback.mode = ControllerFeedback.CtrlMode.Value(mode.name)
    feedback.status = ControllerFeedback.CtrlStatus.Value(status.name)
    feedback.cmd.velocity = velocity
    feedback.cmd.yaw_rate = yaw_rate
    feedback.timestamp = timestamp
    return feedback
