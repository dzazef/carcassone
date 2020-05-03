import {applyMiddleware, combineReducers, createStore} from "redux";
import {gameReducer} from "./reducers/gameReducer";
import {wsReducer} from "./reducers/wsReducer";
import {mainReducer} from "./reducers/mainReducer";
import {lobbyReducer} from "./reducers/lobbyReducer";
// import {playerReducer} from "./reducers/playerReducer";
import wsMiddleware from './../ws/middleware';
import {composeWithDevTools} from 'redux-devtools-extension';

const rootReducer = combineReducers({
    state: mainReducer,
    ws: wsReducer,
    game: gameReducer,
    lobby: lobbyReducer
    // player: playerReducer
})

const middleware = [wsMiddleware]

// noinspection JSCheckFunctionSignatures
const store = createStore(rootReducer,
    composeWithDevTools(applyMiddleware(...middleware)));

export default store;