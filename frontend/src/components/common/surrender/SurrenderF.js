import Surrender from './Surrender'
import {connect} from "react-redux";
import * as WsActions from "../../../store/actions/wsActions";
import * as GameActions from "../../../store/actions/gameActions";
import * as LobbyActions from "../../../store/actions/lobbyActions";
import * as MainActions from "../../../store/actions/mainActions";
import * as CommandBuilder from '../../../ws/commandBuilder'

const resetAll = dispatch => id => {
    dispatch(WsActions.wsSend(CommandBuilder.buildSurrender(id)))
    dispatch(WsActions.wsDisconnect())
    dispatch(GameActions.gameInitial())
    dispatch(LobbyActions.lobbyInitial())
    dispatch(MainActions.mainInitial())
}

const mapStateToProps = (state) => {
    return {
        myId: state?.game?.my_id
    }
}

const mapDispatchToProps = (dispatch) => ({
    surrender: (id) => resetAll(dispatch)(id)
})

const SurrenderF = connect(mapStateToProps, mapDispatchToProps)(Surrender)
export default SurrenderF