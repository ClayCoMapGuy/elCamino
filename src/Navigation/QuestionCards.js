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
        <div className='OptionGrid'>
        <p>Page: {value + 1} of {QuestionGroups.length}</p>    
        <button onClick={()=>setValue(0)}>Back to start</button>
         <ul>{
            QuestionGroups[value].map(cardList=>( //Maps the QuestionGroups array
                //Key to keep items organized per React rules
                <li 
                className="questionListItems"
                key={Questions[cardList].id}> 
                    <button 
                        className="questionButtons" //CSS class
                        //onClick function that changes the state to the ID of the question displayed.
                        onClick={()=>setValue((Questions[cardList].nextPage))}> 
                        <div className='Button_inline_image'>Placeholder for image</div>
                        <div className='Button_inline_text'>{Questions[cardList].questionText} - to page {Questions[cardList].nextPage + 1}</div>
                        <div className='Button_inline_icon'>Placeholder for arrow image</div>
                    </button>
                </li>
                ))
         }</ul>  
         </div>
         )   
}