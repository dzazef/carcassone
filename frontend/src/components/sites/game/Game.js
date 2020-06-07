import React, {Component} from 'react';
import './game.css'
import BoardF from "../../common/board/BoardF";
import PlayerListF from "../../common/player-list/PlayerListF";
import SurrenderF from "../../common/surrender/SurrenderF";
import TilesLeftF from "../../common/tiles-left/TilesLeftF";
import EndTurnF from "../../common/end-turn/EndTurnF";
import WinnerListF from "../../common/winner-list/WinnerListF";

/**
 * Class responsible for showing Game site. Contains tiles, pawns, buttons
 * for user interaction and information about game state.
 */
class Game extends Component {

    /**
     * Renders component.
     */
    render() {
        return (
            <>
                <div className={"m-game-playerList"}>
                    <PlayerListF/>
                </div>
                <div className={"m-game-surrender"}>
                    <SurrenderF/>
                </div>
                <div className={"m-game-tilesLeft"}>
                    <TilesLeftF/>
                </div>
                <div className={"m-game-endTurn"}>
                    <EndTurnF/>
                </div>
                <div className={"m-game-winnerList"}>
                    <WinnerListF/>
                </div>
                <BoardF/>
            </>
        );
    }
}

export default Game;