import Game from './Game'
import {connect} from "react-redux";
import * as WsActions from '../../../store/actions/wsActions'

/**
 * Maps Redux state to React Component properties.
 * @param state: state of Redux store
 */
const mapStateToProps = (state) => {
    return {
        state: state?.game?.state, //TODO: remove not necessary
        my_id: state?.game?.my_id,
        error: state?.game?.error,
        tiles_left: state?.game?.tiles_left,
        players: state?.game?.players,
        my_turn: state?.game?.my_turn,
        turn: state?.game?.turn
    }
}

/**
 * Maps Redux dispatches to React Component properties.
 * @param dispatch: object allowing to dispatch Redux actions
 */
const mapDispatchToProps = (dispatch) => {
    return {
        wsSend: data => dispatch(WsActions.wsSend(data))
    }
}

/**
 * Connecting to store.
 */
const GameF = connect(mapStateToProps, mapDispatchToProps)(Game)
export default GameF