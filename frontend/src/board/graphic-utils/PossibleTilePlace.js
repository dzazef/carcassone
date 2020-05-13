import * as PIXI from 'pixi.js';

export class PossibleTilePlace {
    /**
     * rysuje miejsce na płytkę
     * @param board plansza, do której należy ta płytka
     */
    constructor(board) {
        this.board = board;
        this.row = 0;  // rząd, w którym znajduje się płytka
        this.column = 0;  // kolumna, w której znajduje się płytka
        this.prepareRect(this.board.tileSize);
        this.setTileCoordinates(0.5, 0.5);
    }

    prepareRect(size) {
        this.rect = new PIXI.Graphics();

        this.lineWidth = 1;  // grubość kontur w pikselach
        this.rect.lineStyle(this.lineWidth, 0xe6e600);
        this.rect.drawRect(0.0, 0.0, size, size);

        this.board.app.stage.addChild(this.rect);
    }

    setTilePosition(x, y) {
        // this.setTileCoordinates(
        //     0.5 + y * (this.board.tileSize / this.board.app.renderer.screen.width),
        //     0.5 + x * (this.board.tileSize / this.board.app.renderer.screen.height));
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
     * ustala współrzędne środka płytki
     * @param x współrzędna x środka płytki (współrzędne znormalizowane)
     * @param y współrzędna y środka płytki (współrzędne znormalizowane)
     */
    setTileCoordinates(x, y) {
        this.rect.x = x * this.board.app.renderer.screen.width - this.rect.width / 2 - this.lineWidth / 2;
        this.rect.y = y * this.board.app.renderer.screen.height - this.rect.height / 2;
    }

    /**
     * przesuwa prostokąt reprezentujący miejsce na płytkę o podane przesunięcie
     * @param dx przyrost w pikselach na osi x
     * @param dy dy przyrost w pikselach na osi y
     */
    move(dx, dy) {
        this.rect.x += dx;
        this.rect.y += dy;
    }

    redraw() {
        // this.setTilePosition(this.row, this.column);
        this.setTileCoordinates(
            0.5 + this.column * (this.board.tileSize / this.board.app.renderer.screen.width),
            0.5 + this.row * (this.board.tileSize / this.board.app.renderer.screen.height));
    }
}