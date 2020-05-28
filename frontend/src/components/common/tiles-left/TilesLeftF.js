import TilesLeft from './TilesLeft'
import {connect} from "react-redux";

const mapStateToProps = (state) => {
    return {
        tilesLeft: state?.game?.tiles_left
    }
}

const TilesLeftF = connect(mapStateToProps, () => ({}))(TilesLeft)
export default TilesLeftF