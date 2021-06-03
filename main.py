import os
import dice, board,snake,ladder
class Master():
    def main(self,Players,PlayersRecord):
        for i in range(self.Players):
            self.PlayersRecord[i]=board.Board.main(self.PlayersRecord[i])
        print(self.PlayersRecord)
        if 100 in self.PlayersRecord:
            print("Hurray.... You WON Player {}".format(self.PlayersRecord.index(100)+1))
            print("Wanna Play Another Match?\nPress 1 for Rematch and 0 For Ending")
            if int(input())==1:
                print("\n\n")
                self.start()
            print("Thanks For Playing, Have A Nice Day Ahead")
        if int(input())==1:
            return self.main(Players,PlayersRecord)

    def start(self):
        print("Hey Welcome In The Game\nChoose The No. Of Players")
        self.Players=int(input())
        self.PlayersRecord=[0]*self.Players
        self.main(self.Players,self.PlayersRecord)
object=Master()
object.start()

