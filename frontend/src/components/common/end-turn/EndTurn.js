import React, {Component} from 'react';
import './end-turn.css'

/**
 * Class responsible for handling ending turn by user.
 */
class EndTurn extends Component {

    /**
     * Renders component.     */
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