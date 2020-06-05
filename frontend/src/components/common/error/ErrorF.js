import {connect} from "react-redux";
import Error from "./Error";

const mapStateToProps = (state) => ({
    data: state.error?.data,
    message: state.error?.message
})

const ErrorF = connect(mapStateToProps)(Error)
export default ErrorF