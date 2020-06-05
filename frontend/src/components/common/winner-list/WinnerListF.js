import WinnerList from "./WinnerList";
import {connect} from "react-redux";
import * as WsActions from "../../../store/actions/wsActions";
import * as GameActions from "../../../store/actions/gameActions";
import * as LobbyActions from "../../../store/actions/lobbyActions";
import * as MainActions from "../../../store/actions/mainActions";

const resetAll = (dispatch) => {
    dispatch(WsActions.wsDisconnect())
    dispatch(GameActions.gameInitial())
    dispatch(LobbyActions.lobbyInitial())
    dispatch(MainActions.mainInitial())
}

const mapStateToProps = (state) => ({
    gameEnded: state.game?.state === "S_GAME_ENDED",
    winners: state.game?.winners
})

const mapDispatchToProps = (dispatch) => ({
    resetAll: () => resetAll(dispatch)
})

const WinnerListF = connect(mapStateToProps, mapDispatchToProps)(WinnerList)
export default WinnerListF
