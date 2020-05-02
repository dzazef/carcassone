from backend.tile.Tile import Tile


def merge(a, b, f):
    # Start with symmetric difference; keys either in A or B, but not both
    merged = {k: a.get(k, b.get(k)) for k in a.keys() ^ b.keys()}
    # Update with 'f()' applied to the intersection
    merged.update({k: f(a[k], b[k]) for k in a.keys() & b.keys()})
    return merged


def merge_dicts(f, *ds):
    dic = {}
    for d in ds:
        dic = merge(dic, d, f)
    return dic


def merge_dicts_during_game(*ds):
    return merge_dicts(lambda x, y: [x[0] + y[0], x[1] + y[1]], *ds)


def merge_dicts_after_game(*ds):
    return merge_dicts(lambda x, y: x + y, *ds)


def attach_left_right(left, right):  # may be useful in board object to link tiles more easily
    if isinstance(left, Tile) and isinstance(right, Tile):
        left.rightTile = right
        right.leftTile = left


def attach_up_down(up, down):
    if isinstance(up, Tile) and isinstance(down, Tile):
        up.downTile = down
        down.upTile = up
