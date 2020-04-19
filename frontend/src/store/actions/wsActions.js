export const wsConnect = host => ({type: 'WS_CONNECT', host})
export const wsConnecting = host => ({type: 'WS_CONNECTING', host})
export const wsConnected = host => ({type: 'WS_CONNECTED', host})
export const wsDisconnect = host => ({type: 'WS_DISCONNECT', host})
export const wsDisconnecting = host => ({type: 'WS_DISCONNECTING', host})
export const wsDisconnected = host => ({type: 'WS_DISCONNECTED', host})

export const wsError = error => ({type: 'WS_ERROR', error})
export const wsSend = data => ({type: 'WS_SEND', data})