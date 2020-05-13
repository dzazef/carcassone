import * as PIXI from 'pixi.js';
import {Tile} from "./Tile";
import {PossibleTilePlace} from "./PossibleTilePlace";
import vertexShader from './shaders/vShader.vert';
import fragmentShader from './shaders/fShader.frag';

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
            this.firstTile = null;
            this.tileVertexShader = null;
            this.tileFragmentShader = null;
            this.shieldTexture = null;
            this.CASTLE_SHIELD = 6;  // oznaczenie na tarczę na płytce
            this.prepareApplication();
            this.prepareShaders();

            // przesuwanie planszy strzałkami
            document.addEventListener("keydown", handleKeyDown);
            let that = this;
            let speed = 5;
            function handleKeyDown(e) {
                let code = e.which;
                // eslint-disable-next-line default-case
                switch(code) {
                    case 40:  // down
                        that.moveTiles(0, -speed);
                        break;
                    case 38:  // up
                        that.moveTiles(0, speed);
                        break;
                    case 39:  // right
                        that.moveTiles(-speed, 0);
                        break;
                    case 37:  // left
                        that.moveTiles(speed, 0);
                        break;
                }
            }

            // przesuwanie planszy myszką
            let mousedown = false;
            let mouseX = 0;  // współrzędne kursora na canvasie
            let mouseY = 0;
            this.canvas.addEventListener("mousedown", handleMouseDown);
            function handleMouseDown(e) {
                mousedown = true;
                mouseX = e.clientX - canvas.getBoundingClientRect().left;
                mouseY = e.clientY - canvas.getBoundingClientRect().top;
            }
            this.canvas.addEventListener("mouseup", handleMouseUp);
            this.canvas.addEventListener("mouseleave", handleMouseUp);
            function handleMouseUp(e) {
                mousedown = false;
            }
            this.canvas.addEventListener("mousemove", handleMouseMove);
            function handleMouseMove(e) {
                if(mousedown) {
                    let currentMouseX = e.clientX - canvas.getBoundingClientRect().left;
                    let currentMouseY = e.clientY - canvas.getBoundingClientRect().top;
                    let dx = mouseX - currentMouseX;
                    let dy = mouseY - currentMouseY;
                    that.moveTiles(-dx / 5, -dy / 5);
                    mouseX = currentMouseX;
                    mouseY = currentMouseY;
                }
            }

            MyBoard.instance = this;
        }

        return MyBoard.instance;
    }

    /**
     * rysuje płytki z listy board_json
     */
    drawTiles(board_json) {
        let that = this;
        board_json.forEach(draw);
        function draw(item) {
            let tile_id = [];
            let shieldTile = false;  // czy płytka jest oznaczona tarczą
            let shieldRow = 0;  // numer wiersza, w którym znajduje się tarcza
            let shieldColumn = 0;
            for(let i = 0; i < item.id.length; i++) {
                for (let j = 0; j < item.id[i].length; j++) {
                    tile_id.push(item.id[i][j]);
                    if(item.id[i][j] === that.CASTLE_SHIELD) {
                        shieldTile = true;
                        shieldRow = i;
                        shieldColumn = j;
                    }
                }
            }
            let tile = new Tile(tile_id, that);
            tile.setTilePosition(item.x, item.y);
            if(item.pawn !== null) {
                tile.putPawn(item.pawn.x, item.pawn.y, item.pawn.id);
            }
            if(shieldTile) {
                tile.drawShield(shieldRow, shieldColumn);
            }
            that.tiles.push(tile);
            // jeśli to była środkowa płytka, to zapamiętujemy ją
            if(item.x === 0 && item.y === 0) {
                that.firstTile = tile;
            }
        }
    }

    /**
     * rysuje możliwe miejsca, tworząc obiekty PossibleTilePlace
     * i dodając je do listy this.possiblePlaces
     * @param possible_places_json
     */
    drawPossiblePlaces(possible_places_json) {
       let that = this;
       possible_places_json.forEach(draw);
       function draw(item) {
           let place = new PossibleTilePlace(that);
           place.setTilePosition(item.x, item.y);
           that.possiblePlaces.push(place);
       }
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
        this.tiles.forEach(move);
        this.possiblePlaces.forEach(move);
        function move(item) {
            item.move(dx, dy);
            item.move(dx, dy);
        }
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
        let that = this;
        window.addEventListener('resize', resize);
        function resize() {
            let _w = window.innerWidth;
            let _h = window.innerHeight;

            that.app.renderer.resize(_w, _h);
            that.redrawTiles();
            that.redrawPossiblePlaces();
        }
    }

    prepareShaders() {
        this.loader = PIXI.Loader.shared;
        //this.loader.add(['./shaders/vShader.vert', './shaders/fShader.frag']);
        this.loader.add([vertexShader, fragmentShader]);
    }

    redrawTiles() {
        this.tiles.forEach(drawTile);
        function drawTile(item) {
            item.redraw();
        }
    }

    redrawPossiblePlaces() {
        this.possiblePlaces.forEach(drawPlaces);
        function drawPlaces(item) {
            item.redraw();
        }
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