import sys

from backend.tile.Tile import Tile


def merge(a, b, f) -> dict:
    # Start with symmetric difference; keys either in A or B, but not both
    merged = {k: a.get(k, b.get(k)) for k in a.keys() ^ b.keys()}
    # Update with 'f()' applied to the intersection
    merged.update({k: f(a[k], b[k]) for k in a.keys() & b.keys()})
    return merged


def merge_dicts(f, *ds) -> dict:
    dic = {}
    for d in ds:
        dic = merge(dic, d, f)
    return dic


def merge_dicts_during_game(*ds) -> dict:
    return merge_dicts(lambda x, y: [x[0] + y[0], x[1] + y[1]], *ds)


def merge_dicts_after_game(*ds) -> dict:
    return merge_dicts(lambda x, y: x + y, *ds)


def attach_left_right(left, right):  # may be useful in board object to link tiles more easily
    if isinstance(left, Tile) and isinstance(right, Tile):
        if left.fit_right(right) and right.fit_left(left):
            left.rightTile = right
            right.leftTile = left
        else:
            sys.stderr.write("Tiles do not fit")


def attach_up_down(up, down):
    if isinstance(up, Tile) and isinstance(down, Tile):
        if up.fit_down(down) and down.fit_up(up):
            up.downTile = down
            down.upTile = up
        else:
            sys.stderr.write("Tiles do not fit")
