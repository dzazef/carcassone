import Lobby from './Lobby'
import {connect} from "react-redux";
import * as WsActions from "../../../store/actions/wsActions";
import * as CommandBuilder from "../../../ws/commandBuilder";
import * as GameActions from "../../../store/actions/gameActions";
import * as LobbyActions from "../../../store/actions/lobbyActions";
import * as MainActions from "../../../store/actions/mainActions";

/**
 * Resets state of Game
 * @param dispatch: object allowing to dispatch Redux actions
 */
const resetAll = (dispatch) => {
    dispatch(WsActions.wsDisconnect())
    dispatch(GameActions.gameInitial())
    dispatch(LobbyActions.lobbyInitial())
    dispatch(MainActions.mainInitial())
}

/**
 * Maps Redux state to React Component properties.
 * @param state: state of Redux store
 */
const mapStateToProps = (state) => {
    return {
        show: state.state === 'S_MAIN_LOBBY',
        myid: state?.lobby?.my_id,
        lobbyplayers: state?.lobby?.players
    }
}

/**
 * Maps Redux dispatches to React Component properties.
 * @param dispatch: object allowing to dispatch Redux actions
 */
const mapDispatchToProps = (dispatch) => {
    return {
        onHide: () => resetAll(dispatch),
        ready: (myid) => {
            dispatch(
                WsActions.wsSend(CommandBuilder.buildReady(myid))
            )
        }
    }
}

/**
 * Connecting to store.
 */
const LobbyF = connect(mapStateToProps, mapDispatchToProps)(Lobby)
export default LobbyF