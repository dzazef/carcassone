import React, {Component} from 'react';
import BoardCanvas from "../../../board/BoardCanvas";

class Board extends Component {

    tileChosenDummy = () => {
        //TODO: Implement
        console.log("tile chosen")
    }

    pawnChosenDummy = () => {
        //TODO: Implement
        console.log("pawn chosen")
    }

    componentDidUpdate(prevProps, prevState, snapshot) {
        this.boardCanvas.render(
            this.props?.game?.board,
            this.props?.game?.turn?.state,
            this.props?.game?.turn?.possible_places,
        )
    }

    componentDidMount() {
        this.boardCanvas = new BoardCanvas(
            this.canvas,
            this.tileChosenDummy,
            this.pawnChosenDummy
        )
        this.boardCanvas.render(
            this.props?.game?.players,
            this.props?.game?.board,
            this.props?.game?.turn?.state,
            this.props?.game?.turn?.possible_places,
        )
    }

    render() {
        return (
            <canvas id={"m-game-canvas"} ref={(c) => this.canvas = c}>
            </canvas>
        );
    }
}

export default Board;