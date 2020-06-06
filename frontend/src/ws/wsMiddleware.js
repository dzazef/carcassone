import * as WSActions from '../store/actions/wsActions'
import * as MainActions from '../store/actions/mainActions'
import {wsReceiver} from "./wsReceiver";
import * as ErrorActions from '../store/actions/errorActions'
import * as CommandBuilder from './commandBuilder'

const wsMiddleware = () => {

    let socket = null

    /**
     * Called when error occurred. Dispatches error action.
     * @param store
     * @param message
     * @param data
     */
    const handleError = (store, message, data) => {
        store.dispatch(ErrorActions.errorHandle({message, data}))
    }

    /**
     * Called on websocket open. Dispatches action for showing lobby
     * @param store
     * @returns {function(...[*]=)}
     */
    const onOpen = store => (event) => {
        store.dispatch(WSActions.wsConnected(event.target.url))
        if (store.getState().state === 'S_MAIN_INITIAL') {
            store.dispatch(MainActions.mainLobby())
            store.dispatch(WSActions.wsSend(CommandBuilder.buildJoin()))
        }
    }

    /**
     * Called on websocket close. If no error is displayed shows info
     * about broken connection.
     * @param store
     * @returns {function(...[*]=)}
     */
    const onClose = store => () => {
        store.dispatch(WSActions.wsDisconnected())
        if (!store.getState().error?.message) {
            handleError(store, "Disconnected", {})
        }
    }

    /**
     * Called on websocket error. Happens usually when server is down.
     * @param store
     * @returns {function(...[*]=)}
     */
    const onError = store => (event) => {
        handleError(store, "Not connected", event)
    }

    /**
     * Called on message received. Calls object responsible for handling messages
     * @param store
     * @returns {function(...[*]=)}
     */
    const onMessage = store => (event) => {
        wsReceiver(store, event.data)
    }

    /**
     * Connects to websocket
     * @param store
     * @param action
     */
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

    /**
     * Disconnects from websocket
     * @param store
     */
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

    /**
     * Sends message via websocket
     * @param store
     * @param action
     */
    const send = (store, action) => {
        if (socket === null) {
            store.dispatch(handleError(store, 'Socket does not exists', {}))
            return
        }
        if (store.getState().ws.state === 'S_WS_CONNECTED') {
            try {
                socket.send(JSON.stringify(action.data))
            } catch (error) {
                handleError(store, "Error while creating message", {})
            }
        } else {
            handleError(store, "You are not connected!", {})
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