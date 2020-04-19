const defaultWSState = {
    state: 'WS_DEFAULT'
}

export const wsReducer = (state = defaultWSState, action) => {
    console.log(`from reducer: ${action.type}`)
    switch (action.type) {
        case 'WS_DEFAULT':
            return defaultWSState
        case 'WS_CONNECTING':
            return {...state, state: 'WS_CONNECTING'}
        case 'WS_CONNECTED':
            return {...state, state: 'WS_CONNECTED'}
        case 'WS_DISCONNECTING':
            return {...state, state: 'WS_DISCONNECTING'}
        case 'WS_DISCONNECTED':
            return {...state, state: 'WS_DISCONNECTED'}
        case 'WS_ERROR':
            return {...state, state: 'WS_ERROR', error: action.error}
        default:
            return state
    }
}