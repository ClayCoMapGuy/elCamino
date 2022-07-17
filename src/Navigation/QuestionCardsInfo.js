


export const Questions = [
    {questionText : 'Building Permit', 
    id : 0, 
    nextPage : 1},
    {questionText : 'Business License', 
    id : 1, 
    nextPage : 1},
    {questionText : 'Alcohal License Renewal/Application', 
    id : 2, 
    nextPage : 1},
    {questionText : 'For a Residential Property', 
    id : 3, 
    nextPage : 2},
    {questionText : 'For a Commerical Property', 
    id : 4, 
    nextPage : 3},
    {questionText : 'A new Permit', 
    id : 5, 
    nextPage : 3},
    {questionText : 'Renewal of an existing permit', 
    id : 6, 
    nextPage : 3},
    {questionText : 'I want to add a deck', 
    id : 7, 
    nextPage : 0},
    {questionText : 'I want to add a room', 
    id : 8, 
    nextPage : 0},
    {questionText : 'I want to add a permanent carport', 
    id : 9, 
    nextPage : 4},
    ];

    //each array is a 'group' of cards displayed on screen at one time, values are the index of the 'Questions' array above.
export const QuestionGroups = [[0,1,2],[3,4,5],[6],[7,8,9],[]];