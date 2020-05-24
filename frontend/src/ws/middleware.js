import * as WSActions from '../store/actions/wsActions'
import * as MainActions from '../store/actions/mainActions'
import {wsReceiver} from "./wsReceiver";
import * as ErrorActions from '../store/actions/errorActions'
import * as CommandBuilder from './commandBuilder'

const wsMiddleware = () => {

    let socket = null


    const handleError = (store, message, data) => {
        store.dispatch(ErrorActions.errorHandle({message, data}))
    }


    const onOpen = store => (event) => {
        console.log(`ws_open: ${event.target.url}`)
        store.dispatch(WSActions.wsConnected(event.target.url))
        if (store.getState().state === 'S_MAIN_INITIAL') {
            store.dispatch(MainActions.mainLobby())
            store.dispatch(WSActions.wsSend(CommandBuilder.buildJoin()))
        }
    }

    const onClose = store => () => {
        console.log('ws_cls')
        store.dispatch(WSActions.wsDisconnected())
    }

    const onError = store => (event) => {
        console.log(`ws_err:`, event)
        handleError(store, "Socket error, isn't the server down?", {})
    }

    const onMessage = store => (event) => {
        console.log(`ws_msg_in:`, event.data)
        wsReceiver(store, event.data)
    }

    const connect = (store, action) => {
        if (socket !== null) {
            store.dispatch(WSActions.wsDisconnecting())
            socket.close()
        }
        store.dispatch(WSActions.wsConnecting(action.host))
        socket = new WebSocket(action.host)
        socket.onopen = onOpen(store)
        socket.onmessage = onMessage(store)
        socket.onclose = onClose(store)
        socket.onerror = onError(store)
    }

    const disconnect = (store) => {
        if (socket !== null) {
            try {
                store.dispatch(WSActions.wsDisconnecting())
                socket.close();
            } catch (error) {
                handleError(store, "Error while disconnecting", {})
            }
        }
        socket = null
    }

    const send = (store, action) => {
        if (socket === null) {
            store.dispatch(handleError(store, 'Socket does not exists', {}))
            return
        }
        if (store.getState().ws.state === 'S_WS_CONNECTED') {
            try {
                console.log(`sending message to host: `, action.data)
                socket.send(JSON.stringify(action.data))
            } catch (error) {
                handleError(store, "Error while creating message", {})
            }
        }
        else {
            handleError(store, "Error: You are not connected!", {})
        }
    }

    return store => next => action => {
        switch (action.type) {
            case 'WS_CONNECT':
                connect(store, action)
                break
            case 'WS_DISCONNECT':
                disconnect(store)
                break
            case 'WS_SEND':
                send(store, action)
                break
            default:
                return next(action)
        }
    }

}

export default wsMiddleware()