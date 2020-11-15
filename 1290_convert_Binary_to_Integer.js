var getDecimalValue = function(head) {
    let num = 0;
    while(head){
        //(num << 1) => Left shift num by 1 position to make way for next bit
        //(num << 1) | head.val => Add next bit to num at least significant position
        num = (num << 1) | head.val;
        head = head.next
    }
    return num;
};
