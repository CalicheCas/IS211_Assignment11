import enum


class Priority(enum.Enum):

    high = "High"
    medium = "Medium"
    low = "Low"


class Status(enum.Enum):

    in_progress = "InProgress"
    completed = "Completed"
    pending = "Pending"
