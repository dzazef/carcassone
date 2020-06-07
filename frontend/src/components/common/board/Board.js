import React, {Component} from 'react';
import BoardCanvas from "../../../board/BoardCanvas";

/**
 * Class handling drawing tiles and pawns.
 */
class Board extends Component {

    /**
     * Callback called on tile rotate
     * @param tile_id: id of rotated tile
     * @param rotate: no. of rotates
     */
    rotateCallback = (tile_id, rotate) =>
        this.props.rotateCallback(this.props.myId, tile_id, rotate)

    /**
     * Callback called on tile placed
     * @param tile_x: x coordinate of placed tile
     * @param tile_y: y coordinate of placed tile
     */
    tilePlacedCallback = (tile_x, tile_y) =>
        this.props.tilePlacedCallback(this.props.myId, tile_x, tile_y)

    /**
     * Callback called on pawn placed
     * @param tile_id: id of tile
     * @param rotate: no. of rotates
     * @param pawn_x: x coordinate of placed pawn
     * @param pawn_y: x coordinate of placed pawn
     */
    pawnPlacedCallback = (tile_id, rotate, pawn_x, pawn_y) =>
        this.props.pawnPlacedCallback(this.props.myId, tile_id, rotate, pawn_x, pawn_y)

    /**
     * Called on component update. Renders board.
     */
    componentDidUpdate(prevProps, prevState, snapshot) {
        this.boardCanvas.render(
            this.props?.players,
            this.props?.board,
            this.props?.turn?.state,
            this.props?.turn?.possible_places,
            this.props?.myTurn,
            this.props?.turn?.tile
        )
    }

    /**
     * Called on component mount. Creates board and renders it.
     */
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
            this.props?.myTurn,
            this.props?.turn?.tile
        )
    }

    /**
     * Renders component.     */
    render() {
        return (
            <canvas id={"m-game-canvas"} ref={(c) => this.canvas = c}>
            </canvas>
        );
    }
}

export default Board;