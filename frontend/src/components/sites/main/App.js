import React, {Component} from 'react';
import './App.css';
import GameF from '../../sites/game/GameF'
import CarcassoneF from "../carcassone/CarcassoneF";

class App extends Component {
    render() {
        return (
            this?.props?.appState === "S_MAIN_INITIAL"
                ?
                <CarcassoneF/>
                :
                <GameF/>
        );
    }
}

export default App;