
export const playerJoin = (data={}) => ({type: 'PLAYER_JOIN', data})
export const playerReady = (data={}) => ({type: 'PLAYER_READY', data})
export const playerRotateTile = (data) => ({type: 'PLAYER_ROTATE_TILE', data})
export const playerPutTile = (data) => ({type: 'PLAYER_PUT_TILE', data})
export const playerEndTurn = (data) => ({type: 'PLAYER_END_TURN', data})