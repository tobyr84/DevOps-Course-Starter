import os

class TodoItem:
    # You call this by running TodoItem(id, title, status)
    def __init__(self, id, title, status, dateLastActivity):
        self.id = id
        self.title = title
        self.status = status
        self.date = dateLastActivity

    @classmethod
    def from_trello_card(cls, trello_card):
        id = trello_card["id"]
        title = trello_card["name"]
        status = ""
        date = trello_card["dateLastActivity"]

        if trello_card["idList"] == os.getenv('NOT_STARTED'):
            status = "Not Started"
        elif trello_card["idList"] == os.getenv('IN_PROGRESS'):
            status = "In Progress"
        elif trello_card["idList"] == os.getenv('COMPLETED'):
            status = "Completed"

        return cls(id, title, status, date)

