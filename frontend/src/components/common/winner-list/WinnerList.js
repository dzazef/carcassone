import React, {Component} from 'react';
import {Modal} from "react-bootstrap";
import Button from "react-bootstrap/Button";
import './winner-list.css'

/**
 * Class responsible for showing final score of the game
 */
class WinnerList extends Component {
    /**
     * Renders component.     */
    render() {
        return (
            <Modal
                show={this.props.gameEnded}
                onHide={() => window.location.reload()}
                size="lg"
                aria-labelledby="contained-modal-title-vcenter"
                centered
            >
                <Modal.Header closeButton>
                    <Modal.Title id="contained-modal-title-vcenter">
                        Winners
                    </Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    {
                        this.props?.winners && //check if defined (should always be!)
                        this.props?.winners?.map((player, i) => (
                                <div
                                    key={i}
                                    className={"m-winnerList-player"}
                                    style={{backgroundColor: player.color}}
                                >
                                    <span
                                        className={"m-winnerList-place"}
                                    >
                                        {`${player.place}. `}
                                    </span>
                                    <span
                                        className={"m-winnerList-name"}
                                    >
                                        {`Player${player.id}`}
                                    </span>
                                    <span
                                        className={"m-winnerList-points"}
                                    >
                                        {player.points}
                                    </span>
                                </div>
                            )
                        )
                    }
                </Modal.Body>
                <Modal.Footer>
                    <Button onClick={() => window.location.reload()}>Close</Button>
                </Modal.Footer>
            </Modal>
        );
    }
}

export default WinnerList;