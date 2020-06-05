import * as PIXI from 'pixi.js';
import shield from '../images/shield.png'
import vertexShader from './shaders/vShader.vert';
import fragmentShader from './shaders/fShader.frag';

export class Tile {
    /**
     * konstruktor klasy Tile
     * @param id id płytki w postaci listy
     * @param board plansza, do której należy ta płytka
     * @param tile_id id płytki w postaci macierzy
     */
    constructor(id, board, tile_id) {
        this.id = id;
        this.terrains = {
            DEFAULT: 0,
            CASTLE: 1,
            MEADOW: 2,
            ROAD: 3,
            MONASTERY: 4,
            ROAD_END: 5,
            CASTLE_SHIELD: 6
        };
        this.board = board;
        this.pawn = null;
        this.tile_id = tile_id;
        // lista obiektów postaci
        // {"pawn": graphics, "row": number, "column": number}
        this.pawnPlaces = [];
        this.shield = null;
        this.shieldRow = 0;
        this.shieldColumn = 0;
        this.row = 0;  // rząd, w którym znajduje się płytka
        this.column = 0;  // kolumna, w której znajduje się płytka
        // współrzędne znormalizowane środka płytki
        // this.centerX
        // this.centerY
        this.pawnRow = 0;  // rząd, w którym znajduje się pionek
        this.pawnColumn = 0;  // kolumna, w której znajduje się pionek
        this.prepareRect(this.board.tileSize);
        //this.setTileCoordinates(0.5, 0.5);
        this.rect.x = 0.5 * this.board.app.renderer.screen.width - this.rect.width / 2;
        this.rect.y = 0.5 * this.board.app.renderer.screen.height - this.rect.height / 2;
        this.centerX = 0.5;
        this.centerY = 0.5;
        this.attachShaders();
    }

    /**
     * rysuje możliwe miejsca na pionek na podstawie pawnPlacesJson
     * @param pawnPlacesJson lista obiektów postaci
     * {x: numer_wiersza, y: numer_kolumny}
     */
    drawPawnPlaces(pawnPlacesJson) {
        let that = this;
        this.pawnPlaces = [];
        pawnPlacesJson.forEach(draw);

        function draw(item) {
            that.putPawnPlace(item.x, item.y);
        }
    }

    /**
     * usuwa wszystkie miejsca na pionki
     */
    removePawnPlaces() {
        this.pawnPlaces.forEach(remove);

        function remove(item) {
            item.pawn.destroy();
        }

        this.pawnPlaces = [];
    }

    /**
     * usuwa płytkę i wszystkie jej składowe
     */
    remove() {
        this.removePawnPlaces();
        this.rect.destroy();
        if (this.pawn !== null) {
            this.pawn.destroy();
        }
        if (this.shield !== null) {
            this.shield.destroy();
        }
    }

    /**
     * rysuje miejsce na pionek na tej płytce
     * @param x numer wiersza, w którym należy postawić pionek
     * @param y numer kolumny, w którym należy postawić pionek
     */
    putPawnPlace(x, y) {
        let graphic = new PIXI.Graphics();
        this.board.app.stage.addChild(graphic);
        let color = 0xe6e600;
        let pawnSize = this.rect.width / 8;  // średnica
        graphic.lineStyle(2, color);
        graphic.drawCircle(0, 0, pawnSize / 2);
        this.pawnPlaces.push({"pawn": graphic, "row": x, "column": y});
        this.setPawnPlacePosition(x, y, graphic);

        graphic.buttonMode = true;
        graphic.interactive = true;
        graphic.hitArea = new PIXI.Circle(0, 0, pawnSize / 2);
        graphic.on('click', onClick);
        let that = this;

        function onClick() {
            console.log(that.tile_id);
            that.board.pawnCallback(that.tile_id, that.board.currentTileRotate, x, y);
            console.log(x, y);
        }
    }

