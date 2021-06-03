import snake,dice,ladder
class Board():
    def main(CurrentPosition):
        DiceValue=dice.Dice.main()
        CurrentPosition+=DiceValue
        if CurrentPosition<=100:
            temp=snake.SnakeAttacks.AttackValues()
            CurrentPosition=snake.SnakeAttacks.main(temp,CurrentPosition)
            temp=ladder.LadderBenifit.LadderValues()
            CurrentPosition=ladder.LadderBenifit.main(temp,CurrentPosition)
            return CurrentPosition
        return CurrentPosition-DiceValue