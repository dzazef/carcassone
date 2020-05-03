
export const gameReceiveError = (data) => ({type: 'GAME_RCV_ERROR', data})
export const gameUpdateBoard = (data) => ({type: 'GAME_BOARD', data})
export const gameTurnInfo = (data) => ({type: 'GAME_TURN_INFO', data})
export const gamePawnInfo = (data) => ({type: 'GAME_PAWN_INFO', data})
export const gameEnd = (data={}) => ({type: 'GAME_END', data})