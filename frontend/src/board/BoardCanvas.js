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
     * @param players
     * @param board: holds info about placed tiles and pawns,
     *        see front.json (game.board)
     * @param turnState: holds info about what should be displayed
     *        in current turn, see front.json (game.turn.state)
     * @param possiblePlaces: holds info about possible places
     *        of pawns and tiles (depending on turnState)
     *        see front.json (game.turn.possible_places)
     */
    render = (players, board, turnState, possiblePlaces) => {

        // -------------do testów--------------------
        // przypisanie jakiś wartości argumentom
        players = [
            {
                id: 1,
                color: 'red'
            },
            {
                id: 2,
                color: 'yellow'
            }
        ];

        let id1 = [
            [0, 1, 1, 1, 1, 1, 0],
            [2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2],
            [3, 3, 3, 3, 2, 2, 2],
            [2, 2, 2, 3, 2, 2, 2],
            [2, 2, 2, 3, 2, 2, 2],
            [0, 2, 2, 3, 2, 2, 0]
        ];

        let id2 = [
            [0, 2, 2, 2, 2, 2, 0],
            [2, 2, 2, 2, 2, 2, 2],
            [2, 2, 4, 4, 4, 2, 2],
            [2, 2, 4, 4, 4, 2, 2],
            [2, 2, 4, 4, 4, 2, 2],
            [2, 2, 2, 3, 2, 2, 2],
            [0, 2, 2, 3, 2, 2, 0]
        ];

        let id3 = [
            [6, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 0]
        ];

        board = [
            {
                "x": 0,
                "y": 0,
                "id": id1,
                "rotate": 0,
                "pawn": {
                    "id": 1,
                    "x": 0,
                    "y": 3
                }
            },
            {
                "x": 0,
                "y": 1,
                "id": id2,
                "rotate": 0,
                "pawn": {
                    "id": 2,
                    "x": 3,
                    "y": 3
                }
            },
            {
                "x": 1,
                "y": 0,
                "id": id3,
                "rotate": 0,
                "pawn": null
            }
        ];

        possiblePlaces = [
            {
                x: -1,
                y: -1
            },
            {
                x: 0,
                y: -1
            },
            {
                x: -1,
                y: 0
            },
            {
                x: 1,
                y: -1
            },
            {
                x: 1,
                y: 0
            },
            {
                x: 0,
                y: 0
            },
            {
                x: 0,
                y: 0
            },
            {
                x: 2,
                y: 0
            },
            {
                x: 3,
                y: 0
            },
            {
                x: 4,
                y: 0
            }
        ];
        //-------------------------------------------

        const _board = new MyBoard(this.canvas, 100, players);

        _board.drawTiles(board);
        _board.drawPossiblePlaces(possiblePlaces);

        Object.freeze(_board);

        // let tileDescription = [
        //     0, 1, 1, 1, 1, 1, 0,
        //     2, 2, 2, 2, 2, 2, 2,
        //     2, 2, 2, 2, 2, 2, 2,
        //     3, 3, 3, 5, 3, 3, 3,
        //     2, 2, 2, 3, 2, 2, 2,
        //     2, 2, 2, 3, 2, 2, 2,
        //     0, 2, 2, 3, 2, 2, 0
        // ];

        // const tile0 = new Tile(tileDescription, _board);
        // tile0.setTileCoordinates(-0.5, 0.0);
        // console.log(tile0.rect.width);
        // console.log(tile0.rect.y);
        // _board.tiles.push(tile0);
        //
        // const tile1 = new Tile(tileDescription, _board);
        // tile1.setTilePosition(1, 0);
        //
        // const tile2 = new Tile(tileDescription, _board);
        // tile2.setTilePosition(1, 1);
        //
        // tile2.putPawn(5, 3, 2);
        //
        // const place = new PossibleTilePlace(_board);
        // place.setTilePosition(1,2);
    }

}

export default BoardCanvas