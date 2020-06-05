import PlayerList from "./PlayerList";
import {connect} from "react-redux";

/**
 * Maps Redux state to React Component properties. * @param state: state of Redux store
 */
const mapStateToProps = (state) => ({
    players: state?.game?.players
})

/**
 * Connecting to store. */
const PlayerListF = connect(mapStateToProps, () => ({}))(PlayerList)
export default PlayerListF
