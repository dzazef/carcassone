const defaultWSState = {
    state: 'S_WS_DEFAULT'
}

export const wsReducer = (state = defaultWSState, action) => {
    switch (action.type) {
        case 'WS_DEFAULT':
            return defaultWSState
        case 'WS_CONNECTING':
            return {...state, state: 'S_WS_CONNECTING'}
        case 'WS_CONNECTED':
            return {...state, state: 'S_WS_CONNECTED'}
        case 'WS_DISCONNECTING':
            return {...state, state: 'S_WS_DISCONNECTING'}
        case 'WS_DISCONNECTED':
            return {...state, state: 'S_WS_DISCONNECTED'}
        default:
            return state
    }
}