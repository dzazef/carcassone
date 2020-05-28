import React, {Component} from 'react';
import './tiles-left.css'
import {ReactComponent as Tile} from '../../../assets/tile.svg'

class TilesLeft extends Component {
    render() {
        return (
            <>
                <div
                    className={"m-tilesleft-root"}
                    style={{display: this.props.tilesLeft === undefined ? "none" : "flex"}}
                >
                    <Tile className={"m-tilesleft-icon"}/>
                    <div className={"m-tilesleft-count"}>{this.props.tilesLeft}</div>
                </div>
            </>
        );
    }
}

export default TilesLeft;