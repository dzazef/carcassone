const defaultGameState = {
    state: "S_GAME_INITIAL",
    tiles_left: undefined,
    players: undefined,
    board: undefined,
    my_turn: undefined,
    player_turn: undefined,
    tile_placed: undefined,
    turn: {
        state: undefined,
        tile: undefined,
        possible_places: undefined
    },
    winners: undefined,
}

const handleGameStart = (state, data) => ({
    ...state,
    state: "S_GAME_ACTIVE",
    my_id: data?.me?.id,
    my_color: data?.me?.color,
    turn: {
        state: "S_EMPTY"
    },
    board: []
})

const handleGameBoard = (state, data) => ({
    ...state,
    tiles_left: data?.tiles_left,
    players: data?.players,
    board: data?.board
})

const handleTurnInfo = (state, data) => ({
    ...state,
    my_turn: (state.my_id === data?.id),
    player_turn: data?.id,
    turn: {
        state: "S_SHOW_POSSIBLE_TILES",
        tile: data?.tile,
        possible_places: data?.possible_places
    }
})

const handlePawnInfo = (state, data) => ({
    ...state,
    my_turn: (state.my_id === data?.id),
    player_turn: data?.id,
    turn: {
        state: "S_SHOW_POSSIBLE_PAWNS",
        tile: data?.tile,
        possible_places: data?.possible_places
    }
})

const handleTilePlaced = (state) => ({
    ...state,
    tile_placed: true
})

const handleEndTurn = (state) => ({
    ...state,
    tile_placed: false,
    turn: {
        state: "S_EMPTY",
    }
})

const handleEnd = (state, data) => ({
    ...state,
    state: "S_GAME_ENDED",
    winners: data?.winners
})

export const gameReducer = (state = defaultGameState, action) => {
    switch (action.type) {
        case 'GAME_INITIAL': // reseting values
            return defaultGameState
        case 'GAME_START': // start game
            return handleGameStart(state, action?.data)
        case 'GAME_BOARD': // board
            return handleGameBoard(state, action?.data)
        case 'GAME_TURN_INFO': // turn_info
            return handleTurnInfo(state, action?.data)
        case 'GAME_PAWN_INFO': // pawn_info
            return handlePawnInfo(state, action?.data)
        case 'GAME_TILE_PLACED': //inner <- show button
            return handleTilePlaced(state)
        case 'GAME_END_TURN': //inner <- end turn
            return handleEndTurn(state)
        case 'GAME_END': // end_game
            return handleEnd(state, action?.data)
        default:
            return state
    }
}