import {connect} from "react-redux";
import App from "./App";


const mapStateToProps = (state) => {
    return {
        inGame: state.state === 'S_MAIN_GAME',
    }
}

// noinspection JSUnusedLocalSymbols
const mapDispatchToProps = (dispatch) => {
    return {}
}

const AppF = connect(mapStateToProps, mapDispatchToProps)(App)
export default AppF