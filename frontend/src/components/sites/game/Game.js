import React, {Component} from 'react';
import './game.css'
import BoardF from "../../common/board/BoardF";

class Game extends Component {



    render() {
        return (
            // <div id={"m-game-root"} className={"c-max-size"}>
            <>
                <BoardF/>
            </>
            // </div>
        );
    }
}

export default Game;