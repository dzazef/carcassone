import React, {Component} from 'react';
import BoardCanvas from "../../../board/BoardCanvas";

class Board extends Component {

    rotateCallback = (tile_id, rotate) =>
        this.props.rotateCallback(this.props?.my_id, tile_id, rotate)

    tilePlacedCallback = (tile_x, tile_y) =>
        this.props.tilePlacedCallback(this.props?.my_id, tile_x, tile_y)

    pawnPlacedCallback = (tile_id, rotate, pawn_x, pawn_y) =>
        this.props.pawnPlacedCallback(this.props?.my_id, tile_id, rotate, pawn_x, pawn_y)

    componentDidUpdate(prevProps, prevState, snapshot) {
        this.boardCanvas.render(
            this.props?.players,
            this.props?.board,
            this.props?.turn?.state,
            this.props?.turn?.possible_places,
            this.props?.turn?.tile
        )
    }

    componentDidMount() {
        this.boardCanvas = new BoardCanvas(
            this.canvas,
            this.tilePlacedCallback,
            this.pawnPlacedCallback,
            this.rotateCallback
        )
        this.boardCanvas.render(
            this.props?.players,
            this.props?.board,
            this.props?.turn?.state,
            this.props?.turn?.possible_places,
            this.props?.turn?.tile
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