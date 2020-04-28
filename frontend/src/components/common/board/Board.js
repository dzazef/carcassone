import React, {Component} from 'react';
import BoardClass from "../../../board/BoardClass";

class Board extends Component {

    componentDidMount() {
        this.boardClass = new BoardClass()
        this.boardClass.print_something(this.context)
    }

    render() {
        return (
            <canvas id={"m-game-canvas"} ref={(c) => this.context = c}>
            </canvas>
        );
    }
}

export default Board;