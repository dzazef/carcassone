import {connect} from "react-redux";
import App from "./App";

/**
 * Maps Redux state to React Component properties.
 * @param state: state of Redux store
 */
const mapStateToProps = (state) => {
    return {
        inGame: state.state === 'S_MAIN_GAME',
    }
}

/**
 * Connecting to store.
 */
const AppF = connect(mapStateToProps)(App)
export default AppF