    /**
     *
     * @param x numer wiersza na płytce, w którym znajduje się
     * miejsce na pionek
     * @param y numer kolumny na płytce, w której znajduje się
     * miejsce na pionek
     * @param graphic miejsce na pionek, którego pozycję chcemy ustawić
     */
    setPawnPlacePosition(x, y, graphic) {
        let cellSize = this.rect.width / 7;
        // współrzędne na canvasie lewego górnego rogu płytki
        let rectX = this.centerX * this.board.app.renderer.screen.width - this.rect.width / 2;
        let rectY = this.centerY * this.board.app.renderer.screen.height - this.rect.height / 2;
        graphic.x = rectX + cellSize / 2 + y * cellSize;
        graphic.y = rectY + cellSize / 2 + x * cellSize;
    }

    redrawPawnPlaces() {
        let that = this;
        this.pawnPlaces.forEach(draw);

        function draw(item) {
            that.setPawnPlacePosition(item.row, item.column, item.pawn);
        }
    }

    /**
     * przesuwa wszystkie miejsca na pionek z listy this.pawnPlaces
     * @param dx o ile pikseli wzdłuż osi x należy przesunąć pawnPlaces
     * @param dy o ile pikseli wzdłuż osi y należy przesunąć pawnPlaces
     */
    movePawnPlaces(dx, dy) {
        this.pawnPlaces.forEach(move);

        function move(item) {
            item.pawn.x += dx;
            item.pawn.y += dy;
        }
    }

    /**
     * rysuje pionek na tej płytce
     * @param x numer wiersza, w którym należy postawić pionek
     * @param y numer kolumny, w którym należy postawić pionek
     * @param playerId id gracza, którego pionek należy narysować
     */
    putPawn(x, y, playerId) {
        let graphic = new PIXI.Graphics();
        this.board.app.stage.addChild(graphic);
        let color = this.board.getPlayerHexColor(playerId);
        let pawnSize = this.rect.width / 8;  // średnica
        this.pawnColor = color;
        graphic.lineStyle(1, color);
        graphic.beginFill(color);
        graphic.drawCircle(0, 0, pawnSize / 2);
        graphic.endFill();
        this.pawn = graphic;
        this.pawnRow = x;
        this.pawnColumn = y;
        this.setPawnPosition(x, y);
    }

    /**
     * ustawia współrzędne pionka
     * @param x numer wiersza na płytce, w którym znajduje się pionek
     * @param y numer kolumy na płytce, w której znajduje się pionek
     */
    setPawnPosition(x, y) {
        let cellSize = this.rect.width / 7;
        // współrzędne na canvasie lewego górnego rogu płytki
        let rectX = this.centerX * this.board.app.renderer.screen.width - this.rect.width / 2;
        let rectY = this.centerY * this.board.app.renderer.screen.height - this.rect.height / 2;
        this.pawn.x = rectX + cellSize / 2 + y * cellSize - 1;
        this.pawn.y = rectY + cellSize / 2 + x * cellSize;
    }

    prepareRect(size) {
        this.rect = new PIXI.Graphics();

        this.rect.beginFill(0x008000);
        this.rect.lineStyle(0, 0x000000);
        this.rect.drawRect(0.0, 0.0, size, size);
        this.rect.endFill();

        this.board.app.stage.addChild(this.rect);
    }

    attachShaders() {
        const uniforms = {
            dimensions: [this.rect.width, this.rect.height],
            tileDescription: this.id,
            uMove: [0.0, 0.0],
            uMove2: [0.0, 0.0],
            DEFAULT: this.terrains.DEFAULT,
            CASTLE: this.terrains.CASTLE,
            MEADOW: this.terrains.MEADOW,
            ROAD: this.terrains.ROAD,
            MONASTERY: this.terrains.MONASTERY,
            ROAD_END: this.terrains.ROAD_END,
            CASTLE_SHIELD: this.terrains.CASTLE_SHIELD
        };

        let that = this;
        this.board.loader.onComplete.add(handleLoadComplete)
        this.board.loader.load();

        function handleLoadComplete() {
            let vShader = that.board.loader.resources[vertexShader].data;
            let fShader = that.board.loader.resources[fragmentShader].data;
            const filter = new PIXI.Filter(vShader, fShader, uniforms);
            // podłączenie filtra do kwadratu
            that.rect.filters = [filter];
        }

        this.uniforms = uniforms;
    }

