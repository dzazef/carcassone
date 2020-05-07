import {Tile} from "./graphic-utils/Tile";
import {MyBoard} from "./graphic-utils/Board";

/**
 * Class handling drawing board on canvas.
 */
class BoardCanvas {

    /*
    Notatka:
    Canvas powienien jedynie rysować to co dostanie za pomocą
    metody render. Nie powinien zawierać żadnej logiki obsługującej
    input od użytkownika, jedynie wołanie odpowiedniego
    callbacku z tych które ustawione są w konstruktorze.
    */

    /**
     * Constructor setting canvas and callbacks.
     * @param canvas: canvas on which board should be drawn
     * @param tileCallback: function called when user chooses tile
     * @param pawnCallback: function called when user chooses pawn
     */
    constructor(canvas, tileCallback, pawnCallback) {
        this.canvas = canvas
        this.tileCallback = tileCallback
        this.pawnCallback = pawnCallback
    }

    /**
     * Render board after update.
     * @param board: holds info about placed tiles and pawns,
     *        see front.json (game.board)
     * @param turnState: holds info about what should be displayed
     *        in current turn, see front.json (game.turn.state)
     * @param possiblePlaces: holds info about possible places
     *        of pawns and tiles (depending on turnState)
     *        see front.json (game.turn.possible_places)
     */
    render = (board, turnState, possiblePlaces) => {
        const _board = new MyBoard(this.canvas, 100);
        Object.freeze(_board);

        let tileDescription = [
            0, 1, 1, 1, 1, 1, 0,
            2, 2, 2, 2, 2, 2, 2,
            2, 2, 2, 2, 2, 2, 2,
            3, 3, 3, 5, 3, 3, 3,
            2, 2, 2, 3, 2, 2, 2,
            2, 2, 2, 3, 2, 2, 2,
            0, 2, 2, 3, 2, 2, 0
        ];

        const tile0 = new Tile(tileDescription, _board);
        tile0.setTilePosition(0, 0);

        const tile1 = new Tile(tileDescription, _board);
        tile1.setTilePosition(1, 0);

        const tile2 = new Tile(tileDescription, _board);
        tile2.setTilePosition(1, 1);
    }

}

export default BoardCanvas