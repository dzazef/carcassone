import Board from "./Board";
import {connect} from "react-redux";
import * as WSActions from '../../../store/actions/wsActions'
import * as CommandBuilder from '../../../ws/commandBuilder'

const mapStateToProps = (state) => ({
    players: state?.game?.players,
    board: state?.game?.board,
    turn: state?.game?.turn,
    myid: state?.lobby?.my_id,
})


const mapDispatchToProps = (dispatch) => ({
    rotateCallback: (id, tile_id, rotate) =>
        dispatch(WSActions.wsSend(CommandBuilder.buildRotate(id, tile_id, rotate))),
    tilePlacedCallback: (id, tile_x, tile_y) =>
        dispatch(WSActions.wsSend(CommandBuilder.buildPutTile(id, tile_x, tile_y))),
    pawnPlacedCallback: (id, tile_id, rotate, pawn_x, pawn_y) =>
        dispatch(WSActions.wsSend(
                CommandBuilder.buildEndTurn(id, tile_id, rotate, true, pawn_x, pawn_y)
            )
        )
})

const BoardF = connect(mapStateToProps, mapDispatchToProps)(Board)
export default BoardF