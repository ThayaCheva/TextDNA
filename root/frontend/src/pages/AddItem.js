import React, {useEffect} from 'react';
import axios from 'axios';
import '../css/popups/AddItem.css';
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faXmark} from '@fortawesome/free-solid-svg-icons';

function AddItem(props) {
   
    if (props.trigger) {
        document.body.style.overflowY = 'hidden';
    }
    else {
        document.body.style.overflowY = 'auto';
    }

    return (props.trigger) ? (
        <div id="additem">
            <div className="additem-container">
                <button className="close-btn" 
                    onClick={props.SetTrigger}>
                    <FontAwesomeIcon className="close-icon" icon={faXmark} />
                </button>
                <div className="additem-header">
                    <h1>Add {props.info.name}</h1>
                </div>
                <form>
                    <div className="additem-input">
                        {props.hasID && <label for="name">{props.info.name} ID:</label>}
                        {props.hasID && <input type="number" id="numberInput" name="numberInput" pattern="[0-9]*" inputMode="numeric" required/>}
                        
                        <label for="name">{props.info.name} Name:</label>
                        <input type="text" id="name" name="name" required/>
                    </div>
                    <button type="submit" className="blue-btn">Add {props.info.name}</button>
                </form>
            </div>
        </div>
    ) : "";
}

export default AddItem;
