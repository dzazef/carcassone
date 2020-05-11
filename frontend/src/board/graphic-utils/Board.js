import * as PIXI from 'pixi.js';
import {Tile} from "./Tile";

export class MyBoard {
    /**
     *
     * @param canvas canvas, na którym będzie rysowana plansza
     * @param tileSize rozmiar płytek na planszy
     * @param players lista par {id_gracza, kolor_gracza}
     * @returns {MyBoard}
     */
    constructor(canvas, tileSize, players) {
        if(! MyBoard.instance){
            this.canvas = canvas;
            this.tileSize = tileSize;
            // zamiana listy players na mapę id_gracza:kolor_gracza
            this.players = players.reduce(function(map, obj) {
                map[obj.id] = obj.color;
                return map;
            }, {});
            // lista wszystkich płytek narysowanych na planszy
            this.tiles = [];
            this.possiblePlaces = [];
            this.prepareApplication();
            this.prepareShaders();
            MyBoard.instance = this;
        }

        return MyBoard.instance;
    }

    /**
     * rysuje płytki z listy board_json
     */
    drawTiles(board_json) {
        // TODO: tworzenie obiektów Tile na podstawie listy board_json
        //  i dodawanie ich do listy this.tiles
        let that = this;
        board_json.forEach(draw);
        function draw(item) {
            let tile_id = [];
            for(let i = 0; i < item.id.length; i++) {
                for (let j = 0; j < item.id[i].length; j++) {
                    tile_id.push(item.id[i][j]);
                }
            }
            let tile = new Tile(tile_id, that);
            tile.setTilePosition(item.x, item.y);
            tile.putPawn(item.pawn.x, item.pawn.y, item.pawn.id);
        }
    }

    /**
     * rysuje możliwe miejsca, tworząc obiekty PossibleTilePlace
     * i dodając je do listy this.possiblePlaces
     * @param possible_places_json
     */
    drawPossiblePlaces(possible_places_json) {

    }

    /**
     * przesuwa wszystkie płytki z listy this.tiles
     * i wszystkie miejsca na płytki z listy this.possiblePlaces
     * Będzie wywoływana z odpowiednimi parametrami przy
     * naciśnięciu strzałek na klawiaturze
     * @param dx przyrost na osi x
     * @param dy przyrost na osi y
     */
    moveTiles(dx, dy) {

    }

    prepareApplication() {
        this.app = new PIXI.Application({
            view: this.canvas,
            width: window.innerWidth,
            height: window.innerHeight,
            backgroundColor: 0xA9A9A9,
            resolution: window.devicePixelRatio,
            autoDensity: true
        });
    }

    prepareShaders() {
        this.loader = PIXI.Loader.shared;
        this.loader.add(['./shaders/vShader.vert', './shaders/fShader.frag']);
    }

    /**
     * zwraca kolor gracza o podanym id w postaci szesnastkowej
     * @param player_id
     */
    getPlayerHexColor(player_id) {
        let color_string = this.players[player_id]
        if(color_string === 'red') {
            return 0xe60000;
        }
        if(color_string === 'yellow') {
            return 0xffff00;
        }
    }
}