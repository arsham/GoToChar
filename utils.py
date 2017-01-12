# Copyright 2016 Arsham Shirvani <arshamshirvani@gmail.com>. All rights reserved.
# Use of this source code is governed by the Apache 2.0 license
# License that can be found in the LICENSE file.

from sublime import Region


class Constants:

    NEXT_MODE = "next"
    BACK_MODE = "back"
    MODES = (NEXT_MODE, BACK_MODE)

    RIGHT = 1
    LEFT = -1


class State:
    """
    Defines the current state of the plug-in.
    An object of this class the only source of the truth.
    """
    invoked = False
    in_plugin = False
    select = False

    def reset(self):
        self.invoked = False
        self.in_plugin = False


state_object = None


def current_state():
    global state_object
    if state_object is None:
        state_object = State()
    return state_object


def remove_last(view):
    """
    Removes the last character entered and returns it because we don't want to display it.
    """
    position = view.sel()[0].begin()
    region = Region(position, position - 1)
    character = view.substr(region)
    view.run_command("left_delete")
    # undoing twice to remove the character and also retain the view's dirty state.
    view.run_command("undo")
    view.run_command("undo")

    return character


def to_next(view, character):
    """
    moves the cursor to the next occurrence of the `character`
    """
    return _find_and_move(view, character, Constants.RIGHT)


def to_back(view, character):
    """
    moves the cursor to the previous occurrence of the `character`
    """
    return _find_and_move(view, character, Constants.LEFT)


def _find_and_move(view, character, direction):
    lines = {}  # a dictionary of cursor region tuple to line region
    for sel in view.sel():
        a = min(sel.a, sel.b)  # normalising the selection region
        b = max(sel.a, sel.b)

        # in case of going right, the add_cell_check points to the character's position
        add_cell_check = 0
        if direction == Constants.LEFT:
            # otherwise it is the left side of it, which is the previous character's position
            add_cell_check = -1

        if a == b and view.substr(a + add_cell_check) == character:
            # to hop over the character if it is the character already, and look up the next one
            a += direction
            b += direction
            sel = Region(a, b)
        lines[(a, b)] = view.line(sel)

    regions = []
    for sel, line in lines.items():
        regions.append(_get_found_regions(view, character, sel, line, direction))

    if regions:
        # because we don't want to clear the selection if there is no region
        view.sel().clear()
        for region in regions:
            view.sel().add(region)

    current_state().reset()


def _get_found_regions(view, character, sel, line, direction):
    """
    Finds the regions of where the cursor(s) should land. It the command is in select mode,
    the regions are apart, otherwise it is on one character.
    :rtype: Region
    """
    if direction == Constants.RIGHT:
        line_portion = Region(sel[0], line.b)
    else:
        line_portion = Region(line.a, sel[1])

    from_sel = view.substr(line_portion)

    if direction == Constants.RIGHT:
        found_pos = from_sel.find(character)
    else:
        found_pos = from_sel.rfind(character)

    if found_pos > 0:
        # otherwise we didn't find anything
        if current_state().select:
            if direction == Constants.RIGHT:
                a = sel[0]
                b = sel[0] + found_pos
            else:
                a = line.a + found_pos
                b = sel[1]
        else:
            if direction == Constants.RIGHT:
                a = b = sel[0] + found_pos
            else:
                a = b = line.a + found_pos

        return Region(a, b)

    # for clearing only the region that can be advanced, we need to
    # push back the current selection
    return Region(sel[0], sel[1])
