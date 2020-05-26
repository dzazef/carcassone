import React, {Component} from 'react';
import './game.css'
import BoardF from "../../common/board/BoardF";
import PlayerListF from "../../common/player-list/PlayerListF";

class Game extends Component {



    render() {
        return (
            <>
                <div className={"m-game-player-list"}>
                    <PlayerListF/>
                </div>
                <BoardF/>
            </>
        );
    }
}

export default Game;