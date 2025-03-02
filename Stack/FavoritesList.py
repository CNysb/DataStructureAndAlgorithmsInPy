from Stack.PositionalList import PositionalList


class FavoritesList:
    def __init__(self) -> None:
        self.data = PositionalList()

    class Item:
        def __init__(self, e) -> None:
            self.value = e
            self.count = 0

    def find_position(self, e):
        walk = self.data.first
        while walk is not None and walk.element != e:
            walk = self.data.after(walk)
        return walk

    def move_up(self, p):
        if p != self.data.first:
            cnt = p.element.count
            walk = self.data.before(p)
            if cnt > walk.element.count:
                while (
                    walk != self.data.first
                    and cnt > self.data.before(walk).element.count
                ):
                    walk = self.data.before(walk)
                self.data.add_before(p, self.data.delete(p))

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def access(self, e):
        p = self.find_position(e)
        if p is None:
            p = self.data.add_last(self.Item(e))
        p.element.count += 1
        self.move_up(p)

    def remove(self, e):
        p = self.find_position(e)
        if p is not None:
            self.data.delete(p)

    def top(self, k):
        if not 1 <= k <= len(self):
            raise ValueError("k must be between 1 and len")
        walk = self.data.first
        for j in range(k):
            item: FavoritesList.Item = walk.element
            yield item.value
            walk = self.data.after(walk)
