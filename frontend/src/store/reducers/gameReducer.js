const defaultGameState = {
    state: "S_GAME_INITIAL"
}

// const checkIfDefined = (...props) => {
//     // usage:
//     // if (!checkIfDefined(data.me.id, data.players)) {
//     //     return handleError(state, 'Incorrect format', data, action.type)
//     // }
//     for (let i = 0; i < props.length; i++) {
//         if (props[i] === undefined) {
//             return false
//         }
//     }
//     return true
// }

const handleGameBoard = (state, action) => {
    const data = action.data
    return {
        ...state,
        state: "S_GAME_ACTIVE",
        tiles_left: data.tiles_left,
        players: data.players,
        board: data.board
    }
}

const handleTurnInfo = (state, action) => {
    const data = action.data
    return {
        ...state,
        my_turn: (state.my_id === data.id),
        player_turn: data.id,
        turn: {
            state: "S_SHOW_POSSIBLE_TILES",
            tile: data.tile,
            possible_places: data.possible_places
        }
    }
}

const handlePawnInfo = (state, action) => {
    const data = action.data
    return {
        ...state,
        my_turn: (state.my_id === data.id),
        player_turn: data.id,
        turn: {
            state: "S_SHOW_POSSIBLE_PAWNS",
            tile: data.tile,
            possible_places: data.possible_places
        }
    }
}

const handleEnd = (state, action) => {
    const data = action.data
    return {
        ...state,
        state: "S_GAME_ENDED",
        winners: data.winners
    }
}

const handleError = (state, message, data, action) => ({
    ...state,
    error: {
        message,
        data,
        action
    }
})

const handleResetError = (state) => ({
    ...state,
    error: undefined
})

export const gameReducer = (state = defaultGameState, action) => {
    try {
        const newState = handleResetError(state)
        console.log('gr: ', action.data) //TODO
        switch (action.type) {
            case 'GAME_INITIAL':
                return defaultGameState
            case 'GAME_BOARD':
                return handleGameBoard(newState, action)
            case 'GAME_TURN_INFO':
                return handleTurnInfo(newState, action)
            case 'GAME_PAWN_INFO':
                return handlePawnInfo(newState, action)
            case 'GAME_END':
                return handleEnd(newState, action)
            case 'GAME_RCV_ERROR':
                return handleError(newState, action.data.message,
                    action.data.data, 'GAME_RCV_ERROR')
            default:
                return state
        }
    } catch (error) {
        return handleError(state, error.message, action.data, action.type)
    }
}
