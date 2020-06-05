import config from "../config.json";
import * as ErrorActions from '../store/actions/errorActions'

/**
 * Redux middleware for handling errors. After an error occurred it is displayed in
 * a popup and hidden after delay set in config.json
 * @returns {function(*=): function(*): function(...[*]=)}
 */
const errorMiddleware = () => {

    let timer;

    return store => next => action => {
        switch (action.type) {
            case 'ERROR_HANDLE':
                clearTimeout(timer)
                timer = setTimeout(
                    () => {
                        store.dispatch(ErrorActions.errorReset())
                    },
                    config.hideErrorTimeout
                )
                return next(action)
            default:
                return next(action)
        }
    }

}

export default errorMiddleware()