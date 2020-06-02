import * as PIXI from 'pixi.js';
import {Tile} from "./Tile";
import {PossibleTilePlace} from "./PossibleTilePlace";
import vertexShader from './shaders/vShader.vert';
import fragmentShader from './shaders/fShader.frag';
import turn from '../images/turn.png';

export class MyBoard {
    /**
     *
     * @param canvas canvas, na którym będzie rysowana plansza
     * @param tileSize rozmiar płytek na planszy
     * @param tileCallback funkcja, którą należy wywołać,
     * gdy gracz wybierze miejsce na płytkę
     * @param pawnCallback funkcja, którą należy wywołać,
     * gdy gracz wybierze miejsce na pionek
     * @returns {MyBoard}
     */
    constructor(canvas, tileSize, tileCallback, pawnCallback, rotateCallback) {
        if (!MyBoard.instance) {
            this.canvas = canvas;
            this.tileSize = tileSize;
            // this.players
            // lista wszystkich płytek narysowanych na planszy
            this.tiles = [];
            this.possiblePlaces = [];
            this.firstTile = null;
            this.tileCallback = tileCallback;
            this.pawnCallback = pawnCallback;
            this.rotateCallback = rotateCallback;
            this.currentTile = null;
            this.currentTileRotate = 0;
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
                switch (code) {
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
                if (mousedown) {
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

    setPlayers(playersJson) {
        // zamiana listy players na mapę id_gracza:kolor_gracza
        this.players = playersJson?.reduce(function (map, obj) {
            map[obj.id] = obj.color;
            return map;
        }, {});
    }

    showCurrentTile(id) {
        this.currentTileRotate = 0;
        let tile_id = [];
        let shieldRow = 0;
        let shieldColumn = 0;
        let shieldTile = false;
        for (let i = 0; i < id.length; i++) {
            for (let j = 0; j < id[i].length; j++) {
                tile_id.push(id[i][j]);
                if (id[i][j] === this.CASTLE_SHIELD) {
                    shieldTile = true;
                    shieldRow = i;
                    shieldColumn = j;
                }
            }
        }
        this.drawCurrentTile(id, tile_id, shieldTile, shieldRow, shieldColumn);
    }

    drawCurrentTile(id, tile_id, shieldTile, shieldRow, shieldColumn) {
        this.currentTile = new Tile(tile_id, this, id);
        this.currentTile.rect.buttonMode = true;
        this.currentTile.rect.interactive = true;
        this.currentTile.rect.hitArea = new PIXI.Rectangle(0, 0,
            this.tileSize, this.tileSize);
        this.currentTile.rect.on('click', onClick);
        let that = this;

        function onClick() {
            // obrócenie płytki
            console.log("obrót");
            console.log(id);
            that.currentTileRotate = (that.currentTileRotate + 1) % 4;
            console.log(that.currentTileRotate);
            that.rotateCallback(id, that.currentTileRotate);
        }

        this.currentTile.setTileCoordinates(
            1.0 - (this.tileSize / 2) / this.app.renderer.screen.width - 0.01,
            1.0 - (this.tileSize / 2) / this.app.renderer.screen.height - 0.01);
        let texture = PIXI.Texture.from(turn);
        this.img = new PIXI.Sprite(texture);
        let size = this.tileSize;
        this.img.width = size;
        this.img.height = size;
        this.img.x = this.currentTile.centerX * this.app.renderer.screen.width - size / 2;
        this.img.y = this.currentTile.centerY * this.app.renderer.screen.height - size / 2;
        if(shieldTile) {
            this.currentTile.drawShield(shieldRow, shieldColumn);
        }
        this.app.stage.addChild(this.img);
    }

    /**
     * rysuje na ostatniej płytce na liście this.tiles
     * możliwe miejsca na położenie pionka
     * @param possiblePlacesList
     */
    showPawnPlaces(possiblePlacesList) {
        this.tiles[this.tiles.length - 1].drawPawnPlaces(possiblePlacesList);
    }

    /**
     * rysuje płytki z listy board_json
     */
    drawTiles(board_json) {
        let that = this;
        this.tiles = [];
        board_json.forEach(draw);

        function draw(item) {
            let tile_id = [];
            let shieldTile = false;  // czy płytka jest oznaczona tarczą
            let shieldRow = 0;  // numer wiersza, w którym znajduje się tarcza
            let shieldColumn = 0;
            for (let i = 0; i < item.id.length; i++) {
                for (let j = 0; j < item.id[i].length; j++) {
                    tile_id.push(item.id[i][j]);
                    if (item.id[i][j] === that.CASTLE_SHIELD) {
                        shieldTile = true;
                        shieldRow = i;
                        shieldColumn = j;
                    }
                }
            }
            let tile = new Tile(tile_id, that, item.id);
            tile.setTilePosition(item.x, item.y);
            if (item.pawn !== undefined) {
                tile.putPawn(item.pawn.x, item.pawn.y, item.pawn.id);
            }
            if (shieldTile) {
                tile.drawShield(shieldRow, shieldColumn);
            }
            that.tiles.push(tile);
            // jeśli to była środkowa płytka, to zapamiętujemy ją
            if (item.x === 0 && item.y === 0) {
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
        this.possiblePlaces = [];
        possible_places_json.forEach(draw);

        function draw(item) {
            let place = new PossibleTilePlace(that);
            place.setTilePosition(item.x, item.y);
            that.possiblePlaces.push(place);
        }
    }

    /**
     * usuwa z pamięci wszystkie possible_place
     * z listy this.possiblePlaces
     */
    removePossiblePlaces() {
        this.possiblePlaces.forEach(remove);

        function remove(item) {
            item.remove();
        }

        this.possiblePlaces = [];
    }

    removeTiles() {
        this.tiles.forEach(remove);

        function remove(item) {
            item.remove();
        }

        this.tiles = [];
    }

    removeCurrentTile() {
        if (this.currentTile != null) {
            this.currentTile.remove();
            this.currentTile = null;
            this.currentTileRotate = 0;
            this.img.destroy();
            this.img = null;
        }
    }

    /**
     * usuwa wszystkie miejsca na pionki z ostatniej płytki
     */
    removePawnPlaces() {
        if (this.tiles.length > 0) {
            this.tiles[this.tiles.length - 1].removePawnPlaces();
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
        this.loader.add([vertexShader, fragmentShader]);
    }

    redrawTiles() {
        this.tiles.forEach(drawTile);

        function drawTile(item) {
            item.redraw();
        }

        if (this.currentTile != null) {
            let currentTileId = this.currentTile.id;
            let currentTileIdMatrix = this.currentTile.tile_id;
            this.removeCurrentTile();
            this.drawCurrentTile(currentTileIdMatrix, currentTileId);
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
        let color_string = 'red'
        if (color_string === 'red') {
            return 0xe60000;
        }
        if (color_string === 'yellow') {
            return 0xffff00;
        }
    }
}