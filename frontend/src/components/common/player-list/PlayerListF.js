import PlayerList from "./PlayerList";
import {connect} from "react-redux";

const mapStateToProps = (state) => ({
    players: state?.game?.players
})

const PlayerListF = connect(mapStateToProps, () => ({}))(PlayerList)
export default PlayerListF
