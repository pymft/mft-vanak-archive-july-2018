class BoardList:
    instances = {}

    def __init__(self, name, is_default=False):
        self.is_default = is_default

        # if self.is_default:
        #     for blist in self.instances.values():  # get all other board list in the current board
        #         blist.is_default = False  # set them False
        #     self.is_default = True
        #
        if self.is_default:    # in the case it's set to default
            for blist in self.instances.values():    # get all other board list in the current board
                if blist is not self:          # and check this item is not self itself
                    blist.is_default = False   #  set them False

        self.name = name
        self.cards = []
        # BoardList.instances[self.name] = self
        if name in BoardList.instances.keys():
            raise Exception
        BoardList.instances.update({self.name: self})

    @classmethod
    def get_default_board(cls):
        return next(filter(lambda b: b.is_default, cls.instances.values()))

    # @staticmethod
    # def pow_2(num):
    #     return num**2

    def get_card_index(self, card):
        return self.cards.index(card)
        # map(lambda c: c.title == card_title, self.cells).index(True)
        # return [ix for ix, value in enumerate(self.cards) if value.title == card_title][0]

    def remove_card(self, card_indx):
        return self.cards.pop(card_indx)

    def add_card(self, card):
        self.cards.append(card)

    def move_card(self, card, other_list):
        indx = self.get_card_index(card)   # indx of card in the current board list
        removed_card = self.remove_card(indx)
        other_list.add_card(removed_card)


class Card:
    def __init__(self, title, brd_list=None):
        self.title = title
        if not brd_list is None:
            brd_list.add_card(self)
        else:
            BoardList.get_default_board().add_card(self)


    @property
    def board_list(self):
        blists = BoardList.instances.values()
        potential_boards = [blist for blist in blists if self in blist.cards]
        # check for errors here ;;
        return potential_boards[0]


    def move(self, dest_boardlist):
        self.board_list.move_card(self, dest_boardlist)
        dest_boardlist.add_card(self)




if __name__ == '__main__':
    defaultBorad = BoardList("default")

    blist_1 = BoardList("to do", is_default=True)
    blist_2 = BoardList("doing")
    blist_3 = BoardList("done")

    card1 = Card("assignment 1")
    card2 = Card("assignment 2")


    card1.move(blist_2)

    print('hi')
