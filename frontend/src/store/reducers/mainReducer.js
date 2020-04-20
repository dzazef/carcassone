const defaultState = 'MAIN_INITIAL'

export const mainReducer = (state = defaultState, action) => {
    switch (action.type) {
        case 'MAIN_INITIAL':
            return 'MAIN_INITIAL'
        case 'MAIN_GAME':
            return 'MAIN_GAME'
        default:
            return state
    }
}