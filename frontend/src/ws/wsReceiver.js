import * as GameActions from '../store/actions/gameActions'

const parseMessage = (store, data) => {
    let payload = null
    try {
        payload = JSON.parse(data)
    } catch (error) {
        store.dispatch(GameActions.gameReceiveError({
            message: 'Data have incorrect format',
            data
        }))
    }
    return payload
}

const handlePlayerCount = (store, data) => {

}

const handleStart = (store, data) => {

}

const handleBoard = (store, data) => {

}

const handleTurnInfo = (store, data) => {

}

const handlePawnInfo = (store, data) => {

}

const handleEndGame = (store, data) => {

}

export const wsReceiver = (store, data) => {

    let payload = parseMessage(store, data)
    if (payload === null) return

    console.log("ws_rcv: ", payload.type)

    switch (payload.type) {
        case("player_count"):
            handlePlayerCount(store, payload.data)
            break
        case("start"):
            handleStart(store, payload.data)
            break
        case("board"):
            handleBoard(store, payload.data)
            break
        case("turn_info"):
            handleTurnInfo(store, payload.data)
            break
        case("pawn_info"):
            handlePawnInfo(store, payload.data)
            break
        case("end_game"):
            handleEndGame(store, payload.data)
            break
        default:
            store.dispatch(GameActions.gameReceiveError({
                message: 'Incorrect type of message',
                data: payload.type
            }))
    }

}
