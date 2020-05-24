const defaultLobbyState = {
    players: []
}

const handleResetError = (state) => ({
    ...state,
    error: undefined
})

const handleError = (state, message, data, action) => ({
    ...state,
    error: {
        message,
        data,
        action
    }
})

const handleLobbyPlayer = (state, action) => {
    return {
        ...state,
        players: action?.data?.lobby,
        my_id: ((state.my_id) ? state.my_id : action?.data?.me?.id)
    }
}

export const lobbyReducer = (state = defaultLobbyState, action) => {
    try {
        const newState = handleResetError(state)
        console.log('lr: ', action.data) //TODO
        switch (action.type) {
            case 'LOBBY_INITIAL':
                return defaultLobbyState
            case 'LOBBY_PLAYER':
                return handleLobbyPlayer(newState, action)
            case 'LOBBY_RCV_ERROR': //TODO: separate reducer
                return handleError(newState, action.data.message,
                    action.data.data, 'GAME_RCV_ERROR')
            default:
                return state
        }
    } catch (error) {
        return handleError(state, error.message, action.data, action.type)
    }
}
