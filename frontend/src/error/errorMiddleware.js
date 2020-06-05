import config from "../config.json";
import * as ErrorActions from '../store/actions/errorActions'

const errorMiddleware = () => {

    let timer;

    return store => next => action => {
        switch (action.type) {
            case 'ERROR_HANDLE':
                clearTimeout(timer)
                timer = setTimeout(
                    () => {store.dispatch(ErrorActions.errorReset())},
                    config.hideErrorTimeout
                )
                return next(action)
            default:
                return next(action)
        }
    }

}

export default errorMiddleware()