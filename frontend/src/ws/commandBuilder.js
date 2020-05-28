export const buildJoin = () => ({
    type: "join",
    data: {}
})

export const buildReady = (id) => ({
    type: "ready",
    data: {
        id
    }
})

export const buildRotate = (id, tile_id, rotate) => ({
    type: "rotate_tile",
    data: {
        id,
        tile: {
            id: tile_id,
            rotate: rotate
        }
    }
})

export const buildPutTile = (id, tile_x, tile_y) => ({
    type: "put_tile",
    data: {
        id,
        x: tile_x,
        y: tile_y
    }
})

export const buildEndTurn = (id, tile_id, rotate, pawn_placed, pawn_x, pawn_y) => ({
    type: "end_turn",
    data: {
        id,
        tile: {
            id: tile_id,
            rotate
        },
        pawn_placed,
        pawn_info: {
            x: pawn_x,
            y: pawn_y
        }
    }
})

export const buildSurrender = (id) => ({
    type: "disconnect",
    data: {
        id
    }
})