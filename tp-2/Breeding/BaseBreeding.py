from typing import List

from Bag import Bag


class BaseBreeder:

    def chunks(l, n):
        """Yield n number of striped chunks from l."""
        for i in range(0, n):
            yield l[i::n]

    def breed(self, bags:List[Bag]) -> List[Bag]:

        for a,b in self.chunks(bags, 2):

