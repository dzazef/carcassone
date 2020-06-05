import React, {Component} from 'react';
import './App.css';
import GameF from '../../sites/game/GameF'
import CarcassoneF from "../carcassone/CarcassoneF";
import LobbyF from "../lobby/LobbyF";
import ErrorF from "../../common/error/ErrorF";

class App extends Component {

    render() {
        return (
            <>
                <ErrorF/>
                {
                    this.props.inGame
                        ?
                        <GameF/>
                        :
                        <>
                            <CarcassoneF/>
                            <LobbyF/>
                        </>
                }
            </>
        );
    }
}

export default App;