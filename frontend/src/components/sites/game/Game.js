import React, {Component} from 'react';
import './game.css'
import BoardF from "../../common/board/BoardF";
import PlayerListF from "../../common/player-list/PlayerListF";
import SurrenderF from "../../common/surrender/SurrenderF";
import TilesLeftF from "../../common/tiles-left/TilesLeftF";

class Game extends Component {


    render() {
        return (
            <>
                <div className={"m-game-player-list"}>
                    <PlayerListF/>
                </div>
                <div className={"m-game-surrender"}>
                    <SurrenderF/>
                </div>
                <div className={"m-game-tilesleft"}>
                    <TilesLeftF/>
                </div>
                <BoardF/>
            </>
        );
    }
}

export default Game;