    /**
     * ustawia płytkę na właściwej pozycji na planszy
     * @param x o ile wierszy ta płytka jest przesunięta względem środkowej płytki
     * @param y o ile kolumn ta płytka jest przesunięta względem środkowej płytki
     */
    setTilePosition(x, y) {
        this.row = x;
        this.column = y;
        if (this.board.firstTile === null) {
            this.setTileCoordinates(
                0.5 + y * (this.board.tileSize / this.board.app.renderer.screen.width),
                0.5 - x * (this.board.tileSize / this.board.app.renderer.screen.height));
        } else {
            // współrzędna x środka pierwszej płytki w postaci znormalizowanej
            let firstTileX = this.board.firstTile.centerX;
            // współrzędna x środka pierwszej płytki w postaci znormalizowanej
            let firstTileY = this.board.firstTile.centerY;

            this.setTileCoordinates(
                firstTileX + y * (this.board.tileSize / this.board.app.renderer.screen.width),
                firstTileY - x * (this.board.tileSize / this.board.app.renderer.screen.height));
        }
    }

    /**
     * przesuwa płytkę i pionka
     * @param dx przyrost w pikselach na osi x
     * @param dy przyrost w pikselach na osi y
     */
    move(dx, dy) {
        // jeśli cała płytka jest widoczna, to jest tylko przesuwana
        if(this.isVisible()) {
            console.log("visible");
            this.centerX += dx / this.board.app.renderer.screen.width;
            this.centerY += dy / this.board.app.renderer.screen.height;
            this.uniforms.uMove[0] += dx / this.board.app.renderer.screen.width * 2;
            this.uniforms.uMove[1] -= dy / this.board.app.renderer.screen.height * 2;
            if (this.pawn !== null) {
                this.pawn.x += dx;
                this.pawn.y += dy;
            }
            if (this.shield !== null) {
                this.shield.x += dx;
                this.shield.y += dy;
            }
            this.movePawnPlaces(dx, dy);
        } else {
            // jeśli część płytki jest poza canvasem, to jest przerysowywana
            console.log("invisible");
            this.rect.destroy();
            this.prepareRect(this.board.tileSize);
            this.setTileCoordinates(this.centerX, this.centerY);
            this.attachShaders();
            this.centerX += dx / this.board.app.renderer.screen.width;
            this.centerY += dy / this.board.app.renderer.screen.height;
            this.uniforms.uMove[0] += dx / this.board.app.renderer.screen.width * 2;
            this.uniforms.uMove[1] -= dy / this.board.app.renderer.screen.height * 2;
            if(this.pawn !== null) {
                let x = this.pawn.x + dx;
                let y = this.pawn.y + dy;
                let color = this.pawnColor;
                this.pawn.destroy();
                let graphic = new PIXI.Graphics();
                this.board.app.stage.addChild(graphic);
                let pawnSize = this.rect.width / 8;  // średnica
                graphic.lineStyle(1, color);
                graphic.beginFill(color);
                graphic.drawCircle(0, 0, pawnSize / 2);
                graphic.endFill();
                this.pawn = graphic;
                this.pawn.x = x;
                this.pawn.y = y;
            }
            if(this.shield != null) {
                let x = this.shield.x + dx;
                let y = this.shield + dy;
                this.shield.destroy();
                let texture = PIXI.Texture.from(shield);
                let img = new PIXI.Sprite(texture);
                let shieldSize = this.rect.width / 5;  // średnica
                img.width = shieldSize;
                img.height = shieldSize;
                this.shield = img;
                this.shield.x = x;
                this.shield.y = y;
                this.board.app.stage.addChild(img);
            }
            let that = this;
            let listOfPawnPlaces = this.pawnPlaces.slice();
            this.pawnPlaces = [];
            listOfPawnPlaces.forEach(redraw);

            function redraw(item) {
                let row = item.row;
                let column = item.column;
                item.pawn.destroy();
                that.putPawnPlace(row, column);
            }
        }
    }

