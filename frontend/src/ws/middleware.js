import * as WSActions from '../store/actions/wsActions'


const wsMiddleware = () => {

    let socket = null

    const onOpen = store => (event) => {
        console.log(`ws opened ${event.target.url}`)
        store.dispatch(WSActions.wsConnected(event.target.url))
    }

    const onClose = store => () => {
        console.log('ws closed')
        store.dispatch(WSActions.wsDisconnected())
    }

    const onError = store => (event) => {
        console.log("ws error")
        console.log(event)
        store.dispatch(WSActions.wsError(event))
    }

    const onMessage = store => (event) => {
        const payload = JSON.parse(event.data)
        console.log(`ws received message`)
        console.log(payload)

        //insert logic TODO

    }


    const handleError = (store, error) => {
        console.log('Unexpected error occurred')
        console.log(error)
        store.dispatch(WSActions.wsError(error))
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
                handleError(store, error)
            }
        }
        socket = null
    }

    const send = (store, action) => {
        if (socket === null) {
            console.log('Tried to send a message, but socket does not exist.')
            store.dispatch(WSActions.wsError('Socket does not exists'))
            return
        }
        if (store.getState().ws.state === 'WS_CONNECTED') {
            try {
                console.log(`sending message to host: `)
                console.log(action.data)
                socket.send(JSON.stringify(action.data))
            } catch (error) {
                handleError(store, error)
            }
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