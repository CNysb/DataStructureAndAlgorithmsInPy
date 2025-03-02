from Stack.FavoritesList import FavoritesList
from Stack.PositionalList import PositionalList


class FavoriatesListMTF(FavoritesList):
    def move_up(self, p):
        if p != self.data.first:
            self.data.add_first(self.data.delete(p))

    def top(self, k):
        if not 1 <= k <= len(self):
            raise ValueError("invalid k")

        temp = PositionalList()
        for item in self.data:
            temp.add_last(item)

        for j in range(k):
            highPos = temp.first
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element.count > highPos.element.count:
                    highPos = walk
                walk = temp.after(walk)
            yield highPos.element.value
            temp.delete(highPos)
