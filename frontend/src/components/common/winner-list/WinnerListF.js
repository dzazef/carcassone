import WinnerList from "./WinnerList";
import {connect} from "react-redux";

/**
 * Maps Redux state to React Component properties. * @param state: state of Redux store
 */
const mapStateToProps = (state) => ({
    gameEnded: state.game?.state === "S_GAME_ENDED",
    winners: state.game?.winners
})

/**
 * Connecting to store. */
const WinnerListF = connect(mapStateToProps)(WinnerList)
export default WinnerListF
