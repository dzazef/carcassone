import React, {Component} from 'react';
import './player.css'
import {ReactComponent as Award} from "../../../assets/award.svg";
import {ReactComponent as Pawn} from "../../../assets/pawn.svg";

/**
 * Class responsible for showing player list in game with their pawns
 * and points left.
 */
class PlayerList extends Component {

    /**
     * Function returning circle in given color
     * @param color: Requested color
     * @returns {*}: Circle in color
     */
    getColorCircle = (color) => (
        <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24"
            height="24"
            width="24">
            >
            <circle
                r="10"
                cy="12"
                cx="12"
                style={{
                    fill: color,
                    stroke: "#000000",
                    fillOpacity: 0.4,
                    strokeWidth: 2,
                }}
            />
        </svg>
    )

    /**
     * Renders component.     */
    render() {
        return (
            <>
                {
                    this.props?.players?.length > 0 &&
                    this.props.players.map((player, idx) => (
                        <div key={idx} className={"m-player-list-player"}>
                            <div
                                className={"m-player-list-name"}>
                                Player{player.id}
                            </div>
                            <div className={"m-player-list-award"}>
                                <Award className={"m-player-list-award-svg"}/>
                                <div>
                                    {player.points}
                                </div>
                            </div>
                            <div className={"m-player-list-pawn"}>
                                <Pawn className={"m-player-list-pawn-svg"}/>
                                <div>
                                    {player.pawns_left}
                                </div>
                            </div>
                            <div className={"m-player-list-color"}>
                                {this.getColorCircle(player.color)}
                            </div>

                        </div>
                    ))
                }
            </>
        );
    }
}

export default PlayerList;