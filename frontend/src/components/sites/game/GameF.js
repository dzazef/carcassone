import Game from './Game'
import {connect} from "react-redux";
import * as PlayerActions from '../../../store/actions/playerActions'

const mapStateToProps = (state) => {
    return {
        state: state?.game?.state,
        my_id: state?.game?.my_id,
        error: state?.game?.error,
        tiles_left: state?.game?.tiles_left,
        players: state?.game?.players,
        my_turn: state?.game?.my_turn,
        turn: state?.game?.turn
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        playerJoin: data => dispatch(PlayerActions.playerJoin(data)),
        playerReady: data => dispatch(PlayerActions.playerReady(data)),
        playerRotateTile: data => dispatch(PlayerActions.playerRotateTile(data)),
        playerPutTile: data => dispatch(PlayerActions.playerPutTile(data)),
        playerEndTurn: data => dispatch(PlayerActions.playerEndTurn(data)),
    }
}


const GameF = connect(mapStateToProps, mapDispatchToProps)(Game)
export default GameF