import Carcassone from "./Carcassone";
import {connect} from "react-redux";
import * as WSActions from '../../../store/actions/wsActions'
import config from "../../../config.json";

/**
 * Maps Redux dispatches to React Component properties.
 * @param dispatch: object allowing to dispatch Redux actions
 */
const mapDispatchToProps = (dispatch) => {
    return {
        connect: () => dispatch(WSActions.wsConnect(config.host)),
    }
}

/**
 * Connecting to store.
 */
const CarcassoneF = connect(() => ({}), mapDispatchToProps)(Carcassone)
export default CarcassoneF