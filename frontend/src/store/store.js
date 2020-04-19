import {applyMiddleware, combineReducers, createStore} from "redux";
import {gameReducer} from "./reducers/gameReducer";
import {wsReducer} from "./reducers/wsReducer";
import {mainReducer} from "./reducers/mainReducer";
import wsMiddleware from './../ws/middleware';
import {composeWithDevTools} from 'redux-devtools-extension';

const rootReducer = combineReducers({
    type: mainReducer,
    ws: wsReducer,
    game: gameReducer
})

const middleware = [wsMiddleware]

// noinspection JSCheckFunctionSignatures
const store = createStore(rootReducer,
    composeWithDevTools(applyMiddleware(...middleware)));

export default store;