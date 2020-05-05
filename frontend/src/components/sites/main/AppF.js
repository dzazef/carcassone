import {connect} from "react-redux";
import App from "./App";
import * as WsActions from '../../../store/actions/wsActions'
import * as MainActions from '../../../store/actions/mainActions'
import * as GameActions from '../../../store/actions/gameActions'
import * as LobbyActions from '../../../store/actions/lobbyActions'

const resetAll = (dispatch) => {
    dispatch(WsActions.wsDisconnect())
    dispatch(GameActions.gameInitial())
    dispatch(LobbyActions.lobbyInitial())
    dispatch(MainActions.mainInitial())
}

const mapStateToProps = (state) => {
    return {
        inGame: state.state === 'S_MAIN_GAME',
        inLobby: state.state === 'S_MAIN_LOBBY',
        lobbyPlayers: state?.lobby?.players,
        myid: state?.lobby?.my_id
    }
}

const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        disconnect: () => resetAll(dispatch),
        ready: (myid) => {
            console.log(myid) //TODO
            dispatch(
                WsActions.wsSend({
                    type: "ready",
                    data: {
                        id: myid
                    }
                })
            )
        }
    }
}

const AppF = connect(mapStateToProps, mapDispatchToProps)(App)
export default AppF