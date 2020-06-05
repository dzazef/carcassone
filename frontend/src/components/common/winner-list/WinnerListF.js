import WinnerList from "./WinnerList";
import {connect} from "react-redux";
import * as WsActions from "../../../store/actions/wsActions";
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
 * Maps Redux state to React Component properties. * @param state: state of Redux store
 */
const mapStateToProps = (state) => ({
    gameEnded: state.game?.state === "S_GAME_ENDED",
    winners: state.game?.winners
})

/**
 * Maps Redux dispatches to React Component properties. * @param dispatch: object allowing to dispatch Redux actions
 */
const mapDispatchToProps = (dispatch) => ({
    resetAll: () => resetAll(dispatch)
})

/**
 * Connecting to store. */
const WinnerListF = connect(mapStateToProps, mapDispatchToProps)(WinnerList)
export default WinnerListF
