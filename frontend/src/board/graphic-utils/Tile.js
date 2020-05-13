import * as PIXI from 'pixi.js';

export class Tile {
    /**
     * konstruktor klasy Tile
     * @param id id płytki
     * @param board plansza, do której należy ta płytka
     */
    constructor(id, board) {
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
        this.row = 0;  // rząd, w którym znajduje się płytka
        this.column = 0;  // kolumna, w której znajduje się płytka
        // współrzędne znormalizowane środka płytki
        // this.centerX
        // this.centerY
        this.pawnRow = 0;  // rząd, w którym znajduje się pionek
        this.pawnColumn = 0;  // kolumna, w której znajduje się pionek
        this.prepareRect(this.board.tileSize);
        this.setTileCoordinates(0.5, 0.5);
        this.attachShaders();
    }

    /**
     * rysuje pionek na tej płytce
     * @param x numer wiersza, w którym należy postawić pionek
     * @param y numer kolumny, w którym należy postawić pionek
     * @param playerId id gracza, którego pionek należy narysować
     */
    putPawn(x, y, playerId) {
        // narazie pionek będzie kółkiem. Jak zadziała,
        // to zmienię na jakiegoś sprite'a
        let graphic = new PIXI.Graphics();
        this.board.app.stage.addChild(graphic);
        let color = this.board.getPlayerHexColor(playerId);
        let pawnSize = this.rect.width / 8;  // średnica
        // graphic.x = this.rect.x + cellSize / 2 + y * cellSize;
        // graphic.y = this.rect.y + cellSize / 2 + x * cellSize;
        graphic.lineStyle(1, color);
        graphic.beginFill(color);
        graphic.drawCircle(0, 0, pawnSize / 2);
        graphic.endFill();
        this.pawn = graphic;
        this.pawnRow = x;
        this.pawnColumn = y;
        this.setPawnPosition(x, y);
    }

    setPawnPosition(x, y) {
        let cellSize = this.rect.width / 7;
        // współrzędne na canvasie lewego górnego rogu płytki
        let rectX = this.centerX * this.board.app.renderer.screen.width - this.rect.width / 2;
        let rectY = this.centerY * this.board.app.renderer.screen.height - this.rect.height / 2;
        // this.pawn.x = this.rect.x + cellSize / 2 + y * cellSize;
        // this.pawn.y = this.rect.y + cellSize / 2 + x * cellSize;
        this.pawn.x = rectX + cellSize / 2 + y * cellSize;
        this.pawn.y = rectY + cellSize / 2 + x * cellSize;
    }

