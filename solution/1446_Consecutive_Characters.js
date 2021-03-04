/**
 * @param {string} s
 * @return {number}
 */
var maxPower = function(s) {
    //Two Pointers
    
    //Base Case:
    if (s.length < 1) {
        return 0;
    }
    if (s.length === 1) {
        return 1;
    }
    //General Case:
    let maxPower = 0;
    let count = 0;
    
    let prevPointer = ' ';
    
    for (let i = 0; i < s.length; i++){
        if (s[i] !== prevPointer){
            count = 1;
            prevPointer = s[i] //c
        } else {
            count++; //3
        }
         maxPower = Math.max(maxPower, count);
    }
    
    return maxPower;
};
