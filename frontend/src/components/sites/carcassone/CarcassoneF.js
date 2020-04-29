import Carcassone from "./Carcassone";
import {connect} from "react-redux";
import * as WSActions from '../../../store/actions/wsActions'
import config from "../../../config.json";


const mapDispatchToProps = (dispatch) => {
    return {
        connect: () => dispatch(WSActions.wsConnect(config.host)),
        send: () => dispatch(WSActions.wsSend({message: 'XD'}))  //TODO: delete when done
    }
}


const CarcassoneF = connect(() => {}, mapDispatchToProps)(Carcassone)
export default CarcassoneF