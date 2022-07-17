import React, {useState} from 'react'
import { Questions, QuestionGroups } from './QuestionCardsInfo'


//updates the cards displayed on click by changing the array being passed into the Cards component.
//it takes in the a value, set to id, and then 
// function UpdateCardView(id) {
    // const test = id
    // console.log(id)
    // return test;
// }

//Draws the question cards on the screen based on the QuestionGroups array in QuestionCardsInfo.js
export function Cards() {
    const [value, setValue] = useState(0); //standard function component state changing 
    
    return (
        <div>
        <p>Page: {value + 1} of {QuestionGroups.length}</p>    
         <ul>{
            QuestionGroups[value].map(cardList=>( //Maps the QuestionGroups array
                //Key to keep items organized per React rules
                <li key={Questions[cardList].id}> 
                    <button 
                  
                        className="" //CSS class
                        //onClick function that changes the state to the ID of the question displayed.
                        onClick={()=>setValue((Questions[cardList].nextPage))}> 
                        {Questions[cardList].questionText} - to page {Questions[cardList].nextPage + 1}
                    </button>
                </li>
                ))
         }</ul>  
         </div>
         )   
}