    prepareRect(size) {
        this.rect = new PIXI.Graphics();

        this.rect.beginFill(0x008000);
        this.rect.lineStyle(1, 0x000000);
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
            const vShader = "attribute vec2 aVertexPosition;\n" +
                "attribute vec2 aTextureCoord;\n" +
                "uniform mat3 projectionMatrix;\n" +
                "varying vec2 vTextureCoord;\n" +
                "\n" +
                "uniform vec2 uMove;\n" +
                "uniform vec2 uMove2;\n" +
                "\n" +
                "void main(void)\n" +
                "{\n" +
                "    gl_Position = vec4((projectionMatrix * vec3(aVertexPosition, 1.0)).xy, 0.0, 1.0) + vec4(uMove, 0.0, 0.0);\n" +
                "    vTextureCoord = aTextureCoord;\n" +
                "}";

            const fShader = "precision mediump float;\n" +
                "\n" +
                "varying vec2 vTextureCoord;\n" +
                "uniform sampler2D uSampler;\n" +
                "uniform vec2 dimensions;\n" +
                "uniform vec4 filterArea;\n" +
                "uniform int tileDescription[49];\n" +
                "uniform int DEFAULT;\n" +
                "uniform int CASTLE;\n" +
                "uniform int MEADOW;\n" +
                "uniform int ROAD_END;\n" +
                "uniform int CASTLE_SHIELD;\n" +
                "uniform int ROAD;\n" +
                "uniform int MONASTERY;\n" +
                "float borderWidth = 0.005;\n" +
                "\n" +
                "// przekształcenie canvasowych współrzędnych\n" +
                "// na współrzędne na spricie ((0,0) - lewy górny róg,\n" +
                "// (1,1) - prawy dolny róg)\n" +
                "vec2 normalizeCoord(vec2 coords) {\n" +
                "    vec2 pixelCoord = vTextureCoord * filterArea.xy;\n" +
                "    return pixelCoord / dimensions;\n" +
                "}\n" +
                "\n" +
                "vec4 meadowColor() {\n" +
                "    return vec4(0.0, 0.5, 0.0, 1.0);\n" +
                "}\n" +
                "\n" +
                "vec4 defaultColor() {\n" +
                "    return meadowColor();\n" +
                "}\n" +
                "\n" +
                "vec4 castleColor() {\n" +
                "    return vec4(0.4, 0.2, 0.0, 1.0);\n" +
                "}\n" +
                "\n" +
                "vec4 roadColor() {\n" +
                "    return vec4(0.4, 0.4, 0.4, 1.0);\n" +
                "}\n" +
                "\n" +
                "vec4 monasteryColor() {\n" +
                "    return vec4(1.0, 0.6, 0.8, 1.0);\n" +
                "}\n" +
                "\n" +
                "vec4 roadEndColor() {\n" +
                "    return vec4(0.0, 0.0, 0.0, 1.0);\n" +
                "}\n" +
                "\n" +
                "// zwraca kolor, jaki odpowiada obszarowi\n" +
                "// o numerze areaNumber\n" +
                "vec4 getColor(int areaNumber) {\n" +
                "    if(areaNumber == DEFAULT) {\n" +
                "        return defaultColor();\n" +
                "    }\n" +
                "    if(areaNumber == MEADOW) {\n" +
                "        return meadowColor();\n" +
                "    }\n" +
                "    if(areaNumber == MONASTERY) {\n" +
                "        return monasteryColor();\n" +
                "    }\n" +
                "    if(areaNumber == ROAD) {\n" +
                "        return roadColor();\n" +
                "    }\n" +
                "    if(areaNumber == ROAD_END) {\n" +
                "        return roadEndColor();\n" +
                "    }\n" +
                "    if(areaNumber == CASTLE) {\n" +
                "        return castleColor();\n" +
                "    }\n" +
                "    // areaNumber == CASTLE_SHIELD\n" +
                "    return castleColor();\n" +
                "}\n" +
                "\n" +
                "int getAreaNumber(float x, float y) {\n" +
                "    for(int i = 0; i < 49; i++) {\n" +
                "        int row = i / 7;\n" +
                "        int column = i - row * 7;\n" +
                "        if(x < float(column + 1) / 7.0 && y < float(row + 1) / 7.0) {\n" +
                "            return tileDescription[i];\n" +
                "        }\n" +
                "    }\n" +
                "    return 0;\n" +
                "}\n" +
                "\n" +
                "void main(void)\n" +
                "{\n" +
                "    // kolor piksela o współrzędnych (na canvasie!)\n" +
                "    // vTextureCoord na obrazie uSampler\n" +
                "    vec4 color = texture2D(uSampler, vTextureCoord);\n" +
                "    vec2 normalizedCoord = normalizeCoord(vTextureCoord);\n" +
                "    float x = normalizedCoord.x;\n" +
                "    float y = normalizedCoord.y;\n" +
                "\n" +
                "    color = getColor(getAreaNumber(x, y));\n" +
                "\n" +
                "    gl_FragColor = color;\n" +
                "}";

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
        if(this.board.firstTile === null) {
            this.setTileCoordinates(
                0.5 + y * (this.board.tileSize / this.board.app.renderer.screen.width),
                0.5 + x * (this.board.tileSize / this.board.app.renderer.screen.height));
        } else {
            // współrzędna x środka pierwszej płytki w postaci znormalizowanej
            let firstTileX = this.board.firstTile.centerX;
            // współrzędna x środka pierwszej płytki w postaci znormalizowanej
            let firstTileY = this.board.firstTile.centerY;

            this.setTileCoordinates(
                firstTileX + y * (this.board.tileSize / this.board.app.renderer.screen.width),
                firstTileY + x * (this.board.tileSize / this.board.app.renderer.screen.height));
        }
    }

    /**
     * przesuwa płytkę i pionka
     * @param dx przyrost w pikselach na osi x
     * @param dy przyrost w pikselach na osi y
     */
    move(dx, dy) {
         this.uniforms.uMove[0] += dx / this.board.app.renderer.screen.width * 2;
         this.uniforms.uMove[1] -= dy / this.board.app.renderer.screen.height * 2;

         this.centerX += dx / this.board.app.renderer.screen.width;
         this.centerY += dy / this.board.app.renderer.screen.height;

        if(this.pawn !== null) {
            this.pawn.x += dx;
            this.pawn.y += dy;
        }
    }

    /**
     * ustala współrzędne środka płytki
     * @param x współrzędna x środka płytki (współrzędne znormalizowane)
     * @param y współrzędna y środka płytki (współrzędne znormalizowane)
     */
    setTileCoordinates(x, y) {
        this.rect.x = x * this.board.app.renderer.screen.width - this.rect.width / 2;
        this.rect.y = y * this.board.app.renderer.screen.height - this.rect.height / 2;
        this.centerX = x;
        this.centerY = y;
    }

    redraw() {
        this.uniforms.uMove[0] = 0.0;
        this.uniforms.uMove[1] = 0.0;
        this.setTileCoordinates(
            0.5 + this.column * (this.board.tileSize / this.board.app.renderer.screen.width),
            0.5 + this.row * (this.board.tileSize / this.board.app.renderer.screen.height));
        console.log(this.row);
        console.log(this.column);
        if(this.pawn !== null) {
            this.setPawnPosition(this.pawnRow, this.pawnColumn);
        }
    }
}
