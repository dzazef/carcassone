import {applyMiddleware, combineReducers, createStore} from "redux";
import {gameReducer} from "./reducers/gameReducer";
import {wsReducer} from "./reducers/wsReducer";
import {mainReducer} from "./reducers/mainReducer";
import {lobbyReducer} from "./reducers/lobbyReducer";
import {errorReducer} from "./reducers/errorReducer"

import wsMiddleware from '../ws/wsMiddleware';
import errorMiddleware from "../error/errorMiddleware";
import {composeWithDevTools} from 'redux-devtools-extension';

/**
 * Root reducer of store
 */
const rootReducer = combineReducers({
    state: mainReducer,
    ws: wsReducer,
    game: gameReducer,
    lobby: lobbyReducer,
    error: errorReducer
})

/**
 * List with middlewares
 */
const middleware = [wsMiddleware, errorMiddleware]

// noinspection JSCheckFunctionSignatures
/**
 * Redux store
 */
const store = createStore(rootReducer,
    composeWithDevTools(applyMiddleware(...middleware)));

export default store;