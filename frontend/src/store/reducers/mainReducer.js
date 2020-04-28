const defaultState = 'S_MAIN_INITIAL'

export const mainReducer = (state = defaultState, action) => {
    switch (action.type) {
        case 'MAIN_INITIAL':
            return 'S_MAIN_INITIAL'
        case 'MAIN_GAME':
            return 'S_MAIN_GAME'
        default:
            return state
    }
}