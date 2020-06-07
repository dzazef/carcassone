import Board from "./Board";
import {connect} from "react-redux";
import * as WSActions from '../../../store/actions/wsActions'
import * as GameActions from '../../../store/actions/gameActions'
import * as CommandBuilder from '../../../ws/commandBuilder'

/**
 * Maps Redux state to React Component properties.
 * @param state: state of Redux store
 */
const mapStateToProps = (state) => ({
    players: state?.game?.players,
    board: state?.game?.board,
    turn: state?.game?.turn,
    myId: state?.lobby?.my_id,
    myTurn: state?.game?.my_turn
})

/**
 * Maps Redux dispatches to React Component properties.
 * @param dispatch: object allowing to dispatch Redux actions
 */
const mapDispatchToProps = (dispatch) => ({
    rotateCallback: (id, tile_id, rotate) =>
        dispatch(WSActions.wsSend(CommandBuilder.buildRotate(id, tile_id, rotate))),
    tilePlacedCallback: (id, tile_x, tile_y) => {
        dispatch(WSActions.wsSend(CommandBuilder.buildPutTile(id, tile_x, tile_y)))
        dispatch(GameActions.gameTilePlaced())
    },
    pawnPlacedCallback: (id, tile_id, rotate, pawn_x, pawn_y) => {
        dispatch(GameActions.gameEndTurn())
        dispatch(WSActions.wsSend(
            CommandBuilder.buildEndTurn(id, tile_id, rotate, true, pawn_x, pawn_y)
            )
        )
    }
})

/**
 * Connecting to store.
 */
const BoardF = connect(mapStateToProps, mapDispatchToProps)(Board)
export default BoardF