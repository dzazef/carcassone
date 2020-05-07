import * as PIXI from 'pixi.js';

export class Tile {
    /**
     * konstruktor klasy Tile
     * @param id id płytki
     * @param board
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
        this.prepareRect(this.board.tileSize);
        this.setTileCoordinates(0.5, 0.5);
        this.attachShaders();
    }

    prepareRect(size) {
        this.rect = new PIXI.Graphics();

        this.rect.beginFill(0x008000);
        this.rect.lineStyle(2, 0x000000);
        this.rect.drawRect(0.0, 0.0, size, size);
        this.rect.endFill();

        this.board.app.stage.addChild(this.rect);
    }

    attachShaders() {
        const uniforms = {
            dimensions: [this.rect.width, this.rect.height],
            tileDescription: this.id,
            DEFAULT: this.terrains.DEFAULT,
            CASTLE: this.terrains.CASTLE,
            MEADOW: this.terrains.MEADOW,
            ROAD: this.terrains.ROAD,
            MONASTERY: this.terrains.MONASTERY,
            ROAD_END: this.terrains.ROAD_END,
            CASTLE_SHIELD: this.terrains.CASTLE_SHIELD
        };

        this.board.loader.onComplete.add(handleLoadComplete)
        this.board.loader.load();
        let that = this;

        function handleLoadComplete() {
            // const vShader = that.board.loader.resources["./shaders/vShader.vert"].data;
            // const fShader = that.board.loader.resources["./shaders/fShader.frag"].data;
            const vShader = "attribute vec2 aVertexPosition;\n" +
                "attribute vec2 aTextureCoord;\n" +
                "uniform mat3 projectionMatrix;\n" +
                "varying vec2 vTextureCoord;\n" +
                "\n" +
                "void main(void)\n" +
                "{\n" +
                "    gl_Position = vec4((projectionMatrix * vec3(aVertexPosition, 1.0)).xy, 0.0, 1.0);\n" +
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
    }

    /**
     * ustala współrzędne środka płytki
     * @param x współrzędna x środka płytki (współrzędne znormalizowane)
     * @param y współrzędna y środka płytki (współrzędne znormalizowane)
     */
    setTileCoordinates(x, y) {
        this.rect.x = x * this.board.app.renderer.screen.width - this.rect.width / 2;
        this.rect.y = y * this.board.app.renderer.screen.height - this.rect.height / 2;
    }
}
