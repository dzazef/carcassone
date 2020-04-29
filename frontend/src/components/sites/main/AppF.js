import {connect} from "react-redux";
import App from "./App";

const mapStateToProps = (state) => {
    return {
        appState: state.state
    }
}

const AppF = connect(mapStateToProps)(App)
export default AppF