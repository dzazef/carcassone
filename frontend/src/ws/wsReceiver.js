import * as GameActions from '../store/actions/gameActions'

const handleError = (store, data) => {
    store.dispatch(GameActions.gameReceiveError({
        message: 'Data have incorrect format',
        data
    }))
}

const parseMessage = (store, data) => {
    let payload = null
    try {
        payload = JSON.parse(data)
    } catch (error) {
        handleError(store, data)
    }
    return payload
}

export const wsReceiver = (store, data) => {

    let payload = parseMessage(store, data)
    if (payload === null) return

    console.log("ws_rcv: ", payload.type)

    switch (payload.type) {
        case("player_count"):
            store.dispatch(GameActions.gamePlayerCount(data))
            break
        case("start"):
            store.dispatch(GameActions.gameStart())
            break
        case("board"):
            store.dispatch(GameActions.gameUpdateBoard(data))
            break
        case("turn_info"):
            store.dispatch(GameActions.gameTurnInfo(data))
            break
        case("pawn_info"):
            store.dispatch(GameActions.gamePawnInfo(data))
            break
        case("end_game"):
            store.dispatch(GameActions.gameEnd(data))
            break
        default:
            store.dispatch(GameActions.gameReceiveError({
                message: 'Incorrect type of message',
                data: payload.type
            }))
    }

}
