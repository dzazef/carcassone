const defaultErrorState = {
    data: undefined,
    message: undefined,
}

export const errorReducer = (state = defaultErrorState, action) => {
    console.log('er: ', action.data)
    switch (action.type) {
        case 'ERROR_HANDLE':
            return {
                data: action.data.data,
                message: action.data.message
            }
        case 'ERROR_RESET':
            return defaultErrorState
        default:
            return state
    }
}