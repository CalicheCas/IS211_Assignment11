class Task(object):

    id = 0
    desc = None
    email = None
    priority = None
    status = "In Progress"

    def __init__(self, id, desc, email, priority):
        self.id = id
        self.desc = desc
        self.email = email
        self.priority = priority
