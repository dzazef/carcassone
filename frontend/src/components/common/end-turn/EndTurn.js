import React, {Component} from 'react';
import './end-turn.css'

class EndTurn extends Component {
    render() {
        return (
            <button
                style={{display: this.props.tilePlaced ? "initial" : "none"}}
                className={"m-endturn-button"}
                onClick={() => this.props.sendEndTurn(this.props.myId)}>
                <div>Zakończ rundę</div>
            </button>
        );
    }
}

export default EndTurn;