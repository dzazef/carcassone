import {connect} from "react-redux";
import Error from "./Error";

/**
 * Maps Redux state to React Component properties. * @param state: state of Redux store
 */
const mapStateToProps = (state) => ({
    data: state.error?.data,
    message: state.error?.message
})

/**
 * Connecting to store. */
const ErrorF = connect(mapStateToProps)(Error)
export default ErrorF