    // zwraca true, jeśli cała płytka jest widoczna na canvasie,
    // false - w przeciwnym przypadku
    isVisible() {
        // // dolna krawędź
        // if(this.centerY + (this.board.tileSize / 2)
        //     / this.board.app.renderer.screen.height > 1.0) {
        //     return false;
        // }
        // // prawa krawędź
        // if(this.centerX + (this.board.tileSize / 2)
        //     / this.board.app.renderer.screen.width > 1.0) {
        //     return false;
        // }
        // // lewa krawędź
        // if(this.centerX - (this.board.tileSize / 2)
        //     / this.board.app.renderer.screen.width < 0.0) {
        //     return false;
        // }
        // // górna krawędź
        // if(this.centerY - (this.board.tileSize / 2)
        //     / this.board.app.renderer.screen.height < 0.0) {
        //     return false;
        // }
        return true;
    }

    /**
     * ustala współrzędne środka płytki
     * @param x współrzędna x środka płytki (współrzędne znormalizowane)
     * @param y współrzędna y środka płytki (współrzędne znormalizowane)
     */
    setTileCoordinates(x, y) {
        // this.rect.x = x * this.board.app.renderer.screen.width - this.rect.width / 2;
        // this.rect.y = y * this.board.app.renderer.screen.height - this.rect.height / 2;
        // this.centerX = x;
        // this.centerY = y;
        this.uniforms.uMove[0] += (x - this.centerX) *2;
        this.uniforms.uMove[1] -= (y - this.centerY) *2;
        this.centerX = x;
        this.centerY = y;
    }

    /**
     * rysuje tarczę na płytce w odpowiednim wierszu i kolumnie
     * @param x numer wiersza
     * @param y numer kolumny
     */
    drawShield(x, y) {
        let texture = PIXI.Texture.from(shield);
        let img = new PIXI.Sprite(texture);
        this.shieldRow = x;
        this.shieldColumn = y;
        this.shieldTexture = texture;
        img.x = this.board.app.renderer.screen.width / 2;
        img.y = this.board.app.renderer.screen.height / 2;
        let shieldSize = this.rect.width / 5;  // średnica
        img.width = shieldSize;
        img.height = shieldSize;
        this.board.app.stage.addChild(img);
        this.shield = img;
        this.setShieldPosition(x, y);
    }

    setShieldPosition(x, y) {
        let cellSize = this.rect.width / 7;
        // współrzędne na canvasie lewego górnego rogu płytki
        let rectX = this.centerX * this.board.app.renderer.screen.width - this.rect.width / 2;
        let rectY = this.centerY * this.board.app.renderer.screen.height - this.rect.height / 2;
        this.shield.x = rectX + y * cellSize;
        this.shield.y = rectY + x * cellSize;
    }

    redraw() {
        this.uniforms.uMove[0] = 0.0;
        this.uniforms.uMove[1] = 0.0;
        this.rect.x = 0.5 * this.board.app.renderer.screen.width - this.rect.width / 2;
        this.rect.y = 0.5 * this.board.app.renderer.screen.height - this.rect.height / 2;
        this.centerX = 0.5;
        this.centerY = 0.5;
        this.setTileCoordinates(
            0.5 + this.column * (this.board.tileSize / this.board.app.renderer.screen.width),
            0.5 - this.row * (this.board.tileSize / this.board.app.renderer.screen.height));
        if (this.pawn !== null) {
            this.setPawnPosition(this.pawnRow, this.pawnColumn);
        }
        if (this.shield !== null) {
            this.setShieldPosition(this.shieldRow, this.shieldColumn);
        }
        this.redrawPawnPlaces();
    }
}
