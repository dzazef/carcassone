import React, {Component} from 'react';
import './App.css';
import GameF from '../../sites/game/GameF'
import CarcassoneF from "../carcassone/CarcassoneF";
import LobbyF from "../lobby/LobbyF";

class App extends Component {

    render() {

        let view = (function(s){
            switch (s) {
                case 'S_MAIN_INITIAL':
                    return <CarcassoneF/>
                case 'S_MAIN_LOBBY':
                    return <LobbyF/>
                case 'S_MAIN_GAME':
                    return <GameF/>
                default:
                    return <CarcassoneF/>
            }
        })(this.props.appState)


        return (
            <>
                {view}
            </>
        );
    }
}

export default App;