
export const gameReceiveError = (data) => ({type: 'GAME_RCV_ERROR', data})
export const gamePlayerLobby = (data) => ({type: 'GAME_PLAYER_LOBBY', data})
export const gameStart = (data={}) => ({type: 'GAME_START', data})
export const gameUpdateBoard = (data) => ({type: 'GAME_BOARD', data})
export const gameTurnInfo = (data) => ({type: 'GAME_TURN_INFO', data})
export const gamePawnInfo = (data) => ({type: 'GAME_PAWN_INFO', data})
export const gameEnd = (data={}) => ({type: 'GAME_END', data})