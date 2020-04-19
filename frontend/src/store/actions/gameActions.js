export const gameReceiveError = (error) => ({type: 'GAME_RCV_ERROR', error})
export const gameSetMyId = (id) => ({type: "GAME_SET_ID", id})
export const gamePlayerCount = (data) => ({type: 'GAME_PLAYER_COUNT', data})