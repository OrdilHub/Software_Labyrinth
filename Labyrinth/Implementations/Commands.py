from Services.ICommand import ICommand


class Quit(ICommand):
    def get_command_tag(self):
        return "quit"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        return True, "Finished"


class GoUp(ICommand):
    """Triggers move up action"""
    def get_command_tag(self):
        return "fwd"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        success, above_cell, won = player.move_up(labyrinth)
        player.execute_cell_action(labyrinth)
        return won, str(success) + ": " + str(above_cell)


class GoDown(ICommand):
    def get_command_tag(self):
        return "bwd"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        success, above_cell, won = player.move_down(labyrinth)
        player.execute_cell_action(labyrinth)
        return won, str(success) + ": " + str(above_cell)


class GoLeft(ICommand):
    def get_command_tag(self):
        return "left"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        success, above_cell, won = player.move_left(labyrinth)
        player.execute_cell_action(labyrinth)
        return won, str(success) + ": " + str(above_cell)


class GoRight(ICommand):
    def get_command_tag(self):
        return "right"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        success, above_cell, won = player.move_right(labyrinth)
        player.execute_cell_action(labyrinth)
        return won, str(success) + ": " + str(above_cell)


class Skip(ICommand):
    def get_command_tag(self):
        return "skip"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        player.execute_cell_action(labyrinth)
        return False, "step executed"