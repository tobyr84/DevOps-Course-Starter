import arrow
class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self): 
        return self._items

    @property
    def to_do(self): 
        output = []

        for item in self._items:
            if item.status == "Not Started":
                output.append(item)

        return output

    @property
    def doing(self): 
        output = []

        for item in self._items:
            if item.status == "In Progress":
                output.append(item)

        return output

    @property
    def done(self): 
        output = []

        for item in self._items:
            if item.status == "Completed":
                output.append(item)

        return output

    @property
    def show_all_done_items(self):
        # if there are 5 or fewer completed tasks

        output = []

        for item in self._items:
            if item.status == "Completed":
                output.append(item)

        if len(output) <= 5:
            return True
        else:
            return False

    @property
    def show_all_done_items_today(self):
        # shows all items that have been clompleted today
        print("Correct Function")
        print(self._items)
        output = []

        for item in self._items:
            print(item.date)
            print(arrow.utcnow())
            print(item.title)
            if item.status == "Completed" and arrow.get(item.date).floor('day') == arrow.utcnow().floor('day'):
                output.append(item)

        return output
  