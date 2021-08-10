// TODO: create a RomanNumerals helper object
var RomanNumerals = {
  
  
    toRoman: function(arabicNumber){
      let number_roman = [
    {number: 1000, roman: "M"},
    {number: 900, roman: "CM"},
    {number: 500, roman: "D"},
    {number: 400, roman: "CD"},
    {number: 100, roman: "C"},
    {number: 90, roman: "XC"},
    {number: 50, roman: "L"},
    {number: 40, roman: "XL"},
    {number: 10, roman: "X"},
    {number: 9, roman: "IX"},
    {number: 5, roman: "V"},
    {number: 4, roman: "IV"},
    {number: 1, roman: "I"}
  ];
      
      let roman = '';
      for(let i = 0; i<number_roman.length; i++){
        if(number_roman[i].number<=arabicNumber){
          roman += number_roman[i].roman;
          arabicNumber -= number_roman[i].number;
          i--;
        }
        
        
      }
      return roman;
      
    },
    
    fromRoman: function(roman){
        var map = {
            IV:4,
            IX:9,
            XL:40,
            XC:90,
            CD:400,
            CM:900,
            I:1,
            V:5,
            X:10,
            L:50,
            C:100,
            D:500,
            M:1000
            };
          
          let number = 0;
          let twoLetters = '';
          let oneLetter =  '';

          for (let i = 0; i<roman.length; i++){
              twoLetters = roman[i] + roman[i+1];
              oneLetter = roman[i];

              twoLetters_num = map[twoLetters];
              oneLetter_num = map[oneLetter];

              if(twoLetters_num != null){
                  number += twoLetters_num;
                  i++;
              }
              else if (oneLetter_num != null){
                  number += oneLetter_num;
              }

          }
          return number;
    }
  }

  console.log(RomanNumerals.toRoman(999)); 
   console.log(RomanNumerals.fromRoman('MDCLXIX'));