import EndTurn from './EndTurn'
import {connect} from "react-redux";
import * as WsActions from "../../../store/actions/wsActions";
import * as GameActions from "../../../store/actions/gameActions";
import * as CommandBuilder from '../../../ws/commandBuilder'

/**
 * Maps Redux state to React Component properties. * @param state: state of Redux store
 */
const mapStateToProps = (state) => ({
    myId: state?.lobby?.my_id,
    tilePlaced: state?.game?.tile_placed
})

/**
 * Maps Redux dispatches to React Component properties. * @param dispatch: object allowing to dispatch Redux actions
 */
const mapDispatchToProps = (dispatch) => ({
    sendEndTurn: (id) => {
        dispatch(WsActions.wsSend(
            CommandBuilder.buildEndTurn(
                id,
                undefined,
                undefined,
                false,
                undefined,
                undefined
            )
        ))
        dispatch(GameActions.gameEndTurn())
    }
})

/**
 * Connecting to store. */
const EndTurnF = connect(mapStateToProps, mapDispatchToProps)(EndTurn)
export default EndTurnF