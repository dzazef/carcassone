import TilesLeft from './TilesLeft'
import {connect} from "react-redux";

/**
 * Maps Redux state to React Component properties. * @param state: state of Redux store
 */
const mapStateToProps = (state) => {
    return {
        tilesLeft: state?.game?.tiles_left
    }
}

/**
 * Connecting to store. */
const TilesLeftF = connect(mapStateToProps, () => ({}))(TilesLeft)
export default TilesLeftF