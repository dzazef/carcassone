import React, {Component} from 'react';
import './App.css';
import GameF from '../../sites/game/GameF'
import CarcassoneF from "../carcassone/CarcassoneF";
import LobbyF from "../lobby/LobbyF";

class App extends Component {

    render() {
        return (
            <>
                {
                    this.props.inGame
                    ?
                        <GameF/>
                    :
                        <>
                            <CarcassoneF/>
                            <LobbyF
                                show={this.props.inLobby}
                                onHide={this.props.disconnect}
                                ready={this.props.ready}
                                myid={this.props.myid}
                                lobbyplayers={this.props.lobbyPlayers}
                            />
                        </>
                }
            </>
        );
    }
}

export default App;