import * as PIXI from 'pixi.js';

export class MyBoard {
    constructor(canvas, tileSize) {
        if(! MyBoard.instance){
            this.canvas = canvas;
            this.tileSize = tileSize;
            this.prepareApplication();
            this.prepareShaders();
            MyBoard.instance = this;
        }

        return MyBoard.instance;
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
}