import * as GameActions from '../store/actions/gameActions'
import * as MainActions from '../store/actions/mainActions'
import * as LobbyActions from '../store/actions/lobbyActions'

const handleError = (store, message, data) => {
    store.dispatch(GameActions.gameReceiveError({
        message,
        data
    }))
}

const parseMessage = (store, data) => {
    let payload = null
    try {
        payload = JSON.parse(data)
    } catch (error) {
        handleError(store, 'Data have incorrect format', data)
    }
    return payload
}

// TODO: make error as single reducer
export const wsReceiver = (store, data) => {

    let payload = parseMessage(store, data)
    if (payload === null) return

    console.log("ws_rcv: ", payload.type)

    switch (payload.type) {
        case("player_count"):
            store.dispatch(LobbyActions.lobbyPlayer(payload.data))
            break
        case("start"):
            store.dispatch(MainActions.mainGame())
            break
        case("board"):
            store.dispatch(GameActions.gameUpdateBoard(payload.data))
            break
        case("turn_info"):
            store.dispatch(GameActions.gameTurnInfo(payload.data))
            break
        case("pawn_info"):
            store.dispatch(GameActions.gamePawnInfo(payload.data))
            break
        case("end_game"):
            store.dispatch(GameActions.gameEnd(payload.data))
            break
        default:
            handleError(store, 'Incorrect type of message', payload.type)
    }

}
