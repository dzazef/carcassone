const defaultLobbyState = {
    players: [],
    my_id: undefined
}

const handleLobbyPlayer = (state, action) => {
    return {
        ...state,
        players: action?.data?.lobby,
        my_id: ((state?.my_id) ? state?.my_id : action?.data?.me?.id)
    }
}

export const lobbyReducer = (state = defaultLobbyState, action) => {
    console.log('lr: ', action.data) //TODO
    switch (action.type) {
        case 'LOBBY_INITIAL':
            return defaultLobbyState
        case 'LOBBY_PLAYER':
            return handleLobbyPlayer(state, action)
        default:
            return state
    }
}
